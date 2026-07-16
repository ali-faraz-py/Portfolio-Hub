"use client";

import { useState } from "react";

const PROJECTS = [
  {
    name: "DEEPFAKE_DETECTOR",
    category: "vision",
    description:
      "Classifies uploaded face images and video as real or AI-generated, with a confidence score and frame-sampling for video.",
    task: "Binary Classification",
    architecture: "EfficientNet-B0",
    dataset: "100k+ labeled faces",
    stack: "PyTorch · FastAPI · Next.js",
    live: "https://deepfake-detector-olive.vercel.app/",
    source: "https://github.com/ali-faraz-py/deepfake-detector",
  },
  {
    name: "PICASSIFY",
    category: "generative",
    description:
      "Transforms any photo into stylized artwork by blending it with a chosen painting's style, using neural style transfer.",
    task: "Neural Style Transfer",
    architecture: "VGG19 (pretrained)",
    dataset: "User content + style pairs",
    stack: "PyTorch · Streamlit",
    live: "https://picassify-art.streamlit.app/",
    source: "https://github.com/ali-faraz-py/Picassify",
  },
  {
    name: "NEURAL_LENS",
    category: "vision",
    description:
      "Real-time image recognition across 1,000+ object categories, built on a ResNet50 backbone.",
    task: "Image Classification",
    architecture: "ResNet50",
    dataset: "ImageNet-pretrained",
    stack: "TensorFlow · Keras · Streamlit",
    live: "https://neural-lens.streamlit.app/",
    source: "https://github.com/ali-faraz-py/NeuralLens",
  },
  {
    name: "DIABETES_DETECTOR",
    category: "health",
    description:
      "Predicts diabetes risk from clinical metrics, with real-time probability scoring and downloadable reports.",
    task: "Risk Classification",
    architecture: "Random Forest",
    dataset: "Clinical health metrics",
    stack: "scikit-learn · Streamlit",
    live: "https://diabetes-risk-diagnostic.streamlit.app/",
    source: "https://github.com/ali-faraz-py/DiabetesDetector",
  },
  {
    name: "SENTIMENT_SENSE",
    category: "nlp",
    description:
      "Aspect-based sentiment analysis dashboard detecting business topics (food, service, price) and emotional context in real time.",
    task: "Aspect-Based Sentiment Analysis",
    architecture: "DistilBERT + BART (zero-shot)",
    dataset: "Business feedback text",
    stack: "Transformers · Streamlit",
    live: "https://sentiment-sense-ai.streamlit.app/",
    source: "https://github.com/ali-faraz-py/SentimentSense",
  },
  {
    name: "AETHERQUANT",
    category: "finance",
    description:
      "Crypto market trend classifier analyzing 24 technical indicators (RSI, MACD, VWAP) via live market data.",
    task: "Market Trend Classification",
    architecture: "XGBoost",
    dataset: "Yahoo Finance (24 indicators)",
    stack: "Pandas · Plotly · Streamlit",
    live: "https://aether-quant.streamlit.app/",
    source: "https://github.com/ali-faraz-py/AetherQuant",
  },
];

const ACCENT = {
  vision: "#2955D6",
  generative: "#B23DD9",
  health: "#1F9D55",
  nlp: "#C9781A",
  finance: "#0E7C86",
};

function NeuralGraphic() {
  // 3 layers: input (3), hidden (4), output (2)
  const inputY = [40, 90, 140];
  const hiddenY = [20, 65, 110, 155];
  const outputY = [55, 120];

  const inputX = 20;
  const hiddenX = 110;
  const outputX = 200;

  const lines = [];
  inputY.forEach((y1, i) => {
    hiddenY.forEach((y2, j) => {
      lines.push(
        <line
          key={`ih-${i}-${j}`}
          x1={inputX}
          y1={y1}
          x2={hiddenX}
          y2={y2}
          stroke="#DEDBD3"
          strokeWidth="1"
        />
      );
    });
  });
  hiddenY.forEach((y1, i) => {
    outputY.forEach((y2, j) => {
      lines.push(
        <line
          key={`ho-${i}-${j}`}
          x1={hiddenX}
          y1={y1}
          x2={outputX}
          y2={y2}
          stroke="#DEDBD3"
          strokeWidth="1"
        />
      );
    });
  });

  return (
    <svg
      viewBox="0 0 220 180"
      className="w-full h-full"
      aria-hidden="true"
    >
      {lines}
      {inputY.map((y, i) => (
        <circle key={`i-${i}`} cx={inputX} cy={y} r="5" fill="#14181C" />
      ))}
      {hiddenY.map((y, i) => (
        <circle
          key={`h-${i}`}
          cx={hiddenX}
          cy={y}
          r="5"
          fill={i === 1 ? "#2955D6" : "#14181C"}
          className={i === 1 ? "live-dot" : ""}
        />
      ))}
      {outputY.map((y, i) => (
        <circle
          key={`o-${i}`}
          cx={outputX}
          cy={y}
          r="5"
          fill={i === 0 ? "#1F9D55" : "#14181C"}
        />
      ))}
    </svg>
  );
}

function ModelCard({ project }) {
  return (
    <div className="group relative border border-hairline rounded-[6px] bg-[#FFFEFC] pl-7 pr-6 py-6 transition-all duration-200 hover:-translate-y-1 hover:shadow-[0_12px_24px_-8px_rgba(20,24,28,0.12)] hover:border-ink/15 overflow-hidden">
      <span
        className="absolute left-0 top-0 bottom-0 w-1"
        style={{ backgroundColor: ACCENT[project.category] }}
      />

      <div className="flex items-center justify-between">
        <h3 className="font-mono text-[14px] font-bold tracking-wide">
          {project.name}
        </h3>
        <span className="font-mono text-[10px] font-bold text-live flex items-center gap-1.5">
          <span className="w-1.5 h-1.5 rounded-full bg-live live-dot inline-block" />
          LIVE
        </span>
      </div>

      <p className="font-body mt-3.5 text-[14px] leading-relaxed text-[#3A3D41]">
        {project.description}
      </p>

      <div className="mt-4.5 pt-4 border-t border-dashed border-hairline grid grid-cols-2 gap-y-3 gap-x-4">
        <div>
          <div className="font-mono uppercase text-[10px] font-bold tracking-wide text-slate">
            Task
          </div>
          <div className="font-body text-[13px] font-medium mt-0.5">
            {project.task}
          </div>
        </div>
        <div>
          <div className="font-mono uppercase text-[10px] font-bold tracking-wide text-slate">
            Architecture
          </div>
          <div className="font-body text-[13px] font-medium mt-0.5">
            {project.architecture}
          </div>
        </div>
        <div>
          <div className="font-mono uppercase text-[10px] font-bold tracking-wide text-slate">
            Dataset
          </div>
          <div className="font-body text-[13px] font-medium mt-0.5">
            {project.dataset}
          </div>
        </div>
        <div>
          <div className="font-mono uppercase text-[10px] font-bold tracking-wide text-slate">
            Stack
          </div>
          <div className="font-body text-[13px] font-medium mt-0.5">
            {project.stack}
          </div>
        </div>
      </div>

      <div className="mt-5.5 flex gap-2">
        <a
          href={project.live}
          target="_blank"
          rel="noopener noreferrer"
          className="flex-1 text-center font-mono text-[11px] font-bold tracking-wide bg-ink text-paper rounded-[6px] py-2.5 transition-opacity hover:opacity-85"
        >
          LAUNCH ↗
        </a>
        <a
          href={project.source}
          target="_blank"
          rel="noopener noreferrer"
          className="flex-1 text-center font-mono text-[11px] font-bold tracking-wide border border-hairline rounded-[6px] py-2.5 transition-colors hover:border-ink"
        >
          SOURCE ↗
        </a>
      </div>
    </div>
  );
}

export default function Home() {
  const [copied, setCopied] = useState(false);

  const handleCopyEmail = () => {
    navigator.clipboard.writeText("syedalifaraz52@gmail.com");
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <main className="min-h-screen bg-paper">
      <div className="max-w-5xl mx-auto px-6">
        <div className="pt-9 flex items-center justify-between font-mono text-[12px] font-bold tracking-wide text-slate">
          <span>SYED_ALI_FARAZ.PORTFOLIO</span>
          <div className="flex gap-6">
            <a
              href="https://github.com/ali-faraz-py"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-ink transition-colors"
            >
              GITHUB
            </a>
            <a
              href="https://www.linkedin.com/in/syed-m-ali-faraz"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-ink transition-colors"
            >
              LINKEDIN
            </a>
            <a
              href="https://www.upwork.com/freelancers/~017cd21f872163dffa?mp_source=share"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-ink transition-colors"
            >
              UPWORK
            </a>
          </div>
        </div>

        <div className="pt-20 pb-16 bg-grid-texture flex flex-col md:flex-row items-center gap-8">
          <div className="flex-1">
            <p className="font-mono text-[12px] font-bold tracking-[0.16em] text-signal">
              MACHINE LEARNING ENGINEER
            </p>
            <h1 className="font-display font-bold mt-4 max-w-2xl text-[2.4rem] sm:text-[3rem] lg:text-[3.5rem] leading-[1.06] tracking-tight">
              I build AI systems that ship — not just notebooks that run once.
            </h1>
            <p className="font-body mt-5 max-w-xl text-[16px] text-slate leading-relaxed">
              Six deployed projects spanning computer vision, NLP, and classic
              ML. Each card below is a spec sheet for a live, working system —
              launch it directly or read the source.
            </p>
            <div className="mt-8 inline-flex items-center gap-2 font-mono text-[12px] text-slate bg-white border border-hairline px-3.5 py-2 rounded-full">
              <span className="w-1.5 h-1.5 rounded-full bg-live live-dot inline-block" />
              6 SYSTEMS IN PRODUCTION
            </div>
          </div>

          <div className="hidden md:block w-[220px] h-[180px] shrink-0 opacity-90">
            <NeuralGraphic />
          </div>
        </div>

        <p className="font-mono text-[11px] font-bold tracking-[0.14em] text-slate uppercase mt-2 mb-5">
          // PROJECT_INDEX
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5 pb-20">
          {PROJECTS.map((project) => (
            <ModelCard key={project.name} project={project} />
          ))}
        </div>

        <footer className="border-t border-hairline py-10 text-center">
          <div className="font-mono text-[12px] text-slate space-x-3">
            <button
              onClick={handleCopyEmail}
              className="hover:text-ink transition-colors cursor-pointer"
            >
              {copied ? "COPIED ✓" : "EMAIL"}
            </button>
            <span>·</span>
            <a
              href="https://github.com/ali-faraz-py"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-ink transition-colors"
            >
              GITHUB
            </a>
            <span>·</span>
            <a
              href="https://www.linkedin.com/in/syed-m-ali-faraz"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-ink transition-colors"
            >
              LINKEDIN
            </a>
            <span>·</span>
            <a
              href="https://www.upwork.com/freelancers/~017cd21f872163dffa?mp_source=share"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-ink transition-colors"
            >
              UPWORK
            </a>
          </div>
          <p className="font-body mt-4 text-[12px] text-slate italic">
            A good developer knows the math behind the code.
          </p>
        </footer>
      </div>
    </main>
  );
}