import streamlit as st

st.set_page_config(
    page_title="Ali Faraz - ML Engineer", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fb 0%, #e8ecf8 50%, #f0e6ff 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #1a1a2e;
        min-height: 100vh;
    }
    
    [data-testid="stMainBlockContainer"] {
        padding: 3rem 1rem;
        max-width: 1200px;
    }
    
    h1 {
        font-family: 'JetBrains Mono', monospace;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff2d55 0%, #ff9500 50%, #30b0c0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 3rem;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255, 45, 85, 0.05), transparent);
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .glass-card:nth-child(1) {
        border-top: 3px solid #ff2d55;
    }
    
    .glass-card:nth-child(2) {
        border-top: 3px solid #ff9500;
    }
    
    .glass-card:nth-child(3) {
        border-top: 3px solid #30b0c0;
    }
    
    .glass-card:nth-child(4) {
        border-top: 3px solid #5ac8fa;
    }
    
    .glass-card:hover {
        border-color: rgba(255, 255, 255, 0.95);
        background: rgba(255, 255, 255, 0.9);
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.12);
    }
    
    .glass-card:hover::before {
        opacity: 1;
    }
    
    .project-title {
        font-size: 1.4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff2d55 0%, #ff9500 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.8rem;
        position: relative;
        z-index: 1;
    }
    
    .glass-card:nth-child(2) .project-title {
        background: linear-gradient(135deg, #ff9500 0%, #34c759 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .glass-card:nth-child(3) .project-title {
        background: linear-gradient(135deg, #30b0c0 0%, #5ac8fa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .glass-card:nth-child(4) .project-title {
        background: linear-gradient(135deg, #5ac8fa 0%, #9b59b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .project-desc {
        font-size: 0.95rem;
        color: #555;
        line-height: 1.7;
        margin-bottom: 1.2rem;
        position: relative;
        z-index: 1;
        font-weight: 400;
    }
    
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .tech-badge {
        background: linear-gradient(135deg, rgba(255, 45, 85, 0.1), rgba(255, 149, 0, 0.1));
        color: #ff2d55;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        border: 1px solid rgba(255, 45, 85, 0.2);
        font-weight: 600;
    }
    
    .glass-card:nth-child(2) .tech-badge {
        background: linear-gradient(135deg, rgba(255, 149, 0, 0.1), rgba(52, 199, 89, 0.1));
        color: #ff9500;
        border-color: rgba(255, 149, 0, 0.2);
    }
    
    .glass-card:nth-child(3) .tech-badge {
        background: linear-gradient(135deg, rgba(48, 176, 192, 0.1), rgba(90, 200, 250, 0.1));
        color: #30b0c0;
        border-color: rgba(48, 176, 192, 0.2);
    }
    
    .glass-card:nth-child(4) .tech-badge {
        background: linear-gradient(135deg, rgba(90, 200, 250, 0.1), rgba(155, 89, 182, 0.1));
        color: #5ac8fa;
        border-color: rgba(90, 200, 250, 0.2);
    }
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .divider {
        height: 1.5px;
        background: linear-gradient(90deg, transparent, rgba(255, 45, 85, 0.2), rgba(255, 149, 0, 0.2), transparent);
        margin: 4rem 0;
    }
    
    .connect-section {
        text-align: center;
        padding: 3rem 1rem;
    }
    
    .connect-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff2d55 0%, #ff9500 50%, #34c759 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
        letter-spacing: -0.5px;
    }
    
    .social-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }
    
    .quote-box {
        background: linear-gradient(135deg, rgba(255, 45, 85, 0.08), rgba(255, 149, 0, 0.08), rgba(52, 199, 89, 0.08));
        border-left: 4px solid;
        border-image: linear-gradient(180deg, #ff2d55 0%, #ff9500 50%, #34c759 100%) 1;
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        max-width: 600px;
        margin: 2rem auto;
        backdrop-filter: blur(15px);
        border-top: 1px solid rgba(255, 255, 255, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.8);
        border-bottom: 1px solid rgba(255, 255, 255, 0.8);
        box-shadow: 0 8px 32px rgba(255, 45, 85, 0.1);
    }
    
    .quote-text {
        font-size: 1.25rem;
        font-style: italic;
        color: #1a1a2e;
        margin-top: 0.8rem;
        font-weight: 500;
    }
    
    .quote-icon {
        font-size: 2rem;
    }
    
    footer {
        text-align: center;
        color: #999;
        font-size: 0.9rem;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1.5px solid rgba(255, 45, 85, 0.1);
    }
    
    [data-testid="stButton"] button {
        background: linear-gradient(135deg, #ff2d55 0%, #ff9500 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.85rem 1.8rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-family: 'Inter', sans-serif !important;
        box-shadow: 0 4px 15px rgba(255, 45, 85, 0.2) !important;
        font-size: 1rem !important;
    }
    
    [data-testid="stButton"] button:active {
        transform: scale(0.95) !important;
        box-shadow: 0 2px 8px rgba(255, 45, 85, 0.3) !important;
    }
    
    [data-testid="stButton"] button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 35px rgba(255, 45, 85, 0.3) !important;
    }
    
    h2 {
        color: #1a1a2e;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        margin: 2rem 0;
        letter-spacing: -0.5px;
    }
    
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem;
        }
        
        .projects-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .quote-box {
            padding: 1.5rem;
        }
        
        [data-testid="stButton"] button {
            padding: 0.7rem 1.5rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Ali Faraz</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Machine Learning Engineer | Deep Learning Specialist</div>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)

st.markdown("""<div class="projects-grid">""", unsafe_allow_html=True)

projects = [
    {
        "title": "💬 Sentiment Sense",
        "desc": "Advanced NLP pipeline using DistilBERT to extract sentiment and aspects from customer reviews.",
        "tags": ["Transformers", "PyTorch", "Hugging Face", "Streamlit"],
        "link": "https://sentiment-sense-ai.streamlit.app/"
    },
    {
        "title": "📈 AetherQuant Finance",
        "desc": "Real-time stock market analysis and sentiment tracking for data-driven investment decisions.",
        "tags": ["Pandas", "Plotly", "NumPy", "Streamlit"],
        "link": "https://aether-quant.streamlit.app/"
    },
    {
        "title": "🔍 Neural Lens",
        "desc": "Image recognition engine with ResNet50 identifying 1000+ object categories with 92%+ accuracy.",
        "tags": ["TensorFlow", "ResNet50", "Computer Vision", "Streamlit"],
        "link": "https://neural-lens.streamlit.app/"
    },
    {
        "title": "🏥 Diabetes Detector",
        "desc": "Medical diagnostic tool using Random Forest to predict health risks from clinical metrics.",
        "tags": ["Scikit-Learn", "ML", "Healthcare", "Streamlit"],
        "link": "https://diabetes-risk-diagnostic.streamlit.app/"
    }
]

cols = st.columns(2)
for idx, project in enumerate(projects):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="glass-card">
                <div class="project-title">{project['title']}</div>
                <div class="project-desc">{project['desc']}</div>
                <div class="tech-stack">
                    {''.join([f'<span class="tech-badge">{tag}</span>' for tag in project['tags']])}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.link_button("View Project →", project["link"], use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<div class='connect-section'>", unsafe_allow_html=True)
st.markdown("<div class='connect-title'>Let's Connect</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 Upwork", "https://www.upwork.com/freelancers/~017cd21f872163dffa?mp_source=share", use_container_width=True)
with col2:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/syed-m-ali-faraz", use_container_width=True)
with col3:
    st.link_button("📂 GitHub", "https://github.com/ali-faraz-py", use_container_width=True)

st.markdown("""
    <div class="quote-box">
        <span class="quote-icon">💡</span>
        <div class="quote-text">"A great developer knows the math behind the code"</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <footer>
        Made with ❤️ by Ali Faraz | © 2026
    </footer>
</div>
""", unsafe_allow_html=True)