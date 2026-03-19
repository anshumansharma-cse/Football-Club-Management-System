# Football-Club-Management-System
Football DBMS Project

This project aims to solve the appalling state of football in India.
If we all play our part & support the ecosystem, surely, someday, we'll restore former glory of India
(Chunni Goswami ERA)

## How does this project help?
The Europeans have mastered the art of 'sports' data analysis, they have reeped fruits in hockey, football & other sports.
We are trying to provide such backend support to our players.

## Technical Details

MySQL (Database)

Python (Backend)

Streamlit (Frontend UI)

It demonstrates core DBMS concepts like:

Relational schema design

Primary & Foreign keys

SQL queries (JOIN, INSERT)

Application-database integration

🏗️ Architecture
Streamlit UI → Python Backend → MySQL Database
🗂️ Project Structure
Backend/ → Database interaction logic
UI/ → Streamlit frontend
DB/ → SQL schema
🧠 Database Design

Tables used:

clubs

players

Relationship:

One club → many players (1)

⚙️ Features

View players with club info

Add new players

Uses SQL JOIN for relational queries

▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Setup MySQL

Run:

SOURCE DB/schema.sql;
3. Run app
streamlit run UI/app.py
📸 Demo

(Add screenshots here)

🚀 Future Improvements

Search & filter players

Delete/update players

Better UI

Authentication system

💡 Learning Outcomes

Learned how backend interacts with DB

Understood SQL joins and relationships

Built a full-stack mini application