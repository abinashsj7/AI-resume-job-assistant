import streamlit as st
from utils import analyze_resume

st.set_page_config(page_title="AI Resume Assistant")

st.title("AI Resume & Job Readiness Assistant")
st.write("Improve your resume and job readiness using AI")

resume_text = st.text_area(
    "Paste your resume here",
    height=200,
    placeholder="Paste resume text..."
)

job_role = st.text_input(
    "Target Job Role",
    placeholder="e.g. Data Analyst, Software Engineer"
)

if st.button("Analyze Resume"):
    if resume_text.strip() == "" or job_role.strip() == "":
        st.warning("Please provide both resume and job role.")
    else:
        with st.spinner("Analyzing resume with AI..."):
            result = analyze_resume(resume_text, job_role)
            st.subheader("AI Analysis Result")
            st.write(result)
