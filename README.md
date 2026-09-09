# Syed Ali Faraz — Portfolio Hub

A single-page portfolio site showcasing six deployed AI/ML projects, each presented as a "model card" — a spec-sheet-style summary (task, architecture, dataset, stack) rather than a generic project tile.

**Live site:** [portfolio-kbaub2rhq-ali-faraz-pys-projects.vercel.app](https://portfolio-kbaub2rhq-ali-faraz-pys-projects.vercel.app/)

---

## What it is

Every project card links to both a live, working demo and its public source code. The design borrows from real ML documentation conventions (model cards, spec sheets) rather than a typical "portfolio template" look — paper-white background, monospace labels, a small animated neural-network diagram in the hero, and category-coded accent colors (vision, generative, health, NLP, finance).

## Featured Projects

- **Deepfake Detector** — PyTorch, EfficientNet-B0, FastAPI, Next.js
- **Picassify** — Neural style transfer, PyTorch, VGG19, Streamlit
- **NeuralLens** — Image classification, MobileNetV2, FastAPI, Next.js
- **Diabetes Detector** — Random Forest, scikit-learn, Streamlit
- **SentimentSense** — Aspect-based sentiment analysis, DistilBERT + BART
- **AetherQuant** — Crypto trend classification, XGBoost

## Tech Stack

- Next.js / React
- Tailwind CSS (v4)
- Custom fonts: Space Grotesk, JetBrains Mono, Inter
- Deployed on Vercel

## Running Locally

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view it.

## Structure

```text
portfolio-hub/
└── src/app/
    ├── page.js       # All project data + page layout
    ├── layout.js     # Font setup
    └── globals.css   # Color theme, animations
```

---

### Author
**Syed M. Ali Faraz** — [GitHub](https://github.com/ali-faraz-py) · [LinkedIn](https://www.linkedin.com/in/syed-m-ali-faraz)