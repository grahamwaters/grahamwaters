# 🧠 Machine Learning Portfolio

> *Projects that push models from prototype to production—with emphasis on reinforcement learning, LLM alignment, and computer‑vision pipelines.*

---

## ⚙️ Core ML Toolbox
<p align="center">
  <img alt="PyTorch"       src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white" />
  <img alt="TensorFlow"    src="https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white" />
  <img alt="Keras"         src="https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white" />
  <img alt="Transformers"  src="https://img.shields.io/badge/HF Transformers-FFBF00?logo=huggingface&logoColor=black" />
  <img alt="scikit-learn" src="https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=black" />
  <img alt="Gymnasium"    src="https://img.shields.io/badge/Gymnasium-00897B?logo=openai&logoColor=white" />
  <img alt="Weights&Biases"src="https://img.shields.io/badge/W&B-FFBE00?logo=weightsandbiases&logoColor=black" />
  <img alt="OpenCV"        src="https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white" />
  <img alt="Docker"        src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
</p>

---

## 🌟 Flagship ML Projects

| Project | Live Metrics | ML Highlights | Major Libraries |
|---------|--------------|---------------|-----------------|
| **RL-GPT** <br><sup>Aligning LLMs with custom rewards</sup> | ![last commit](https://img.shields.io/github/last-commit/grahamwaters/RL-GPT) ![commit activity](https://img.shields.io/github/commit-activity/m/grahamwaters/RL-GPT) | Implements PPO‑style RLHF loops to fine‑tune GPT‑family models on domain‑specific tasks; integrates W&B sweeps. | `PyTorch`, `transformers`, `RLHF`, `wandb` |
| **SceneSort Clustering** | ![last commit](https://img.shields.io/github/last-commit/grahamwaters/SceneSort_Clustering) | Unsupervised vision pipeline—CLIP embeddings + HDBSCAN + UMAP for automatic scene grouping. | `PyTorch`, `CLIP`, `HDBSCAN`, `UMAP` |
| **density_prompt** | ![last commit](https://img.shields.io/github/last-commit/grahamwaters/density_prompt) | Quantifies token‑density vs. output quality; uses regression & bootstrap tests to model LLM behaviour. | `OpenAI API`, `statsmodels`, `scikit-learn` |
| **WatchMeOS** | ![last commit](https://img.shields.io/github/last-commit/grahamwaters/WatchMeOS) | Gesture‑first shell that fuses MediaPipe pose‑estimation with fuzzy‑logic classifiers; edge‑deployable. | `MediaPipe`, `OpenCV`, `NumPy`, `TensorFlow Lite` |
| **GrahamsSimulations** | ![last commit](https://img.shields.io/github/last-commit/grahamwaters/GrahamsSimulations) | Collection of physics‑based sims (Q‑learning lander, humanoid stick walker) used to generate synthetic RL data. | `Gymnasium`, `PyTorch`, `Matplotlib` |

---

## 🗂️ Supporting ML/AI Repositories

- **Milton** – GUI notebook with built‑in ML helpers for rapid experimentation.
- **Lorebook Generator for NovelAI** – NLP pipeline + zero‑shot classification for character/entity extraction.
- **medium_titles_analysis** – XGBoost ranking model on headline engagement.
- **HowTimeFlies** – CV + clustering to visualise temporal drift in Google image results.

---

## 🔄 Typical ML Workflow

1. **Problem Framing & Data Contract** – define reward, constraints, SLA.
2. **Data Curation** – automated scrapers & quality filters, tracked via `dvc`.
3. **Experimentation** – modular notebooks, versioned configs, W&B logging.
4. **Evaluation** – custom metrics, robustness tests, bias & fairness checks.
5. **Deployment** – Dockerised microservice with REST or gRPC endpoint; CD via GitHub Actions.

---

### 🤝 Collaboration & Consultancy

> Interested in LLM alignment, RL for control systems, or computer‑vision products? **Let’s chat!** Reach out on [LinkedIn](https://www.linkedin.com/in/grahamwatersdatascientist/) or open a discussion in any repo listed above.
