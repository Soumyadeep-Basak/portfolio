import streamlit as st
from datetime import datetime
import base64

# Page config
# Page config
st.set_page_config(
    page_title="Soumyadeep Basak - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make it look like shadcn/ui
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {
    position: fixed !important;
    top: 10px !important;
    right: 10px !important;
    z-index: 999 !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
}
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root variables (shadcn-like) */
   :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96%;
    --secondary-foreground: 222.2 84% 4.9%;
    --muted: 210 40% 96%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96%;
    --accent-foreground: 222.2 84% 4.9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.75rem;
    
    /* Custom shadow variables for consistency */
    --card-shadow: 0 2px 8px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.06);
    --card-shadow-hover: 0 8px 25px rgba(0, 0, 0, 0.12), 0 4px 10px rgba(0, 0, 0, 0.08);
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
    
    /* Global styles */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #f8fafc;
        color: hsl(var(--foreground));
    }
    
    .main .block-container {
        background: #f8fafc;
    }
    
    /* Hero section */
/* Hero section */
    .hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 5rem 2rem;
    border-radius: 16px;
    margin: 2rem 0;
    text-align: center;
    color: white;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    position: relative;
    overflow: hidden;
}
.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.15"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
    pointer-events: none;
}
.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
    background: linear-gradient(45deg, #fff, #e0e7ff, #c7d2fe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    position: relative;
    z-index: 1;
}
    
    .hero-subtitle {
        font-size: 1.25rem;
        opacity: 0.9;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    /* Card components */
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    width: 4px;
    background: var(--primary-gradient);
}
.card,
.education-card,
.contact-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: var(--radius);
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: var(--card-shadow);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out;
}
/* Consistent hover effects for all cards */
.card:hover,
.education-card:hover,
.contact-card:hover {
    box-shadow: var(--card-shadow-hover);
    transform: translateY(-4px);
    border-color: rgba(102, 126, 234, 0.2);
}
    
    
    .card-header {
        margin-bottom: 1rem;
    }
    
    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: hsl(var(--foreground));
        margin-bottom: 0.5rem;
    }
    
    .card-description {
        color: hsl(var(--muted-foreground));
        font-size: 0.875rem;
    }
    
    /* Button styles */
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: var(--radius);
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.5rem 1rem;
        text-decoration: none;
        transition: all 0.2s;
        border: none;
        cursor: pointer;
    }
    
    .btn-primary {
        background: hsl(var(--primary));
        color: hsl(var(--primary-foreground));
    }
    
    .btn-primary:hover {
        background: hsl(var(--primary) / 0.9);
        transform: translateY(-1px);
    }
    
    .btn-secondary {
        background: hsl(var(--secondary));
        color: hsl(var(--secondary-foreground));
        border: 1px solid hsl(var(--border));
    }
    
    .btn-secondary:hover {
        background: hsl(var(--accent));
    }
    
    /* Badge styles */
    .badge-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
    margin-top: 0.75rem;
}
.badge {
    display: inline-flex;
    align-items: center;
    border-radius: 9999px;
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 500;
    background: hsl(var(--secondary));
    color: hsl(var(--secondary-foreground));
    white-space: nowrap; /* Prevent text wrapping inside badges */
}
    
    /* Navigation */
    .nav-container {
        background: hsl(var(--card));
        border-bottom: 1px solid hsl(var(--border));
        padding: 1rem 2rem;
        margin-bottom: 2rem;
        position: sticky;
        top: 0;
        z-index: 100;
        backdrop-filter: blur(10px);
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .nav-brand {
        font-size: 1.5rem;
        font-weight: 700;
        color: hsl(var(--foreground));
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        color: hsl(var(--muted-foreground));
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s;
    }
    
    .nav-link:hover {
        color: hsl(var(--foreground));
    }
    
    /* Grid layouts */
    .grid {
        display: grid;
        gap: 1.5rem;
    }
    
    .grid-cols-1 { grid-template-columns: 1fr; }
    .grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
    .grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
    
    @media (max-width: 768px) {
    .grid-cols-2, .grid-cols-3 {
        grid-template-columns: 1fr;
    }
    .hero-title {
        font-size: 2.5rem;
    }
    .nav-links {
        display: none;
    }
    
    /* Add these for better mobile experience */
    .hero-section {
        padding: 3rem 1rem;
    }
    
    .section-header {
        font-size: 1.75rem;
        margin: 3rem 0 2rem 0;
    }
    
    .card {
        margin: 0.5rem 0;
        padding: 1.25rem;
    }
    
    .contact-card div {
        flex-direction: column;
        gap: 0.75rem;
    }
}
    
    /* Progress bars */
    .progress {
        width: 100%;
        height: 0.5rem;
        background: hsl(var(--secondary));
        border-radius: 9999px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2);
        transition: width 0.3s ease;
    }
    
    /* Timeline */
    .timeline-item {
    border-left: 2px solid hsl(var(--border));
    padding-left: 1.5rem;
    margin-bottom: 2.5rem; /* Increase from 2rem */
    position: relative;
    padding-bottom: 1rem; /* Add bottom padding */
}
.timeline-description {
    color: hsl(var(--muted-foreground));
    line-height: 1.6;
    margin-top: 0.5rem; /* Add top margin */
}
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: hsl(var(--primary));
    }
    
    .timeline-date {
        color: hsl(var(--muted-foreground));
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .timeline-title {
        font-size: 1.125rem;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    
    /* Contact section */
    .contact-card {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid hsl(var(--border));
        border-radius: var(--radius);
        padding: 2rem;
        text-align: center;
    }
    
    /* Section headers */
    /* Standardize section headers */
/* Update your .section-header styles */
.section-header {
    font-size: 2.25rem;
    font-weight: 700;
    text-align: center;
    margin: 4rem 0 3rem 0;
    color: hsl(var(--foreground));
    position: relative;
    z-index: 10; /* Add z-index to keep underline visible */
}
.section-header::after {
    content: '';
    position: absolute;
    bottom: -0.5rem;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 2px;
    z-index: 11; /* Higher z-index for underline */
}
    
    /* Education specific styles */
/* Update your education grid to ensure equal heights */
.education-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
    align-items: stretch; /* This ensures equal heights */
}
/* For the columns in Streamlit, add this to make them equal height */
.element-container:has(.education-card) {
    height: 100%;
}
    
   /* Replace the existing .education-card styles with: */
/* Replace your existing .education-card styles with: */
.education-card {
    background: hsl(var(--card)); /* Match other cards */
    border: 1px solid hsl(var(--border)); /* Match other cards */
    border-radius: var(--radius);
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05); /* Match other cards */
    transition: all 0.2s ease-in-out; /* Add hover transition */
    position: relative;
    overflow: hidden;
    height: 100%; /* Equal height */
    display: flex;
    flex-direction: column;
    z-index: 1; /* Lower z-index than header */
}
/* Add hover effect like other cards */
.education-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}
/* Keep the left border accent but make it match your theme */
.education-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2); /* Match your theme colors */
}
/* Fix the degree title styling */
.degree-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 0.75rem;
    color: hsl(var(--foreground)); /* Match other card titles */
    line-height: 1.4;
}
/* Fix school name styling */
.school-name {
    color: #667eea; /* Keep the accent color but make it consistent */
    font-weight: 500;
    margin-bottom: 0.5rem;
    font-size: 1rem;
}
/* Fix date styling */
.education-date {
    color: hsl(var(--muted-foreground)); /* Match other cards */
    font-size: 0.875rem;
    margin-bottom: 0.75rem;
    font-weight: 500;
}
/* Fix GPA badge styling */
.gpa {
    background: hsl(var(--secondary)); /* Match other badges */
    color: hsl(var(--secondary-foreground)); /* Match other badges */
    padding: 0.25rem 0.75rem;
    border-radius: 9999px; /* Match badge border radius */
    font-size: 0.75rem;
    font-weight: 500;
    display: inline-block;
    margin-bottom: 0.75rem;
}
    
    /* Responsive container */
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    /* Remove streamlit padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    /* Add smooth animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
@keyframes pulse {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
}
.card {
    animation: fadeInUp 0.6s ease-out;
    box-shadow: var(--card-shadow);
}
.card:hover {
    box-shadow: var(--card-shadow-hover);
    transform: translateY(-4px);
}
.btn:hover {
    animation: pulse 0.3s ease-in-out;
}
        
    }
</style>
""", unsafe_allow_html=True)


# JavaScript for smooth scrolling navigation (using HTML onclick instead)
st.markdown("""
<script>
function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({
        behavior: 'smooth'
    });
}
</script>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <div class="nav-content">
        <div class="nav-brand">Soumyadeep Basak</div>
        <div class="nav-links">
            <a onclick="document.getElementById('about').scrollIntoView({behavior: 'smooth'})" class="nav-link">About</a>
            <a onclick="document.getElementById('projects').scrollIntoView({behavior: 'smooth'})" class="nav-link">Projects</a>
            <a onclick="document.getElementById('experience').scrollIntoView({behavior: 'smooth'})" class="nav-link">Experience</a>
            <a onclick="document.getElementById('education').scrollIntoView({behavior: 'smooth'})" class="nav-link">Education</a>
            <a onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'})" class="nav-link">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="container">
    <div class="hero-section">
        <h1 class="hero-title">Machine Learning & Data Science Enthusiast</h1>
        <p class="hero-subtitle">Solving real-world problems with scalable ML systems</p>
        <div style="margin-top: 2rem;">
            <a onclick="document.getElementById('projects').scrollIntoView({behavior: 'smooth'})" class="btn btn-primary" style="margin: 0.5rem; cursor: pointer;">View Projects</a>
            <a onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'})" class="btn btn-secondary" style="margin: 0.5rem; cursor: pointer;">Get In Touch</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# About Section
st.markdown('<div class="container">', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h2 class="card-title">About Me</h2>
            <p class="card-description">Machine Learning | Data Science | Software Development</p>
        </div>
        <div>
            <p style="line-height: 1.6; margin-bottom: 1rem;">
                I am currently in my final year pursuing a B.Tech in Computer Science from Institute of Engineering and Management, Kolkata (GPA: 9.18). I enjoy building intelligent systems that blend deep learning, data engineering, and human-centric design.
            </p>
            <p style="line-height: 1.6;">
                From personalized recommender systems at WEBEL to gamified LMS platforms at IIT Ropar, my work spans across predictive modeling, backend systems, and research-driven design.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Skills</h3>
        </div>
        <div>
        <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between;">
                    <span>Machine Learning</span>
                    <span>80%</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 85%;"></div>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between;">
                    <span>Deep Learning</span>
                    <span>90%</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 85%;"></div>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between;">
                    <span>Time Series</span>
                    <span>92%</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 90%;"></div>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between;">
                    <span>Recommendation Systems</span>
                    <span>85%</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 85%;"></div>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between;">
                    <span>Computer Vision</span>
                    <span>80%</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 80%;"></div>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between;">
                    <span>NLP</span>
                    <span>80%</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 85%;"></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
# Technologies Section
# Technologies Section
# Technologies Section
st.markdown("""
<div class="card" style="margin-top: 2rem;">
    <div class="card-header">
        <h3 class="card-title">Technologies & Tools</h3>
        <p class="card-description">ML, Web Development, and Data Engineering Toolkit</p>
    </div>
    <div>
        <h4 style="margin: 1rem 0 0.5rem 0; font-weight: 600;">ML & Data Science</h4>
        <div style="margin-bottom: 1.5rem;">
            <span class="badge">TensorFlow</span>
            <span class="badge">Scikit-learn</span>
            <span class="badge">Keras</span>
            <span class="badge">Pandas</span>
            <span class="badge">NumPy</span>
            <span class="badge">OpenCV</span>
            <span class="badge">Matplotlib</span>
            <span class="badge">NLTK</span>
        </div>
        <h4 style="margin: 1rem 0 0.5rem 0; font-weight: 600;">Web</h4>
        <div style="margin-bottom: 1.5rem;">
            <span class="badge">Streamlit</span>
            <span class="badge">Flask</span>
            <span class="badge">FASTAPI</span>
            <span class="badge">HTML</span>
            <span class="badge">CSS</span>
        </div>
        <h4 style="margin: 1rem 0 0.5rem 0; font-weight: 600;">Cloud & DevOps</h4>
        <div>
            <span class="badge">AWS</span>
            <span class="badge">Git</span>
            <span class="badge">Jupyter Notebook</span>
        </div>
        <h4 style="margin: 1rem 0 0.5rem 0; font-weight: 600;">Databases</h4>
        <div>
            <span class="badge">MySQL</span>
            <span class="badge">PostgreSQL</span>
            <span class="badge">MongoDB</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Projects Section
st.markdown('<h2 class="section-header" id="projects">Featured Projects</h2>', unsafe_allow_html=True)

# Use columns instead of complex grid for better compatibility
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Smart-Captcha System</h3>
            <p class="card-description">Deep Learning • Anomaly Detection • Real-time Data</p>
        </div>
        <div>
            <p style="line-height: 1.6; margin-bottom: 1rem; color: hsl(var(--muted-foreground));">
                A frictionless security solution that analyzes real-time user behavior—like form input and mouse movement—to silently detect bots, triggering CAPTCHA only when necessary and significantly improving user experience.     </p>
            <div style="margin-bottom: 1rem;">
                <span class="badge">Python</span>
                <span class="badge">Tensorflow</span>
                <span class="badge">FastAPI</span>
                <span class="badge">Docker</span>
            </div>
            <div>
                <a href="#" class="btn btn-primary" style="margin-right: 0.5rem;">Live Demo</a>
                <a href="https://github.com/Soumyadeep-Basak/botv1" class="btn btn-secondary">GitHub</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    

    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">CryptoSecure</h3>
            <p class="card-description">Anomaly Detection • Backend • Blockhain •Real-time</p>
        </div>
        <div>
            <p style="line-height: 1.6; margin-bottom: 1rem; color: hsl(var(--muted-foreground));">
                A platform that assigns safety scores to crypto wallets by combining supervised (XGBoost) and unsupervised (Auto-Encoder) ML models with graph-based anomaly detection. The system factors in transaction behavior, wallet age, and KYC status to identify scam-linked wallets and assess risk in real time.
            </p>
            <div style="margin-bottom: 1rem;">
                <span class="badge">Python</span>
                <span class="badge">XgBoost</span>
                <span class="badge">Tensorflow</span>
                <span class="badge">FastAPI</span>
                <span class="badge">Redis</span>
            </div>
            <div>
                <a href="#" class="btn btn-primary" style="margin-right: 0.5rem;">Live Demo</a>
                <a href="https://github.com/Soumyadeep-Basak/htfHackermen" class="btn btn-secondary">GitHub</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Poly-Market Analyzer</h3>
            <p class="card-description">Deep Learning • Time Series </p>
        </div>
        <div>
            <p style="line-height: 1.6; margin-bottom: 1rem; color: hsl(var(--muted-foreground));">
                A resource-efficient stock forecasting tool using co-movement-based clustering and shared-layer-LSTM and Ticker-aware-LSTM with custom embeddings models to predict Nifty50 trends, enabling a single model to handle multiple stocks with high accuracy.
            </p>
            <div style="margin-bottom: 1rem;">
            <span class="badge">Python</span>
                <span class="badge">Tensorflow</span>
                <span class="badge">Statsmodel</span>
                <span class="badge">Streamlit</span>
            </div>
            <div>
                <a href="#" class="btn btn-primary" style="margin-right: 0.5rem;">Live Demo</a>
                <a href="#" class="btn btn-secondary">GitHub</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">SecureMind</h3>
            <p class="card-description">RAG • Chatbot • Blockchain </p>
        </div>
        <div>
            <p style="line-height: 1.6; margin-bottom: 1rem; color: hsl(var(--muted-foreground));">
                A secure, localized Retrieval-Augmented Generation (RAG) chatbot that integrates LLMs with document-based Q&A capabilities. It supports on-device model inference and utilizes IPFS (InterPlanetary File System) for decentralized storage providing enhanced security, privacy, and accessibility even in offline or remote environments.
            </p>
            <div style="margin-bottom: 1rem;">
                <span class="badge">Python</span>
                <span class="badge">Ethereum</span>
                <span class="badge">HuggingFace</span>
                <span class="badge">Llama.cpp</span>
                <span class="badge">Streamlit </span>
            </div>
            <div>
                <a href="#" class="btn btn-primary" style="margin-right: 0.5rem;">Live Demo</a>
                <a href="https://github.com/Soumyadeep-Basak/SecureMind" class="btn btn-secondary">GitHub</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Experience Section
# Experience Section
st.markdown("""
<div class="container">
    <h2 class="section-header" id="experience">Experience</h2>
    <div class="card">
        <div class="timeline-item">
            <div class="timeline-date">April 2025 - Present</div>
            <h3 class="timeline-title">Data Science Intern • WEBEL.</h3>
            <p class="timeline-description">
                Recommender System Development: Built a personalized hybrid recommender using user-based collaborative filtering on over 20M real service records, queried via PostgreSQL.<br> 
                Algorithm Engineering: Designed a multi-source similarity model combining demographics, historical usage, and service co-occurrence with rule-based eligibility filters to recommend from a pool of 313 government services.<br> 
                Interactive Deployment: Deployed a Streamlit-based dashboard for real-time recommendations with adaptive feedback loop for continuous personalization.
            </p>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">May 2024 - July 2024</div>
            <h3 class="timeline-title">Research Intern • IIT Ropar</h3>
            <p class="timeline-description">
                Built Google Sheets LMS: Developed a learning management system using Apps Script, automating academic data workflows and improving efficiency by 95%. <br>
                Web Integration: Created a Flask-based dashboard that visualized LMS statistics from Sheets and automated email notifications.<br>
                Gamification: Added badge rewards using proven strategies to improve user engagement.<br>
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Education Section - replace your existing education section with:
st.markdown('<h2 class="section-header" id="education">Education</h2>', unsafe_allow_html=True)

# Use columns for education cards with equal height containers
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="education-card">
        <h3 class="degree-title">Bachelor of Technology in Computer Science with specialization in artificial intelligence & machine learning</h3>
        <div class="school-name">Institute of Engineering and Management</div>
        <div class="education-date">2022 - 2026</div>
        <div class="gpa">GPA: 9.18/10.0</div>
        <p style="color: hsl(var(--muted-foreground)); line-height: 1.6; margin-bottom: 1rem; flex-grow: 1;">
            Specialized in Machine Learning and Artificial Intelligence with focus on practical applications and research.
        </p>
        <div>
            <span class="badge">Machine Learning</span>
            <span class="badge">Deep Learning</span>
            <span class="badge">NLP</span>
            <span class="badge">Computer Vision</span>
            <span class="badge">Time Series</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="education-card">
        <h3 class="degree-title">High Secondary (XII)</h3>
        <div class="school-name">Hariyana Vidya Mandir</div>
        <div class="education-date">2009 - 2022</div>
        <div class="gpa">X: 94% | XII: 91.66%</div>
        <p style="color: hsl(var(--muted-foreground)); line-height: 1.6; margin-bottom: 1rem; flex-grow: 1;">
            Studied in Science stream with focus on Physics, Chemistry, Mathematics, and Computer Science. Built strong foundation in analytical thinking and problem-solving.
        </p>
        <div>
            <span class="badge">Python</span>
            <span class="badge">Soft Skills</span>
            <span class="badge">Mathematics</span>
            <span class="badge">DBMS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
# Certifications section
# st.markdown("""
# <div style="margin-top: 2rem;">
#     <div class="card">
#         <div class="card-header">
#             <h3 class="card-title">Certifications & Achievements</h3>
#             <p class="card-description">Professional certifications and academic honors</p>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # Use columns for certifications
# cert_col1, cert_col2 = st.columns(2)

# with cert_col1:
#     st.markdown("""
#     <div class="card">
#         <h4 style="font-weight: 600; margin-bottom: 0.5rem;">Certifications</h4>
#         <ul style="list-style: none; padding: 0; color: hsl(var(--muted-foreground));">
#             <li style="margin-bottom: 0.5rem;">🏆 AWS Certified Machine Learning - Specialty (2023)</li>
#             <li style="margin-bottom: 0.5rem;">🏆 Google Cloud Professional ML Engineer (2022)</li>
#             <li style="margin-bottom: 0.5rem;">🏆 TensorFlow Developer Certificate (2021)</li>
#             <li style="margin-bottom: 0.5rem;">🏆 Deep Learning Specialization - Coursera (2020)</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)

# with cert_col2:
#     st.markdown("""
#     <div class="card">
#         <h4 style="font-weight: 600; margin-bottom: 0.5rem;">Academic Honors</h4>
#         <ul style="list-style: none; padding: 0; color: hsl(var(--muted-foreground));">
#             <li style="margin-bottom: 0.5rem;">🎓 Dean's List - All Semesters</li>
#             <li style="margin-bottom: 0.5rem;">🎓 Outstanding Graduate Student Award</li>
#             <li style="margin-bottom: 0.5rem;">🎓 Phi Beta Kappa Honor Society</li>
#             <li style="margin-bottom: 0.5rem;">🎓 Research Excellence Award</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)



# Contact Section
st.markdown("""
<h2 class="section-header" id="contact">Let's Connect</h2>
<div class="contact-card">
    <h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Ready to collaborate?</h3>
    <p style="color: hsl(var(--muted-foreground)); margin-bottom: 2rem;">
        I'm always open to discussing new opportunities and interesting projects.
    </p>
    <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a href="mailto:basaksoumyadeep04@gmail.com" class="btn btn-primary">📧 Email Me</a>
        <a href="https://www.linkedin.com/in/soumyadeep-basak-7609b2283/" class="btn btn-secondary">💼 LinkedIn</a>
        <a href="https://github.com/Soumyadeep-Basak/" class="btn btn-secondary">🐙 GitHub</a>
        <a href="https://drive.google.com/file/d/1ovSGe75oznr-4WffRPxj5AU2YUcauUR1/view?usp=sharing" class="btn btn-secondary">📄 Download CV</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; margin-top: 3rem; border-top: 1px solid hsl(var(--border)); color: hsl(var(--muted-foreground));">
    <p>© Soumyadeep Basak.</p>
</div>
""", unsafe_allow_html=True)