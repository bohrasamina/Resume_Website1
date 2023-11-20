from pathlib import Path
import streamlit as st

from PIL import Image

#---Path Settings--
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets"/ "profile-pic.png"

#--- General Settings---
Page_TITLE = "Digital CV | Samina Bohra"
Page_ICON = "wave:"
Name = "Samina Bohra"
Description = """
Software Tester
"""
Email = "samina1410@gmail.com"
Social_Media = {
    "LinkedIn" : "https://www.linkedin.com/in/samina-bohra/",
    "GitHub" : "https://github.com/",
}

st.set_page_config(page_title=Page_TITLE, page_icon=Page_ICON)

#---Load CSS, profile pic & PDF--
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


#----Hero Section---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label="⬇️ Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧",Email)

#----Social Links---
st.write("#")
cols = st.columns(len(Social_Media))
for index, (platform, link) in enumerate(Social_Media.items()):
    cols[index].write(f"[{platform}]({link})")


#----Experience & Qualification----
st.write("#")
st.subheader("Qualification")
st.write("""
Masters in Business Administration (2011-2013) - K.K.Wagh College of Management\n
Bachelors in Computer Science (2009-2011) - R.C.Patel College of ACS
""")

#---Skills---
st.write("#")
st.subheader("Skills")
st.write("""
         -Programming: Python, SQL.\n
         -Data Visualisation: PowerBi, Ms-Excel\n
         -Testing tools: Postman, Jira, Confluence, Bugzilla, Charles, Wireshark,CI/CD pipelines\n
         -Soft-skills: Adaptability, Critical Thinking, Leadership, Collaboration\n
         """)

#-----Work History---
st.write("#")
st.subheader("Work History")
st.write("-----")

#----Job 1
st.write("**Software Tester | TSYS Payment Solutions**")
st.write("12/2019 - 02/2023")
st.write("""
•	Conducted testing of REST API-based backend system called Spectrum\n
•	Performed API automation using Postman and JavaScript, utilizing the Newman command line collection runner\n
•	Hands on experience of testing API based front end and backend application developed on microservice Architecture.\n 
•	Using debugging tools like Charles and Wireshark to analyze API flows\n
•	Collaborated with cross-functional teams of solution Architect, Developers, Integration teams, Scrum Masters to ensure the quality and reliability of the deliverables.\n 
•	Expertly utilized defect tracking tools such as Jira and Confluence to identify, document, and manage issues.\n
•	Translated functional and non-functional requirements into comprehensive test cases.\n
•	Set up test data and executed test cases to validate system functionality and performance.\n
•	Managed bug reporting and tracking processes, facilitating effective resolution and closure.

""")
#----Job 2
st.write("#")
st.write("**Software Tester | JLT Group**")
st.write("12/2018 - 09/2029")
st.write("""
•	Strong understanding of manual testing methodologies, test case development, and execution.\n
•	Proficient in creating and maintaining test documentation, including test plans, test cases, and test reports.\n
•	Excellent problem-solving and analytical skills with a keen eye for detail.\n
•	Familiarity with various testing tools and bug tracking systems, such as JIRA, TestRail, and Bugzilla.\n
•	Collaborative team player with effective communication skills for reporting issues and collaborating with development teams.\n
•	Strong knowledge of software development life cycle (SDLC) and testing methodologies.\n
""")


#----Job 3
st.write("#")
st.write("**Associate | Ocwen Financial Ltd**")
st.write("01/2015 - 09/2016")
st.write("""
•	Research and solving customer queries related to insurance and tax.\n
•	Auditing client's escrow account.\n
•	Creating financial statements and providing it to clients.\n
•	Maintaining and updating financial records of clients.\n
•	Managing and keeping track of the client's financial data.\n
•	Ownership of sub-process which includes pulling data, distributing, accomplishment and submissions of daily task.\n
""")


