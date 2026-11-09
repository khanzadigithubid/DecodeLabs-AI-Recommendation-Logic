# 🎬 AI Movie Recommendation System

> **DecodeLabs Internship – Project 03 | AI Recommendation Logic**

---

## 📌 Project Objective

Build a complete, beginner-friendly AI recommendation system that:
1. Accepts user preferences (favourite movie genres)
2. Matches those preferences against a curated movie dataset
3. Calculates a similarity/match score for every movie
4. Ranks and displays personalised recommendations in a polished web UI

---

## ✨ Features

| Feature | Details |
|---|---|
| Multi-genre selection | Pick one or more genres from a sidebar multiselect |
| Similarity scoring | Custom Python algorithm — no external AI library needed |
| Ranked results | Movies sorted by match score, highest first |
| Score badges | Colour-coded: 🟢 ≥70 % · 🟡 40–69 % · 🔴 <40 % |
| Adjustable filters | Control max results and minimum match percentage |
| Score chart | Bar chart showing the score distribution of results |
| Movie catalogue | Browse all 25 movies in an expandable table |
| Error handling | Handles empty selections and missing file gracefully |
| Responsive layout | Clean dark-cinema Streamlit theme |

---

## 🗂️ Project Structure

```
Project 03/
├── app.py           # Main Streamlit application
├── movies.csv       # Dataset of 25 movies with genre, tags, description, year & IMDb rating
├── requirements.txt # Python dependencies
└── README.md        # This file
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Streamlit 1.35** | Interactive web UI |
| **Pandas 2.2** | CSV loading & DataFrame manipulation |

No external AI APIs, paid services, or pre-built recommendation engines are used.

---

## ⚙️ Installation

### Prerequisites
- Python 3.10 or higher installed
- pip package manager

### Steps

```bash
# 1. Navigate to the project folder
cd "Project 03"

# 2. (Optional but recommended) create a virtual environment
python -m venv venv

# Activate – Windows PowerShell
venv\Scripts\Activate.ps1

# Activate – macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
streamlit run app.py
```

Streamlit will open the app automatically at **http://localhost:8501**

---

## 🧠 How the Recommendation Logic Works

The recommendation engine is built entirely in plain Python — no ML library needed.

### Algorithm Overview

```
Score (0–100) = Genre Score (0–60) + Tag Score (0–40)
```

#### Step 1 – Genre Match (up to 60 points)
- The user's selected genres are tokenised (e.g. `"Sci-Fi"` → `{"sci", "fi"}`).
- Each movie's genre field is tokenised the same way.
- If **any token overlaps**, the movie earns **60 points**.

#### Step 2 – Tag Keyword Match (up to 40 points)
- Every movie has a `tags` column with descriptive keywords (e.g. `action thriller crime`).
- Overlapping keywords between the movie's tags and the user's genre tokens are counted.
- Score = `(matched_tags / total_movie_tags) × 40`

#### Step 3 – Ranking
- All movies with a score > 0 are sorted descending.
- The top N results (user-configurable, default 10) are returned.
- A minimum score filter can further narrow results.

### Why This Approach?
- Transparent and explainable — you can see exactly why each movie was recommended.
- No training data or model files required.
- Easy to extend with more columns (cast, director, release decade, etc.).

---

## 🖥️ Example Output

**User selects:** `Action`, `Sci-Fi`

| Rank | Title | Genre | Score | Year |
|------|-------|-------|-------|------|
| 🥇 | Doctor Strange | Sci-Fi | 82.5% | 2016 |
| 🥈 | Interstellar | Sci-Fi | 78.0% | 2014 |
| 🥉 | The Dark Knight | Action | 74.3% | 2008 |
| #4 | Inception | Sci-Fi | 70.0% | 2010 |
| #5 | The Avengers | Action | 68.6% | 2012 |

---

## 🧪 Testing Checklist

- [x] Single genre selection (e.g. only `Horror`) → returns only horror/thriller films
- [x] Multiple genres (e.g. `Action` + `Romance`) → returns mixed results ranked by score
- [x] No genre selected → warning message shown, no crash
- [x] Minimum score slider set to 80 → only high-confidence matches shown
- [x] Missing `movies.csv` → friendly error message shown
- [x] All 25 movies verified for correct genre/tag alignment
- [x] Score calculation verified: genre match = 60 pts base, tag overlap scales 0–40 pts

---

## 👨‍💻 Author

Built as part of the **DecodeLabs AI & Python Internship – Project 03**.
