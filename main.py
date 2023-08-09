from pathlib import Path
import streamlit as st
from PIL import Image

# Path settings
currDir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = currDir / "Styles" / "main.css"
resume_file = currDir / "Assets" / "PrinceSatyam.pdf"
profile_pic = currDir / "Assets" / "prince_pass_photo.jpeg"

# General settings
PAGE_TITLE = "Digital Resume | Prince Satyam"
PAGE_ICON = ":wave:"
NAME = "Prince Satyam"
DESCRIPTION = """
Software Professional with over 2+ years of experience in software development
"""
EMAIL = "satyamprince199@gmail.com"

SOCIAL_MEDIA = {
    "Email": "https://mail.google.com/mail/?view=cm&fs=1&to=" + EMAIL,
    "LinkedIn": "https://www.linkedin.com/in/prince-satyam"
}
PROJECTS = {
    "ATV": "Made a All Terrain Vehicle as my final year project, took it to ATVC and scored 3rd rank",
    "Banking System": "Python project to create a new account, check balance, deposit money, update account and so on just like Indian Banking System"
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
    - Develop, maintain and enhance the product as per clients' and market demands
    - Implement the API's and maintain it with the respective CAD systems
    - Also involved in QA works and automated maximum manual testing efforts
    - Leading the QA group, providing KT and guiding colleagues wherever required
    - Developed test cases using selenium for our web application
    - Ensure high performance of the application
    """
)

# Skills
st.write("#")
st.subheader("Skills")
st.write(
    """
    - Python
    - Data Structures & Algorithms
    - JavaScript
    - Selenium
    - Java (Basics)
    - CATIA
    """
)

# Work History
st.write("#")
st.subheader("Work History")
st.write("---")
# Jobs
st.write("Wipro, Pune")
st.write("Project Engineer")
st.write("July, 2021 - Present")
st.write(
    """
    - Develop, maintain and enhance the product as per clients' and market demands
    - Implement the API's and maintain it with the respective CAD systems
    - Also involved in QA works and automated maximum manual testing efforts
    - Leading the QA group, providing KT and guiding colleagues wherever required
    - Developed test cases using selenium for our web application
    - Ensure high performance of the application
    """
)

# Projects
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write("{} :".format(project))
    st.write("{}".format(link))

# Deploy this resume to the internet: To Do