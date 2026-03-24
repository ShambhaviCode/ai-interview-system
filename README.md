# 🤖 AI-Powered Autonomous Interview & Surveillance System

---

## 📌 Overview

This project is a **semi industry-level AI system** combining:

* 🧠 AI Interview Engine (NLP)
* 👁️ Real-Time Surveillance (Computer Vision)
* ⚙️ Decision Intelligence Engine

It evaluates candidates using **video + audio + text** to generate:

* 📊 Score
* 🚨 Alerts
* 📄 Final Report

---

## 🏗️ Project Structure (With Ownership)

```id="projstruct01"
ai-interview-system/
│
├── backend/  
│   ├── api-gateway/                    # 🔹 Ishan Pankaj Jadhav (Architecture + APIs)
│   ├── interview-service/              # 🔹 Messiah Prince N, Adityaraj Jadhav (NLP logic)
│   ├── surveillance-service/           # 🔹 Shambhavi M K, Aditya Gour (Video APIs)
│   ├── behavior-analysis/              # 🔹 Ganga Siva Prasad (Cheating logic)
│   ├── decision-core/                  # 🔹 Ishan Pankaj Jadhav (Scoring engine)
│   ├── alert-manager/                  # 🔹 Aditya Gour (Alert APIs)
│   ├── session-manager/                # 🔹 Shambhavi M K (Session handling)
│   ├── data-layer/                     # 🔹 Kodati Ramya Sree, Radhika Gupta (DB & storage)
│   └── common/
│
├── ai-models/  
│   ├── face-detection/                 # 🔹 Ishan Dudhat, Ganga Siva Prasad
│   ├── emotion-recognition/            # 🔹 Messiah Prince N, Kaveri Desai
│   ├── object-detection/               # 🔹 Akshat Rana, Adityaraj Jadhav
│   ├── nlp-interview/                  # 🔹 Messiah Prince N, Kaveri Desai
│   └── model-serving/                  # 🔹 Akshat Rana (Model APIs)
│
├── frontend/  
│   ├── candidate-app/                  # 🔹 Aditi Yadav, Akshat Rana
│   ├── admin-dashboard/                # 🔹 Yash Wankhede, Aditi Yadav
│
├── realtime-engine/  
│   ├── websocket-server/               # 🔹 Shambhavi M K
│   ├── stream-processor/               # 🔹 Ishan Dudhat
│
├── infrastructure/  
│   ├── docker/                         # 🔹 Aditi Yadav
│   ├── ci-cd/                          # 🔹 Aditi Yadav
│
├── docs/                               # 🔹 Radhika Gupta
├── tests/                              # 🔹 Entire Team
└── README.md
```

---

## 👨‍💻 Team Contributions

### 👑 Team Lead

* **Ishan Pankaj Jadhav**

  * System architecture
  * API design
  * Decision engine
  * Integration supervision

---

### 🧠 AI / ML Team

* **Messiah Prince N** → NLP + Emotion Detection
* **Kaveri Ravi Desai** → NLP + Voice Analysis
* **Akshat Rana** → Object Detection + Model Integration
* **Adityaraj Jadhav** → AI Support + Alert Intelligence
* **Ishan Dudhat** → Computer Vision + Streaming
* **Ganga Siva Prasad** → Behavior Analysis + Gaze Detection

---

### 💻 Backend Team

* **Shambhavi M K** → APIs + WebSockets + Sessions
* **Aditya Gour** → API Integration + Alerts + Automation

---

### 🎨 Frontend Team

* **Aditi Yadav** → Candidate UI + Admin Panel
* **Yash Wankhede** → Dashboard + Data Visualization

---

### 📊 Data & Analytics Team

* **Kodati Ramya Sree** → Database + Analytics
* **Radhika Gupta** → Data Tracking + Documentation

---

### ⚙️ DevOps / Deployment

* **Aditi Yadav** → Docker + CI/CD + Cloud Setup

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash id="clone01"
git clone https://github.com/YOUR-USERNAME/ai-interview-system.git
cd ai-interview-system
```

### 2. Setup Environment

```bash id="env01"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Backend

```bash id="run01"
uvicorn backend.api-gateway.main:app --reload
```

---

## 🌿 Git Workflow

### Create Branch

```bash id="branch01"
git checkout -b feature-task-name
```

### Commit & Push

```bash id="push01"
git add .
git commit -m "Added feature"
git push origin feature-task-name
```

### Pull Request

* Submit PR on GitHub
* Wait for review (Team Lead)

---

## 🤝 Contribution Rules

### ✅ Must Follow:

* Work only in your assigned module
* Do NOT push to `main` directly
* Always create a branch
* Pull latest changes before starting

```bash id="pull01"
git pull origin main
```

---

### ❌ Avoid:

* Editing other modules without discussion
* Large unstructured commits
* Breaking existing code

---

## 🧪 Testing

* Each module must be tested before merging
* Fix bugs before raising PR

---

## 🚀 Deployment

```bash id="deploy01"
docker-compose build
docker-compose up
```

---

## 📊 Project Status

🚧 Phase-wise Development (1 → 5)

---

## 🧠 Final Note

This project follows a **modular AI + microservices architecture**, designed for:

* Scalability
* Real-time processing
* Industry-level implementation

---

