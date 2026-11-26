# 🛡️ EduAegis: Multi-Subject AI Tutor & Subjective Grader

**EduAegis** is a fullstack AI tutoring and governed subjective evaluation platform spanning **Physics, Chemistry, and Mathematics** across **Classes 8th, 9th, and 10th** (aligned with **CBSE, ICSE, and State Boards**). Inspired by modern systems like [www.edcafe.ai](https://www.edcafe.ai), it features an end-to-end **AI Governance Framework** with **Human-in-the-Loop review, teacher controlled mark release, and a student/parent challenge appeal system**.

> **Dual Deployment Architecture:**
> 1. **Streamlit Deployment** (Streamlit Community Cloud & local `streamlit run streamlit_app.py`).
> 2. **Vercel Fullstack Deployment** (Next.js 16 + React 19).
> 3. **Laptop as Local Server** (Persists all data in `eduaegis_data.json` without cloud lock-in).

---

## 🌟 Key Functional Highlights

### 1. Multi-Subject Scope (Physics, Chemistry, Mathematics)
- Not restricted to Physics! Full multi-subject subjective evaluation for:
  - **⚛️ Physics**: Motion, Force & Laws of Motion, Gravitation, Work & Energy, Sound, Light, Electricity.
  - **🧪 Chemistry**: Matter in Our Surroundings, Evaporation & Latent Heat, States of Matter, Atoms & Molecules, Chemical Reactions.
  - **📐 Mathematics**: Number Systems, Rational vs Irrational numbers, Rationalizing Denominators, Laws of Exponents, Linear Equations.
- **Candidate Academic Selectors**:
  - Select **Board** (CBSE, ICSE, State Board, Cambridge).
  - Select **Class** (8th, 9th, 10th).
  - Select **Subject** (Physics, Chemistry, Mathematics).

### 2. Open Box Text Input for Custom Topics
- In case a student wants help with *any custom topic*, an open text box is provided:
  - *"Type any custom topic you need help practicing or clearing doubts..."* (e.g. *Law of Conservation of Mass*, *Pythagoras Theorem*, *Refraction through Prism*).
  - EduAegis fetches/synthesizes curriculum details, core formulas, hidden-solution examples, and a 5-question test paper specifically tailored for that topic!

### 3. AI Tutor Tab (Concept Learning & Clearing with Audio)
- Explains concepts in **plain, simple, conversational English** like the best subject teacher.
- **Embedded Speech Narration**: Built-in speech synthesis teacher audio player with Play, Pause, and Speed controls (0.85x, 1.0x, 1.2x).
- **Everyday Real-World Analogies**: Breaks down abstract formulas into relatable situations (cricket catches, karate tile strikes, earthen pot cooling).
- **Socratic Mastery Check**: Interactive progressive example loop where students confirm *"I Understood!"* or request *"Explain with another real-life example"*.

### 4. AI Grader Tab (Subjective Assessment & Practice)
- **Practice Solved Examples with Hidden Solutions**: Practice problems where step-by-step solved solutions are concealed by default and revealed only on-demand.
- **5-Question Subjective Paper**: 20-mark diagnostic test spanning definitions, conceptual reasoning, and numerical derivations.
- **1-Click Demo Loaders**:
  - 🌟 **20/20 Exemplary Answer**
  - ⚖️ **12/20 Average Answer**
  - ⚠️ **5/20 Misconception Answer**
- **Transparent Step-by-Step Scoring**: Explains **where marks were awarded and why marks were deducted**.
- **Authentic Citations**: Links to official [NCERT Textbooks](https://ncert.nic.in), Khan Academy, and HyperPhysics.

### 5. AI Governance Framework (The "Aegis" Shield)
1. **Teacher Directives (edcafe.ai Inspired)**: Teachers enforce custom instructions (strict SI unit penalties, partial step credit, spelling tolerance).
2. **Controlled Release**: Evaluated papers enter `PENDING_TEACHER_RELEASE`. Scores cannot be published without manual teacher approval.
3. **Teacher Mark Overrides**: Teachers can adjust any mark up/down and add qualitative feedback.
4. **Student & Parent Appeal System**:
   - Once released, the student chooses:
     - **1 - I Accept**: Locks marks as final and archives them in academic records.
     - **2 - I Challenge**: Allows student to select specific questions, write their detailed justification, and submit an appeal to the teacher's re-check queue.

---

## 🚀 How to Deploy EduAegis on Streamlit (Step-by-Step)

You can run EduAegis on your local laptop or deploy it to **Streamlit Community Cloud** (100% free hosting):

### Step 1: Run Streamlit Locally on Your Laptop
1. Ensure Python 3.10+ is installed.
2. Open terminal in the project directory:
   ```bash
   cd C:\Users\ADMIN\.gemini\antigravity\scratch\eduaegis
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```
   *(Or double-click [`run_streamlit.bat`](run_streamlit.bat) on Windows)*
3. Your browser will automatically open at: **`http://localhost:8501`**

---

### Step 2: Deploy to Streamlit Community Cloud (Free Online Web URL)
Streamlit Community Cloud deploys directly from GitHub:

1. **Initialize Git & Push to GitHub**:
   ```bash
   cd C:\Users\ADMIN\.gemini\antigravity\scratch\eduaegis
   git init
   git add .
   git commit -m "Deploy EduAegis on Streamlit"
   git remote add origin https://github.com/<your-username>/eduaegis.git
   git branch -M main
   git push -u origin main
   ```
2. **Deploy on Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
   - Click **"New app"**.
   - Select:
     - **Repository:** `<your-username>/eduaegis`
     - **Branch:** `main`
     - **Main file path:** `streamlit_app.py`
   - Click **"Deploy"**!
3. In under 2 minutes, your app will be live at a public URL like:  
   `https://eduaegis.streamlit.app`

---

## 🌐 Deploying to Vercel (Next.js Fullstack)

If you wish to deploy the Next.js fullstack version to Vercel:

1. Push the repository to GitHub.
2. Go to [vercel.com](https://vercel.com) and click **"Add New Project"**.
3. Select your repository `eduaegis`.
4. Vercel automatically detects Next.js. Click **"Deploy"**.
5. Live in ~60 seconds at `https://eduaegis.vercel.app`.

---

## 📊 IIM Faculty PowerPoint Deck

A slide presentation (`.pptx`) is located at:  
📄 **[`EduAegis_IIM_Capstone_Presentation.pptx`](EduAegis_IIM_Capstone_Presentation.pptx)**

### Deck Outline:
- **Slide 1**: Title Slide (EduAegis: Multi-Subject AI Tutor & Governed Grader).
- **Slide 2**: The Subjective Evaluation Dilemma in Indian K-12.
- **Slide 3**: Product Vision & edcafe.ai Benchmarking.
- **Slide 4**: Module 1 — Socratic AI Tutor with Conversational Narration & Multi-Modal Ingestion.
- **Slide 5**: Module 2 — Rigorous Step-by-Step Subjective Grader (Physics, Chemistry, Maths).
- **Slide 6**: The 4-Pillar AI Governance Framework (Human-in-the-Loop, Controlled Release, Student Appeal).
- **Slide 7**: End-to-End System Workflow Architecture.
- **Slide 8**: Technology Stack & Dual Deployment (Streamlit + Vercel + Laptop Server).
- **Slide 9**: Strategic B2B Business Model & School Scalability.
- **Slide 10**: Live Prototype Walkthrough & Impact Metrics.
- **Slide 11**: Ethical Alignment (NITI Aayog / UNESCO AI Ethics) & Q&A.
"# Edu-Aegis" 
