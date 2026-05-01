import streamlit as st

st.set_page_config(page_title="Portfolio Hub", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    :root {
        color-scheme: light;
    }

    .stApp {
        background: linear-gradient(180deg, #F6F8FF 0%, #FFFFFF 45%, #F8FBFF 100%);
        color: #111827;
        font-family: 'Inter', sans-serif;
    }

    .hero-card,
    .project-card,
    .contact-card {
        background: rgba(255, 255, 255, 0.96);
        border: 1px solid rgba(15, 23, 42, 0.08);
        border-radius: 22px;
        box-shadow: 0 20px 60px rgba(15, 23, 42, 0.08);
        padding: 32px;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .project-card:hover,
    .contact-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 28px 80px rgba(15, 23, 42, 0.12);
    }

    .hero-title {
        font-size: 3.35rem;
        font-weight: 800;
        line-height: 1.05;
        letter-spacing: -0.04em;
        margin: 0;
    }

    .hero-subtitle {
        color: #475569;
        font-size: 1.15rem;
        line-height: 1.8;
        max-width: 760px;
        margin: 1rem 0 0;
    }

    .key-metrics {
        display: grid;
        grid-template-columns: repeat(3, minmax(120px, 1fr));
        gap: 16px;
        margin-top: 32px;
    }

    .metric {
        background: #F8FAFC;
        border-radius: 16px;
        padding: 18px 20px;
        text-align: center;
    }

    .metric h3 {
        margin: 0 0 6px;
        font-size: 1.4rem;
        color: #0F172A;
    }

    .metric p {
        margin: 0;
        color: #64748B;
        font-size: 0.95rem;
    }

    .section-title {
        font-size: 1.65rem;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .project-card {
        padding: 28px;
        min-height: 320px;
    }

    .project-card h3 {
        margin: 0 0 14px;
        font-size: 1.35rem;
    }

    .project-card p {
        color: #334155;
        line-height: 1.75;
        margin-bottom: 18px;
        font-size: 0.98rem;
    }

    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 20px;
    }

    .tech-tag {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 8px 14px;
        border-radius: 999px;
        background: #EEF2FF;
        color: #4338CA;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(79, 70, 229, 0.12);
    }

    .project-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 56px;
        height: 56px;
        border-radius: 18px;
        margin-bottom: 20px;
        font-size: 1.2rem;
    }

    .primary-button {
        background: #312E81;
        color: #FFFFFF !important;
        border-radius: 999px;
        padding: 12px 22px;
        font-weight: 700;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .primary-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 30px rgba(59, 56, 154, 0.18);
    }

    .contact-card {
        text-align: center;
    }

    .contact-card h4 {
        margin: 0 0 10px;
        font-size: 1.05rem;
    }

    .contact-card p {
        margin: 0;
        color: #475569;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='hero-card'>"
    "<div style='display:flex;flex-direction:column;gap:24px;'>"
    "<div>"
    "<p style='margin:0;color:#4338CA;font-weight:700;font-size:0.95rem;letter-spacing:0.16em;text-transform:uppercase;'>Portfolio Showcase</p>"
    "<h1 class='hero-title'>Crafting modern software, intelligent products, and growth-focused experiences.</h1>"
    "<p class='hero-subtitle'>I build scalable Python applications, machine learning tools, and data-driven solutions for startups and enterprises. Explore projects that blend clean code, strong design, and real-world results.</p>"
    "</div>"
    "<div class='key-metrics'>"
    "<div class='metric'><h3>12+</h3><p>Projects launched</p></div>"
    "<div class='metric'><h3>7+</h3><p>Industry domains</p></div>"
    "<div class='metric'><h3>95%</h3><p>Client satisfaction</p></div>"
    "</div>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Featured Projects</h2>", unsafe_allow_html=True)


def project_card(title, desc, tags, link, color, icon):
    st.markdown(
        f"""
        <div class='project-card'>
            <div class='project-badge' style='background: {color}20; color: {color};'>
                {icon}
            </div>
            <h3>{title}</h3>
            <p>{desc}</p>
            <div class='badge-container'>
                {''.join([f'<span class="tech-tag">{t}</span>' for t in tags])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<a class='primary-button' href='{link}' target='_blank'>View Project →</a>",
        unsafe_allow_html=True,
    )

col1, col2 = st.columns(2, gap='large')
with col1:
    project_card(
        title='Sentiment Sense: Aspect AI',
        desc='An NLP platform with DistilBERT and Zero-Shot classification that extracts food, service, and price sentiment from reviews.',
        tags=['Transformers', 'Hugging Face', 'PyTorch', 'Streamlit'],
        link='https://sentiment-sense-ai.streamlit.app/',
        color='#0B79F7',
        icon='🧠',
    )
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    project_card(
        title='AetherQuant Finance',
        desc='A quantitative finance analytics tool for market signals, sentiment scoring and portfolio visualization.',
        tags=['Pandas', 'NumPy', 'Plotly', 'Streamlit'],
        link='https://aether-quant.streamlit.app/',
        color='#1E3A8A',
        icon='📈',
    )

with col2:
    project_card(
        title='Neural Lens: Vision AI',
        desc='A ResNet50-based vision engine that identifies over 1,000 object categories with high accuracy and confidence scoring.',
        tags=['TensorFlow', 'Keras', 'ResNet50', 'Image Classification'],
        link='https://neural-lens.streamlit.app/',
        color='#D946EF',
        icon='🔍',
    )
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    project_card(
        title='Diabetes Diagnostic Tool',
        desc='A predictive health dashboard using Random Forest to identify risk factors and support clinical decisions.',
        tags=['Scikit-Learn', 'Streamlit', 'Joblib'],
        link='https://diabetes-risk-diagnostic.streamlit.app/',
        color='#059669',
        icon='🩺',
    )

st.markdown("<div style='height: 36px;'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Connect & Collaborate</h2>", unsafe_allow_html=True)

foot_col1, foot_col2, foot_col3 = st.columns(3, gap='large')

with foot_col1:
    st.markdown(
        """
        <div class='contact-card'>
            <h4>Hire me</h4>
            <p>Freelance contracts, product builds, and AI consulting.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<a class='primary-button' href='https://www.upwork.com/freelancers/~017cd21f872163dffa?mp_source=share' target='_blank'>Upwork Profile</a>", unsafe_allow_html=True)

with foot_col2:
    st.markdown(
        """
        <div class='contact-card'>
            <h4>Network</h4>
            <p>Let's connect and talk about the next product idea.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<a class='primary-button' href='https://www.linkedin.com/in/syed-m-ali-faraz' target='_blank'>LinkedIn Profile</a>", unsafe_allow_html=True)

with foot_col3:
    st.markdown(
        """
        <div class='contact-card'>
            <h4>Explore code</h4>
            <p>Open-source projects, reproducible notebooks, and engineering samples.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<a class='primary-button' href='https://github.com/ali-faraz-py' target='_blank'>Github Profile</a>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #475569; margin-top: 44px; font-size: 0.95rem;'>A good developer knows the math behind the code — and designs solutions that feel polished.</p>", unsafe_allow_html=True)
