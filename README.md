# 🤖 AI-Powered Autonomous Interview & Surveillance System

## 📌 Overview

This project is a **semi industry-level AI system** that combines:

* 🧠 **AI Interview Engine (NLP-based)**
* 👁️ **Real-Time Surveillance System (Computer Vision)**
* ⚙️ **Decision Intelligence Engine**

The system evaluates candidates using **multi-modal inputs (video, audio, text)** to generate:

* 📊 Performance Score
* 🚨 Behavioral Alerts
* 📄 Final Evaluation Report

---

## 🎯 Key Features

* Automated AI Interview (NLP)
* Face Detection & Emotion Analysis
* Object Detection (Cheating Monitoring)
* Real-Time Alert System
* Multi-Modal Decision Engine
* Admin Dashboard & Reports

---

## 🏗️ Project Structure

```
ai-interview-system/
│
├── backend/                     # 🔧 Backend APIs & Core Logic
│   ├── api-gateway/             # Handles all incoming requests
│   ├── interview-service/       # NLP interview logic (➡️ AI/NLP Team)
│   ├── surveillance-service/    # Video stream handling (➡️ CV Team)
│   ├── behavior-analysis/       # Cheating detection logic (➡️ AI Team)
│   ├── decision-core/           # Final scoring & decision engine (➡️ Core AI Team)
│   ├── alert-manager/           # Alert generation system (➡️ Backend Team)
│   ├── session-manager/         # Interview session handling (➡️ Backend Team)
│   ├── data-layer/              # Database & storage (➡️ Data Team)
│   └── common/                  # Shared utilities/config
│
├── ai-models/                   # 🧠 AI Models
│   ├── face-detection/          # Face detection model (➡️ CV Team)
│   ├── emotion-recognition/     # Emotion analysis model (➡️ CV Team)
│   ├── object-detection/        # Object detection (YOLO) (➡️ CV Team)
│   ├── nlp-interview/           # NLP/LLM logic (➡️ NLP Team)
│   └── model-serving/           # Model APIs (➡️ AI Backend Team)
│
├── frontend/                    # 💻 Frontend Applications
│   ├── candidate-app/           # Candidate interview UI (➡️ Frontend Team)
│   ├── admin-dashboard/         # Admin panel & analytics (➡️ Frontend Team)
│
├── realtime-engine/             # ⚡ Real-Time Processing
│   ├── websocket-server/        # Live communication (➡️ Backend Team)
│   ├── stream-processor/        # Frame processing pipeline (➡️ CV Team)
│
├── infrastructure/              # 🚀 Deployment & DevOps
│   ├── docker/                  # Docker configs (➡️ DevOps Team)
│   ├── ci-cd/                   # CI/CD pipelines (➡️ DevOps Team)
│
├── docs/                        # 📄 Documentation (➡️ Documentation Team)
├── tests/                       # 🧪 Testing (➡️ QA Team)
├── logs/                        # 📜 Logs
└── README.md
```

---

## 👨‍💻 Team Responsibilities

| Domain        | Responsibility                  |
| ------------- | ------------------------------- |
| AI/ML Team    | Models (NLP, CV, scoring)       |
| Backend Team  | APIs, logic, integration        |
| Frontend Team | UI (candidate + admin)          |
| CV Team       | Face, emotion, object detection |
| DevOps Team   | Deployment, Docker, CI/CD       |
| Data Team     | DB, analytics, reports          |

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-interview-system.git
cd ai-interview-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Backend

```bash
uvicorn backend.api-gateway.main:app --reload
```

---

## 🌿 Git Workflow (IMPORTANT)

### 🔹 Create Branch

```bash
git checkout -b feature-your-task
```

### 🔹 Commit Changes

```bash
git add .
git commit -m "Added feature"
git push origin feature-your-task
```

### 🔹 Create Pull Request

* Go to GitHub
* Click **Compare & Pull Request**
* Submit for review

---

## 🤝 Contribution Guidelines

### ✅ Rules:

* Do NOT push directly to `main`
* Always create a **new branch**
* Write **clear commit messages**
* Pull latest code before working:

```bash
git pull origin main
```

---

### 📌 Task Assignment Rule

* Work ONLY in your assigned folder/module
* Do NOT modify other modules without permission
* Follow folder structure strictly

---

### 🧪 Testing

* Test your code before pushing
* Avoid breaking existing functionality

---

## 🚀 Deployment (Basic)

```bash
docker-compose build
docker-compose up
```

---

## 📊 Project Status

🚧 In Development (Phase-wise Execution)

---

## 📌 Future Scope

* Voice analysis (stress detection)
* Eye tracking system
* Multi-language NLP
* Cloud-scale deployment

---

## 🧠 Final Note

This project follows a **microservices + AI pipeline architecture**, designed for:

* Scalability
* Real-time processing
* Industry-level modular development

---

## 👑 Team Lead

**Ishan Pankaj Jadhav**

---

## 📄 License

This project is for academic & research purposes.
