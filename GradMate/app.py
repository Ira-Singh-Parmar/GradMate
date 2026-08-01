from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def get_states():
    con = sqlite3.connect("colleges.db")
    cursor = con.cursor()

    cursor.execute("SELECT DISTINCT LOWER(TRIM(State)) FROM colleges")
    states = [row[0] for row in cursor.fetchall() if row[0]]

    con.close()
    return states

def get_districts():
    con = sqlite3.connect("colleges.db")
    cursor = con.cursor()

    cursor.execute("""
        SELECT DISTINCT LOWER(TRIM(District))
        FROM colleges
        WHERE District IS NOT NULL
    """)

    districts = [row[0] for row in cursor.fetchall()]

    con.close()
    return districts

def get_college_types():
    con = sqlite3.connect("colleges.db")
    cursor = con.cursor()

    cursor.execute("""
        SELECT DISTINCT LOWER(TRIM(`College Type`))
        FROM colleges
        WHERE `College Type` IS NOT NULL
    """)

    types = [row[0] for row in cursor.fetchall()]
    con.close()

    return types

def get_locations():
    con = sqlite3.connect("colleges.db")
    cursor = con.cursor()

    cursor.execute("SELECT DISTINCT LOWER(TRIM(Location)) FROM colleges")
    locations = [row[0] for row in cursor.fetchall() if row[0]]

    con.close()
    return locations


def simple_match(message):
    message = message.lower()

    keywords = {
        "states": get_states(),

        "districts": get_districts(),

        "college_types": get_college_types(),

        "managements": [
            "central government",
            "state government",
            "government",
            "private",
            "un-aided",
            "aided",
            "university",
            "local body"
        ],

        "locations": [
            "urban",
            "rural"
        ]
    }

    state = next(
        (s for s in sorted(keywords["states"], key=len, reverse=True) if s in message),
        None
    )

    district = next(
        (d for d in sorted(keywords["districts"], key=len, reverse=True) if d in message),
        None
    )

    college_type = next(
        (c for c in keywords["college_types"] if c in message),
        None
    )

    management = next(
        (
            m for m in sorted(
                keywords["managements"],
                key=len,
                reverse=True
            )
            if m in message
        ),
        None
    )

    location = next(
        (l for l in keywords["locations"] if l in message),
        None
    )


    # Extract year
    year = None

    for word in message.split():
        if word.isdigit() and len(word) == 4:
            year = int(word)


    # Extract limit
    limit = None

    for word in message.split():
        if word.isdigit():
            number = int(word)

            if number <= 100:
                limit = number
                break


    # University search
    university = None

    if "under" in message and "university" in message:
        university = message.split("under")[-1].strip()


    # College name search
    college_name = message


    remove_words = [
        "show",
        "me",
        "details",
        "detail",
        "of",
        "college",
        "colleges",
        "about",
        "tell",
        "find",
        "search",
        "in",
        "the"
    ]


    for word in remove_words:
        college_name = college_name.replace(word, " ")


    # Remove detected filters
    filters = [
        state,
        district,
        college_type,
        management,
        location,
        university
    ]


    for item in filters:
        if item:
            college_name = college_name.replace(item, " ")


    college_name = " ".join(college_name.split())


    # Only search name if something meaningful remains
    if college_name:
        # avoid searching only numbers
        if not college_name.isdigit():
            pass
        else:
            college_name = None
    else:
        college_name = None


    return (
        state,
        district,
        college_type,
        management,
        location,
        year,
        university,
        limit,
        college_name
    )

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()
    state, district, college_type, management, location, year, university, limit, college_name = simple_match(user_msg)

    con = sqlite3.connect("colleges.db")
    df = pd.DataFrame()

    if user_msg.strip() in ["hello", "hi", "hey"]:
        bot_msg = "Hi there! GradMate🎓 here! Any queries regarding the selection of colleges..? Ask me maybe I'll help you out...😊"
    
    elif "how are you" in user_msg:
        bot_msg = "I'm just a bunch of code, but I'm doing great!"

    elif "bye" in user_msg:
        bot_msg = "Goodbye!👋 Have a nice day!😊"
    
    else:
        # Start building the SQL query
        query = "SELECT Name, State, District, Management, `Year Of Establishment`, `University Name` FROM colleges WHERE 1=1"
        params = []

        if state:
            query += " AND LOWER(TRIM(State)) = ?"
            params.append(state)

        if district:
            query += " AND LOWER(TRIM(District)) LIKE ?"
            params.append(f"%{district}%")

        if college_type:
            query += " AND LOWER(TRIM(`College Type`)) LIKE ?"
            params.append(f"%{college_type}%")

        if management == "private":
            query += """
            AND (
                LOWER(Management) LIKE '%private%'
            )
            """

        elif management == "government":
            query += """
            AND (
                LOWER(Management) LIKE '%state government%'
                OR LOWER(Management) LIKE '%central government%'
            )
            """

        elif management:
            query += " AND LOWER(TRIM(Management)) LIKE ?"
            params.append(f"%{management}%")

        if location:
            query += " AND LOWER(TRIM(Location)) = ?"
            params.append(location)

        if year:
            query += " AND `Year Of Establishment` <= ?"
            params.append(year)

        if university:
            query += " AND LOWER(`University Name`) LIKE ?"
            params.append(f"%{university}%")

        if college_name:
            query += " AND LOWER(Name) LIKE ?"
            params.append(f"%{college_name}%")
        
        if limit:
            query += " LIMIT ?"
            params.append(limit)

        df = pd.read_sql_query(query, con, params=params)
        con.close()

        if not df.empty:
            bot_msg = f"""
            Found {len(df)} colleges matching your query :<br><br>

            <div class="table-container">
                {df.to_html(classes="colleges-table", index=False)}
            </div>
            """
        else:
            bot_msg = "Sorry, I couldn't find any college matching your query. Try again!"

    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)