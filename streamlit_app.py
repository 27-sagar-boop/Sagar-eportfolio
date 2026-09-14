import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Sagar | Financial Planning & Advisory",
    page_icon="assets/profile.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"

# ---------- helpers ----------
def img_to_base64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()

def file_bytes(path):
    return Path(path).read_bytes()

profile_b64 = img_to_base64(ASSETS / "profile.jpg")

# ---------- styling ----------
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', -apple-system, sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }
    .hero {
        display: flex;
        align-items: center;
        gap: 32px;
        margin-bottom: 8px;
    }
    .hero img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #1F2A44;
    }
    .hero-name {
        font-size: 34px;
        font-weight: 700;
        color: #1F2A44;
        margin-bottom: 4px;
    }
    .hero-headline {
        font-size: 16px;
        color: #4B5A6A;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #1F2A44;
        border-bottom: 2px solid #1F2A44;
        padding-bottom: 6px;
        margin-top: 36px;
        margin-bottom: 14px;
    }
    .card {
        background: #F7F8FA;
        border: 1px solid #E3E7EC;
        border-radius: 10px;
        padding: 18px 20px;
        margin-bottom: 14px;
    }
    .card-title {
        font-size: 17px;
        font-weight: 700;
        color: #1F2A44;
        margin-bottom: 4px;
    }
    .card-meta {
        font-size: 13px;
        color: #6B7686;
        margin-bottom: 8px;
    }
    .skill-badge {
        display: inline-block;
        background: #E9EEF5;
        color: #1F2A44;
        padding: 4px 12px;
        border-radius: 14px;
        font-size: 13px;
        margin: 3px 4px 3px 0;
    }
    .skill-group-label {
        font-size: 13px;
        font-weight: 700;
        color: #4B5A6A;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 10px;
        margin-bottom: 4px;
    }
    a.link-pill {
        display: inline-block;
        background: #1F2A44;
        color: #ffffff !important;
        text-decoration: none;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 14px;
        margin: 4px 6px 4px 0;
    }
    a.link-pill:hover { background: #35496B; }
    .contact-line {
        font-size: 14px;
        color: #4B5A6A;
        margin-bottom: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- hero ----------
st.markdown(
    f"""
    <div class="hero">
        <img src="data:image/jpeg;base64,{profile_b64}">
        <div>
            <div class="hero-name">Sagar</div>
            <div class="hero-headline">PGDM Finance | Financial Planning &amp; Portfolio Advisory | Building AI-Driven Financial Tools</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    I'm a PGDM Finance student at Fortune Institute of International Business (FIIB), focused on
    financial planning, investment research, and portfolio construction. During my Corporate Internship
    at AnytimeInvest Services, I worked directly with financial advisors — conducting risk profiling,
    building client investment recommendations, and eventually designing AI-driven tools to support
    advisor workflows and portfolio planning. I'm especially interested in the intersection of financial
    advisory and applied AI: using well-scoped tools and structured prompts to make financial planning
    faster and more consistent, without losing the human judgement responsible advice needs.
    """
)

col1, col2, col3, col4 = st.columns(4)
col1.markdown('<a class="link-pill" href="https://www.linkedin.com/in/sagar-takkar/" target="_blank">LinkedIn</a>', unsafe_allow_html=True)
col2.markdown('<a class="link-pill" href="https://github.com/27-sagar-boop" target="_blank">GitHub</a>', unsafe_allow_html=True)
col3.markdown('<a class="link-pill" href="https://niveshguide.netlify.app/" target="_blank">Try Nivesh Compass</a>', unsafe_allow_html=True)
with col4:
    st.download_button(
        "Download Resume",
        data=file_bytes(ASSETS / "Resume_Sagar.pdf"),
        file_name="Sagar_Resume.pdf",
        mime="application/pdf",
    )

# ---------- education ----------
st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <div class="card-title">Post Graduate Diploma in Management (PGDM), Finance</div>
        <div class="card-meta">Fortune Institute of International Business (FIIB) &nbsp;|&nbsp; 2025 – 2027</div>
    </div>
    <div class="card">
        <div class="card-title">Bachelor of Commerce (Hons.)</div>
        <div class="card-meta">University of Delhi &nbsp;|&nbsp; 2020 – 2023</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- skills ----------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

def badges(items):
    return "".join(f'<span class="skill-badge">{i}</span>' for i in items)

st.markdown('<div class="skill-group-label">Financial Planning & Advisory</div>', unsafe_allow_html=True)
st.markdown(badges([
    "Financial Planning", "Mutual Fund Advisory", "Risk Profiling",
    "Portfolio Construction", "Ratio & Financial Statement Analysis",
]), unsafe_allow_html=True)

st.markdown('<div class="skill-group-label">Analytical Skills</div>', unsafe_allow_html=True)
st.markdown(badges([
    "Technical & Fundamental Analysis", "Financial Data Interpretation", "Analytical Thinking",
]), unsafe_allow_html=True)

st.markdown('<div class="skill-group-label">Digital & AI Tools</div>', unsafe_allow_html=True)
st.markdown(badges([
    "MS Excel", "Power BI", "Python (Beginner)", "Generative AI Prompt Engineering",
]), unsafe_allow_html=True)

# ---------- projects ----------
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
        <div class="card-title">AdvisorPrep AI — Pre-Meeting Briefing Workflow</div>
        <div class="card-meta">Corporate Internship Program (CIP) Project &nbsp;|&nbsp; AnytimeInvest Services Private Limited</div>
        <p><b>Problem:</b> Financial advisors were spending 20–40 minutes per client manually drafting
        pre-meeting briefs from raw client portal data, with inconsistent quality under time pressure.</p>
        <p><b>What I did:</b> Designed a five-prompt ChatGPT workflow paired with a structured Excel
        input template that converts client data into a draft pre-meeting briefing — covering financial
        position, goal observations, portfolio notes, insurance adequacy, and a discussion agenda.</p>
        <p><b>Tools:</b> ChatGPT (prompt engineering), Excel, service blueprinting</p>
        <p><b>Output:</b> Cut advisor preparation time from 20–40 minutes to 5–8 minutes per client;
        demonstrated live to and validated by corporate mentor Ms. Ayushi Srivastava.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.download_button(
    "View CIP Report (PDF)",
    data=file_bytes(ASSETS / "CIP_Report_AdvisorPrep_AI.pdf"),
    file_name="CIP_Report_AdvisorPrep_AI.pdf",
    mime="application/pdf",
    key="cip_report",
)

st.markdown(
    """
    <div class="card" style="margin-top:14px;">
        <div class="card-title">Nivesh Compass — AI-Based Financial Planning Tool</div>
        <div class="card-meta">Self-built, deployed live</div>
        <p><b>Problem:</b> Retail investors rarely have an easy way to see how their risk appetite and
        investment amount translate into an actual asset allocation and a realistic range of returns.</p>
        <p><b>What I did:</b> Built and deployed a live interactive web application that takes a user's
        investment amount, risk appetite, and time horizon, and generates a suggested asset allocation
        across equity, debt, gold, and liquid categories with illustrative historical return ranges.</p>
        <p><b>Tools:</b> HTML, CSS, JavaScript, asset-allocation logic design</p>
        <p><b>Output:</b> A live, publicly accessible portfolio-planning tool.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('<a class="link-pill" href="https://niveshguide.netlify.app/" target="_blank">Try it live →</a>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card" style="margin-top:14px;">
        <div class="card-title">Financial Analysis: Maruti Suzuki Ltd. vs Tata Motors Ltd.</div>
        <div class="card-meta">Academic Project</div>
        <p>Analyzed 4-year financial statements using horizontal and vertical methods to compare growth,
        margins, costs, cash flows, EPS, dividends, and overall financial stability of the two companies.</p>
        <p><b>Tools:</b> MS Excel, ratio analysis</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- experience ----------
st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <div class="card-title">Corporate Intern, Mutual Fund Distribution & Client Advisory</div>
        <div class="card-meta">AnytimeInvest Services Private Limited, New Delhi &nbsp;|&nbsp; May – Jul 2026</div>
        <ul>
            <li>Conducted structured financial planning discussions with clients, evaluating income, goals,
            existing investments, and risk appetite to recommend suitable mutual fund and portfolio strategies.</li>
            <li>Performed risk profiling for 50 client relationships, aligning asset allocation with individual
            risk appetite and financial goals.</li>
            <li>Applied technical and fundamental analysis frameworks to evaluate equity and mutual fund
            options for portfolio construction; simulated a ₹25 lakh portfolio management exercise generating
            a ₹20,000–30,000 return within a week.</li>
            <li>Onboarded 50 clients onto the AnytimeInvest advisory platform and converted 2 to Prime
            Membership through personalized financial planning guidance.</li>
        </ul>
    </div>
    <div class="card">
        <div class="card-title">Social Immersion Program</div>
        <div class="card-meta">Believe in the Invisible &nbsp;|&nbsp; Summer 2026</div>
        <ul>
            <li>Aligned with UN SDG 3 (Good Health and Well-Being) and SDG 10 (Reduced Inequalities)
            through a Social Immersion Program.</li>
            <li>Observed and engaged with children with disabilities (0–8 years), gaining exposure to
            early intervention, therapy practices, and inclusive care approaches.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- certifications ----------
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
st.markdown(badges([
    "AI for Communication — LinkedIn Learning",
    "Power BI — LinkedIn Learning",
    "Excel — LinkedIn Learning",
    "Statistics Foundation — LinkedIn Learning",
    "Inventory Management Foundation — LinkedIn Learning",
    "Data Analyst Mindset — LinkedIn Learning",
]), unsafe_allow_html=True)

# ---------- contact ----------
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="contact-line">Email: connect.sagartakkar@gmail.com</div>
    <div class="contact-line">Phone: +91 8708740773</div>
    """,
    unsafe_allow_html=True,
)
col1, col2 = st.columns(2)
col1.markdown('<a class="link-pill" href="https://www.linkedin.com/in/sagar-takkar/" target="_blank">Connect on LinkedIn</a>', unsafe_allow_html=True)
col2.markdown('<a class="link-pill" href="https://github.com/27-sagar-boop" target="_blank">View GitHub</a>', unsafe_allow_html=True)
