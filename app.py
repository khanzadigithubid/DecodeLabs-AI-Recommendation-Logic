"""
CineAI – AI Movie Recommendation System
DecodeLabs Internship · Project 03
"""

import streamlit as st
import pandas as pd

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CineAI – Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── FULL PROFESSIONAL CSS ─────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ═══════════════════════════════════════════
   BASE
═══════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background: #060614 !important;
    color: #e2e8f0 !important;
    margin: 0; padding: 0;
}

.main > .block-container {
    background: #060614 !important;
    padding: 2.5rem 3rem 4rem !important;
    max-width: 1280px !important;
}

/* ═══════════════════════════════════════════
   SIDEBAR
═══════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: #0b0b18 !important;
    border-right: 1px solid rgba(99,102,241,0.2) !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
}
[data-testid="stSidebar"] section {
    padding: 0 1.25rem !important;
}

/* All sidebar text */
[data-testid="stSidebar"],
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] small {
    color: #cbd5e1 !important;
}

/* ═══════════════════════════════════════════
   MULTISELECT
═══════════════════════════════════════════ */
/* Outer wrapper */
[data-testid="stMultiSelect"] { margin: 0 !important; }

/* The input box */
[data-testid="stMultiSelect"] [data-baseweb="select"] > div:first-child {
    background: #13132a !important;
    border: 1.5px solid #2d2f55 !important;
    border-radius: 10px !important;
    min-height: 44px !important;
    padding: 4px 8px !important;
    transition: border-color .2s, box-shadow .2s !important;
}
[data-testid="stMultiSelect"] [data-baseweb="select"] > div:first-child:focus-within {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,.18) !important;
}

/* Typed text */
[data-testid="stMultiSelect"] input {
    color: #e2e8f0 !important;
    font-size: 0.9rem !important;
    caret-color: #818cf8 !important;
}
[data-testid="stMultiSelect"] input::placeholder {
    color: #4b5563 !important;
}

/* Selected chips / tags */
[data-baseweb="tag"] {
    background: rgba(99,102,241,.2) !important;
    border: 1px solid rgba(99,102,241,.45) !important;
    border-radius: 8px !important;
    padding: 2px 10px !important;
    margin: 2px !important;
}
[data-baseweb="tag"] span {
    color: #a5b4fc !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
}
[data-baseweb="tag"] [role="presentation"] svg { fill: #818cf8 !important; }

/* Dropdown popup */
[data-baseweb="popover"] > div,
[data-baseweb="menu"],
ul[data-baseweb="menu"] {
    background: #13132a !important;
    border: 1px solid #2d2f55 !important;
    border-radius: 12px !important;
    box-shadow: 0 24px 64px rgba(0,0,0,.75) !important;
    overflow: hidden !important;
    padding: 4px !important;
}
/* Options */
[data-baseweb="menu"] li,
[data-baseweb="menu"] [role="option"] {
    background: transparent !important;
    color: #94a3b8 !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    margin: 1px 0 !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    transition: background .15s !important;
}
[data-baseweb="menu"] li *,
[data-baseweb="menu"] [role="option"] * {
    color: #94a3b8 !important;
}
[data-baseweb="menu"] li:hover,
[data-baseweb="menu"] [role="option"]:hover {
    background: rgba(99,102,241,.15) !important;
}
[data-baseweb="menu"] li:hover *,
[data-baseweb="menu"] [role="option"]:hover * {
    color: #c7d2fe !important;
}
[data-baseweb="menu"] [aria-selected="true"] {
    background: rgba(99,102,241,.25) !important;
}
[data-baseweb="menu"] [aria-selected="true"] * {
    color: #818cf8 !important;
    font-weight: 700 !important;
}

/* ═══════════════════════════════════════════
   SLIDER
═══════════════════════════════════════════ */
[data-testid="stSlider"] p,
[data-testid="stSlider"] span { color: #94a3b8 !important; }

[data-testid="stSlider"] [data-testid="stTickBar"] { display: none !important; }

/* Track fill */
[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
}

/* ═══════════════════════════════════════════
   BUTTON
═══════════════════════════════════════════ */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    color: #ffffff !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.3px !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.65rem 1.25rem !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(99,102,241,.4) !important;
    transition: all .2s ease !important;
    cursor: pointer !important;
}
[data-testid="stButton"] > button:hover {
    box-shadow: 0 8px 28px rgba(99,102,241,.6) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* ═══════════════════════════════════════════
   METRICS
═══════════════════════════════════════════ */
[data-testid="metric-container"] {
    background: #0f0f1e !important;
    border: 1px solid #1a1b35 !important;
    border-radius: 16px !important;
    padding: 22px 26px !important;
    transition: border-color .2s !important;
}
[data-testid="metric-container"]:hover {
    border-color: rgba(99,102,241,.35) !important;
}
[data-testid="metric-container"] [data-testid="stMetricLabel"] p {
    color: #475569 !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-size: 1.75rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
}
[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    color: #6366f1 !important;
    font-size: 0.78rem !important;
}

/* ═══════════════════════════════════════════
   EXPANDER
═══════════════════════════════════════════ */
[data-testid="stExpander"] {
    background: #0f0f1e !important;
    border: 1px solid #1a1b35 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}
[data-testid="stExpander"] summary {
    padding: 14px 20px !important;
}
[data-testid="stExpander"] summary p {
    color: #64748b !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
}
[data-testid="stExpander"] summary:hover p {
    color: #94a3b8 !important;
}

/* ═══════════════════════════════════════════
   DIVIDER
═══════════════════════════════════════════ */
hr {
    border: none !important;
    border-top: 1px solid #1a1b35 !important;
    margin: 1.5rem 0 !important;
}

/* ═══════════════════════════════════════════
   SCROLLBAR
═══════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #060614; }
::-webkit-scrollbar-thumb { background: #1e1b4b; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #4338ca; }

/* ═══════════════════════════════════════════
   GENERAL
═══════════════════════════════════════════ */
p { color: #94a3b8 !important; line-height: 1.65 !important; }
h1, h2, h3, h4 { color: #f8fafc !important; }
a { color: #818cf8 !important; }

/* Streamlit default borders */
[data-testid="stVerticalBlock"] > div { gap: 0 !important; }
</style>
""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# DATA & ENGINE
# ═════════════════════════════════════════════════════════════════════════════
@st.cache_data
def load_movies(path="movies.csv"):
    df = pd.read_csv(path)
    df["genre_lower"] = df["genre"].str.lower().str.strip()
    df["tags_lower"]  = df["tags"].str.lower().str.strip()
    return df


def similarity(row, genres):
    score = 0.0
    mt = set(row["genre_lower"].replace("-", " ").split())
    ut = set()
    for g in genres:
        ut.update(g.lower().replace("-", " ").split())
    if mt & ut:
        score += 60.0
    tg = set(row["tags_lower"].split())
    if tg:
        score += (len(tg & ut) / len(tg)) * 40.0
    return round(min(score, 100.0), 1)


def recommend(df, genres, top_n=10):
    if not genres:
        return pd.DataFrame()
    df = df.copy()
    df["score"] = df.apply(lambda r: similarity(r, genres), axis=1)
    return (df[df["score"] > 0]
            .sort_values("score", ascending=False)
            .head(top_n)
            .reset_index(drop=True))


# ═════════════════════════════════════════════════════════════════════════════
# CONSTANTS & HELPERS
# ═════════════════════════════════════════════════════════════════════════════
ALL_GENRES = ["Action", "Sci-Fi", "Drama", "Romance", "Horror", "Thriller", "Animation"]

GM = {
    "Action"   : {"c": "#f43f5e", "i": "💥", "bg": "rgba(244,63,94,.1)"},
    "Sci-Fi"   : {"c": "#38bdf8", "i": "🚀", "bg": "rgba(56,189,248,.1)"},
    "Drama"    : {"c": "#c084fc", "i": "🎭", "bg": "rgba(192,132,252,.1)"},
    "Romance"  : {"c": "#f472b6", "i": "💕", "bg": "rgba(244,114,182,.1)"},
    "Horror"   : {"c": "#94a3b8", "i": "👻", "bg": "rgba(148,163,184,.1)"},
    "Thriller" : {"c": "#fb923c", "i": "🔪", "bg": "rgba(251,146,60,.1)"},
    "Animation": {"c": "#34d399", "i": "🎨", "bg": "rgba(52,211,153,.1)"},
}


def hex_rgb(h):
    h = h.lstrip("#")
    return ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))


def chip(genre):
    g = GM.get(genre, {"c": "#818cf8", "i": "🎬", "bg": "rgba(129,140,248,.1)"})
    return (f'<span style="display:inline-flex;align-items:center;gap:5px;'
            f'background:{g["bg"]};color:{g["c"]};'
            f'border:1px solid rgba({hex_rgb(g["c"])},.35);'
            f'border-radius:8px;padding:4px 12px;font-size:0.78rem;'
            f'font-weight:600;margin:3px 4px 3px 0;letter-spacing:.2px;">'
            f'{g["i"]} {genre}</span>')


def score_pill(score):
    if score >= 70:
        c, label = "#10b981", "Strong Match"
    elif score >= 40:
        c, label = "#f59e0b", "Good Match"
    else:
        c, label = "#64748b", "Partial"
    w = int(score)
    bar_gradient = f"background:linear-gradient(90deg,{c},{c}88)"
    return (
        '<div style="margin:14px 0 6px;">'
        '<div style="display:flex;justify-content:space-between;'
        'align-items:center;margin-bottom:7px;">'
        f'<span style="font-size:0.73rem;color:{c};font-weight:700;'
        f'text-transform:uppercase;letter-spacing:.6px;">{label}</span>'
        f'<span style="font-size:1rem;color:{c};font-weight:800;">{score}%</span>'
        '</div>'
        '<div style="background:#1a1b35;border-radius:99px;height:6px;overflow:hidden;">'
        f'<div style="{bar_gradient};height:6px;width:{w}%;border-radius:99px;"></div>'
        '</div>'
        '</div>'
    )


# ═════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═════════════════════════════════════════════════════════════════════════════
with st.sidebar:

    # ── Brand bar ────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:linear-gradient(135deg,#6366f1,#8b5cf6);
                padding:28px 24px 22px;margin:-1rem -1rem 0;
                border-bottom:1px solid rgba(255,255,255,.08);">
      <div style="display:flex;align-items:center;gap:12px;">
        <div style="width:40px;height:40px;background:rgba(255,255,255,.15);
                    border-radius:10px;display:flex;align-items:center;
                    justify-content:center;font-size:1.25rem;
                    border:1px solid rgba(255,255,255,.2);">🎬</div>
        <div>
          <div style="color:#fff;font-weight:800;font-size:1.15rem;
                      letter-spacing:-.3px;">CineAI</div>
          <div style="color:rgba(255,255,255,.55);font-size:0.7rem;
                      letter-spacing:.6px;text-transform:uppercase;">
            Movie Recommender</div>
        </div>
      </div>
    </div>

    <div style="padding:20px 0 0;">
      <div style="background:rgba(99,102,241,.08);border:1px solid rgba(99,102,241,.2);
                  border-radius:10px;padding:12px 14px;margin-bottom:20px;">
        <p style="color:#94a3b8 !important;font-size:0.8rem;line-height:1.7;margin:0;">
          <b style="color:#818cf8;">How it works:</b><br>
          1&nbsp; Pick genres below<br>
          2&nbsp; Adjust result filters<br>
          3&nbsp; Click <b style="color:#a5b4fc;">Get Recommendations</b>
        </p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Genre label ───────────────────────────────────────────────────────────
    st.markdown("""
    <p style="color:#475569 !important;font-size:0.68rem;font-weight:700;
              text-transform:uppercase;letter-spacing:1px;margin:0 0 8px;">
      Favourite Genres
    </p>""", unsafe_allow_html=True)

    selected_genres = st.multiselect(
        "genres",
        options=ALL_GENRES,
        default=[],
        placeholder="Select genres…",
        label_visibility="collapsed",
    )

    if selected_genres:
        st.markdown(
            '<div style="margin:8px 0 4px;">'
            + "".join(chip(g) for g in selected_genres)
            + '</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # ── Filters ───────────────────────────────────────────────────────────────
    st.markdown("""
    <p style="color:#475569 !important;font-size:0.68rem;font-weight:700;
              text-transform:uppercase;letter-spacing:1px;margin:0 0 10px;">
      Filters
    </p>""", unsafe_allow_html=True)

    top_n     = st.slider("Max results",          3, 25,  10, 1)
    min_score = st.slider("Minimum match score (%)", 0, 100, 0, 5)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    recommend_clicked = st.button("✦  Get Recommendations", use_container_width=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="margin-top:32px;padding-top:16px;
                border-top:1px solid #1a1b35;">
      <p style="color:#1e293b !important;font-size:0.7rem;line-height:1.8;margin:0;">
        <span style="color:#334155;">DecodeLabs Internship</span><br>
        Project 03 &middot; AI Recommendation Logic
      </p>
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# MAIN AREA
# ═════════════════════════════════════════════════════════════════════════════

# ── Load data ─────────────────────────────────────────────────────────────────
try:
    movies_df = load_movies("movies.csv")
except FileNotFoundError:
    st.error("⚠️  movies.csv not found. Place it in the same folder as app.py.")
    st.stop()

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:48px 0 40px;">
  <h1 style="color:#f8fafc !important;font-size:3rem;font-weight:900;
             line-height:1.1;margin:0 0 16px;letter-spacing:-1px;">
    Find Your Next<br>
    <span style="background:linear-gradient(135deg,#818cf8 0%,#c084fc 50%,#f472b6 100%);
                 -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                 background-clip:text;">Favourite Film</span>
  </h1>

  <p style="color:#475569 !important;font-size:1rem;max-width:500px;
            line-height:1.7;margin:0;">
    Select your preferred genres from the sidebar and let our
    recommendation engine surface the most relevant movies for you.
  </p>
</div>
""", unsafe_allow_html=True)

# ── STAT CARDS ────────────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
c1.metric("Movies in Catalogue", len(movies_df))
c2.metric("Available Genres",    len(ALL_GENRES))
c3.metric("Selected Genres",     len(selected_genres))

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
st.divider()

# ── WELCOME SCREEN ────────────────────────────────────────────────────────────
if not recommend_clicked:

    # Steps
    steps = [
        ("01", "#6366f1", "Choose Genres",
         "Pick one or more genres from the sidebar that match your taste."),
        ("02", "#8b5cf6", "Set Filters",
         "Control how many results to show and the minimum match score."),
        ("03", "#a78bfa", "Get Results",
         "Click Get Recommendations and explore your personalised list."),
    ]
    cols = st.columns(3)
    for col, (num, color, title, desc) in zip(cols, steps):
        col.markdown(f"""
        <div style="background:#0f0f1e;border:1px solid #1a1b35;
                    border-radius:16px;padding:28px 24px;height:100%;">
          <div style="width:36px;height:36px;background:rgba({hex_rgb(color)},.15);
                      border:1px solid rgba({hex_rgb(color)},.3);
                      border-radius:10px;display:flex;align-items:center;
                      justify-content:center;margin-bottom:16px;">
            <span style="color:{color};font-weight:800;font-size:0.85rem;">{num}</span>
          </div>
          <h4 style="color:#f1f5f9 !important;font-size:0.95rem;
                     font-weight:700;margin:0 0 8px;">{title}</h4>
          <p style="color:#475569 !important;font-size:0.82rem;
                    line-height:1.6;margin:0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

    # Genre showcase grid
    st.markdown("""
    <p style="color:#475569 !important;font-size:0.68rem;font-weight:700;
              text-transform:uppercase;letter-spacing:1px;margin:0 0 14px;">
      Available Genres
    </p>""", unsafe_allow_html=True)

    gcols = st.columns(len(ALL_GENRES))
    for col, genre in zip(gcols, ALL_GENRES):
        g = GM.get(genre, {"c": "#818cf8", "i": "🎬", "bg": "rgba(129,140,248,.1)"})
        col.markdown(f"""
        <div style="background:#0f0f1e;border:1px solid #1a1b35;
                    border-top:2px solid {g['c']};
                    border-radius:12px;padding:18px 8px;text-align:center;">
          <div style="font-size:1.5rem;margin-bottom:8px;">{g['i']}</div>
          <div style="color:#64748b;font-size:0.72rem;font-weight:600;
                      letter-spacing:.3px;">{genre}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

    with st.expander("📋  Browse Full Movie Catalogue"):
        st.dataframe(
            movies_df[["title","genre","year","rating","description"]].rename(columns={
                "title":"Title","genre":"Genre","year":"Year",
                "rating":"IMDb ⭐","description":"Description"
            }),
            use_container_width=True, hide_index=True,
        )
    st.stop()

# ── VALIDATION ────────────────────────────────────────────────────────────────
if not selected_genres:
    st.markdown("""
    <div style="background:#1c0a0a;border:1px solid rgba(239,68,68,.3);
                border-radius:12px;padding:16px 20px;
                display:flex;align-items:center;gap:14px;">
      <span style="font-size:1.3rem;">⚠️</span>
      <div>
        <div style="color:#fca5a5;font-weight:700;font-size:0.9rem;">
          No genres selected</div>
        <div style="color:#7f1d1d;font-size:0.82rem;margin-top:3px;">
          Please pick at least one genre from the sidebar panel.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ── COMPUTE ───────────────────────────────────────────────────────────────────
with st.spinner("Analysing your preferences…"):
    results_df = recommend(movies_df, selected_genres, top_n=top_n)

if not results_df.empty:
    results_df = results_df[results_df["score"] >= min_score].reset_index(drop=True)

# ── RESULTS HEADER ────────────────────────────────────────────────────────────
pills_html = "".join(chip(g) for g in selected_genres)
st.markdown(f"""
<div style="background:#0f0f1e;border:1px solid #1a1b35;border-radius:14px;
            padding:22px 28px;margin-bottom:28px;">
  <p style="color:#334155 !important;font-size:0.68rem;font-weight:700;
            text-transform:uppercase;letter-spacing:1px;margin:0 0 10px;">
    Showing results for
  </p>
  <div style="margin-bottom:12px;">{pills_html}</div>
  <p style="color:#334155 !important;font-size:0.82rem;margin:0;">
    <span style="color:#6366f1;font-weight:700;">{len(results_df)}</span>
    &nbsp;movie(s) matched your preferences
  </p>
</div>
""", unsafe_allow_html=True)

# ── NO RESULTS ────────────────────────────────────────────────────────────────
if results_df.empty:
    st.markdown("""
    <div style="background:#0f0f1e;border:1px solid #1a1b35;
                border-radius:16px;padding:52px;text-align:center;">
      <div style="font-size:2.8rem;margin-bottom:14px;">🔍</div>
      <h3 style="color:#f1f5f9 !important;font-size:1.1rem;margin:0 0 8px;">
        No results found</h3>
      <p style="color:#334155 !important;font-size:0.85rem;max-width:320px;
                margin:0 auto;">
        Try lowering the minimum score or picking different genres.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ── MOVIE CARDS ───────────────────────────────────────────────────────────────
MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}

for rank, (_, mv) in enumerate(results_df.iterrows(), start=1):
    g      = GM.get(mv["genre"], {"c": "#818cf8", "i": "🎬", "bg": "rgba(129,140,248,.1)"})
    gc     = g["c"]
    gi     = g["i"]
    gbg    = g["bg"]
    grgb   = hex_rgb(gc)
    medal  = MEDALS.get(rank, f"#{rank}")
    title  = mv["title"]
    year   = int(mv["year"])
    rating = mv["rating"]
    genre  = mv["genre"]
    desc   = mv["description"]
    bar_html = score_pill(mv["score"])

    card_top = (
        f'<div style="position:relative;background:#0f0f1e;border:1px solid #1a1b35;'
        f'border-radius:16px;padding:26px 30px 22px 34px;margin-bottom:16px;overflow:hidden;">'
        f'<div style="position:absolute;top:0;left:0;bottom:0;width:4px;'
        f'background:{gc};border-radius:16px 0 0 16px;"></div>'
        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;'
        f'flex-wrap:wrap;gap:10px;margin-bottom:12px;">'
        f'<div>'
        f'<span style="font-size:1.08rem;font-weight:800;color:#f8fafc;">'
        f'{medal}&nbsp; {title}</span>'
        f'<span style="color:#334155;font-size:0.78rem;margin-left:10px;">{year}</span>'
        f'</div>'
        f'<div style="display:flex;align-items:center;gap:6px;background:#1a1500;'
        f'border:1px solid #3d2f00;border-radius:8px;padding:5px 12px;">'
        f'<span style="color:#fbbf24;">★</span>'
        f'<span style="color:#fbbf24;font-size:0.85rem;font-weight:700;">{rating}</span>'
        f'<span style="color:#44330a;font-size:0.72rem;">IMDb</span>'
        f'</div></div>'
        f'<span style="display:inline-flex;align-items:center;gap:5px;background:{gbg};'
        f'color:{gc};border:1px solid rgba({grgb},.3);border-radius:8px;'
        f'padding:4px 12px;font-size:0.78rem;font-weight:600;">{gi}&nbsp;{genre}</span>'
    )
    card_bottom = (
        f'<p style="color:#475569;font-size:0.85rem;line-height:1.7;margin:12px 0 0;">'
        f'{desc}</p></div>'
    )

    st.markdown(card_top + bar_html + card_bottom, unsafe_allow_html=True)

# ── SUMMARY ROW ───────────────────────────────────────────────────────────────
st.divider()
s1, s2, s3 = st.columns(3)
s1.metric("Top Pick",      results_df.iloc[0]["title"])
s2.metric("Average Score", f"{results_df['score'].mean():.1f}%")
s3.metric("Total Shown",   len(results_df))

# ── CHART ─────────────────────────────────────────────────────────────────────
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
with st.expander("📊  Score Distribution Chart"):
    st.bar_chart(
        results_df[["title", "score"]].set_index("title"),
        color="#6366f1",
        height=280,
    )

# ── HINT ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:#0f0f1e;border:1px solid #1a1b35;
            border-radius:10px;padding:14px 20px;margin-top:20px;
            display:flex;align-items:center;gap:12px;">
  <span style="color:#6366f1;font-size:1rem;font-weight:700;">↩</span>
  <p style="color:#334155 !important;font-size:0.82rem;margin:0;">
    Want different results?&nbsp;
    <span style="color:#818cf8;font-weight:600;">
      Update your genre selection in the sidebar and click
      Get Recommendations again.
    </span>
  </p>
</div>
""", unsafe_allow_html=True)
