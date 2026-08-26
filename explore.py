"""
L7 — Streamlit Exploration App  (STARTER)
===========================================
Run with:
    streamlit run solution.py

Your goal: build an interactive app called "Python Learning Journey" that
uses 5+ widget types and shows content that changes based on widget values.

KEY CONCEPT — The re-run model:
    Every time a user interacts with a widget, Streamlit re-executes the
    ENTIRE script from top to bottom. This means:
      • Widget functions (st.slider, st.selectbox, etc.) both RENDER the
        widget AND RETURN the current value in the same call.
      • Just use the returned value immediately — no event handlers needed.
      • Write code like a normal top-to-bottom Python script.

Widgets to use (at least 5):
    st.slider()       — returns a number (int or float)
    st.selectbox()    — returns one item from a list
    st.radio()        — returns one item from a list (shown as radio buttons)
    st.multiselect()  — returns a list of selected items
    st.text_input()   — returns a string
    st.checkbox()     — returns True or False
"""

import streamlit as st

# ── Page configuration ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="Python Learning Journey",
    page_icon="🐍",
    layout="centered",
)

st.title("🐍 Python Learning Journey")
st.caption("Adjust the widgets to explore your progress and learning path.")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 1 — st.slider
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("1. Experience Level")

weeks = st.slider("How many weeks have you been coding?", min_value=0, max_value=52, value=8, step=1)

if weeks == 52:
    level_label = "Advanced"
elif weeks >= 36:
    level_label = "Intermediate"
else: level_label = "Beginner"

st.metric(label="Experience Level: ", value=level_label, delta=f"weeks")



st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 2 — st.selectbox
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("2. Current Topic")

topic = st.selectbox("Choose a topic:", ["variables", "lambdas", "pandas", "SQLAlchemy", "lists"])

tips = {
    "variables": "Variables store values so you can reuse and update data in your program.",
    "lambdas": "Lambda functions are short, anonymous functions written in a single expression.",
    "pandas": "Pandas is a Python library for loading, analyzing, and transforming tabular data.",
    "SQLAlchemy": "SQLAlchemy lets Python applications interact with SQL databases using Python objects and queries.",
    "lists": "Lists are ordered, changeable collections that can store multiple values.",
}

st.write(f"{tips[topic]}")
    
    

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 3 — st.radio
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("3. Learning Style")

style = st.radio(
    "What is your preferred learning style for computer programming?",
    ["Reading docs", "Watching videos", "Building projects", "Pair programming"],
    horizontal=True
)

# Match each preferred learning style with a helpful coding resource.
resources = {
    "Reading docs": "Python official documentation: docs.python.org",
    "Watching videos": "Corey Schafer's Python tutorials on YouTube",
    "Building projects": "Real Python project tutorials: realpython.com",
    "Pair programming": "Exercism's Python track with community mentoring",
}
# Display a learning resource recommendation based on the selected style.
st.info(f"Recommended resource: {resources[style]}")


st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 4 — st.multiselect
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("4. Tools & Libraries You Use")

selected_tools = st.multiselect(
    "What are your preferred tools?",
    ["pandas", "FastAPI", "Streamlit", "SQLite", "requests"], default=["requests", "Streamlit"],
)

if selected_tools:
    st.write("Your toolkit:")
    for tool in selected_tools:
        st.write(f"✅ {tool}")
else:
    st.warning("Select at least one tool to see your toolkit!")



st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 5 — st.text_input
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("5. Project Idea Generator")

project_keyword = st.text_input("Enter a keyword to generate project ideas:", placeholder="Type here...")

if project_keyword:
    st.write(f"A {project_keyword} tracker that stores data in SQLite.")
    st.write(f"A {project_keyword} quiz app that tests the user's knowledge.")
    st.write(f"A {project_keyword} dashboard that displays useful statistics.")
else:
    st.info("Enter a keyword to generate project ideas.")
    


st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 6 — st.checkbox
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("6. Progress Summary")


show_summary = st.checkbox("Show my personalized learning summary", value=True)

st.success(
    f"Well done! You have been coding for {weeks} weeks. You are committed to learning more about {topic}. You have a solid understanding of your pereferred '{style}' learning style, and you now know there are great resources you can explore ({resources[style]}). The next step can be to utilize your toolkit ({selected_tools}) to begin working on one of the generated project ideas based on your interest in {project_keyword}. Wishing you much success!"
)
