import streamlit as st
# Skill-based mapping
skill_to_career = {
    "python": "Data Scientist",
    "machine learning": "ML Engineer",
    "deep learning": "AI Researcher",
    "web development": "Frontend Developer",
    "react": "Full Stack Developer",
    "java": "Backend Developer",
    "excel": "Data Analyst",
    "communication": "Sales Executive",
    "graphic design": "UI/UX Designer",
    "writing": "Content Writer",
    "teaching": "Educator",
    "sql": "Database Administrator",
    "linux": "System Administrator",
    "cloud": "Cloud Engineer",
    "android": "Mobile App Developer"
}

# MBTI-based mapping
mbti_to_careers = {
    "INTJ": ["Strategic Planner", "Software Architect", "Data Scientist"],
    "INFP": ["Writer", "Counselor", "Artist"],
    "ENFP": ["Creative Director", "Public Relations", "Life Coach"],
    "ISTJ": ["Accountant", "Analyst", "Auditor"],
    "ISFJ": ["Nurse", "Librarian", "Elementary Teacher"],
    "ENTP": ["Entrepreneur", "Marketing Manager", "Product Designer"],
    "ESTJ": ["Project Manager", "Operations Manager", "Military Officer"],
    "ESFP": ["Performer", "Event Planner", "Customer Support"]
}

#MBTI QUIZ FUNCTION

def get_mbti(ei, sn, tf, jp):
    mbti = ""
    mbti += "E" if ei == "Extroverted" else "I"
    mbti += "S" if sn == "Sensing" else "N"
    mbti += "T" if tf == "Thinking" else "F"
    mbti += "J" if jp == "Judging" else "P"
    return mbti

#CAREER SUGGESTION FUNCTION

def suggest_careers(skills_input, mbti_type):
    skills = [skill.strip().lower() for skill in skills_input.split(",")]
    skill_careers = {skill_to_career[skill] for skill in skills if skill in skill_to_career}
    personality_careers = set(mbti_to_careers.get(mbti_type, []))
    
    if skill_careers and personality_careers:
        matched = skill_careers & personality_careers
        if matched:
            return list(matched), mbti_type
        return list(skill_careers | personality_careers), mbti_type
    elif skill_careers:
        return list(skill_careers), mbti_type
    elif personality_careers:
        return list(personality_careers), mbti_type
    else:
        return ["No suitable career found. Try more skills or retake the quiz."], mbti_type

#STREAMLIT UI

st.set_page_config(page_title="Career Guidance with MBTI", layout="centered")
st.title("🎯 Career Guidance App with MBTI")
st.write("Enter your skills and take a short MBTI quiz to get career suggestions.")

#Skills Input
user_skills = st.text_input("🔧 Your Skills (comma-separated)", placeholder="e.g., Python, Communication, SQL")

#MBTI Quiz
st.subheader("🧠 MBTI Personality Quiz (Answer honestly!)")

ei = st.radio("1. Do you enjoy social gatherings?", ["Extroverted", "Introverted"])
sn = st.radio("2. Do you focus more on facts or ideas?", ["Sensing", "Intuitive"])
tf = st.radio("3. Are you more logical or empathetic in decisions?", ["Thinking", "Feeling"])
jp = st.radio("4. Do you prefer plans or spontaneity?", ["Judging", "Perceiving"])

#Suggest Careers
if st.button("🎯 Suggest Career"):
    if not user_skills.strip():
        st.warning("Please enter at least one skill.")
    else:
        mbti_type = get_mbti(ei, sn, tf, jp)
        suggestions, mbti_result = suggest_careers(user_skills, mbti_type)
        
        st.success(f"🧬 Your MBTI Personality Type: {mbti_result}")
        st.subheader("✅ Suggested Career(s):")
        for career in suggestions:
            st.markdown(f"- {career}")