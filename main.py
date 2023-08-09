from pathlib import Path
import streamlit as st
from PIL import Image

# Path settings
currDir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = currDir / "Styles" / "main.css"
resume_file = currDir / "Assets" / "Prince_Satyam_Resume.pdf"
profile_pic = currDir / "Assets" / "prince_pass_photo.jpeg"

# General settings
PAGE_TITLE = "Digital Resume | Prince Satyam"
PAGE_ICON = ":wave:"
NAME = "Prince Satyam"
DESCRIPTION = """
Experienced Software Engineer with a proven track record in software development spanning over 2+ years
"""
EMAIL = "satyamprince199@gmail.com"

SOCIAL_MEDIA = {
    "Email": "https://mail.google.com/mail/?view=cm&fs=1&to=" + EMAIL,
    "LinkedIn": "https://www.linkedin.com/in/prince-satyam"
}
PROJECTS = {
    "- ATV": "Made a All Terrain Vehicle as my final year project, took it to ATVC and scored 3rd rank",
    "- Banking System": "Developed a Python script that simulates an Indian Banking System, enabling functions such as creating a new account, checking balance, depositing money, updating account information and so on."
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF & PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    # st.write("",EMAIL)

# Social media links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for idx, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[idx].write(f"[{platform}]({link})")

# Exprience & Qualifications
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    Software professional with over 2+ years of experience and proven knowledge in Software Development, highly skilled in brainstorming and coding features & enhancements. Possesses an understanding of developing end-to-end applications as per client requirements and quality norms. Also adaptive at looking after QA works and developing testing frameworks.
    """
)
st.write(
    """
    - B.Tech ( Mechanical || 2017 - 2021 || 81.50%)
    Lakshmi Narain College Of Technology, Bhopal, Madhya Pradesh
    - Xll ( PCM || 2014 - 2016 || 77.80%)
    St. Joseph's School, NTPC, Kahalgaon, Bihar
    - X (2013 - 2014 || 8.8 cgpa )
    DAV Public School, NTPC, Kahalgaon, Bihar
    """
)

# Work History
st.write("#")
st.subheader("Work History")
st.write("---")
# Jobs
st.write("Wipro, Bangalore")
st.write("Project Engineer")
st.write("July, 2021 - Present")
st.write(
    """
    - Software Development: I am accountable for the development, maintenance, and continuous improvement of our desktop application in accordance with the specific requirements of clients and market demands.
    - UI Enhancement and Feature Development: I am involved in enhancing the user interfaces (UIs) and introducing new features to the application using Python, thereby enriching the user experience and meeting evolving market expectations
    - CAD Integration: I collaborate with various CAD APIs and proficiently integrate them into our product using C++. This enables in gaining a comprehensive understanding of diverse CAD Models along with their features and properties into our application.
    - Diagnostic Development: I design and implement complex diagnostics using Python, aimed at evaluating the suitability of models for production. These diagnostics are critical in identifying potential defects and ensuring the production of high-quality models.
    - QA and Test Automation: I actively contributed to quality assurance efforts by automating numerous manual testing processes in the past, leading to improved efficiency and reliability. Additionally, I have played a key role in leading the QA group, imparting knowledge on development and QA activities, and providing guidance to colleagues as needed.
    - Selenium Test Cases: I have developed test cases using Selenium for our web application, contributing to the comprehensive testing and validation of its functionalities.
    - Performance Optimization: I am dedicated to ensuring high performance and optimal functionality of the application, constantly striving to enhance its overall efficiency and responsiveness.
    """
)

# Skills
st.write("#")
st.subheader("Skills")
st.write(
    """
    - Python
    - Python Software Development & Python Application Programming
    - Data Structures & Algorithms
    - C++
    - C++ Application Programming
    - JavaScript
    - Selenium
    - Rest APIs
    - JSON
    - XML
    - CAD APIs
    - CAD Systems (CATIA, SolidWorks, NX, Creo, Inventor, A3D, JT & STEP)
    - Backend Development
    - Agile
    - Scrum
    """
)

# Projects
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write("{} :".format(project))
    st.write("{}".format(link))

# What's going on currently
st.write("#")
st.subheader("In-Progress Tasks")
st.write("---")
st.write("- Data Science Learning Journey")
st.write("""
      Actively enhancing skills in data science through self-directed learning and online courses.
      Gaining proficiency in key data science concepts, including Data analysis and visualization,
      Machine learning algorithms and techniques,
      Statistical analysis and hypothesis testing,
      Data preprocessing and cleaning.
      Exploring real-world datasets to apply theoretical knowledge and gain practical insights.
""")
st.write("- Creating Movie Recommender System")
st.write("""
    By utilizing the skills of data science, I am creating a webpage which can suggests movies to users based on their preferences
""")

# Deploy this resume to the internet