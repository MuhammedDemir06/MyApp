import streamlit as st
from github import Github
import random

st.set_page_config(page_title='Muhammed\'s Portfolio', layout="wide", page_icon='👨‍🔬')

st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
    visibility: hidden;
}
.css-1v8iw71.eknhn3m4
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html= True)

st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
    visibility: hidden;
}
.css-1v8iw71.eknhn3m4
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html= True)

info = {
    'name': 'Muhammed Demir',
    'Mobile': '8103795345',
    'Email': 'muhammed.demir3406@gmail.com',
    'skills': ["C#", "Python", "Unity", "Game Development"],
    'youtube_url': 'https://youtube.com/@muhammed0_dem?si=5rC5gDIiVXMC-bDR',
    "fiver": "https://www.fiverr.com/s/yvWoZye",
    "linkedin": "https://www.linkedin.com/in/muhammed-demir-945625311?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "instagram": "https://www.instagram.com/muhammed.demir.0?igsh=cWUwN3Z3aXAxZXln",
    "github": "https://github.com/MuhammedDemir06",
    "facebook": "https://www.facebook.com/share/DKvv5gRAuRysBNEG/?mibextid=qi2Omg",
}

about = "I have dedicated the past two years of my career to honing my skills as a game developer specializing in artificial intelligence development. Driven by an insatiable curiosity for technology and innovation, I am deeply committed to continuously improving my expertise while staying at the forefront of industry advancements. This passion extends beyond professional obligation; it is a personal pursuit that fuels my enthusiasm for creating and contributing to cutting-edge projects in both the gaming and artificial intelligence domains."

st.subheader('About me')
st.write(about)

st.subheader('Skills & Tools ⚒️')

def skill_tab():
    rows, cols = len(info['skills']) // 5, 5
    skills = iter(info['skills'])
    if len(info['skills']) % 5 != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(5)
        for index_ in range(5):
            try:
                columns[index_].button(next(skills))
            except:
                break

with st.spinner(text="Loading section..."):
    skill_tab()

def get_github_project_links(username, token=None):
    if token:
        g = Github(token)
    else:
        g = Github()  # If you're using this script for personal use, you might not need a token

    user = g.get_user(username)
    repos = user.get_repos()

    project_links = [repo.html_url for repo in repos]

    return project_links

def show_github_projects(links):
    for link in links:
        label = link.split("/")[-1]
        # Choose a random colorful emoji
        emojis = ["🌟", "💡", "🔥", "💻", "👩‍💻"]
        emoji = random.choice(emojis)
        # Create shield badge markdown with colorful emoji
        shield_badge = f'[![GitHub Project: {label}](https://img.shields.io/badge/GitHub-{label}-blue)]({link}) {emoji}'
        # Display shield badge
        st.markdown(shield_badge, unsafe_allow_html=True)

st.subheader("Projects")
github_username = "MuhammedDemir06"
if st.button("Fetch GitHub Repositories"):
    links = get_github_project_links(github_username)
    show_github_projects(links)

st.subheader("Links")

st.markdown("""
    <style>
    .link-button {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        font-size: 16px;
        font-weight: bold;
        color: white;
        text-align: center;
        text-decoration: none;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .link-icon {
        margin-right: 8px;
    }
    .youtube {
        background-color: #FF0000;
    }
    .fiverr {
        background-color: #1DBF73;
    }
    .linkedin {
        background-color: #0077B5;
    }
    .instagram {
        background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
    }
    .github {
        background-color: #333;
    }
    .facebook {
        background-color: #1877F2;
    }
    .link-button:hover {
        opacity: 0.3;
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <div>
        <a href='https://youtube.com/@muhammed0_dem?si=5rC5gDIiVXMC-bDR' class='link-button youtube'>
            <i class='fab fa-youtube link-icon'></i>YouTube
        </a>
        <a href='https://www.fiverr.com/s/yvWoZye' class='link-button fiverr'>
            <i class='fas fa-briefcase link-icon'></i>Fiverr
        </a>
        <a href='https://www.linkedin.com/in/muhammed-demir-945625311?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app' class='link-button linkedin'>
            <i class='fab fa-linkedin link-icon'></i>LinkedIn
        </a>
        <a href='https://www.instagram.com/muhammed.demir.0?igsh=cWUwN3Z3aXAxZXln' class='link-button instagram'>
            <i class='fab fa-instagram link-icon'></i>Instagram
        </a>
        <a href='https://github.com/MuhammedDemir06' class='link-button github'>
            <i class='fab fa-github link-icon'></i>GitHub
        </a>
        <a href='https://www.facebook.com/share/DKvv5gRAuRysBNEG/?mibextid=qi2Omg' class='link-button facebook'>
            <i class='fab fa-facebook link-icon'></i>Facebook
        </a>
    </div>
    """, unsafe_allow_html=True)

st.subheader('Wish to connect?')
st.markdown(f'📧: {info["Email"]}')