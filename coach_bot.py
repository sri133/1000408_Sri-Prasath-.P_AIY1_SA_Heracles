+import streamlit as st
import google.generativeai as genai
import pandas as pd

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="CoachBot AI 🏆",
    page_icon="💪",
    layout="centered"
)

st.title("🏃‍♂️ CoachBot AI – Smart Fitness Assistant")
st.caption("AI-powered virtual coach for youth athletes")

### -------------------------------
### API SETUP
### -------------------------------
##api_key = st.sidebar.text_input("🔑 Enter Gemini API Key", type="password")
##
##if api_key:
##    genai.configure(api_key=api_key)

# -------------------------------
# USER INPUTS
# -------------------------------
st.subheader("👤 Athlete Profile")

sport = st.selectbox(
    "Sport",
    ["Football", "Cricket", "Basketball", "Athletics", "Badminton", "Hockey", "Calisthenics", ""]
)

position = st.text_input("Player Position (e.g., Striker, Bowler, Goalkeeper)")

injury = st.text_area(
    "Injury History / Risk Zone",
    placeholder="e.g., Knee strain, ankle sprain, none"
)

goal = st.selectbox(
    "Primary Goal",
    ["Build Stamina", "Increase Strength", "Post-Injury Recovery",
     "Speed & Agility", "Tactical Improvement"]
)

diet = st.selectbox(
    "Diet Preference",
    ["Vegetarian", "Non-Vegetarian", "Eggetarian", "Vegan"]
)

intensity = st.selectbox(
    "Training Intensity",
    ["Low", "Moderate", "High"]
)

# -------------------------------
# MODEL TUNING
# -------------------------------
st.subheader("🧪 AI Tuning (For Evaluation Evidence)")

temperature = st.slider(
    "Creativity vs Safety (Temperature)",
    0.1, 0.9, 0.3
)

# -------------------------------
# PROMPT ENGINEERING
# -------------------------------
def build_prompt():
    return f"""
You are CoachBot AI, a certified youth sports coach and fitness scientist.

Athlete details:
- Sport: {sport}
- Position: {position}
- Injury history: {injury}
- Training goal: {goal}
- Diet preference: {diet}
- Training intensity: {intensity}

Generate the following in clear sections:
1. Safe workout plan (position-specific)
2. Injury-aware precautions and recovery tips
3. Tactical or skill-based coaching advice
4. Nutrition and hydration guidance
5. Warm-up and cooldown routine

Use simple language suitable for young athletes.
Avoid unsafe or high-risk exercises.
"""

# -------------------------------
# AI RESPONSE
# -------------------------------
if st.button("🚀 Generate Training Plan"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    else:
        with st.spinner("CoachBot AI is thinking like a real coach..."):
            model = genai.GenerativeModel(
                model_name="gemini-1.5-pro",
                generation_config={
                    "temperature": temperature
                }
            )

            response = model.generate_content(build_prompt())
            st.success("✅ Personalized Coaching Plan Ready!")
            st.markdown(response.text)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("⚠️ Educational use only. Consult a professional coach or doctor for medical conditions.")




##import streamlit as st
##import google.generativeai as genai
##import pandas as pd
##from datetime import datetime
##
### --------------------------------------------------
### PAGE CONFIG
### --------------------------------------------------
##st.set_page_config(
##    page_title="CoachBot AI",
##    page_icon="🏋️",
##    layout="wide"
##)
##
### --------------------------------------------------
### API CONFIGURATION
### --------------------------------------------------
##genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
##model = genai.GenerativeModel("gemini-1.5-pro")
##
### --------------------------------------------------
### APP HEADER
### --------------------------------------------------
##st.title("🏋️ CoachBot AI")
##st.markdown(
##    """
##    **CoachBot AI** is a Generative AI–powered virtual sports coach designed for  
##    **young athletes** to receive **safe, personalized, and position-specific coaching**.
##    """
##)
##
### --------------------------------------------------
### SIDEBAR – USER PROFILE INPUT
### --------------------------------------------------
##st.sidebar.header("👤 Athlete Profile")
##
##age = st.sidebar.slider("Age", 10, 20, 15)
##sport = st.sidebar.selectbox(
##    "Sport",
##    ["Football", "Cricket", "Basketball", "Athletics", "Badminton", "Hockey"]
##)
##position = st.sidebar.text_input("Playing Position (e.g., Striker, Bowler)")
##injury = st.sidebar.text_input("Injury History / Risk Area (if any)")
##goal = st.sidebar.selectbox(
##    "Primary Training Goal",
##    [
##        "Build Stamina",
##        "Improve Strength",
##        "Post-Injury Recovery",
##        "Skill Improvement",
##        "Match Preparation"
##    ]
##)
##diet = st.sidebar.selectbox(
##    "Diet Preference",
##    ["Vegetarian", "Non-Vegetarian", "Vegan"]
##)
##
##temperature = st.sidebar.slider(
##    "Creativity Level (Model Temperature)",
##    0.3, 0.9, 0.7
##)
##
### --------------------------------------------------
### PROMPT ENGINEERING FUNCTIONS (10+ FEATURES)
### --------------------------------------------------
##def generate_prompt(task_type):
##    base_context = f"""
##    You are a certified youth sports coach and fitness expert.
##
##    Athlete Profile:
##    Age: {age}
##    Sport: {sport}
##    Position: {position}
##    Injury History: {injury}
##    Training Goal: {goal}
##    Diet Preference: {diet}
##
##    Important Rules:
##    - Be injury-aware and safety-focused
##    - Avoid medical diagnosis
##    - Use youth-friendly, motivational language
##    - Ensure progressive and realistic training
##    """
##
##    task_prompts = {
##        "Workout Plan": "Generate a position-specific workout plan.",
##        "Recovery Plan": "Create a safe post-injury recovery routine.",
##        "Warm-Up & Cooldown": "Design warm-up and cooldown routines.",
##        "Tactical Advice": "Provide tactical and decision-making tips.",
##        "Nutrition Plan": "Generate a weekly nutrition guide.",
##        "Mental Training": "Suggest mental focus and confidence techniques.",
##        "Hydration Strategy": "Provide hydration and electrolyte guidance.",
##        "Match-Day Prep": "Create a match-day preparation checklist.",
##        "Weekly Schedule": "Generate a 7-day balanced training schedule.",
##        "Injury Prevention": "Suggest injury prevention and mobility drills."
##    }
##
##    return base_context + "\nTask:\n" + task_prompts[task_type]
##
### --------------------------------------------------
### MAIN UI – FEATURE TABS
### --------------------------------------------------
##tabs = st.tabs([
##    "🏃 Workout",
##    "🩹 Recovery",
##    "🧠 Tactics",
##    "🥗 Nutrition",
##    "📅 Weekly Plan",
##    "🧘 Mental & Safety"
##])
##
### --------------------------------------------------
### TAB 1 – WORKOUT
### --------------------------------------------------
##with tabs[0]:
##    st.subheader("🏃 Personalized Workout Plan")
##
##    if st.button("Generate Workout Plan"):
##        prompt = generate_prompt("Workout Plan")
##        response = model.generate_content(
##            prompt,
##            generation_config={"temperature": temperature}
##        )
##        st.success("Workout Plan Generated")
##        st.write(response.text)
##
### --------------------------------------------------
### TAB 2 – RECOVERY
### --------------------------------------------------
##with tabs[1]:
##    st.subheader("🩹 Recovery & Injury-Safe Training")
##
##    if st.button("Generate Recovery Plan"):
##        prompt = generate_prompt("Recovery Plan")
##        response = model.generate_content(
##            prompt,
##            generation_config={"temperature": 0.3}
##        )
##        st.success("Recovery Plan Generated")
##        st.write(response.text)
##
### --------------------------------------------------
### TAB 3 – TACTICAL COACHING
### --------------------------------------------------
##with tabs[2]:
##    st.subheader("🧠 Tactical & Skill Improvement")
##
##    if st.button("Generate Tactical Advice"):
##        prompt = generate_prompt("Tactical Advice")
##        response = model.generate_content(
##            prompt,
##            generation_config={"temperature": temperature}
##        )
##        st.success("Tactical Advice Generated")
##        st.write(response.text)
##
### --------------------------------------------------
### TAB 4 – NUTRITION
### --------------------------------------------------
##with tabs[3]:
##    st.subheader("🥗 Nutrition Guidance")
##
##    if st.button("Generate Nutrition Plan"):
##        prompt = generate_prompt("Nutrition Plan")
##        response = model.generate_content(
##            prompt,
##            generation_config={"temperature": 0.6}
##        )
##        st.success("Nutrition Plan Generated")
##        st.write(response.text)
##
### --------------------------------------------------
### TAB 5 – WEEKLY PLAN (STRUCTURED OUTPUT)
### --------------------------------------------------
##with tabs[4]:
##    st.subheader("📅 Weekly Training Schedule")
##
##    if st.button("Generate Weekly Schedule"):
##        prompt = generate_prompt("Weekly Schedule")
##        response = model.generate_content(
##            prompt,
##            generation_config={"temperature": 0.5}
##        )
##
##        st.success("Weekly Plan Generated")
##        st.write(response.text)
##
### --------------------------------------------------
### TAB 6 – MENTAL + SAFETY
### --------------------------------------------------
##with tabs[5]:
##    st.subheader("🧘 Mental Training & Injury Prevention")
##
##    col1, col2 = st.columns(2)
##
##    with col1:
##        if st.button("Mental Training Tips"):
##            prompt = generate_prompt("Mental Training")
##            response = model.generate_content(
##                prompt,
##                generation_config={"temperature": 0.7}
##            )
##            st.write(response.text)
##
##    with col2:
##        if st.button("Injury Prevention Guide"):
##            prompt = generate_prompt("Injury Prevention")
##            response = model.generate_content(
##                prompt,
##                generation_config={"temperature": 0.3}
##            )
##            st.write(response.text)
##
### --------------------------------------------------
### FOOTER
### --------------------------------------------------
##st.markdown("---")
##st.caption(
##    "CoachBot AI | Built using Gemini 1.5 Pro | Educational Use Only | "
##    f"Session Time: {datetime.now().strftime('%d %b %Y %H:%M')}"
##)
