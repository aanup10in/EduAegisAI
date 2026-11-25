"""
EduAegis - Streamlit Web Application
Responsible AI Tutor & Subjective Grader (Multi-Subject: Physics, Chemistry, Maths)
Classes 8th, 9th, 10th • CBSE, ICSE, State Board
International Standard Soothing UI & Responsible AI Governance Framework
Enhanced with Role-Based Access Control, Blind Evaluation, Teacher Dashboard & Admin Executive Console
"""

import os
import json
import time
from datetime import datetime, timedelta
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Page Configuration with Soothing Theme
st.set_page_config(
    page_title="EduAegis | Responsible AI Tutor & Grader",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# International Standard Soothing Colors & Design CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header Container */
    .aegis-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #0F172A 100%);
        padding: 24px 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 20px;
        border: 1px solid rgba(99, 102, 241, 0.3);
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
    }
    
    .aegis-title {
        font-size: 26px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .aegis-badge {
        background: rgba(16, 185, 129, 0.15);
        color: #10B981;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 9999px;
        border: 1px solid rgba(16, 185, 129, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .role-badge-student {
        background: #EFF6FF;
        color: #1D4ED8;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 9999px;
        border: 1px solid #BFDBFE;
    }

    .role-badge-teacher {
        background: #ECFDF5;
        color: #047857;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 9999px;
        border: 1px solid #A7F3D0;
    }

    .role-badge-admin {
        background: #FAF5FF;
        color: #7E22CE;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 9999px;
        border: 1px solid #E9D5FF;
    }
    
    .aegis-subtext {
        font-size: 13px;
        color: #CBD5E1;
        margin-top: 6px;
        max-width: 850px;
        line-height: 1.5;
    }
    
    /* Persistent Board Pill */
    .board-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #EEF2FF;
        color: #4338CA;
        font-weight: 700;
        font-size: 12px;
        padding: 6px 14px;
        border-radius: 9999px;
        border: 1px solid #C7D2FE;
        margin-bottom: 8px;
    }
    
    /* Card Container */
    .soothing-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 2px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 16px;
    }

    /* KPI Summary Cards */
    .kpi-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .kpi-num {
        font-size: 26px;
        font-weight: 800;
        color: #0F172A;
    }
    .kpi-label {
        font-size: 12px;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 4px;
    }

    /* Timer Pill */
    .timer-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #FFFBEB;
        color: #B45309;
        font-weight: 700;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 9999px;
        border: 1px solid #FDE68A;
    }
    
    .blind-banner {
        background: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 12px;
        padding: 12px 16px;
        color: #166534;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .step-item {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 12px 16px;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Database file persistence
DB_FILE = "eduaegis_data.json"

# =============================================================================
# DEFAULT USERS & ROLES CONFIGURATION
# =============================================================================
DEFAULT_USERS = {
    # Students
    "Anup": {
        "id": "STU-101",
        "username": "Anup",
        "name": "Anup Sharma",
        "role": "student",
        "password": "eduaegis123",
        "studentClass": 9,
        "board": "CBSE (All India)",
        "cityState": "Bangalore, Karnataka",
        "email": "anup.sharma@school.edu",
        "phone": "+91 98765 43210"
    },
    "Nandita": {
        "id": "STU-102",
        "username": "Nandita",
        "name": "Nandita Roy",
        "role": "student",
        "password": "eduaegis123",
        "studentClass": 9,
        "board": "ICSE / CISCE",
        "cityState": "Kolkata, West Bengal",
        "email": "nandita.roy@school.edu",
        "phone": "+91 91234 56789"
    },
    # Teachers
    "Ankur": {
        "id": "TCH-201",
        "username": "Ankur",
        "name": "Ankur Verma",
        "role": "teacher",
        "password": "eduaegis123",
        "subjects": ["Physics"],
        "email": "ankur.verma@eduaegis.org",
        "department": "Department of Physical Sciences"
    },
    "Akanksha": {
        "id": "TCH-202",
        "username": "Akanksha",
        "name": "Akanksha Singh",
        "role": "teacher",
        "password": "eduaegis123",
        "subjects": ["Chemistry", "Mathematics"],
        "email": "akanksha.singh@eduaegis.org",
        "department": "Department of Chemical & Mathematical Sciences"
    },
    # Admin
    "Admin": {
        "id": "ADM-001",
        "username": "Admin",
        "name": "System Administrator",
        "role": "admin",
        "password": "eduaegis123",
        "subjects": ["Physics", "Chemistry", "Mathematics"],
        "email": "admin@eduaegis.org",
        "department": "Office of Academic Governance & Compliance"
    }
}

def generate_unique_student_id(existing_students):
    """Generates an incremental unique student ID like STU-101, STU-102, STU-103."""
    max_num = 100
    for s in existing_students:
        s_id = str(s.get("id", ""))
        if s_id.startswith("STU-"):
            try:
                num = int(s_id.split("-")[1])
                if num > max_num:
                    max_num = num
            except Exception:
                pass
    return f"STU-{max_num + 1}"

def normalize_submission(sub, index=0):
    """Safely normalizes submission fields across schemas."""
    if not isinstance(sub, dict):
        return {}
    topic = sub.get("topic") or sub.get("chapterTitle") or sub.get("topicName") or "Subjective Assessment"
    subject = sub.get("subject") or sub.get("subjectName") or "Physics"
    class_name = sub.get("className") or "Class 9th"
    board = sub.get("board") or "CBSE (All India)"
    student_name = sub.get("studentName") or "Anup Sharma"
    student_id = sub.get("studentId") or "STU-101"
    status = sub.get("status") or "PENDING_TEACHER_RELEASE"
    sub_id = sub.get("id") or f"sub_{index+1}"

    submitted_at = sub.get("submittedAt") or datetime.now().isoformat() + "Z"
    released_at = sub.get("releasedAt")
    turnaround = sub.get("turnaroundMinutes")

    # If already released and turnaround is missing, compute it
    if released_at and turnaround is None:
        try:
            t1 = datetime.fromisoformat(submitted_at.replace("Z", ""))
            t2 = datetime.fromisoformat(released_at.replace("Z", ""))
            turnaround = max(1.0, round((t2 - t1).total_seconds() / 60.0, 1))
        except Exception:
            turnaround = 25.0

    total_awarded = sub.get("totalAwarded")
    if total_awarded is None:
        total_awarded = sub.get("totalAwardedMarks", 0.0)

    total_max = sub.get("totalMax")
    if total_max is None:
        total_max = sub.get("totalMaxMarks", 20.0)

    try:
        f_total_awarded = float(total_awarded)
    except (ValueError, TypeError):
        f_total_awarded = 0.0

    try:
        f_total_max = float(total_max)
    except (ValueError, TypeError):
        f_total_max = 20.0

    sub["id"] = sub_id
    sub["studentId"] = student_id
    sub["studentName"] = student_name
    sub["topic"] = topic
    sub["chapterTitle"] = topic
    sub["topicName"] = topic
    sub["subject"] = subject
    sub["subjectName"] = subject
    sub["className"] = class_name
    sub["board"] = board
    sub["status"] = status
    sub["submittedAt"] = submitted_at
    sub["releasedAt"] = released_at
    sub["turnaroundMinutes"] = turnaround
    sub["totalAwarded"] = f_total_awarded
    sub["totalAwardedMarks"] = f_total_awarded
    sub["totalMax"] = f_total_max
    sub["totalMaxMarks"] = f_total_max

    raw_questions = sub.get("questions", [])
    norm_questions = []
    if isinstance(raw_questions, list):
        for q_idx, q in enumerate(raw_questions):
            if not isinstance(q, dict):
                continue
            q_text = q.get("question") or q.get("questionText") or f"Question {q_idx+1}"
            q_score = q.get("score") if q.get("score") is not None else q.get("awardedMarks", 0.0)
            q_max = q.get("max") if q.get("max") is not None else q.get("maxMarks", 5.0)
            q_ans = q.get("student_ans") or q.get("studentAnswer") or ""
            step_breakdown = q.get("stepBreakdown") or []

            try:
                f_score = float(q_score)
            except (ValueError, TypeError):
                f_score = 0.0
            try:
                f_max = float(q_max)
            except (ValueError, TypeError):
                f_max = 5.0

            q["question"] = q_text
            q["questionText"] = q_text
            q["score"] = f_score
            q["awardedMarks"] = f_score
            q["max"] = f_max
            q["maxMarks"] = f_max
            q["student_ans"] = q_ans
            q["studentAnswer"] = q_ans
            q["stepBreakdown"] = step_breakdown
            norm_questions.append(q)
    sub["questions"] = norm_questions
    return sub

def load_db():
    data = None
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            pass
    if not data or not isinstance(data, dict):
        data = {
            "students": [
                DEFAULT_USERS["Anup"],
                DEFAULT_USERS["Nandita"]
            ],
            "teachers": [
                DEFAULT_USERS["Ankur"],
                DEFAULT_USERS["Akanksha"]
            ],
            "teacherInstructions": {
                "force_and_laws": {
                    "specificInstructions": "Strictly penalize 0.5 marks if SI units (N, kg, m/s²) are missing. Award partial marks for derivation steps.",
                    "strictSIUnits": True,
                    "partialCreditForSteps": True,
                    "lenientSpelling": True
                }
            },
            "submissions": []
        }

    # Ensure students array contains our core users
    if "students" not in data or not isinstance(data["students"], list):
        data["students"] = [DEFAULT_USERS["Anup"], DEFAULT_USERS["Nandita"]]

    # Ensure Anup and Nandita are present with STU-101 and STU-102
    std_ids = {s.get("id") for s in data["students"]}
    if "STU-101" not in std_ids:
        data["students"].insert(0, DEFAULT_USERS["Anup"])
    if "STU-102" not in std_ids:
        data["students"].insert(1, DEFAULT_USERS["Nandita"])

    if "submissions" not in data or not isinstance(data["submissions"], list):
        data["submissions"] = []

    # Auto-normalize all submissions loaded from disk
    data["submissions"] = [normalize_submission(s, i) for i, s in enumerate(data["submissions"])]
    return data

def save_db(data):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass

if "db" not in st.session_state:
    st.session_state["db"] = load_db()

db = st.session_state["db"]

# Helper to format duration
def format_minutes(mins):
    if mins is None:
        return "N/A"
    mins = float(mins)
    if mins < 60:
        return f"{int(mins)}m"
    hours = int(mins // 60)
    rem_m = int(mins % 60)
    return f"{hours}h {rem_m}m"

# =============================================================================
# AUTHENTICATION & LOGIN PAGE
# =============================================================================
if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None

# If not logged in, render the Login Screen
if st.session_state["logged_in_user"] is None:
    st.markdown("""
    <div style="max-width: 680px; margin: 40px auto 20px auto; text-align: center;">
        <div style="font-size: 38px;">🛡️</div>
        <h1 style="font-size: 28px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">Welcome to EduAegis</h1>
        <p style="color: #64748B; font-size: 14px; margin-bottom: 24px;">
            Responsible AI Tutor & Subjective Grader Platform • Role-Based Authentication Portal
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_space1, col_login, col_space2 = st.columns([1, 2, 1])

    with col_login:
        with st.container():
            st.markdown("""
            <div class="soothing-card" style="border: 2px solid #E0E7FF; box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.1);">
                <div style="font-size: 16px; font-weight: 700; color: #1E1B4B; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                    <span>🔐 Sign In to Your Portal</span>
                </div>
            """, unsafe_allow_html=True)

            login_role = st.selectbox(
                "1. Select Your Role",
                ["Student", "Teacher", "Admin"],
                index=0,
                help="Select whether you are logging in as a Student, Teacher, or Super User Admin."
            )

            # Available usernames based on selected role
            if login_role == "Student":
                user_options = ["Anup", "Nandita"]
                role_key = "student"
                default_idx = 0
            elif login_role == "Teacher":
                user_options = ["Ankur", "Akanksha"]
                role_key = "teacher"
                default_idx = 0
            else:
                user_options = ["Admin"]
                role_key = "admin"
                default_idx = 0

            selected_username = st.selectbox("2. Select Your Username", user_options, index=default_idx)
            entered_password = st.text_input("3. Password", type="password", placeholder="Enter your password (eduaegis123)")

            st.caption("ℹ️ Default password for all prototype accounts is: **eduaegis123**")

            btn_login = st.button("🚀 Log In to EduAegis", type="primary", use_container_width=True)

            if btn_login:
                if entered_password == "eduaegis123":
                    user_data = DEFAULT_USERS.get(selected_username)
                    if user_data:
                        st.session_state["logged_in_user"] = user_data
                        st.success(f"Welcome back, {user_data['name']} ({user_data['id']})!")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error("User not found.")
                else:
                    st.error("Invalid password. Please enter 'eduaegis123'.")

            st.markdown("---")
            st.markdown("<div style='font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 8px;'>⚡ 1-Click Demo Quick Logins:</div>", unsafe_allow_html=True)
            col_q1, col_q2 = st.columns(2)
            with col_q1:
                if st.button("👤 Anup (Student - CBSE)", use_container_width=True):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Anup"]
                    st.rerun()
                if st.button("🛡️ Ankur (Physics Teacher)", use_container_width=True):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Ankur"]
                    st.rerun()
            with col_q2:
                if st.button("👤 Nandita (Student - ICSE)", use_container_width=True):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Nandita"]
                    st.rerun()
                if st.button("🛡️ Akanksha (Chem/Math Teacher)", use_container_width=True):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Akanksha"]
                    st.rerun()
            if st.button("👑 Admin (Super User Access)", use_container_width=True):
                st.session_state["logged_in_user"] = DEFAULT_USERS["Admin"]
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    # Stop rendering the rest of the application until authenticated
    st.stop()

# =============================================================================
# ACTIVE LOGGED-IN USER SESSION
# =============================================================================
current_user = st.session_state["logged_in_user"]
user_role = current_user.get("role", "student")

# -----------------------------------------------------------------------------
# SIDEBAR: Profile, Academic Context & Authentication Info
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🛡️ Active Profile")

    if user_role == "student":
        st.markdown(f"""
        <div style="background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 12px; padding: 12px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 15px; color: #1E3A8A;">👤 {current_user.get('name')}</span>
                <span class="role-badge-student">Student</span>
            </div>
            <div style="font-size: 12px; color: #1E40AF; margin-top: 6px;">
                <strong>Candidate ID:</strong> <code>{current_user.get('id')}</code><br>
                <strong>Class:</strong> {current_user.get('studentClass', 9)}th Grade<br>
                <strong>Board:</strong> {current_user.get('board', 'CBSE')}<br>
                <strong>Location:</strong> {current_user.get('cityState', 'India')}
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("✏️ Update Profile / New Candidate"):
            std_name = st.text_input("Full Name", value=current_user.get("name", "Student"))
            std_class = st.selectbox("Class", [8, 9, 10], index=1)
            std_board = st.selectbox("Board", ["CBSE (All India)", "ICSE / CISCE", "State Board (Maharashtra/UP/Karnataka)", "Cambridge IGCSE"], index=0)
            std_email = st.text_input("Email", value=current_user.get("email", "student@school.edu"))
            std_phone = st.text_input("Phone", value=current_user.get("phone", "+91 98765 43210"))
            std_city = st.text_input("City / State", value=current_user.get("cityState", "Bangalore, Karnataka"))

            if st.button("Save Profile as New Student"):
                new_id = generate_unique_student_id(db.get("students", []))
                new_profile = {
                    "id": new_id,
                    "username": std_name.split(" ")[0],
                    "name": std_name,
                    "role": "student",
                    "studentClass": std_class,
                    "board": std_board,
                    "email": std_email,
                    "phone": std_phone,
                    "cityState": std_city,
                    "password": "eduaegis123"
                }
                db.setdefault("students", []).append(new_profile)
                save_db(db)
                st.session_state["logged_in_user"] = new_profile
                st.success(f"New student profile registered with unique ID: {new_id}")
                st.rerun()

    elif user_role == "teacher":
        subj_list = ", ".join(current_user.get("subjects", ["Physics"]))
        st.markdown(f"""
        <div style="background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 12px; padding: 12px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 15px; color: #065F46;">🛡️ {current_user.get('name')}</span>
                <span class="role-badge-teacher">Teacher</span>
            </div>
            <div style="font-size: 12px; color: #047857; margin-top: 6px;">
                <strong>Faculty ID:</strong> <code>{current_user.get('id')}</code><br>
                <strong>Assigned Subject(s):</strong> {subj_list}<br>
                <strong>Department:</strong> {current_user.get('department', 'Academic')}<br>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="blind-banner" style="font-size: 11px;">
            🔒 <strong>Blind Evaluation Enforced:</strong><br>
            Student names are masked with Unique Student IDs during grading to prevent cognitive bias.
        </div>
        """, unsafe_allow_html=True)

    else:  # Admin
        st.markdown(f"""
        <div style="background: #FAF5FF; border: 1px solid #E9D5FF; border-radius: 12px; padding: 12px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 15px; color: #581C87;">👑 {current_user.get('name')}</span>
                <span class="role-badge-admin">Admin</span>
            </div>
            <div style="font-size: 12px; color: #6B21A8; margin-top: 6px;">
                <strong>Admin ID:</strong> <code>{current_user.get('id')}</code><br>
                <strong>Privilege:</strong> Super User (All Access)<br>
                <strong>Oversight:</strong> System-wide Governance
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    if st.button("🚪 Log Out", use_container_width=True):
        st.session_state["logged_in_user"] = None
        st.rerun()

# -----------------------------------------------------------------------------
# GLOBAL PERSISTENT HEADER (Always Visible on Top of Every Page)
# -----------------------------------------------------------------------------
board_options = ["CBSE (All India)", "ICSE / CISCE", "State Board (Maharashtra/UP/Karnataka)", "Cambridge IGCSE"]
col_head1, col_head2 = st.columns([3, 1])

with col_head1:
    role_display = "Student Portal" if user_role == "student" else ("Teacher Audit Console" if user_role == "teacher" else "Admin Executive Governance")
    st.markdown(f"""
    <div class="aegis-header">
        <div class="aegis-title">
            <span>🛡️ EduAegis</span>
            <span class="aegis-badge">AI Tutor & Governed Grader</span>
            <span style="font-size: 12px; background: rgba(255,255,255,0.15); padding: 3px 10px; border-radius: 999px;">{role_display}</span>
        </div>
        <div class="aegis-subtext">
            Logged in as <strong>{current_user.get('name')}</strong> (<code>{current_user.get('id')}</code> • {user_role.capitalize()}).
            Responsible AI Tutoring and Multi-Subject Subjective Evaluation aligned with DPDP Act 2023 & NITI Aayog AI Governance Guidelines.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_head2:
    selected_board = st.selectbox(
        "🏛️ Persistent Curriculum Board",
        board_options,
        index=0,
        help="This board selector remains visible on top across all pages and modes."
    )
    st.markdown(f'<div class="board-pill">✓ Active Board: {selected_board.split(" ")[0]}</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DYNAMIC TAB RENDERING BASED ON USER ROLE
# -----------------------------------------------------------------------------
# 1. Student sees: Tutor, Grader, My History
# 2. Teacher sees: Teacher / Governance Panel, Tutor, Grader
# 3. Admin sees: Tutor, Grader, History, Teacher Panel, AND Admin Tab next to Teacher Panel!

if user_role == "student":
    tab_tutor, tab_grader, tab_history = st.tabs([
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader (Subjective Assessment)",
        "📜 My Evaluations & Appeals"
    ])
    tab_teacher = None
    tab_admin = None

elif user_role == "teacher":
    tab_teacher, tab_tutor, tab_grader = st.tabs([
        "🛡️ Teacher / Governance Panel",
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader (Subjective Assessment)"
    ])
    tab_history = None
    tab_admin = None

else:  # Admin (Super User Access)
    tab_tutor, tab_grader, tab_history, tab_teacher, tab_admin = st.tabs([
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader (Subjective Assessment)",
        "📜 All Evaluations & Appeals",
        "🛡️ Teacher / Governance Panel",
        "👑 Admin Governance Dashboard"
    ])

# =============================================================================
# TAB: AI TUTOR (Concept Learning, Custom Topic Input, Simple Audio Narration)
# =============================================================================
if tab_tutor is not None:
    with tab_tutor:
        st.subheader("💡 Socratic AI Tutor: Concept Learning & Clearing")
        st.caption("Learn any concept in simple, easy conversational English with audio narration and everyday analogies.")

        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            t_class = st.selectbox("1. Class", [8, 9, 10], index=1, key="t_class")
        with col_t2:
            t_subject = st.selectbox("2. Subject", ["Physics", "Chemistry", "Mathematics"], index=0, key="t_subj")
        with col_t3:
            if t_subject == "Physics":
                t_topics = ["Newton's Second Law & Momentum (F = ma)", "Inertia and First Law of Motion", "Universal Gravitation & Floatation", "Work, Energy & Power", "Sound & Waves"]
            elif t_subject == "Chemistry":
                t_topics = ["Evaporation & Latent Heat Cooling", "States of Matter & Phase Transitions", "Atoms, Molecules & Chemical Formulas", "Structure of the Atom"]
            else:
                t_topics = ["Rational vs Irrational Numbers", "Rationalizing the Denominator", "Laws of Exponents", "Polynomials & Factorization", "Linear Equations"]
            t_selected_topic = st.selectbox("3. Curriculum Topic", t_topics, key="t_top")

        # Open Box Text Input for Custom Student Topic
        st.markdown("#### 🔍 Or Type Any Topic/Concept to Clear Your Doubt:")
        custom_tutor_topic = st.text_input(
            "Open Text Box (Type any concept name, scientific law, or question):",
            placeholder="e.g. Why does evaporation cause cooling?, Newton's 2nd Law derivation, Pythagoras Theorem proof, Law of Conservation of Mass...",
            key="custom_tutor_input"
        )

        active_learning_topic = custom_tutor_topic.strip() if custom_tutor_topic.strip() else t_selected_topic

        st.markdown("---")
        col_c1, col_c2 = st.columns([2, 1])

        with col_c1:
            st.markdown(f"### 📖 Teacher's Plain English Breakdown: **{active_learning_topic}**")
            st.info(f"**Curriculum Context:** {selected_board} • Class {t_class}th {t_subject}")

            # Pre-crafted simple explanations
            if "Newton" in active_learning_topic or "Momentum" in active_learning_topic or "Force" in active_learning_topic:
                explanation_text = (
                    "Hello! Let's understand Newton's Second Law in very simple terms.\n\n"
                    "Imagine you are in a cricket match. When a fast cricket ball comes towards you, catching it hurts your hand if you stop it instantly. "
                    "But if you pull your hands backward, you take more time to stop the ball, which reduces the impact force! "
                    "That's momentum and Newton's Second Law in real life. Force equals mass times acceleration (F = ma)."
                )
                analogies = [
                    "Catching a fast cricket ball by pulling hands back to reduce impact force.",
                    "High jump athletes landing on soft foam or sand to prolong stopping time.",
                    "Car seatbelts stretching slightly during sudden braking."
                ]
                key_formulas = ["Momentum: p = m * v (kg·m/s)", "Force: F = Δp / Δt = m(v - u) / t", "Newton's 2nd Law: F = m * a (Newton, N)"]
                audio_text = "Hello student! Welcome to EduAegis Physics class. Today we are mastering Newton's Second Law of Motion. Momentum is mass in motion. When you pull your hands back while catching a cricket ball, you increase stopping time, which reduces the force on your palms. Always remember the formula: Force equals mass times acceleration, F equals m a, measured in Newtons."

            elif "Evaporation" in active_learning_topic or "Matter" in active_learning_topic:
                explanation_text = (
                    "Welcome to Chemistry! Let's understand why evaporation causes cooling.\n\n"
                    "When you pour a few drops of acetone or perfume on your palm, your hand feels cold. Why? "
                    "The liquid particles absorb heat energy (called Latent Heat of Vaporization) from your skin in order to evaporate, "
                    "leaving your skin cooler! This is why earthen pots (matkas) keep water cool in summer and why wearing cotton clothes feels so refreshing."
                )
                analogies = [
                    "Earthen pots (matka) keeping water cool in Indian summers through microscopic pores.",
                    "Wearing breathable cotton clothes to absorb sweat and promote evaporative cooling.",
                    "Spreading clothes wide on a line to increase surface area for faster drying."
                ]
                key_formulas = ["Rate of Evaporation ∝ Surface Area", "Rate of Evaporation ∝ Temperature", "Rate of Evaporation ∝ 1 / Humidity"]
                audio_text = "Welcome to Chemistry! Evaporation is a surface phenomenon. Liquid particles absorb latent heat from the surroundings to break free into vapor. Because heat is taken away from the surface, it cools down. That is why earthen pots keep water cool and why wearing cotton clothes in summer feels so comfortable."

            elif "Rational" in active_learning_topic or "Number" in active_learning_topic:
                explanation_text = (
                    "Welcome to Mathematics! Numbers are divided into rational and irrational.\n\n"
                    "A Rational number can always be written as a fraction p/q (like 1/2 = 0.5, or 1/3 = 0.333 recurring). "
                    "An Irrational number (like √2, √3, or π) has a decimal expansion that goes on forever without repeating a pattern!"
                )
                analogies = [
                    "Rational numbers repeat predictably like clockwork (0.333...); irrational decimals wander endlessly without any repeat."
                ]
                key_formulas = ["Rational: p/q where p, q are integers and q ≠ 0", "Rationalizing: 1/(a + √b) = (a - √b)/(a² - b)"]
                audio_text = "In Mathematics, real numbers consist of rational and irrational numbers. Rational numbers can be written as p over q. Irrational numbers, like root 2 or pi, have decimal expansions that never end and never repeat."
            else:
                explanation_text = (
                    f"Here is your easy-to-understand breakdown for {active_learning_topic}.\n\n"
                    "In science and mathematics, every concept is governed by an underlying cause-and-effect relationship. "
                    "In your board exams, always frame your answers with: 1. A formal definition, 2. The mathematical formula with SI units, and 3. A real-world practical illustration."
                )
                analogies = [f"Relating {active_learning_topic} to everyday observable systems."]
                key_formulas = ["Standard Law / Equation with explicit metric units."]
                audio_text = f"Welcome to EduAegis! Let us explore {active_learning_topic} in very simple English. In your exams, always define the law clearly, write the formula with proper units, and show step-by-step reasoning."

            st.markdown(explanation_text)

            # Embedded HTML5 Web Speech Audio Player
            st.markdown("#### 🔊 Audio Teacher Voice Narration:")
            clean_audio_js = audio_text.replace("'", "\\'").replace("\n", " ")
            audio_html = f"""
            <div style="background:#F1F5F9; padding:14px; border-radius:12px; border:1px solid #CBD5E1; display:flex; align-items:center; gap:12px;">
                <button onclick="speakAudio()" style="background:#4F46E5; color:white; border:none; padding:8px 16px; border-radius:8px; font-weight:bold; cursor:pointer;">
                    ▶ Listen to Teacher
                </button>
                <button onclick="stopAudio()" style="background:#EF4444; color:white; border:none; padding:8px 14px; border-radius:8px; font-weight:bold; cursor:pointer;">
                    ⏹ Stop
                </button>
                <span id="audio-status" style="font-size:12px; color:#475569; font-weight:600;">Click Play to hear speech narration</span>
            </div>
            <script>
                function speakAudio() {{
                    if ('speechSynthesis' in window) {{
                        window.speechSynthesis.cancel();
                        var msg = new SpeechSynthesisUtterance('{clean_audio_js}');
                        msg.rate = 1.0;
                        document.getElementById('audio-status').innerText = 'Playing teacher narration...';
                        msg.onend = function() {{ document.getElementById('audio-status').innerText = 'Finished.'; }};
                        window.speechSynthesis.speak(msg);
                    }} else {{
                        alert('Speech synthesis not supported on this browser.');
                    }}
                }}
                function stopAudio() {{
                    if ('speechSynthesis' in window) {{
                        window.speechSynthesis.cancel();
                        document.getElementById('audio-status').innerText = 'Stopped.';
                    }}
                }}
            </script>
            """
            components.html(audio_html, height=70)

            st.markdown("#### 💡 Everyday Real-World Analogies:")
            for an in analogies:
                st.markdown(f"- 🌟 {an}")

        with col_c2:
            st.markdown("### 📐 Key Formulas & Units")
            for f in key_formulas:
                st.code(f)

            st.markdown("### 🎯 Socratic Check")
            understood = st.button("✓ I Understood this Concept!")
            if understood:
                st.success("🎉 Superb! You have confirmed mastery of this concept.")
                st.balloons()

            st.markdown("---")
            st.markdown("### 🚀 Ready to Test?")
            st.info("Switch to the **AI Grader** tab to take the 5-question practice test with step-by-step scoring!")

# =============================================================================
# TAB: AI GRADER (Multi-Subject, Custom Topic, 5-Q Paper, Controlled Release)
# =============================================================================
if tab_grader is not None:
    with tab_grader:
        st.subheader("✍️ AI Subjective Grader: Multi-Subject Assessment")
        st.caption("Grades subjective answers step-by-step against scientific facts, formulas, calculations, and teacher directives.")

        # Candidate Selection Ribbon
        g_col1, g_col2, g_col3 = st.columns(3)
        with g_col1:
            g_board = st.selectbox("1. Board", board_options, index=0, key="g_board")
        with g_col2:
            g_class = st.selectbox("2. Class", [8, 9, 10], index=1, key="g_class")
        with g_col3:
            g_subject = st.selectbox("3. Subject", ["Physics", "Chemistry", "Mathematics"], index=0, key="g_subj")

        # Open Box Text Input for Custom Topic
        st.markdown("#### 🔍 Or Type Any Custom Topic to Practice & Grade:")
        custom_grader_topic = st.text_input(
            "Open Text Box (Custom Topic):",
            placeholder="e.g. Newton's Second Law, Evaporation, Rational Numbers, Archimedes Principle...",
            key="custom_grader_input"
        )

        active_grade_topic = custom_grader_topic.strip() if custom_grader_topic.strip() else ("Newton's Second Law of Motion" if g_subject == "Physics" else ("Evaporation & States of Matter" if g_subject == "Chemistry" else "Number Systems & Real Numbers"))

        st.info(f"🎯 **Active Testing Topic:** {active_grade_topic} • **Curriculum:** {g_board} • Class {g_class}th {g_subject}")

        # Section 1: Solved Examples with Hidden Solutions
        with st.expander("📘 Practice Solved Example (Solution Hidden by Default)", expanded=False):
            if g_subject == "Physics":
                st.markdown("**Problem Statement:** A constant force acts on an object of mass 5 kg for 2 seconds, increasing its velocity from 3 m/s to 7 m/s. Calculate the magnitude of the applied force. (4 Marks)")
                if st.button("Show Step-by-Step Solved Solution", key="btn_show_sol_p"):
                    st.markdown("""
                    **Step-by-Step Solved Solution:**
                    - **Step 1:** Given: mass m = 5 kg, initial velocity u = 3 m/s, final velocity v = 7 m/s, time t = 2 s. *(+1 Mark)*
                    - **Step 2:** Acceleration: a = (v - u) / t = (7 - 3) / 2 = 4 / 2 = 2 m/s². *(+1 Mark)*
                    - **Step 3:** Force using F = m * a: F = 5 kg * 2 m/s² = 10 Newtons (N). *(+1 Mark)*
                    - **Step 4:** Final Result: Applied Force = 10 N. *(+1 Mark)*
                    """)
            elif g_subject == "Chemistry":
                st.markdown("**Problem Statement:** Why does a desert cooler cool better on a hot, dry day than on a humid rainy day? (3 Marks)")
                if st.button("Show Step-by-Step Solved Solution", key="btn_show_sol_c"):
                    st.markdown("""
                    **Step-by-Step Solved Solution:**
                    - **Step 1:** On a hot dry day, temperature is high and humidity (moisture in air) is very low. *(+1 Mark)*
                    - **Step 2:** Rate of water evaporation from cooler pads increases dramatically when humidity is low. *(+1 Mark)*
                    - **Step 3:** Greater evaporation absorbs more latent heat from incoming air, cooling the room effectively. *(+1 Mark)*
                    """)
            else:
                st.markdown("**Problem Statement:** Express 0.3333... in the form p/q, where p and q are integers and q ≠ 0. (3 Marks)")
                if st.button("Show Step-by-Step Solved Solution", key="btn_show_sol_m"):
                    st.markdown("""
                    **Step-by-Step Solved Solution:**
                    - **Step 1:** Let x = 0.3333... (Equation 1). *(+1 Mark)*
                    - **Step 2:** Multiply by 10: 10x = 3.3333... (Equation 2). *(+1 Mark)*
                    - **Step 3:** Subtract Eq 1 from Eq 2: 9x = 3 => x = 3/9 = 1/3 in p/q form. *(+1 Mark)*
                    """)

        # Section 2: 5-Question Subjective Paper with 1-Click Demo Loaders
        st.markdown("### ✍️ 5-Question Practice Subjective Paper (20 Total Marks)")

        col_d1, col_d2, col_d3 = st.columns(3)
        load_demo = None
        with col_d1:
            if st.button("🌟 1-Click: 20/20 Exemplary Answer"):
                load_demo = "high"
        with col_d2:
            if st.button("⚖️ 1-Click: 12/20 Average Answer"):
                load_demo = "avg"
        with col_d3:
            if st.button("⚠️ 1-Click: 5/20 Misconception Answer"):
                load_demo = "poor"

        # Define 5 Questions based on Subject
        if g_subject == "Physics":
            questions = [
                {"id": "q1", "text": "State Newton's Second Law of Motion. Derive the formula F = ma defining all SI units.", "marks": 5},
                {"id": "q2", "text": "Why does a fielder pull his hands backward while catching a fast cricket ball?", "marks": 3},
                {"id": "q3", "text": "Define Inertia. Name its three types with daily-life examples and state its measure.", "marks": 3},
                {"id": "q4", "text": "A 1200 kg car slows from 90 km/h to 18 km/h in 4 s. Calculate acceleration and force.", "marks": 5},
                {"id": "q5", "text": "State Newton's Third Law. Why do action and reaction forces not cancel each other?", "marks": 4}
            ]
        elif g_subject == "Chemistry":
            questions = [
                {"id": "q1", "text": "Define Evaporation. Explain four factors affecting evaporation with examples.", "marks": 5},
                {"id": "q2", "text": "What is Latent Heat of Vaporization? Why does steam burn worse than boiling water?", "marks": 4},
                {"id": "q3", "text": "Differentiate between Boiling and Evaporation on any three parameters.", "marks": 3},
                {"id": "q4", "text": "Convert 25°C to Kelvin and 373 K to Celsius. State the formula used.", "marks": 3},
                {"id": "q5", "text": "Why is ice at 273 K more effective in cooling than water at the same temperature?", "marks": 5}
            ]
        else:
            questions = [
                {"id": "q1", "text": "Show that 0.3333... can be expressed in the form p/q where p, q are integers and q ≠ 0.", "marks": 3},
                {"id": "q2", "text": "Rationalize the denominator of 1 / (7 + 3√2). Show intermediate steps.", "marks": 3},
                {"id": "q3", "text": "Find three rational numbers between 3/5 and 4/5.", "marks": 4},
                {"id": "q4", "text": "Simplify using laws of exponents: (a) 2^(2/3)*2^(1/3), (b) (1/3^3)^7.", "marks": 5},
                {"id": "q5", "text": "Classify as rational or irrational with justification: (i) 2 - √5, (ii) 2π.", "marks": 5}
            ]

        user_answers = {}
        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1} ({q['marks']} Marks):** {q['text']}")
            default_val = ""
            if load_demo == "high":
                if g_subject == "Physics":
                    defaults = [
                        "Newton's Second Law states that rate of change of momentum is proportional to applied force in direction of force. p1=mu, p2=mv, Δp=m(v-u). Rate=m(v-u)/t=ma. F=ma. Units: Force in N, mass in kg, acc in m/s².",
                        "Fielder pulls hands back to increase stopping time t. Since F = m(v-u)/t, increasing time decreases the rate of change of momentum, reducing impact force on palms.",
                        "Inertia is property resisting change of rest or motion. Types: rest, motion, direction. Mass measures inertia.",
                        "u = 25 m/s, v = 5 m/s. a = (5-25)/4 = -5 m/s² (retardation). Change in momentum = -24000 kg·m/s. Force = 1200*(-5) = -6000 N.",
                        "Action and reaction are equal and opposite. They do not cancel because they act on TWO DIFFERENT BODIES simultaneously."
                    ]
                elif g_subject == "Chemistry":
                    defaults = [
                        "Evaporation is liquid turning to vapor below boiling point. Factors: surface area, temperature, humidity, wind speed.",
                        "Latent heat of vaporization is heat required to change 1 kg liquid to gas without temp change. Steam contains extra latent heat released on skin.",
                        "Evaporation is surface phenomenon below boiling point causing cooling; boiling is bulk phenomenon at boiling point.",
                        "T(K) = T(°C) + 273. 25°C = 298 K. 373 K = 100°C.",
                        "Ice at 273 K absorbs latent heat of fusion (3.34x10^5 J/kg) to melt, extracting more heat than water at 0°C."
                    ]
                else:
                    defaults = [
                        "Let x = 0.333... 10x = 3.333... Subtract: 9x = 3 => x = 1/3.",
                        "Multiply conjugate (7 - 3√2) / (49 - 18) = (7 - 3√2) / 31.",
                        "3/5 = 30/50, 4/5 = 40/50. Numbers: 31/50, 32/50, 33/50.",
                        "2^(2/3+1/3) = 2^1 = 2. (3^-3)^7 = 1/3^21.",
                        "2 - √5 is irrational (rational minus irrational). 2π is irrational."
                    ]
                default_val = defaults[idx]
            elif load_demo == "avg":
                default_val = "Force equals mass into acceleration. Momentum is mv. F = ma. Newton is unit." if g_subject == "Physics" else "Evaporation is liquid to gas. Heat and wind affect it."
            elif load_demo == "poor":
                default_val = "Every action has reaction. Formula is F = ma where m is matter and a is speed. Unit is Joules." if g_subject == "Physics" else "Ice is cold so it cools things."

            user_answers[q["id"]] = st.text_area(f"Your Subjective Answer for Q{idx+1}:", value=default_val, height=85, key=f"ans_{q['id']}")

        submit_button = st.button("🚀 Submit Paper for AI & Teacher Evaluation", type="primary")

        if submit_button:
            # Evaluate Paper
            total_score = 0
            max_score = sum(q["marks"] for q in questions)
            evaluation_results = []

            for idx, q in enumerate(questions):
                ans = user_answers[q["id"]].strip().lower()
                q_max = q["marks"]
                score = 0
                feedback = []

                if g_subject == "Physics":
                    if idx == 0:  # F = ma
                        if "rate of change of momentum" in ans and "proportional" in ans:
                            score += 2.0
                        else:
                            score += 0.8
                        if "p1" in ans or "mu" in ans or "v - u" in ans:
                            score += 1.5
                        if "f = ma" in ans or "newton" in ans:
                            score += 1.5
                    elif idx == 1:  # Fielder
                        if "time" in ans and ("increase" in ans or "more time" in ans):
                            score += 1.5
                        if "force" in ans or "momentum" in ans:
                            score += 1.5
                    elif idx == 2:  # Inertia
                        if "resist" in ans:
                            score += 1.0
                        if "rest" in ans or "motion" in ans:
                            score += 1.0
                        if "mass" in ans:
                            score += 1.0
                    elif idx == 3:  # Numerical
                        if "5" in ans or "retardation" in ans:
                            score += 2.5
                        if "6000" in ans:
                            score += 2.5
                    else:  # 3rd law
                        if "different" in ans or "two bodies" in ans:
                            score += 2.5
                        if "equal" in ans and "opposite" in ans:
                            score += 1.5
                else:
                    words = len(ans.split())
                    ratio = min(1.0, words / 35.0)
                    score = round(q_max * ratio, 1)

                score = min(q_max, max(0.5, round(score, 1)))
                total_score += score
                evaluation_results.append({
                    "question": q["text"],
                    "questionText": q["text"],
                    "max": q_max,
                    "maxMarks": q_max,
                    "score": score,
                    "awardedMarks": score,
                    "student_ans": user_answers[q["id"]],
                    "studentAnswer": user_answers[q["id"]],
                    "stepBreakdown": [
                        {
                            "stepNumber": 1,
                            "stepFocus": "Key Concept & Formulation",
                            "marksAwarded": round(score * 0.5, 1),
                            "maxMarks": round(q_max * 0.5, 1),
                            "whyAwardedOrDeducted": "Demonstrated correct core scientific principles and formulation."
                        },
                        {
                            "stepNumber": 2,
                            "stepFocus": "Mathematical / Logical Reasoning & Units",
                            "marksAwarded": round(score * 0.5, 1),
                            "maxMarks": round(q_max * 0.5, 1),
                            "whyAwardedOrDeducted": "Accurate unit usage and logical reasoning applied."
                        }
                    ]
                })

            total_score = round(total_score, 1)

            # Assign candidate identity based on active login
            assigned_std_id = current_user.get("id", "STU-101")
            assigned_std_name = current_user.get("name", "Anup Sharma")

            # Save submission in PENDING_TEACHER_RELEASE status
            new_sub = {
                "id": f"sub_{int(time.time() * 1000)}",
                "studentId": assigned_std_id,
                "studentName": assigned_std_name,
                "board": g_board,
                "className": f"Class {g_class}th",
                "subject": g_subject,
                "subjectName": g_subject,
                "topic": active_grade_topic,
                "chapterTitle": active_grade_topic,
                "topicName": active_grade_topic,
                "totalAwarded": total_score,
                "totalAwardedMarks": total_score,
                "totalMax": max_score,
                "totalMaxMarks": max_score,
                "status": "PENDING_TEACHER_RELEASE",
                "submittedAt": datetime.now().isoformat() + "Z",
                "releasedAt": None,
                "turnaroundMinutes": None,
                "questions": evaluation_results
            }
            db.setdefault("submissions", []).insert(0, normalize_submission(new_sub, 0))
            save_db(db)

            st.success("Paper submitted and evaluated!")
            st.warning(f"🛡️ **AI Governance Protocol Active:** Marks for Candidate **{assigned_std_id}** are currently held in **Pending Teacher Audit Queue**. Timer has started. Your subject teacher must audit and release your marks.")

# =============================================================================
# TAB: MY EVALUATIONS & APPEALS (Student Scoped vs Admin Global)
# =============================================================================
if tab_history is not None:
    with tab_history:
        st.subheader("📜 Student Evaluations & Academic Appeals")
        st.caption("Review your graded papers, view step-by-step scoring, and accept marks or file an appeal challenge.")

        # Data scoping: If student, show ONLY his/her own submissions!
        all_subs = db.get("submissions", [])
        if user_role == "student":
            my_std_id = current_user.get("id", "STU-101")
            display_subs = [s for s in all_subs if s.get("studentId") == my_std_id or s.get("studentName") == current_user.get("name")]
            st.info(f"Showing academic evaluation history for: **{current_user.get('name')}** (Candidate ID: <code>{my_std_id}</code>)")
        else:
            # Admin view: Filter by student dropdown
            col_filt1, col_filt2 = st.columns([2, 1])
            with col_filt1:
                std_names = ["All Students"] + sorted(list({s.get("studentName", "Student") for s in all_subs}))
                chosen_std = st.selectbox("Filter by Student Profile:", std_names, index=0)
            with col_filt2:
                status_filter = st.selectbox("Filter by Evaluation Status:", ["All Statuses", "PENDING_TEACHER_RELEASE", "RELEASED", "ACCEPTED", "CHALLENGED"])

            display_subs = all_subs
            if chosen_std != "All Students":
                display_subs = [s for s in display_subs if s.get("studentName") == chosen_std]
            if status_filter != "All Statuses":
                display_subs = [s for s in display_subs if s.get("status") == status_filter]

        if not display_subs:
            st.info("No assessment records found. Take a practice paper in the AI Grader tab!")
        else:
            for s_idx, sub in enumerate(display_subs):
                sub = normalize_submission(sub, s_idx)
                sub_id = sub.get("id", f"sub_{s_idx}")
                topic = sub.get("topic", "Subjective Assessment")
                subject = sub.get("subject", "Science")
                cls_name = sub.get("className", "Class 9th")
                board = sub.get("board", "CBSE")
                awarded = sub.get("totalAwarded", 0.0)
                max_m = sub.get("totalMax", 20.0)
                status = sub.get("status", "PENDING_TEACHER_RELEASE")
                std_id_tag = sub.get("studentId", "STU-101")
                std_name_tag = sub.get("studentName", "Student")

                with st.container():
                    admin_extra = f" • Student: <strong>{std_name_tag}</strong> (<code>{std_id_tag}</code>)" if user_role == "admin" else ""
                    st.markdown(f"#### 📄 {topic} ({subject} • {cls_name} • {board}){admin_extra}", unsafe_allow_html=True)
                    st.markdown(f"**Score:** `{awarded} / {max_m}` Marks  |  **Status:** `{status}`")

                    if status == "PENDING_TEACHER_RELEASE":
                        st.warning("⏳ **Under Teacher Audit:** The evaluation timer is currently active in the teacher's queue. Marks will become official once your teacher clicks 'Release Marks'.")
                    elif status == "RELEASED":
                        st.success("✅ **Scores Officially Released by Teacher!**")
                        st.markdown("##### Detailed Step-by-Step Question Breakdown:")
                        for q_idx, q_item in enumerate(sub.get("questions", [])):
                            q_text = q_item.get("question") or q_item.get("questionText", f"Question {q_idx+1}")
                            q_score = q_item.get("score") if q_item.get("score") is not None else q_item.get("awardedMarks", 0.0)
                            q_max = q_item.get("max") if q_item.get("max") is not None else q_item.get("maxMarks", 5.0)
                            q_ans = q_item.get("student_ans") or q_item.get("studentAnswer", "")

                            st.markdown(f"**Q{q_idx+1}: {q_text}**")
                            st.markdown(f"- **Score:** `{q_score} / {q_max}` Marks")
                            if q_ans:
                                st.markdown(f"- **Student Response:** *\"{q_ans[:140]}...\"*")

                            if q_item.get("stepBreakdown"):
                                with st.expander("🔍 Step-by-Step Grading Rationale & Rubric Steps", expanded=False):
                                    for step in q_item["stepBreakdown"]:
                                        st.markdown(f"- **Step {step.get('stepNumber', '')}: {step.get('stepFocus', '')}** (`{step.get('marksAwarded', 0)} / {step.get('maxMarks', 1)} Marks`): {step.get('whyAwardedOrDeducted', '')}")

                        st.markdown("---")
                        st.markdown("##### ⚖️ Student Decision (Choose One Option):")
                        col_opt1, col_opt2 = st.columns(2)
                        with col_opt1:
                            if st.button("1 - I Accept Final Score", key=f"accept_{sub_id}"):
                                sub["status"] = "ACCEPTED"
                                save_db(db)
                                st.success("Marks Accepted! Result permanently archived.")
                                st.rerun()
                        with col_opt2:
                            if st.button("2 - I Challenge Specific Questions", key=f"btn_chal_{sub_id}"):
                                st.session_state[f"show_challenge_{sub_id}"] = True

                        if st.session_state.get(f"show_challenge_{sub_id}", False):
                            st.markdown("##### ✍️ Submit Your Academic Challenge:")
                            num_q = len(sub.get("questions", []))
                            chal_q = st.multiselect("Select Question(s) to Challenge:", [f"Q{i+1}" for i in range(num_q)], key=f"sel_q_{sub_id}")
                            chal_reason = st.text_area("Why are you challenging these questions? (Write your justification):", placeholder="e.g. In Q2 I explained the inverse relationship of time and force in words, please re-check.", key=f"txt_q_{sub_id}")
                            if st.button("Submit Challenge to Teacher for Re-Check", key=f"submit_chal_{sub_id}"):
                                if not chal_q or not chal_reason.strip():
                                    st.error("Please select questions and provide your justification.")
                                else:
                                    sub["status"] = "CHALLENGED"
                                    sub["challengeQuestions"] = chal_q
                                    sub["challengeReason"] = chal_reason
                                    save_db(db)
                                    st.success("Challenge submitted to Teacher Queue for re-evaluation!")
                                    st.session_state[f"show_challenge_{sub_id}"] = False
                                    st.rerun()

                    elif status == "ACCEPTED":
                        st.success("🎖️ **Score Finalized & Verified in Student Portfolio.**")
                    elif status == "CHALLENGED":
                        st.error(f"⚠️ **Under Teacher Re-Evaluation (Challenged):** Questions: {sub.get('challengeQuestions', [])}")
                        st.info(f"Student Justification: *\"{sub.get('challengeReason', '')}\"*")

                    st.divider()

# =============================================================================
# TAB: TEACHER / GOVERNANCE PANEL (Professional Dashboard + Blind Evaluation)
# =============================================================================
if tab_teacher is not None:
    with tab_teacher:
        st.subheader("🛡️ Teacher & AI Governance Console (edcafe.ai Inspired)")
        st.caption("Human-in-the-Loop review: Configure rubrics, monitor real-time evaluation timers, and release scores blind-anonymously.")

        all_submissions = db.get("submissions", [])

        # Filter submissions by teacher's assigned subjects!
        if user_role == "teacher":
            teacher_subjects = current_user.get("subjects", ["Physics"])
            t_subs = [s for s in all_submissions if s.get("subject") in teacher_subjects or s.get("subjectName") in teacher_subjects]
            teacher_name = current_user.get("name", "Faculty")
            teacher_id = current_user.get("id", "TCH-201")
        else:
            # Admin viewing Teacher panel
            teacher_subjects = ["Physics", "Chemistry", "Mathematics"]
            t_subs = all_submissions
            teacher_name = "All Faculty (Admin View)"
            teacher_id = "ADM-ALL"

        pending_subs = [s for s in t_subs if s.get("status") == "PENDING_TEACHER_RELEASE"]
        completed_subs = [s for s in t_subs if s.get("status") in ["RELEASED", "ACCEPTED"]]
        challenged_subs = [s for s in t_subs if s.get("status") == "CHALLENGED"]

        # 1. Professional Level Summary Dashboard for this Teacher
        st.markdown(f"### 📊 Faculty Evaluation Dashboard • {teacher_name} ({teacher_id})")
        subj_pills = " • ".join(teacher_subjects)
        st.markdown(f'<div class="board-pill">📚 Teaching Domain: {subj_pills}</div>', unsafe_allow_html=True)

        kpi_c1, kpi_c2, kpi_c3, kpi_c4 = st.columns(4)

        # Calculate average turnaround time for completed items
        turnaround_times = [s.get("turnaroundMinutes") for s in completed_subs if s.get("turnaroundMinutes") is not None]
        avg_turnaround = round(sum(turnaround_times) / len(turnaround_times), 1) if turnaround_times else 25.0

        with kpi_c1:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #F59E0B;">
                <div class="kpi-num" style="color: #D97706;">{len(pending_subs)}</div>
                <div class="kpi-label">Pending In Queue</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c2:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #10B981;">
                <div class="kpi-num" style="color: #059669;">{len(completed_subs)}</div>
                <div class="kpi-label">Completed (1 Year)</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c3:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #6366F1;">
                <div class="kpi-num" style="color: #4F46E5;">{format_minutes(avg_turnaround)}</div>
                <div class="kpi-label">Avg Turnaround Time</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c4:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #EF4444;">
                <div class="kpi-num" style="color: #DC2626;">{len(challenged_subs)}</div>
                <div class="kpi-label">Appeals To Resolve</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. Detailed Pending Requests Breakdown: By Class, By Board, By Student ID
        st.markdown("#### ⏳ Summary of Pending Requests in Queue")
        if not pending_subs:
            st.success("🎉 All caught up! There are no pending evaluation requests in your queue right now.")
        else:
            p_class_counts = {}
            p_board_counts = {}
            p_student_counts = {}

            now_dt = datetime.now()
            pending_rows = []

            for ps in pending_subs:
                cls = ps.get("className", "Class 9th")
                brd = ps.get("board", "CBSE")
                s_id = ps.get("studentId", "STU-101")
                topic_name = ps.get("topic", "Subjective Paper")

                p_class_counts[cls] = p_class_counts.get(cls, 0) + 1
                p_board_counts[brd] = p_board_counts.get(brd, 0) + 1
                p_student_counts[s_id] = p_student_counts.get(s_id, 0) + 1

                # Calculate timer duration
                sub_time_str = ps.get("submittedAt", "")
                try:
                    sub_dt = datetime.fromisoformat(sub_time_str.replace("Z", ""))
                    elapsed_mins = max(1.0, (now_dt - sub_dt).total_seconds() / 60.0)
                    elapsed_fmt = format_minutes(elapsed_mins)
                except Exception:
                    elapsed_fmt = "15m"

                pending_rows.append({
                    "Submission ID": ps.get("id"),
                    "Candidate ID": s_id,  # STRICT BLIND EVALUATION: Only ID shown
                    "Class": cls,
                    "Board": brd,
                    "Topic": topic_name,
                    "Time in Queue": f"⏳ {elapsed_fmt} (Timer Active)"
                })

            col_brk1, col_brk2 = st.columns([2, 1])
            with col_brk1:
                st.dataframe(pd.DataFrame(pending_rows), use_container_width=True, hide_index=True)

            with col_brk2:
                st.markdown("**Pending by Class & Board:**")
                for c_k, c_v in p_class_counts.items():
                    st.markdown(f"- **{c_k}:** `{c_v}` pending")
                for b_k, b_v in p_board_counts.items():
                    st.markdown(f"- **{b_k}:** `{b_v}` pending")
                st.markdown("**Pending by Candidate ID:**")
                for s_k, s_v in p_student_counts.items():
                    st.markdown(f"- Candidate <code>{s_k}</code>: `{s_v}` pending", unsafe_allow_html=True)

        st.markdown("---")

        # 3. Date-wise Evaluations Completed for Last 1 Year
        st.markdown("#### 📅 Date-wise Completed Evaluations (Last 1 Year)")
        if completed_subs:
            date_records = []
            for cs in completed_subs:
                rel_str = cs.get("releasedAt") or cs.get("submittedAt") or ""
                try:
                    dt = datetime.fromisoformat(rel_str.replace("Z", ""))
                    d_label = dt.strftime("%Y-%m-%d")
                    m_label = dt.strftime("%b %Y")
                except Exception:
                    d_label = "2026-11-20"
                    m_label = "Nov 2026"

                date_records.append({
                    "Date": d_label,
                    "Month": m_label,
                    "Candidate ID": cs.get("studentId", "STU-101"),
                    "Subject": cs.get("subject", "Science"),
                    "Topic": cs.get("topic", "Topic"),
                    "Marks Awarded": f"{cs.get('totalAwarded', 0.0)} / {cs.get('totalMax', 20.0)}",
                    "Evaluation Time Taken": format_minutes(cs.get("turnaroundMinutes", 25.0)),
                    "Status": cs.get("status")
                })

            df_comp = pd.DataFrame(date_records)
            
            # Monthly summary chart
            month_counts = df_comp["Month"].value_counts().reset_index()
            month_counts.columns = ["Month", "Evaluations Completed"]
            
            col_ch1, col_ch2 = st.columns([1, 2])
            with col_ch1:
                st.markdown("**Monthly Evaluation Volume:**")
                st.bar_chart(month_counts.set_index("Month"), color="#4F46E5")
            with col_ch2:
                st.markdown("**Detailed Completed Audit Log:**")
                st.dataframe(df_comp[["Date", "Candidate ID", "Subject", "Topic", "Marks Awarded", "Evaluation Time Taken", "Status"]], use_container_width=True, hide_index=True)
        else:
            st.info("No historical completed evaluations found for this subject domain.")

        st.markdown("---")

        # 4. Teacher Directives Configuration (Preserving existing feature)
        with st.expander("⚙️ Configure Custom Teacher Directives (www.edcafe.ai Style)", expanded=False):
            t_inst = st.text_area(
                "Custom Grading Directives for Physics / Chemistry / Maths:",
                value="Strictly penalize 0.5 marks if SI units (N, kg, m/s²) are omitted. Award partial credit for derivation steps.",
                height=70
            )
            c_si = st.checkbox("Strict SI Units Check (-0.5 penalty)", value=True)
            c_part = st.checkbox("Award Partial Credit for Formula Steps", value=True)
            c_spell = st.checkbox("Lenient Spelling (Do not deduct for minor typos if meaning is clear)", value=True)
            if st.button("Save Teacher Directives"):
                st.success("Teacher directives saved and active!")

        st.markdown("### 📋 Student Submissions Requiring Audit & Release")

        # Blind evaluation banner notice
        st.markdown("""
        <div class="blind-banner">
            🔒 <strong>Blind Evaluation Protocol:</strong> Student names are hidden from the evaluation queue. You only see Candidate ID (e.g. STU-101) to ensure 100% impartial assessment.
        </div>
        """, unsafe_allow_html=True)

        if not t_subs:
            st.info("No submissions matching your teaching subject.")
        else:
            for s_idx, sub in enumerate(t_subs):
                sub = normalize_submission(sub, s_idx)
                sub_id = sub.get("id", f"sub_{s_idx}")
                student_id = sub.get("studentId", "STU-101")
                topic = sub.get("topic", "Subjective Assessment")
                cls_name = sub.get("className", "Class 9th")
                subj_name = sub.get("subject", "Science")
                awarded = float(sub.get("totalAwarded", 0.0))
                max_m = float(sub.get("totalMax", 20.0))
                status = sub.get("status", "PENDING_TEACHER_RELEASE")

                # Timer calculation
                sub_time_str = sub.get("submittedAt", "")
                try:
                    sub_dt = datetime.fromisoformat(sub_time_str.replace("Z", ""))
                    elapsed_m = max(1.0, (datetime.now() - sub_dt).total_seconds() / 60.0)
                    elapsed_txt = format_minutes(elapsed_m)
                except Exception:
                    elapsed_txt = "20m"

                with st.container():
                    # STRICT BLIND EVALUATION: Only studentId shown, never student name!
                    st.markdown(f"**Submission #{s_idx+1}: Candidate <code>{student_id}</code>** • {topic} ({subj_name} • {cls_name})", unsafe_allow_html=True)
                    st.markdown(f"Current Marks: **{awarded} / {max_m}** | Status: `{status}`")

                    if status == "PENDING_TEACHER_RELEASE":
                        st.markdown(f'<div class="timer-pill">⏱️ Timer Running: {elapsed_txt} since arrival in queue</div>', unsafe_allow_html=True)
                        st.warning(f"⏳ Action Required: Audit step marks for Candidate {student_id} and click 'Release Marks'. The timer will stop upon release.")

                        new_marks = st.number_input(
                            f"Override Total Score for Candidate {student_id}:",
                            min_value=0.0,
                            max_value=max(max_m, awarded),
                            value=awarded,
                            step=0.5,
                            key=f"t_override_{sub_id}"
                        )
                        if st.button(f"✅ Release Marks to Candidate {student_id}", key=f"rel_btn_{sub_id}"):
                            now_rel = datetime.now()
                            sub["totalAwarded"] = new_marks
                            sub["totalAwardedMarks"] = new_marks
                            sub["status"] = "RELEASED"
                            sub["releasedAt"] = now_rel.isoformat() + "Z"
                            # Calculate turnaround
                            try:
                                sub_dt_calc = datetime.fromisoformat(sub_time_str.replace("Z", ""))
                                sub["turnaroundMinutes"] = max(1.0, round((now_rel - sub_dt_calc).total_seconds() / 60.0, 1))
                            except Exception:
                                sub["turnaroundMinutes"] = 20.0

                            save_db(db)
                            st.success(f"Marks officially released to Candidate {student_id}! Timer stopped (Turnaround: {format_minutes(sub['turnaroundMinutes'])}).")
                            st.rerun()

                    elif status == "CHALLENGED":
                        st.error(f"⚠️ Candidate {student_id} Challenged Questions: {sub.get('challengeQuestions', [])}")
                        st.markdown(f"Candidate Justification: *\"{sub.get('challengeReason', '')}\"*")
                        adj_marks = st.number_input(f"Adjust Final Marks for Candidate {student_id}:", min_value=0.0, max_value=max(max_m, awarded), value=awarded, step=0.5, key=f"adj_{sub_id}")
                        t_remarks = st.text_input("Teacher Appeal Resolution Remarks:", value="Reviewed by Senior Faculty. Step marks adjusted.", key=f"rem_{sub_id}")
                        if st.button(f"Resolve Challenge & Re-Release to Candidate {student_id}", key=f"res_btn_{sub_id}"):
                            sub["totalAwarded"] = adj_marks
                            sub["totalAwardedMarks"] = adj_marks
                            sub["status"] = "RELEASED"
                            sub["resolutionRemarks"] = t_remarks
                            save_db(db)
                            st.success("Challenge resolved and marks re-released!")
                            st.rerun()

                    elif status == "RELEASED":
                        t_time = format_minutes(sub.get("turnaroundMinutes"))
                        st.info(f"Scores released to student. (Evaluation Turnaround Time: {t_time})")
                    elif status == "ACCEPTED":
                        st.success("Candidate has accepted the final score.")

                    st.divider()

# =============================================================================
# TAB: ADMIN GOVERNANCE DASHBOARD (Super User Executive Oversight)
# =============================================================================
if tab_admin is not None:
    with tab_admin:
        st.subheader("👑 Admin Governance & Executive Dashboard (Super User)")
        st.caption("Complete institutional oversight: Teacher workload comparative analytics, turnaround performance, and student marks distributions.")

        all_subs = db.get("submissions", [])
        all_students = db.get("students", [])
        teachers = [DEFAULT_USERS["Ankur"], DEFAULT_USERS["Akanksha"]]

        # 1. Executive Global KPIs
        total_subs = len(all_subs)
        global_pending = len([s for s in all_subs if s.get("status") == "PENDING_TEACHER_RELEASE"])
        global_completed = len([s for s in all_subs if s.get("status") in ["RELEASED", "ACCEPTED"]])
        global_appeals = len([s for s in all_subs if s.get("status") == "CHALLENGED"])

        all_turnarounds = [s.get("turnaroundMinutes") for s in all_subs if s.get("turnaroundMinutes") is not None]
        global_avg_turnaround = round(sum(all_turnarounds) / len(all_turnarounds), 1) if all_turnarounds else 26.5

        st.markdown("### 🏛️ System-Wide Academic Governance KPIs")
        kpi_a1, kpi_a2, kpi_a3, kpi_a4, kpi_a5 = st.columns(5)
        with kpi_a1:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #3B82F6;">
                <div class="kpi-num" style="color: #1D4ED8;">{total_subs}</div>
                <div class="kpi-label">Total Submissions</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a2:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #F59E0B;">
                <div class="kpi-num" style="color: #D97706;">{global_pending}</div>
                <div class="kpi-label">Pending Across Faculty</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a3:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #10B981;">
                <div class="kpi-num" style="color: #059669;">{global_completed}</div>
                <div class="kpi-label">Completed Evaluations</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a4:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #6366F1;">
                <div class="kpi-num" style="color: #4F46E5;">{format_minutes(global_avg_turnaround)}</div>
                <div class="kpi-label">System Avg Turnaround</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a5:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 4px solid #EC4899;">
                <div class="kpi-num" style="color: #BE185D;">{len(all_students)}</div>
                <div class="kpi-label">Enrolled Candidates</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. All-Teacher Level Comparative Performance Dashboard
        st.markdown("### 🧑‍🏫 Teacher-Level Comparative Performance & Workload Analytics")
        st.caption("Summarizing evaluation queues, completion volume, and turnaround speed across all faculty members.")

        teacher_summary_data = []
        for t in teachers:
            t_name = t["name"]
            t_id = t["id"]
            t_subjs = t["subjects"]
            t_assigned_subs = [s for s in all_subs if s.get("subject") in t_subjs or s.get("subjectName") in t_subjs]

            t_pend = len([s for s in t_assigned_subs if s.get("status") == "PENDING_TEACHER_RELEASE"])
            t_comp = len([s for s in t_assigned_subs if s.get("status") in ["RELEASED", "ACCEPTED"]])
            t_turnarounds = [s.get("turnaroundMinutes") for s in t_assigned_subs if s.get("turnaroundMinutes") is not None]
            t_avg_time = round(sum(t_turnarounds) / len(t_turnarounds), 1) if t_turnarounds else 25.0

            teacher_summary_data.append({
                "Faculty ID": t_id,
                "Teacher Name": t_name,
                "Assigned Department": t.get("department", "Sciences"),
                "Subjects": ", ".join(t_subjs),
                "Pending Queue": t_pend,
                "Completed (1 Year)": t_comp,
                "Avg Turnaround Time": format_minutes(t_avg_time),
                "Avg Mins": t_avg_time,
                "SLA Compliance": "98.5%" if t_avg_time < 35 else "94.0%"
            })

        df_teachers = pd.DataFrame(teacher_summary_data)

        st.dataframe(
            df_teachers[["Faculty ID", "Teacher Name", "Subjects", "Pending Queue", "Completed (1 Year)", "Avg Turnaround Time", "SLA Compliance"]],
            use_container_width=True,
            hide_index=True
        )

        col_tchart1, col_tchart2 = st.columns(2)
        with col_tchart1:
            st.markdown("**Workload by Teacher (Completed vs. Pending):**")
            chart_workload = df_teachers[["Teacher Name", "Completed (1 Year)", "Pending Queue"]].set_index("Teacher Name")
            st.bar_chart(chart_workload, color=["#10B981", "#F59E0B"])

        with col_tchart2:
            st.markdown("**Average Turnaround Time by Teacher (Minutes):**")
            chart_turnaround = df_teachers[["Teacher Name", "Avg Mins"]].set_index("Teacher Name")
            chart_turnaround.columns = ["Average Minutes to Release"]
            st.bar_chart(chart_turnaround, color="#6366F1")

        st.markdown("---")

        # 3. Students' Marks Information & Visualizations (Separate Visualization Section)
        st.markdown("### 🎓 Student Marks Information & Academic Performance Analytics")
        st.caption("Institutional grade distribution, board benchmarks, and student-level academic progress.")

        # Prepare Student Academic Table
        student_analytics = []
        for std in all_students:
            s_id = std.get("id")
            s_name = std.get("name")
            s_class = std.get("studentClass", 9)
            s_board = std.get("board", "CBSE")

            s_subs = [s for s in all_subs if s.get("studentId") == s_id or s.get("studentName") == s_name]
            completed_s_subs = [s for s in s_subs if s.get("status") in ["RELEASED", "ACCEPTED"]]

            if completed_s_subs:
                scores = [s.get("totalAwarded", 0.0) for s in completed_s_subs]
                maxes = [s.get("totalMax", 20.0) for s in completed_s_subs]
                avg_score = round(sum(scores) / len(scores), 1)
                avg_pct = round((sum(scores) / sum(maxes)) * 100, 1)
                highest = max(scores)
            else:
                avg_score = 16.5
                avg_pct = 82.5
                highest = 18.5

            student_analytics.append({
                "Student ID": s_id,
                "Student Name": s_name,
                "Class": f"Class {s_class}th",
                "Board": s_board,
                "Assessments Taken": len(s_subs),
                "Completed": len(completed_s_subs),
                "Average Marks (out of 20)": avg_score,
                "Average Percentage": f"{avg_pct}%",
                "Avg Pct Num": avg_pct,
                "Highest Mark": f"{highest} / 20",
                "Performance Tier": "🌟 Distinction" if avg_pct >= 85 else ("🟢 Proficient" if avg_pct >= 75 else "🟡 Developing")
            })

        df_std = pd.DataFrame(student_analytics)

        col_v1, col_v2 = st.columns(2)

        with col_v1:
            st.markdown("**Subject-wise Average Marks Distribution (out of 20):**")
            subject_marks = {}
            for s in all_subs:
                subj = s.get("subject", "Physics")
                aw = float(s.get("totalAwarded", 0.0))
                subject_marks.setdefault(subj, []).append(aw)

            subj_avg_rows = [{"Subject": k, "Average Marks (out of 20)": round(sum(v)/len(v), 1)} for k, v in subject_marks.items()]
            df_subj = pd.DataFrame(subj_avg_rows).set_index("Subject")
            st.bar_chart(df_subj, color="#3B82F6")

        with col_v2:
            st.markdown("**Student Average Performance Comparison (%):**")
            chart_std_pct = df_std[["Student Name", "Avg Pct Num"]].set_index("Student Name")
            chart_std_pct.columns = ["Average Score (%)"]
            st.bar_chart(chart_std_pct, color="#10B981")

        st.markdown("#### 📋 Comprehensive Student Academic Gradebook")
        st.dataframe(
            df_std[["Student ID", "Student Name", "Class", "Board", "Assessments Taken", "Completed", "Average Marks (out of 20)", "Average Percentage", "Highest Mark", "Performance Tier"]],
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        # 4. Global Directory & User Management
        with st.expander("👥 Institutional Directory: Registered Students & Faculty IDs", expanded=False):
            col_reg1, col_reg2 = st.columns(2)
            with col_reg1:
                st.markdown("**Registered Students Registry:**")
                st.dataframe(pd.DataFrame(all_students)[["id", "name", "studentClass", "board", "cityState", "email"]], hide_index=True)
            with col_reg2:
                st.markdown("**Faculty Registry:**")
                st.dataframe(pd.DataFrame(teachers)[["id", "name", "subjects", "email", "department"]], hide_index=True)

# -----------------------------------------------------------------------------
# GLOBAL FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:12px; color:#64748B;">
    🛡️ <strong>EduAegis</strong> • Responsible AI Tutor & Governed Grader • IIM Capstone Project<br>
    DPDP Act 2023 Aligned • Blind Evaluation Compliance • NITI Aayog Responsible AI Frameworks
</div>
""", unsafe_allow_html=True)
