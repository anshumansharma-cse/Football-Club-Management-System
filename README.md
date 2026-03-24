# ⚽ Football Club Management System

> A DBMS project built to bring data-driven football management to Indian football.
> Inspired by the Chunni Goswami era — *"someday, we'll restore former glory."*

---

## 🎯 What Does This Project Do?

European football clubs have mastered sports data analytics — it shows in their results.
This project provides a lightweight backend + UI to manage club & player data, track league standings, and simulate a transfer market. It's a starting point for the kind of infrastructure Indian football deserves.

---

## 🛠️ Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Database | MySQL                   |
| Backend  | Python (`mysql-connector-python`) |
| Frontend | Streamlit               |

---

## 🗄️ Database Design

### Tables

| Table            | Description                              |
|------------------|------------------------------------------|
| `clubs`          | Club info — city, titles, coach, stadium |
| `players`        | Players with position, age, nationality  |
| `league_table`   | Standings: W/D/L, GF/GA/GD/Pts          |
| `transfer_market`| Players listed for transfer with value   |

### Relationships
- `clubs` → `players` : **One-to-Many** (one club has many players)
- `clubs` → `transfer_market` : **One-to-Many**
- Foreign keys with `ON DELETE SET NULL` + `ON UPDATE CASCADE`

---

## ⚙️ Features

- 👀 **View Players** — with club name via SQL JOIN
- 🔍 **Search Players** — partial name match
- ➕ **Add Players & Clubs** — form-based input with validation
- 📊 **League Table** — sorted by points & goal difference
- 💸 **Transfer Market** — list and browse players for transfer

---

## 🏗️ Architecture

```
Streamlit UI (app.py)
      ↓
Python Backend (db.py)
      ↓
MySQL Database (football_db)
```

---

## 📁 Project Structure

```
football-club-management/
├── app.py          # Streamlit frontend
├── db.py           # All DB functions (queries, inserts)
├── schema.sql      # Database schema + seed data
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up MySQL
```sql
SOURCE schema.sql;
```
> Update `db.py` with your MySQL credentials if needed.

### 3. Run the app
```bash
streamlit run app.py
```

---

## 🧠 DBMS Concepts Demonstrated

- Relational schema design
- Primary & Foreign Keys
- `ON DELETE SET NULL` / `ON UPDATE CASCADE`
- Parameterised queries (`%s`) — prevents SQL injection
- `JOIN` across tables
- `LIKE` for search
- `ORDER BY` with multiple columns
- `AUTO_INCREMENT` surrogate keys

---

## 🚀 Future Improvements

- [ ] Player stats (goals, assists, ratings)
- [ ] Update / delete players
- [ ] Authentication for admin actions
- [ ] Charts — top scorers, age distribution
- [ ] Export data to CSV

---

## 💡 Learning Outcomes

- How Python connects to and interacts with a relational DB
- Writing safe, parameterised SQL queries
- Building a full-stack mini app with Streamlit
- Designing normalized schemas with foreign key relationships
