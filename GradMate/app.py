from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def simple_match(message):
    message = message.lower()

    keywords = {
        "states": ["andaman and nicobar islands", "delhi", "tamil nadu", "maharashtra", "karnataka"],
        "managements": ["central government", "state government", "private"],
        "locations": ["urban", "rural"]
    }

    # Extract known values
    state = next((s for s in keywords["states"] if s in message), None)
    management = next((m for m in keywords["managements"] if m in message), None)
    location = next((l for l in keywords["locations"] if l in message), None)

    # Extract year
    year = None
    for word in message.split():
        if word.isdigit() and len(word) == 4:
            year = int(word)

    # Extract university (if user says 'under')
    university = None
    if "under" in message and "university" in message:
        university = message.split("under")[-1].strip()

    return state, management, location, year, university


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()
    state, management, location, year, university = simple_match(user_msg)

    con = sqlite3.connect("colleges.db")
    df = pd.DataFrame()

    if "hello" in user_msg or "hi" in user_msg:
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
            query += " AND LOWER(State) = ?"
            params.append(state)
        if management:
            query += " AND LOWER(Management) = ?"
            params.append(management)
        if location:
            query += " AND LOWER(Location) = ?"
            params.append(location)
        if year:
            query += " AND `Year Of Establishment` <= ?"
            params.append(year)
        if university:
            query += " AND LOWER(`University Name`) LIKE ?"
            params.append(f"%{university}%")

        df = pd.read_sql_query(query, con, params=params)
        con.close()

        if not df.empty:
            bot_msg = df.to_html(classes="colleges-table", index=False)
        else:
            bot_msg = "Sorry, I couldn't find any college matching your query. Try again!"

    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)