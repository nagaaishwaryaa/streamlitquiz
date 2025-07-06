import streamlit as st

# Set up page
st.set_page_config(page_title="Quiz Competition", page_icon="🧠")

st.title("🎯 Quiz Competition")
st.write("Answer the questions below and test your knowledge!")

# Define quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Mark Twain", "Leo Tolstoy", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"],
        "answer": "Carbon Dioxide"
    }
]

# Track score
score = 0

# Display each question
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    selected = st.radio("Choose an answer:", q['options'], key=i)

    if selected == q['answer']:
        score += 1

# Show result after submission
if st.button("Submit Quiz"):
    st.success(f"✅ You scored {score} out of {len(questions)}")
    st.balloons()
