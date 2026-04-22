import streamlit as st

st.set_page_config(page_title="Portfolio Hub", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #FDFDFD;
    }
    
    /* This is the magic fix for alignment */
    [data-testid="stVerticalBlock"] > div:has(div.project-card) {
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .project-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #EAEAEA;
        /* Fixed height for the text area */
        height: 200px; 
        overflow: hidden;
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        border-color: #007BFF;
    }

    /* Ensures the badge area doesn't vary in height */
    .badge-container {
        height: 50px;
        margin-top: 10px;
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
    }

    .tech-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        background-color: #E3F2FD;
        color: #1976D2;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Software Solutions Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Python Developer | Machine Learning Engineer | Data Scientist</p>", unsafe_allow_html=True)

st.divider()

def project_card(title, desc, tags, link, color="#007BFF"):
    # We wrap everything in a container to manage the vertical flow
    container = st.container()
    with container:
        st.markdown(f"""
            <div class="project-card" style="border-top: 5px solid {color};">
                <h3 style="color: {color}; margin-top: 0;">{title}</h3>
                <p style="color: #444; font-size: 15px;">{desc}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Tags stay in their own fixed-height zone
        tag_html = "".join([f'<span class="tech-tag">{t}</span>' for t in tags])
        st.markdown(f'<div class="badge-container">{tag_html}</div>', unsafe_allow_html=True)
        
        # The button will now naturally align because the elements above it are height-constrained
        st.link_button(f"View {title} →", link, use_container_width=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    project_card(
        "Sentiment Sense: Aspect AI",
        "An advanced NLP pipeline using DistilBERT and Zero-Shot Classification to extract specific aspects (Food, Service, Price) and sentiment from text.",
        ["Transformers", "Hugging Face", "PyTorch", "Streamlit"],
        "https://sentiment-sense-ai.streamlit.app/",
        color="#00FFAA"
    )

    project_card(
        "AetherQuant Finance",
        "A quantitative finance tool for analyzing stock market trends and sentiment through real-time data streaming.",
        ["Pandas", "NumPy", "Plotly", "Streamlit"],
        "https://aether-quant.streamlit.app/",
        color="#29B5E8"
    )

with col2:
    project_card(
        "Diabetes Diagnostic Tool",
        "A medical diagnostic interface utilizing Random Forest classification to predict health risks from clinical metrics.",
        ["Scikit-Learn", "Streamlit", "Joblib"],
        "https://diabetes-risk-diagnostic.streamlit.app/",
        color="#00D26A"
    )
    
    project_card(
        "Real-Time Currency Converter",
        "A financial utility that fetches live exchange rates from external APIs to perform high-precision currency conversions.",
        ["Requests", "API Integration", "Python"],
        "https://github.com/ali-faraz-py/Python-CurrencyConverter",
        color="#8E44AD"
    )

st.divider()
st.subheader("Connect & Collaborate")

foot_col1, foot_col2, foot_col3 = st.columns(3)

with foot_col1:
    st.link_button("💼 Hire me on Upwork", "https://www.upwork.com/freelancers/~017cd21f872163dffa?mp_source=share", use_container_width=True)

with foot_col2:
    st.link_button("🔗 Connect on LinkedIn", "https://www.linkedin.com/in/syed-m-ali-faraz", use_container_width=True)

with foot_col3:
    st.link_button("📂 View Github Profile", "https://github.com/ali-faraz-py", use_container_width=True)

st.markdown("<p style='text-align: center; font-size: 12px; margin-top: 50px;'>A good developer knows the math behind the code.</p>", unsafe_allow_html=True)