# GradMate 🎓

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![GitHub PRs](https://img.shields.io/github/issues-pr/Ira-Singh-Parmar/GradMate?style=for-the-badge)](https://github.com/Ira-Singh-Parmar/GradMate/pulls)
[![GitHub Issues](https://img.shields.io/github/issues/Ira-Singh-Parmar/GradMate?style=for-the-badge)](https://github.com/Ira-Singh-Parmar/GradMate/issues)

> An intelligent, conversational web application designed to streamline higher education discovery by matching students with ideal colleges based on tailored academic and financial criteria.

---

## 📌 Executive Summary

Navigating post-secondary options often requires filtering through scattered admission guidelines, complex cutoff tables, and varied fee structures. **GradMate** simplifies this process through a unified, chatbot-driven interface. By allowing users to query criteria such as location, courses offered, entrance cutoffs, ratings, and budgets in natural language, GradMate reduces decision friction and empowers students to make well-informed academic choices.

---

## ⚡ Key Capabilities

* **Conversational Query Processing:** Dynamic assistance tailored to student inquiries without complex search forms.
* **Criteria-Based Filtering:** Search institutions by multi-variable parameters including target scores, location preferences, and maximum tuition thresholds.
* **Cutoff & Eligibility Assessment:** Helps candidates evaluate viable institutions against their academic standing and entrance test results.
* **Institutions Comparison:** Review ratings and overall institution metrics to optimize safety and target choices.

---

## 🛠 Tech Stack & Dependencies

* **Backend Language:** Python
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3, JavaScript
* **Data Processing:** Python Data Structures / JSON / Pandas

---

## 🚀 Getting Started

Follow the instructions below to set up and run a local instance of **GradMate**.

### Prerequisites

* **Python 3.8+** installed on your local environment.
* **Git** installed for version control.

### Installation & Execution

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ira-Singh-Parmar/GradMate.git
   cd GradMate
   ```

2. **Establish a Virtual Environment**
   * **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Core Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not present yet, install Flask directly: `pip install flask`)*

4. **Launch the Application**
   ```bash
   python app.py
   ```

5. **Access Local Server**
   Open your browser and navigate to `[http://127.0.0.1:5000/](http://127.0.0.1:5000/)` to initialize the interface.

---

## 🤝 Contributing

Contributions are welcomed. To propose changes or introduce new features:

1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes with descriptive messages (`git commit -m 'Add NewFeature'`).
4. Push your updates to your branch (`git push origin feature/NewFeature`).
5. Open a formal Pull Request against the `main` branch.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
