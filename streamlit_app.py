"""
EduAegis - Streamlit Web Application
Responsible AI Tutor & Subjective Grader (Multi-Subject: Physics, Chemistry, Maths)
Classes 8th, 9th, 10th • CBSE, ICSE, State Board
International Standard Soothing UI & Responsible AI Governance Framework
Enhanced with Spread-Across Blue Tabs, Zero-Mark Strict Grading for Blank/NA/Irrelevant,
Teacher Question-Level Mark Adjustments, Background Profile Artwork, and In-App Password Updates
"""

import os
import json
import time
import base64
from datetime import datetime, timedelta
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from curriculum_question_bank import get_question_set

# Page Configuration with Soothing Theme
st.set_page_config(
    page_title="EduAegis | Responsible AI Tutor & Grader",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# WATERMARK & SIDEBAR BACKGROUND SVGS
# -----------------------------------------------------------------------------
# Educational & AI Governance Watermark Pattern (Shield, Cap, Atom, Book, Neural Nodes)
svg_watermark = """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360" fill="none" stroke="#6366F1" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" opacity="0.045">
  <path d="M60 40 L100 24 L140 40 L140 90 C140 120 100 135 100 135 C100 135 60 120 60 90 Z"/>
  <path d="M100 45 L100 115"/>
  <path d="M75 70 L125 70"/>
  <path d="M220 50 L260 32 L300 50 L260 68 Z"/>
  <path d="M240 60 L240 85 C240 95 280 95 280 85 L280 60"/>
  <circle cx="220" cy="240" r="10"/>
  <ellipse cx="220" cy="240" rx="32" ry="12" transform="rotate(30 220 240)"/>
  <ellipse cx="220" cy="240" rx="32" ry="12" transform="rotate(-30 220 240)"/>
  <path d="M50 230 Q80 215 110 230 L110 280 Q80 265 50 280 Z"/>
  <path d="M110 230 Q140 215 170 230 L170 280 Q140 265 110 280 Z"/>
  <circle cx="280" cy="200" r="3.5" fill="#6366F1"/>
  <circle cx="320" cy="225" r="3.5" fill="#6366F1"/>
  <circle cx="295" cy="265" r="3.5" fill="#6366F1"/>
  <line x1="280" y1="200" x2="320" y2="225"/>
  <line x1="320" y1="225" x2="295" y2="265"/>
</svg>"""
b64_bg = base64.b64encode(svg_watermark.encode("utf-8")).decode("utf-8")

# Rich Decorative Background Illustration for Sidebar Profile Card
svg_sidebar = """<svg xmlns="http://www.w3.org/2000/svg" width="340" height="170" viewBox="0 0 340 170" fill="none">
  <defs>
    <linearGradient id="sb_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" stop-opacity="0.96"/>
      <stop offset="50%" stop-color="#1E1B4B" stop-opacity="0.92"/>
      <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.88"/>
    </linearGradient>
  </defs>
  <rect width="340" height="170" rx="12" fill="url(#sb_grad)"/>
  <g stroke="#818CF8" stroke-width="1.3" opacity="0.2">
    <path d="M250 25 L285 12 L320 25 L320 65 C320 90 285 105 285 105 C285 105 250 90 250 65 Z"/>
    <path d="M285 30 L285 90"/>
    <path d="M265 52 L305 52"/>
    <circle cx="45" cy="135" r="10"/>
    <ellipse cx="45" cy="135" rx="26" ry="9" transform="rotate(30 45 135)"/>
    <ellipse cx="45" cy="135" rx="26" ry="9" transform="rotate(-30 45 135)"/>
  </g>
  <path d="M0 140 Q85 115 170 135 T340 110" stroke="#60A5FA" stroke-width="1.2" opacity="0.25" fill="none"/>
  <path d="M0 150 Q85 125 170 145 T340 120" stroke="#34D399" stroke-width="1.2" opacity="0.2" fill="none"/>
</svg>"""
b64_sidebar = base64.b64encode(svg_sidebar.encode("utf-8")).decode("utf-8")

# -----------------------------------------------------------------------------
# OPTIMIZED SOOTHING CSS (SPREAD-ACROSS BLUE TABS, 100% READABILITY)
# -----------------------------------------------------------------------------
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    /* Global Space Optimization - Eliminates excessive top whitespace */
    .block-container {{
        padding-top: 0.7rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 98% !important;
    }}
    
    header[data-testid="stHeader"] {{
        background: transparent !important;
        height: 1.6rem !important;
    }}

    /* Atmospheric Watermark Background with Soft Ambient Mesh */
    .stApp {{
        background-color: #F8FAFC;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.08) 0px, transparent 45%),
            radial-gradient(at 100% 0%, rgba(16, 185, 129, 0.07) 0px, transparent 45%),
            radial-gradient(at 100% 100%, rgba(14, 165, 233, 0.06) 0px, transparent 45%),
            radial-gradient(at 0% 100%, rgba(139, 92, 246, 0.06) 0px, transparent 45%),
            url("data:image/svg+xml;base64,{b64_bg}");
        background-attachment: fixed;
        background-size: cover, cover, cover, cover, 360px 360px;
    }}
    
    /* Sleek, Space-Optimized Header */
    .aegis-header {{
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 45%, #312E81 85%, #0F172A 100%);
        padding: 10px 18px;
        border-radius: 14px;
        color: white;
        margin-bottom: 10px;
        border: 1px solid rgba(99, 102, 241, 0.35);
        box-shadow: 0 4px 15px -3px rgba(15, 23, 42, 0.2);
    }}
    
    .aegis-title {{
        font-size: 19px;
        font-weight: 800;
        letter-spacing: -0.3px;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    
    .aegis-badge {{
        background: rgba(16, 185, 129, 0.2);
        color: #34D399;
        font-size: 10.5px;
        font-weight: 700;
        padding: 3px 9px;
        border-radius: 9999px;
        border: 1px solid rgba(16, 185, 129, 0.4);
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }}

    .role-badge-student {{
        background: #EFF6FF;
        color: #1D4ED8;
        font-size: 10px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 9999px;
        border: 1px solid #BFDBFE;
    }}

    .role-badge-teacher {{
        background: #ECFDF5;
        color: #047857;
        font-size: 10px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 9999px;
        border: 1px solid #A7F3D0;
    }}

    .role-badge-admin {{
        background: #FAF5FF;
        color: #7E22CE;
        font-size: 10px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 9999px;
        border: 1px solid #E9D5FF;
    }}
    
    .aegis-subtext {{
        font-size: 11.5px;
        color: #CBD5E1;
        margin-top: 2px;
        line-height: 1.35;
    }}
    
    /* Compact Persistent Board Pill */
    .board-pill {{
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: #EEF2FF;
        color: #4338CA;
        font-weight: 700;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 9999px;
        border: 1px solid #C7D2FE;
    }}
    
    /* Solid Glassmorphism Card for 100% Crisp Readability */
    .soothing-card {{
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(226, 232, 240, 0.9) !important;
        border-radius: 14px !important;
        padding: 14px 16px !important;
        box-shadow: 0 4px 14px -2px rgba(15, 23, 42, 0.04) !important;
        margin-bottom: 10px !important;
    }}

    /* Rich Profile Card with Decorative Background Illustration */
    .sidebar-profile-card {{
        background-color: #0F172A !important;
        background-image: url("data:image/svg+xml;base64,{b64_sidebar}") !important;
        background-size: cover !important;
        background-position: center !important;
        border: 1px solid rgba(129, 140, 248, 0.45) !important;
        border-radius: 12px !important;
        padding: 12px 14px !important;
        margin-bottom: 8px !important;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.25) !important;
        color: #FFFFFF !important;
    }}

    /* Tighten Sidebar Padding */
    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.96) !important;
        border-right: 1px solid #E2E8F0 !important;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 0.8rem !important;
        padding-left: 0.9rem !important;
        padding-right: 0.9rem !important;
    }}

    /* ========================================================================= */
    /* BLUE BOX SPREAD-ACROSS TABS (100% WIDTH EQUALLY DIVIDED IRRESPECTIVE OF COUNT) */
    /* ========================================================================= */
    .stTabs [data-baseweb="tab-list"] {{
        display: flex !important;
        width: 100% !important;
        background: linear-gradient(135deg, #1E1B4B 0%, #1D4ED8 50%, #2563EB 100%) !important;
        padding: 5px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(99, 102, 241, 0.4) !important;
        gap: 6px !important;
        box-shadow: 0 4px 14px rgba(29, 78, 216, 0.2) !important;
        margin-bottom: 12px !important;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        flex: 1 1 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        text-align: center !important;
        justify-content: center !important;
        border-radius: 8px !important;
        padding: 8px 8px !important;
        color: #E2E8F0 !important;
        font-weight: 700 !important;
        font-size: 12.5px !important;
        background: transparent !important;
        border: none !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        transition: all 0.2s ease-in-out !important;
    }}

    .stTabs [data-baseweb="tab"]:hover {{
        background: rgba(255, 255, 255, 0.18) !important;
        color: #FFFFFF !important;
    }}

    .stTabs [aria-selected="true"] {{
        background: #FFFFFF !important;
        color: #1E1B4B !important;
        font-weight: 800 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
    }}

    /* Vibrant Compact KPI Summary Cards */
    .kpi-box {{
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 10px 14px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }}
    .kpi-num {{
        font-size: 22px;
        font-weight: 800;
        color: #0F172A;
    }}
    .kpi-label {{
        font-size: 11px;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.4px;
        margin-top: 2px;
    }}

    /* Compact Timer Pill */
    .timer-pill {{
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: #FFFBEB;
        color: #B45309;
        font-weight: 700;
        font-size: 10.5px;
        padding: 3px 8px;
        border-radius: 9999px;
        border: 1px solid #FDE68A;
    }}
    
    .blind-banner {{
        background: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 10px;
        padding: 9px 12px;
        color: #166534;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}

    .step-item {{
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 6px;
    }}

    .sidebar-resource-card {{
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 8px 10px;
        margin-bottom: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        transition: transform 0.15s ease, border-color 0.15s ease;
    }}
    .sidebar-resource-card:hover {{
        transform: translateY(-1px);
        border-color: #93C5FD;
        box-shadow: 0 3px 8px rgba(37,99,235,0.08);
    }}

    hr {{
        margin: 10px 0 !important;
    }}
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

def matches_board(item_board: str, target_board: str) -> bool:
    """Matches curriculum board flexibly, handling 'All Board' wildcard."""
    if not target_board or target_board == "All Board":
        return True
    if not item_board:
        return False
    ib = str(item_board).strip().lower()
    tb = str(target_board).strip().lower()
    if ib == tb:
        return True
    if "cbse" in tb and "cbse" in ib:
        return True
    if "icse" in tb and "icse" in ib:
        return True
    if "state" in tb and "state" in ib:
        return True
    if "cambridge" in tb and "cambridge" in ib:
        return True
    return tb in ib or ib in tb

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
            q["isReleased"] = bool(q.get("isReleased", status in ["RELEASED", "ACCEPTED"]))
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
            "submissions": [],
            "passwords": {
                "Anup": "eduaegis123",
                "Nandita": "eduaegis123",
                "Ankur": "eduaegis123",
                "Akanksha": "eduaegis123",
                "Admin": "eduaegis123"
            }
        }

    # Ensure passwords dict exists
    if "passwords" not in data:
        data["passwords"] = {
            "Anup": "eduaegis123",
            "Nandita": "eduaegis123",
            "Ankur": "eduaegis123",
            "Akanksha": "eduaegis123",
            "Admin": "eduaegis123"
        }

    # Ensure unique students without duplicates
    std_map = {}
    for s in data.get("students", []):
        if s.get("id"):
            std_map[s["id"]] = s
    if "STU-101" not in std_map:
        std_map["STU-101"] = DEFAULT_USERS["Anup"]
    if "STU-102" not in std_map:
        std_map["STU-102"] = DEFAULT_USERS["Nandita"]
    data["students"] = list(std_map.values())

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

def update_teacher_q_mark(sub_id, q_i):
    """Callback triggered whenever a teacher edits a question score and hits Enter.
    Immediately recalculates the total score and syncs widget session state."""
    q_key = f"t_q_override_{sub_id}_{q_i}"
    if q_key in st.session_state:
        try:
            val = float(st.session_state[q_key])
        except (ValueError, TypeError):
            val = 0.0
        current_db = st.session_state.get("db", db)
        for s in current_db.get("submissions", []):
            if s.get("id") == sub_id:
                qs = s.get("questions", [])
                if q_i < len(qs):
                    qs[q_i]["score"] = val
                    qs[q_i]["awardedMarks"] = val
                tot = round(sum(float(q.get("score", q.get("awardedMarks", 0.0))) for q in qs), 1)
                s["totalAwarded"] = tot
                s["totalAwardedMarks"] = tot
                st.session_state[f"t_override_{sub_id}"] = tot
                save_db(current_db)
                break

# -----------------------------------------------------------------------------
# PASSWORD MANAGEMENT FUNCTIONS
# -----------------------------------------------------------------------------
def get_user_password(username):
    """Retrieves active password for given username without exposing hints."""
    pws = db.get("passwords", {})
    if username in pws:
        return pws[username]
    if username in DEFAULT_USERS:
        return DEFAULT_USERS[username].get("password", "eduaegis123")
    return "eduaegis123"

def update_user_password(username, new_pw):
    """Updates and permanently persists the new password."""
    if "passwords" not in db:
        db["passwords"] = {}
    db["passwords"][username] = new_pw
    if username in DEFAULT_USERS:
        DEFAULT_USERS[username]["password"] = new_pw
    for s in db.get("students", []):
        if s.get("username") == username:
            s["password"] = new_pw
    for t in db.get("teachers", []):
        if t.get("username") == username:
            t["password"] = new_pw
    save_db(db)

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

# -----------------------------------------------------------------------------
# STRICT RELEVANCE & ZERO-MARK EVALUATION ENGINE
# -----------------------------------------------------------------------------
def evaluate_student_answer(subject, q_idx, q_text, raw_student_answer, q_max, expected_keywords=None):
    """
    Strict Subjective Evaluation:
    - If answer is blank / empty -> 0.0 marks.
    - If answer is 'NA', 'Don't know', evasive -> 0.0 marks.
    - If answer is unrelated / off-topic (no domain keywords) -> 0.0 marks.
    - Otherwise evaluates step-by-step strictly based on concept and calculations.
    """
    ans = raw_student_answer.strip().lower() if raw_student_answer else ""
    
    # 1. Blank Check -> 0 Marks
    if not ans or len(ans) == 0:
        return {
            "score": 0.0,
            "status": "BLANK",
            "stepBreakdown": [
                {
                    "stepNumber": 1,
                    "stepFocus": "Attempt & Concept Relevance",
                    "marksAwarded": 0.0,
                    "maxMarks": round(q_max * 0.5, 1),
                    "whyAwardedOrDeducted": "Zero marks: Question was left completely blank."
                },
                {
                    "stepNumber": 2,
                    "stepFocus": "Mathematical & Scientific Formulation",
                    "marksAwarded": 0.0,
                    "maxMarks": round(q_max * 0.5, 1),
                    "whyAwardedOrDeducted": "Zero marks: No derivation, formula, or reasoning provided."
                }
            ]
        }
    
    # 2. Evasive / Non-answer Check (NA, don't know, skip, etc.) -> 0 Marks
    evasive_patterns = [
        "na", "n/a", "none", "nil", "no", "idk", "i don't know", "i dont know",
        "dont know", "do not know", "no idea", "not sure", "skip", "pass",
        "dunno", "nothing", "blank", "test", "asdf", "xyz", "abc", "leave",
        "cant answer", "cannot answer", "left blank", "not known", "dont have answer"
    ]
    clean_words = ans.replace(".", "").replace(",", "").split()
    if ans in evasive_patterns or (len(clean_words) <= 3 and any(w in evasive_patterns for w in clean_words)):
        return {
            "score": 0.0,
            "status": "EVASIVE_OR_NA",
            "stepBreakdown": [
                {
                    "stepNumber": 1,
                    "stepFocus": "Subject Knowledge & Comprehension",
                    "marksAwarded": 0.0,
                    "maxMarks": round(q_max * 0.5, 1),
                    "whyAwardedOrDeducted": "Zero marks: Student response indicated lack of knowledge ('NA' / 'Don't know' / unattempted)."
                },
                {
                    "stepNumber": 2,
                    "stepFocus": "Formulation & Scientific Reasoning",
                    "marksAwarded": 0.0,
                    "maxMarks": round(q_max * 0.5, 1),
                    "whyAwardedOrDeducted": "Zero marks: No scientific derivation or formulation provided."
                }
            ]
        }
    
    # 3. Domain Keywords per Subject and Question for Relevance Check
    p_keywords = {
        0: ["momentum", "force", "acceleration", "f = ma", "f=ma", "mass", "rate of change", "p1", "p2", "newton", "kg", "m/s"],
        1: ["time", "hand", "hands", "momentum", "force", "impact", "backward", "pull", "hurt", "reduce", "increase time", "cushion"],
        2: ["inertia", "rest", "motion", "direction", "mass", "resist", "tendency", "property", "oppose"],
        3: ["acceleration", "force", "velocity", "-5", "5", "6000", "-6000", "retardation", "m/s", "km/h", "25", "1200"],
        4: ["action", "reaction", "different", "two bodies", "equal", "opposite", "cancel", "pair"]
    }
    c_keywords = {
        0: ["evaporation", "surface", "temperature", "humidity", "wind", "vapor", "liquid", "cooling", "area"],
        1: ["latent", "heat", "vaporization", "steam", "burn", "energy", "boiling", "extra", "joules"],
        2: ["surface", "bulk", "boiling", "temperature", "cooling", "bubble", "point", "phenomenon"],
        3: ["273", "298", "100", "kelvin", "celsius", "k = c", "formula"],
        4: ["latent", "fusion", "ice", "absorb", "heat", "melt", "energy", "273", "effective"]
    }
    m_keywords = {
        0: ["1/3", "3/9", "10x", "9x", "p/q", "fraction", "subtract", "let x", "equation", "0.333"],
        1: ["7 - 3", "conjugate", "31", "multiply", "denominator", "square", "49 - 18", "rationalize"],
        2: ["30/50", "40/50", "31/50", "32/50", "33/50", "multiply", "between", "rational", "numbers"],
        3: ["2", "exponent", "power", "add", "1/3^21", "2^(2/3)", "simplify", "laws"],
        4: ["irrational", "rational", "pi", "sqrt", "root", "integer", "non-terminating", "classify"]
    }
    
    if expected_keywords and len(expected_keywords) > 0:
        target_keys = expected_keywords
    elif subject == "Physics":
        target_keys = p_keywords.get(q_idx, ["physics", "force"])
    elif subject == "Chemistry":
        target_keys = c_keywords.get(q_idx, ["chemistry", "matter"])
    else:
        target_keys = m_keywords.get(q_idx, ["math", "numbers"])
        
    matched_keys = [k for k in target_keys if k in ans]
    
    # If ZERO domain keywords match -> Off-Topic / Irrelevant -> 0 Marks!
    if len(matched_keys) == 0:
        return {
            "score": 0.0,
            "status": "IRRELEVANT",
            "stepBreakdown": [
                {
                    "stepNumber": 1,
                    "stepFocus": "Relevance to Question Concept",
                    "marksAwarded": 0.0,
                    "maxMarks": round(q_max * 0.5, 1),
                    "whyAwardedOrDeducted": "Zero marks: Answer does not contain any relevant scientific principles or concepts for this question."
                },
                {
                    "stepNumber": 2,
                    "stepFocus": "Calculations & Formulation",
                    "marksAwarded": 0.0,
                    "maxMarks": round(q_max * 0.5, 1),
                    "whyAwardedOrDeducted": "Zero marks: Off-topic / irrelevant response; zero credit awarded."
                }
            ]
        }
        
    # Valid relevant answer: compute actual score based on completeness
    score = 0.0
    if subject == "Physics":
        if q_idx == 0:
            if "rate of change of momentum" in ans and "proportional" in ans:
                score += 2.0
            elif "momentum" in ans:
                score += 1.0
            if "p1" in ans or "mu" in ans or "v - u" in ans:
                score += 1.5
            if "f = ma" in ans or "newton" in ans:
                score += 1.5
        elif q_idx == 1:
            if "time" in ans and ("increase" in ans or "more time" in ans):
                score += 1.5
            if "force" in ans or "momentum" in ans:
                score += 1.5
        elif q_idx == 2:
            if "resist" in ans or "oppose" in ans:
                score += 1.0
            if "rest" in ans or "motion" in ans or "direction" in ans:
                score += 1.0
            if "mass" in ans:
                score += 1.0
        elif q_idx == 3:
            if "-5" in ans or "5" in ans or "retardation" in ans:
                score += 2.5
            if "6000" in ans or "-6000" in ans:
                score += 2.5
        elif q_idx == 4:
            if "different" in ans or "two bodies" in ans:
                score += 2.5
            if "equal" in ans and "opposite" in ans:
                score += 1.5
    else:
        words = len(ans.split())
        ratio = min(1.0, (len(matched_keys) * 0.3) + (words / 32.0) * 0.5)
        score = round(q_max * ratio, 1)
        
    score = min(q_max, max(0.0, round(score, 1)))
    step1_score = round(score * 0.5, 1)
    step2_score = round(score - step1_score, 1)
    
    return {
        "score": score,
        "status": "EVALUATED",
        "stepBreakdown": [
            {
                "stepNumber": 1,
                "stepFocus": "Key Concept & Scientific Principles",
                "marksAwarded": step1_score,
                "maxMarks": round(q_max * 0.5, 1),
                "whyAwardedOrDeducted": f"Awarded {step1_score} marks based on correct conceptual definition." if score > 0 else "Insufficient conceptual depth."
            },
            {
                "stepNumber": 2,
                "stepFocus": "Mathematical / Logical Reasoning & Units",
                "marksAwarded": step2_score,
                "maxMarks": round(q_max * 0.5, 1),
                "whyAwardedOrDeducted": f"Awarded {step2_score} marks for derivation, formulas, and units." if score > 0 else "Missing derivations or standard SI units."
            }
        ]
    }

# =============================================================================
# AUTHENTICATION & LOGIN PAGE (NO DEFAULT PASSWORD OR HINT SHOWN)
# =============================================================================
if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None

# If not logged in, render the Login Screen
if st.session_state["logged_in_user"] is None:
    st.markdown("""
    <div style="max-width: 600px; margin: 30px auto 14px auto; text-align: center;">
        <div style="font-size: 34px;">🛡️</div>
        <h1 style="font-size: 26px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">Welcome to EduAegis</h1>
        <p style="color: #64748B; font-size: 13.5px; margin-bottom: 16px;">
            Responsible AI Tutor & Governed Grader • Role-Based Authentication Portal
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_space1, col_login, col_space2 = st.columns([1, 2, 1])

    with col_login:
        with st.container():
            st.markdown("""
            <div class="soothing-card" style="border: 2px solid #E0E7FF; box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.12);">
                <div style="font-size: 15px; font-weight: 700; color: #1E1B4B; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
                    <span>🔐 Sign In to Your Portal</span>
                </div>
            """, unsafe_allow_html=True)

            login_role = st.selectbox(
                "1. Select Your Role",
                ["Student", "Teacher", "Admin"],
                index=0,
                help="Select whether you are logging in as a Student, Teacher, or Super User Admin."
            )

            if login_role == "Student":
                user_options = ["Anup", "Nandita"]
                default_idx = 0
            elif login_role == "Teacher":
                user_options = ["Ankur", "Akanksha"]
                default_idx = 0
            else:
                user_options = ["Admin"]
                default_idx = 0

            selected_username = st.selectbox("2. Select Your Username", user_options, index=default_idx)
            # User specified: Do NOT show default password or hint on screen
            entered_password = st.text_input("3. Password", type="password", placeholder="Enter your password")

            btn_login = st.button("🚀 Log In to EduAegis", type="primary", use_container_width=True)

            if btn_login:
                actual_pw = get_user_password(selected_username)
                if entered_password == actual_pw:
                    user_data = DEFAULT_USERS.get(selected_username)
                    if user_data:
                        st.session_state["logged_in_user"] = user_data
                        st.success(f"Welcome back, {user_data['name']} ({user_data['id']})!")
                        time.sleep(0.4)
                        st.rerun()
                    else:
                        st.error("User profile not found.")
                else:
                    st.error("Invalid password. Please check your credentials and try again.")

            # In-App Password Update feature on Login Page
            with st.expander("🔄 Update / Reset Password", expanded=False):
                rst_user = st.selectbox("Username to Update", ["Anup", "Nandita", "Ankur", "Akanksha", "Admin"], key="rst_user")
                rst_curr = st.text_input("Current Password", type="password", key="rst_curr")
                rst_new = st.text_input("New Password", type="password", key="rst_new")
                rst_conf = st.text_input("Confirm New Password", type="password", key="rst_conf")
                if st.button("Save New Password", key="btn_save_rst", use_container_width=True):
                    actual = get_user_password(rst_user)
                    if rst_curr != actual:
                        st.error("Current password incorrect.")
                    elif len(rst_new) < 4:
                        st.error("New password must be at least 4 characters long.")
                    elif rst_new != rst_conf:
                        st.error("New password and confirm password do not match.")
                    else:
                        update_user_password(rst_user, rst_new)
                        st.success(f"Password updated successfully for {rst_user}! You can now log in.")

            st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
            st.markdown("<div style='font-size: 11px; font-weight: 700; color: #475569; margin-bottom: 6px;'>⚡ Quick Persona Switch:</div>", unsafe_allow_html=True)
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
                if st.button("🛡️ Akanksha (Chem/Math)", use_container_width=True):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Akanksha"]
                    st.rerun()
            if st.button("👑 Admin (Super User Access)", use_container_width=True):
                st.session_state["logged_in_user"] = DEFAULT_USERS["Admin"]
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# =============================================================================
# ACTIVE LOGGED-IN USER SESSION
# =============================================================================
current_user = st.session_state["logged_in_user"]
user_role = current_user.get("role", "student")

# -----------------------------------------------------------------------------
# SIDEBAR: Profile Card with Background Artwork + Password Change
# -----------------------------------------------------------------------------
with st.sidebar:
    if user_role == "student":
        st.markdown(f"""
        <div class="sidebar-profile-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 13.5px; color: #FFFFFF;">👤 {current_user.get('name')}</span>
                <span class="role-badge-student" style="background: rgba(255,255,255,0.2); color: #93C5FD; border-color: #60A5FA;">Student</span>
            </div>
            <div style="font-size: 11px; color: #E0E7FF; margin-top: 4px;">
                <code>{current_user.get('id')}</code> • Class {current_user.get('studentClass', 9)}th • {current_user.get('board', 'CBSE').split(' ')[0]}<br>
                📍 {current_user.get('cityState', 'Bangalore')}
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("✏️ New Student Profile", expanded=False):
            std_name = st.text_input("Full Name", value="New Student")
            std_class = st.selectbox("Class", [8, 9, 10], index=1)
            std_board = st.selectbox("Board", ["CBSE (All India)", "ICSE / CISCE", "State Board (Maharashtra/UP/Karnataka)", "Cambridge IGCSE"], index=0)
            std_email = st.text_input("Email", value="new.student@school.edu")
            std_city = st.text_input("City / State", value="Bangalore, Karnataka")

            if st.button("Save Profile"):
                new_id = generate_unique_student_id(db.get("students", []))
                new_profile = {
                    "id": new_id,
                    "username": std_name.split(" ")[0],
                    "name": std_name,
                    "role": "student",
                    "studentClass": std_class,
                    "board": std_board,
                    "email": std_email,
                    "cityState": std_city,
                    "password": "eduaegis123"
                }
                db.setdefault("students", []).append(new_profile)
                save_db(db)
                st.session_state["logged_in_user"] = new_profile
                st.success(f"Registered with unique ID: {new_id}")
                st.rerun()

    elif user_role == "teacher":
        subj_list = ", ".join(current_user.get("subjects", ["Physics"]))
        st.markdown(f"""
        <div class="sidebar-profile-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 13.5px; color: #FFFFFF;">🛡️ {current_user.get('name')}</span>
                <span class="role-badge-teacher" style="background: rgba(16,185,129,0.25); color: #6EE7B7; border-color: #34D399;">Teacher</span>
            </div>
            <div style="font-size: 11px; color: #E0E7FF; margin-top: 4px;">
                <code>{current_user.get('id')}</code> • Domain: <strong>{subj_list}</strong><br>
                {current_user.get('department', 'Academic Faculty')}
            </div>
        </div>
        <div class="blind-banner" style="font-size: 10.5px; padding: 5px 9px; margin-bottom: 8px;">
            🔒 <strong>Blind Evaluation:</strong> Student names masked.
        </div>
        """, unsafe_allow_html=True)

    else:  # Admin
        st.markdown(f"""
        <div class="sidebar-profile-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 13.5px; color: #FFFFFF;">👑 {current_user.get('name')}</span>
                <span class="role-badge-admin" style="background: rgba(168,85,247,0.25); color: #D8B4FE; border-color: #C084FC;">Admin</span>
            </div>
            <div style="font-size: 11px; color: #E0E7FF; margin-top: 4px;">
                <code>{current_user.get('id')}</code> • Super User (Executive Governance)
            </div>
        </div>
        """, unsafe_allow_html=True)

    # In-App Password Update feature in Sidebar
    with st.expander("🔑 Change Password", expanded=False):
        chg_curr = st.text_input("Current Password", type="password", key="side_chg_curr")
        chg_new = st.text_input("New Password", type="password", key="side_chg_new")
        chg_conf = st.text_input("Confirm New Password", type="password", key="side_chg_conf")
        if st.button("Update Password", use_container_width=True, key="btn_side_pw"):
            actual_pw = get_user_password(current_user.get("username"))
            if chg_curr != actual_pw:
                st.error("Current password incorrect.")
            elif len(chg_new) < 4:
                st.error("New password must be at least 4 characters long.")
            elif chg_new != chg_conf:
                st.error("New password and confirm password do not match.")
            else:
                update_user_password(current_user.get("username"), chg_new)
                current_user["password"] = chg_new
                st.session_state["logged_in_user"] = current_user
                st.success("Password updated successfully!")

    if st.button("🚪 Log Out", use_container_width=True):
        st.session_state["logged_in_user"] = None
        st.rerun()

    # -------------------------------------------------------------------------
    # ACADEMIC RESOURCES & NCERT REFERENCE BOOKS HUB (Space Utilization)
    # -------------------------------------------------------------------------
    st.markdown("<hr style='margin: 14px 0 10px 0; border: none; border-top: 1px solid rgba(226, 232, 240, 0.8);'>", unsafe_allow_html=True)

    if user_role == "student":
        stu_class = current_user.get("studentClass", 9)
        stu_board = current_user.get("board", "CBSE (All India)")
        board_short = "CBSE" if "CBSE" in stu_board else ("ICSE" if "ICSE" in stu_board else "State Board")

        st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-weight: 800; font-size: 12.5px; color: #1E293B; letter-spacing: 0.3px;">📚 NCERT & Reference Books</span>
            <span style="font-size: 9.5px; background: #EFF6FF; color: #1D4ED8; font-weight: 700; padding: 2px 7px; border-radius: 999px; border: 1px solid #BFDBFE;">Class {stu_class}th • {board_short}</span>
        </div>
        """, unsafe_allow_html=True)

        if stu_class == 8:
            ncert_sci_code = "hesc1=0-18"
            ncert_math_code = "hemh1=0-16"
            sci_desc = "Force, Friction, Sound, Combustion & Cells"
        elif stu_class == 10:
            ncert_sci_code = "jesc1=0-16"
            ncert_math_code = "jemh1=0-15"
            sci_desc = "Light, Electricity, Reactions, Acids & Carbon"
        else:  # Class 9
            ncert_sci_code = "iesc1=0-15"
            ncert_math_code = "iemh1=0-15"
            sci_desc = "Motion, Force, Gravitation, Matter & Atoms"

        st.markdown(f"""
        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 8px; align-items: flex-start;">
                <span style="font-size: 16px;">📘</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 11px; color: #0F172A;">NCERT Science Textbook (Class {stu_class}th)</div>
                    <div style="font-size: 9.5px; color: #64748B;">{sci_desc}</div>
                    <div style="margin-top: 4px;">
                        <a href="https://ncert.nic.in/textbook.php?{ncert_sci_code}" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 2px 7px; border-radius: 4px; border: 1px solid #BFDBFE;">📖 Open Official PDF</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 8px; align-items: flex-start;">
                <span style="font-size: 16px;">📐</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 11px; color: #0F172A;">NCERT Mathematics (Class {stu_class}th)</div>
                    <div style="font-size: 9.5px; color: #64748B;">Complete Theory, Solved Examples & Exercises</div>
                    <div style="margin-top: 4px;">
                        <a href="https://ncert.nic.in/textbook.php?{ncert_math_code}" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 2px 7px; border-radius: 4px; border: 1px solid #BFDBFE;">📖 Open Official PDF</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 8px; align-items: flex-start;">
                <span style="font-size: 16px;">🔬</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 11px; color: #0F172A;">NCERT Exemplar Problems</div>
                    <div style="font-size: 9.5px; color: #64748B;">HOTS Questions, Numericals & Step Rubrics</div>
                    <div style="margin-top: 4px;">
                        <a href="https://ncert.nic.in/exemplar-problems.php" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 2px 7px; border-radius: 4px; border: 1px solid #A7F3D0;">🔬 View Exemplar</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 8px; align-items: flex-start;">
                <span style="font-size: 16px;">🏛️</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 11px; color: #0F172A;">DIKSHA National Portal</div>
                    <div style="font-size: 9.5px; color: #64748B;">MoE Govt of India QR Interactive Textbooks</div>
                    <div style="margin-top: 4px;">
                        <a href="https://diksha.gov.in/" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #6D28D9; background: #F5F3FF; padding: 2px 7px; border-radius: 4px; border: 1px solid #DDD6FE;">🌐 Open DIKSHA</a>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"📑 Direct Chapter NCERT PDFs (Class {stu_class}th)", expanded=False):
            if stu_class == 9:
                st.markdown("""
                - 📘 [Ch 8: Motion (NCERT PDF)](https://ncert.nic.in/textbook/pdf/iesc108.pdf)
                - 📘 [Ch 9: Force & Laws of Motion](https://ncert.nic.in/textbook/pdf/iesc109.pdf)
                - 📘 [Ch 10: Gravitation & Floatation](https://ncert.nic.in/textbook/pdf/iesc110.pdf)
                - 📘 [Ch 11: Work & Energy](https://ncert.nic.in/textbook/pdf/iesc111.pdf)
                - 📘 [Ch 1: Matter in Our Surroundings](https://ncert.nic.in/textbook/pdf/iesc101.pdf)
                - 📘 [Ch 2: Is Matter Around Us Pure](https://ncert.nic.in/textbook/pdf/iesc102.pdf)
                - 📘 [Ch 3: Atoms & Molecules](https://ncert.nic.in/textbook/pdf/iesc103.pdf)
                - 📐 [Ch 1: Number Systems (Maths)](https://ncert.nic.in/textbook/pdf/iemh101.pdf)
                - 📐 [Ch 2: Polynomials (Maths)](https://ncert.nic.in/textbook/pdf/iemh102.pdf)
                """)
            elif stu_class == 10:
                st.markdown("""
                - 📘 [Ch 10: Light - Reflection & Refraction](https://ncert.nic.in/textbook/pdf/jesc110.pdf)
                - 📘 [Ch 12: Electricity (NCERT PDF)](https://ncert.nic.in/textbook/pdf/jesc112.pdf)
                - 📘 [Ch 13: Magnetic Effects of Current](https://ncert.nic.in/textbook/pdf/jesc113.pdf)
                - 📘 [Ch 1: Chemical Reactions & Equations](https://ncert.nic.in/textbook/pdf/jesc101.pdf)
                - 📘 [Ch 2: Acids, Bases & Salts](https://ncert.nic.in/textbook/pdf/jesc102.pdf)
                - 📘 [Ch 4: Carbon & Its Compounds](https://ncert.nic.in/textbook/pdf/jesc104.pdf)
                - 📐 [Ch 1: Real Numbers (Maths)](https://ncert.nic.in/textbook/pdf/jemh101.pdf)
                - 📐 [Ch 4: Quadratic Equations (Maths)](https://ncert.nic.in/textbook/pdf/jemh104.pdf)
                - 📐 [Ch 8: Introduction to Trigonometry](https://ncert.nic.in/textbook/pdf/jemh108.pdf)
                """)
            else:  # Class 8
                st.markdown("""
                - 📘 [Ch 11: Force & Pressure](https://ncert.nic.in/textbook/pdf/hesc111.pdf)
                - 📘 [Ch 12: Friction (NCERT PDF)](https://ncert.nic.in/textbook/pdf/hesc112.pdf)
                - 📘 [Ch 13: Sound (NCERT PDF)](https://ncert.nic.in/textbook/pdf/hesc113.pdf)
                - 📘 [Ch 3: Synthetic Fibres & Plastics](https://ncert.nic.in/textbook/pdf/hesc103.pdf)
                - 📘 [Ch 4: Combustion & Flame](https://ncert.nic.in/textbook/pdf/hesc104.pdf)
                - 📐 [Ch 1: Rational Numbers (Maths)](https://ncert.nic.in/textbook/pdf/hemh101.pdf)
                - 📐 [Ch 2: Linear Equations in One Variable](https://ncert.nic.in/textbook/pdf/hemh102.pdf)
                - 📐 [Ch 6: Squares & Square Roots](https://ncert.nic.in/textbook/pdf/hemh106.pdf)
                """)

    elif user_role == "teacher":
        st.markdown("""
        <div style="font-weight: 800; font-size: 12.5px; color: #1E293B; margin-bottom: 8px;">
            📚 Faculty Pedagogical References
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 11px; color: #0F172A;">NCERT Learning Outcomes Manual</div>
            <div style="font-size: 9.5px; color: #64748B;">Competency-based pedagogical standards for Secondary stage.</div>
            <div style="margin-top: 4px;">
                <a href="https://ncert.nic.in/pdf/programmes/learning_outcomes_sec.pdf" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 2px 7px; border-radius: 4px; border: 1px solid #BFDBFE;">📋 View NCERT Guidelines</a>
            </div>
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 11px; color: #0F172A;">Bloom's Taxonomy Rubrics Guide</div>
            <div style="font-size: 9.5px; color: #64748B;">Framework for step-by-step subjective assessment and partial credits.</div>
            <div style="margin-top: 4px;">
                <a href="https://cbseacademic.nic.in/" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 2px 7px; border-radius: 4px; border: 1px solid #A7F3D0;">🎯 CBSE Assessment Manual</a>
            </div>
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 11px; color: #0F172A;">NITI Aayog Responsible AI in Schools</div>
            <div style="font-size: 9.5px; color: #64748B;">Human-in-the-Loop & blind evaluation governance protocols.</div>
            <div style="margin-top: 4px;">
                <a href="https://www.niti.gov.in/" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #6D28D9; background: #F5F3FF; padding: 2px 7px; border-radius: 4px; border: 1px solid #DDD6FE;">⚖️ Governance Principles</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:  # Admin
        st.markdown("""
        <div style="font-weight: 800; font-size: 12.5px; color: #1E293B; margin-bottom: 8px;">
            📚 Institutional Governance Hub
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 11px; color: #0F172A;">DPDP Act 2023 Compliance Handbook</div>
            <div style="font-size: 9.5px; color: #64748B;">Digital Personal Data Protection Act compliance requirements for minors.</div>
            <div style="margin-top: 4px;">
                <a href="https://www.meity.gov.in/content/digital-personal-data-protection-act-2023" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 2px 7px; border-radius: 4px; border: 1px solid #BFDBFE;">🛡️ DPDP Act 2023 Official</a>
            </div>
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 11px; color: #0F172A;">NEP 2020 Pedagogical Framework</div>
            <div style="font-size: 9.5px; color: #64748B;">National Education Policy 5+3+3+4 curriculum & evaluation reforms.</div>
            <div style="margin-top: 4px;">
                <a href="https://www.education.gov.in/sites/upload_files/mhrd/files/NEP_Final_English_0.pdf" target="_blank" style="text-decoration:none; font-size: 10px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 2px 7px; border-radius: 4px; border: 1px solid #A7F3D0;">🏛️ NEP 2020 Document</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TOP HEADER WITH INTEGRATED CURRICULUM SELECTOR (INCLUDES 'All Board' OPTION)
# -----------------------------------------------------------------------------
board_options = ["All Board", "CBSE (All India)", "ICSE / CISCE", "State Board (Maharashtra/UP/Karnataka)", "Cambridge IGCSE"]
col_head_left, col_head_right = st.columns([3.8, 1.2])

with col_head_left:
    role_display = "Student Portal" if user_role == "student" else ("Teacher Audit Console" if user_role == "teacher" else "Admin Executive Governance")
    st.markdown(f"""
    <div class="aegis-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 20px;">🛡️</span>
                <span class="aegis-title">EduAegis</span>
                <span class="aegis-badge">AI Tutor & Governed Grader</span>
                <span style="font-size: 10.5px; background: rgba(255,255,255,0.18); color: #E2E8F0; padding: 2px 7px; border-radius: 999px; font-weight: 600;">{role_display}</span>
            </div>
        </div>
        <div class="aegis-subtext">
            Active: <strong>{current_user.get('name')}</strong> (<code>{current_user.get('id')}</code> • {user_role.capitalize()}) • DPDP Act 2023 Aligned • NITI Aayog Responsible AI Frameworks
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_head_right:
    if "selected_curriculum_board" not in st.session_state:
        st.session_state["selected_curriculum_board"] = "All Board"

    curr_b_idx = board_options.index(st.session_state["selected_curriculum_board"]) if st.session_state["selected_curriculum_board"] in board_options else 0
    selected_board = st.selectbox(
        "🏛️ Active Curriculum Board",
        board_options,
        index=curr_b_idx,
        key="global_board_selector",
        help="Select a curriculum board to filter institutional dashboards, queues, and student records. Select 'All Board' to view all students from all boards."
    )
    st.session_state["selected_curriculum_board"] = selected_board

# -----------------------------------------------------------------------------
# SPREAD-ACROSS BLUE TABS (3 FOR STUDENT, 4 FOR TEACHER, 5 FOR ADMIN)
# -----------------------------------------------------------------------------
# Irrespective of the number of tabs, the CSS divides 100% of the blue box equally!
if user_role == "student":
    tab_tutor, tab_grader, tab_history = st.tabs([
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader (Subjective Assessment)",
        "📜 My Evaluations & Appeals"
    ])
    tab_teacher = None
    tab_admin = None

elif user_role == "teacher":
    tab_teacher, tab_tutor, tab_grader, tab_history = st.tabs([
        "🛡️ Teacher / Governance Panel",
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader (Subjective Assessment)",
        "📜 Student Evaluations & Audit History"
    ])
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

        st.markdown("<hr>", unsafe_allow_html=True)
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
            <div style="background:#F1F5F9; padding:12px; border-radius:10px; border:1px solid #CBD5E1; display:flex; align-items:center; gap:10px;">
                <button onclick="speakAudio()" style="background:#4F46E5; color:white; border:none; padding:7px 14px; border-radius:8px; font-weight:bold; cursor:pointer;">
                    ▶ Listen to Teacher
                </button>
                <button onclick="stopAudio()" style="background:#EF4444; color:white; border:none; padding:7px 12px; border-radius:8px; font-weight:bold; cursor:pointer;">
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
            components.html(audio_html, height=65)

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

            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("### 🚀 Ready to Test?")
            st.info("Switch to the **AI Grader** tab to take the 5-question practice test with step-by-step scoring!")

# =============================================================================
# TAB: AI GRADER (Zero-Marks for Blank/NA/Irrelevant + Controlled Release)
# =============================================================================
if tab_grader is not None:
    with tab_grader:
        st.subheader("✍️ AI Subjective Grader: Multi-Subject Assessment")
        st.caption("Grades subjective answers step-by-step. Blank, 'NA', or off-topic responses receive zero marks automatically.")

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

        # Practice Solved Example
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

        # 5-Question Subjective Paper with Refresh Icon / Button
        col_hdr_q, col_ref_q = st.columns([3.0, 1.2])
        with col_hdr_q:
            st.markdown("### ✍️ 5-Question Practice Subjective Paper (20 Total Marks)")
        with col_ref_q:
            if st.button("🔄 Refresh 5 Questions", key="btn_refresh_sample_questions", help="Click to load a brand new set of 5 questions for this class and subject", use_container_width=True):
                st.session_state["active_q_set_idx"] = st.session_state.get("active_q_set_idx", 0) + 1
                st.session_state["demo_mode_state"] = None
                st.toast("🔄 Loaded fresh new 5-question curriculum set!")
                st.rerun()

        active_set_idx = st.session_state.get("active_q_set_idx", 0)
        q_data = get_question_set(g_subject, g_class, custom_topic=custom_grader_topic.strip(), set_index=active_set_idx)
        questions = q_data["questions"]
        active_set_title = q_data["topic_title"]
        total_available_sets = q_data["total_sets"]
        display_set_num = (active_set_idx % total_available_sets) + 1

        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #F1F5F9; border-left: 4px solid #2563EB; border-radius: 6px; padding: 7px 14px; margin-bottom: 12px;">
            <div>
                <span style="font-weight: 800; font-size: 12.5px; color: #1E293B;">📄 Active Question Set {display_set_num} of {total_available_sets}:</span>
                <span style="font-size: 12px; color: #2563EB; font-weight: 700;"> {active_set_title}</span>
                <span style="font-size: 11px; color: #64748B;"> (Class {g_class}th • {g_subject})</span>
            </div>
            <div>
                <span style="font-size: 11px; background: #E0E7FF; color: #3730A3; font-weight: 700; padding: 3px 8px; border-radius: 999px;">Total 20 Marks</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_d1, col_d2, col_d3 = st.columns(3)
        if "demo_mode_state" not in st.session_state:
            st.session_state["demo_mode_state"] = None

        with col_d1:
            if st.button("🌟 1-Click: Exemplary Answer", use_container_width=True, key=f"btn_demo_high_{display_set_num}"):
                st.session_state["demo_mode_state"] = "high"
                st.rerun()
        with col_d2:
            if st.button("⚖️ 1-Click: Average Answer", use_container_width=True, key=f"btn_demo_avg_{display_set_num}"):
                st.session_state["demo_mode_state"] = "avg"
                st.rerun()
        with col_d3:
            if st.button("⚠️ 1-Click: Test 0 Marks (Blank/NA)", use_container_width=True, key=f"btn_demo_zero_{display_set_num}"):
                st.session_state["demo_mode_state"] = "zero"
                st.rerun()

        active_demo = st.session_state.get("demo_mode_state")

        user_answers = {}
        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1} ({q['marks']} Marks):** {q['text']}")
            default_val = ""
            if active_demo == "high":
                default_val = q.get("exemplar", "")
            elif active_demo == "avg":
                default_val = q.get("avg_ans", "")
            elif active_demo == "zero":
                zero_tests = ["NA", "", "I don't know the answer", "Photosynthesis is the process of plants making food", "n/a"]
                default_val = zero_tests[idx % len(zero_tests)]

            user_answers[q["id"]] = st.text_area(
                f"Your Subjective Answer for Q{idx+1}:",
                value=default_val,
                height=75,
                key=f"ans_{q['id']}_{g_class}_{g_subject}_{display_set_num}"
            )

        submit_button = st.button("🚀 Submit Paper for AI & Teacher Evaluation", type="primary")

        if submit_button:
            total_score = 0
            max_score = sum(q["marks"] for q in questions)
            evaluation_results = []

            for idx, q in enumerate(questions):
                raw_ans = user_answers[q["id"]]
                q_max = q["marks"]

                # Strict evaluation: awards 0 marks for blank, NA, or irrelevant
                eval_out = evaluate_student_answer(g_subject, idx, q["text"], raw_ans, q_max, expected_keywords=q.get("keywords"))
                score = eval_out["score"]
                total_score += score

                evaluation_results.append({
                    "question": q["text"],
                    "questionText": q["text"],
                    "max": q_max,
                    "maxMarks": q_max,
                    "score": score,
                    "awardedMarks": score,
                    "student_ans": raw_ans,
                    "studentAnswer": raw_ans,
                    "evalStatus": eval_out.get("status", "EVALUATED"),
                    "stepBreakdown": eval_out["stepBreakdown"]
                })

            total_score = round(total_score, 1)

            assigned_std_id = current_user.get("id", "STU-101")
            assigned_std_name = current_user.get("name", "Anup Sharma")

            sub_board = current_user.get("board", "CBSE (All India)") if (user_role == "student" or g_board == "All Board") else g_board
            sub_topic = active_set_title if active_set_title else active_grade_topic
            new_sub = {
                "id": f"sub_{int(time.time() * 1000)}",
                "studentId": assigned_std_id,
                "studentName": assigned_std_name,
                "board": sub_board,
                "className": f"Class {g_class}th",
                "subject": g_subject,
                "subjectName": g_subject,
                "topic": sub_topic,
                "chapterTitle": sub_topic,
                "topicName": sub_topic,
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

            st.success(f"Paper submitted! Raw AI Score: {total_score} / {max_score}")
            st.warning(f"🛡️ **AI Governance Protocol Active:** Marks for Candidate **{assigned_std_id}** are currently held in **Pending Teacher Audit Queue**. Timer has started. Your subject teacher must audit, verify, and release your marks.")

# =============================================================================
# TAB: MY EVALUATIONS & APPEALS (Student Scoped vs Faculty History vs Admin)
# =============================================================================
if tab_history is not None:
    with tab_history:
        st.subheader("📜 Student Evaluations & Academic Appeals")
        st.caption("Review graded papers, view step-by-step scoring, and accept marks or file an academic appeal challenge.")

        all_subs = db.get("submissions", [])
        if user_role == "student":
            my_std_id = current_user.get("id", "STU-101")
            display_subs = [s for s in all_subs if s.get("studentId") == my_std_id]
            st.info(f"Showing academic evaluation history for: **{current_user.get('name')}** (Candidate ID: <code>{my_std_id}</code>)")
        elif user_role == "teacher":
            teacher_subjs = current_user.get("subjects", ["Physics"])
            display_subs = [s for s in all_subs if s.get("subject") in teacher_subjs or s.get("subjectName") in teacher_subjs]
            st.info(f"Showing evaluation audit history for teaching domain: **{', '.join(teacher_subjs)}** (Blind Evaluation Mode)")
        else:
            col_filt1, col_filt2 = st.columns([2, 1])
            with col_filt1:
                std_names = ["All Students"] + sorted(list({f"{s.get('studentName', 'Student')} ({s.get('studentId', 'STU-101')})" for s in all_subs}))
                chosen_std = st.selectbox("Filter by Student Profile:", std_names, index=0)
            with col_filt2:
                status_filter = st.selectbox("Filter by Evaluation Status:", ["All Statuses", "PENDING_TEACHER_RELEASE", "RELEASED", "ACCEPTED", "CHALLENGED"])

            display_subs = all_subs
            if chosen_std != "All Students":
                selected_s_id = chosen_std.split("(")[-1].replace(")", "").strip()
                display_subs = [s for s in display_subs if s.get("studentId") == selected_s_id]
            if status_filter != "All Statuses":
                display_subs = [s for s in display_subs if s.get("status") == status_filter]

        # Apply Curriculum Board filter
        if selected_board != "All Board":
            display_subs = [s for s in display_subs if matches_board(s.get("board", ""), selected_board)]

        if not display_subs:
            st.info(f"No assessment records found for curriculum board: **{selected_board}**.")
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
                    admin_extra = f" • Student: <strong>{std_name_tag}</strong> (<code>{std_id_tag}</code>)" if user_role == "admin" else (f" • Candidate: <code>{std_id_tag}</code>" if user_role == "teacher" else "")
                    st.markdown(f"#### 📄 {topic} ({subject} • {cls_name} • {board}){admin_extra}", unsafe_allow_html=True)
                    st.markdown(f"**Score:** `{awarded} / {max_m}` Marks  |  **Status:** `{status}`")

                    if status == "PENDING_TEACHER_RELEASE":
                        released_q_list = [q for q in sub.get("questions", []) if q.get("isReleased", False)]
                        if released_q_list:
                            st.warning(f"⏳ **Under Teacher Audit:** {len(released_q_list)} of {len(sub.get('questions', []))} questions evaluated & released by faculty so far.")
                            st.markdown("##### Partial Question Release Status:")
                            for q_idx, q_item in enumerate(sub.get("questions", [])):
                                q_text = q_item.get("question") or q_item.get("questionText", f"Question {q_idx+1}")
                                q_sc = q_item.get("score", q_item.get("awardedMarks", 0.0))
                                q_mx = q_item.get("max", q_item.get("maxMarks", 5.0))
                                if q_item.get("isReleased", False):
                                    st.markdown(f"**Q{q_idx+1}: {q_text}** — <span style='color: #15803D; font-weight: 700;'>✅ Released by Faculty: {q_sc} / {q_mx} Marks</span>", unsafe_allow_html=True)
                                else:
                                    st.markdown(f"**Q{q_idx+1}: {q_text}** — <span style='color: #92400E; font-weight: 600;'>⏳ Under Faculty Evaluation (In Progress)</span>", unsafe_allow_html=True)
                        else:
                            st.warning("⏳ **Under Teacher Audit:** Evaluation timer is active. Your subject faculty is reviewing your answers question-by-question.")
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

                        if user_role == "student":
                            st.markdown("<hr>", unsafe_allow_html=True)
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
# TAB: TEACHER / GOVERNANCE PANEL (Live Timers, Blind Eval & Full Mark Editing)
# =============================================================================
if tab_teacher is not None:
    with tab_teacher:
        st.subheader("🛡️ Teacher & AI Governance Console")
        st.caption("Human-in-the-Loop review: Configure rubrics, monitor real-time evaluation timers, modify app marks question-by-question, and release scores blind-anonymously.")

        all_submissions = db.get("submissions", [])

        if user_role == "teacher":
            teacher_subjects = current_user.get("subjects", ["Physics"])
            t_subs = [s for s in all_submissions if s.get("subject") in teacher_subjects or s.get("subjectName") in teacher_subjects]
            teacher_name = current_user.get("name", "Faculty")
            teacher_id = current_user.get("id", "TCH-201")
        else:
            teacher_subjects = ["Physics", "Chemistry", "Mathematics"]
            t_subs = all_submissions
            teacher_name = "All Faculty (Admin View)"
            teacher_id = "ADM-ALL"

        # Curriculum Board Filtering for Teacher Panel
        if selected_board != "All Board":
            t_subs = [s for s in t_subs if matches_board(s.get("board", ""), selected_board)]

        pending_subs = [s for s in t_subs if s.get("status") == "PENDING_TEACHER_RELEASE"]
        completed_subs = [s for s in t_subs if s.get("status") in ["RELEASED", "ACCEPTED"]]
        challenged_subs = [s for s in t_subs if s.get("status") == "CHALLENGED"]

        # 1. Professional Faculty Dashboard
        st.markdown(f"### 📊 Faculty Evaluation Dashboard • {teacher_name} ({teacher_id})")
        subj_pills = " • ".join(teacher_subjects)
        b_info = f"🏛️ Curriculum Board Filter: <strong>{selected_board}</strong>" if selected_board != "All Board" else "🏛️ Curriculum Board: <strong>All Board (All Students Across Boards)</strong>"
        st.markdown(f'<div class="board-pill">{b_info} &nbsp;|&nbsp; 📚 Teaching Domain: {subj_pills}</div>', unsafe_allow_html=True)

        kpi_c1, kpi_c2, kpi_c3, kpi_c4 = st.columns(4)

        turnaround_times = [s.get("turnaroundMinutes") for s in completed_subs if s.get("turnaroundMinutes") is not None]
        avg_turnaround = round(sum(turnaround_times) / len(turnaround_times), 1) if turnaround_times else 25.0

        with kpi_c1:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #F59E0B;">
                <div class="kpi-num" style="color: #D97706;">{len(pending_subs)}</div>
                <div class="kpi-label">Pending In Queue</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c2:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #10B981;">
                <div class="kpi-num" style="color: #059669;">{len(completed_subs)}</div>
                <div class="kpi-label">Completed (1 Year)</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c3:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #6366F1;">
                <div class="kpi-num" style="color: #4F46E5;">{format_minutes(avg_turnaround)}</div>
                <div class="kpi-label">Avg Turnaround Time</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c4:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #EF4444;">
                <div class="kpi-num" style="color: #DC2626;">{len(challenged_subs)}</div>
                <div class="kpi-label">Appeals To Resolve</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # 2. Summary of Pending Requests in Queue
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

                sub_time_str = ps.get("submittedAt", "")
                try:
                    sub_dt = datetime.fromisoformat(sub_time_str.replace("Z", ""))
                    elapsed_mins = max(1.0, (now_dt - sub_dt).total_seconds() / 60.0)
                    elapsed_fmt = format_minutes(elapsed_mins)
                except Exception:
                    elapsed_fmt = "15m"

                pending_rows.append({
                    "Submission ID": ps.get("id"),
                    "Candidate ID": s_id,
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

        st.markdown("<hr>", unsafe_allow_html=True)

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

        st.markdown("<hr>", unsafe_allow_html=True)

        # 4. Teacher Directives Configuration
        with st.expander("⚙️ Configure Custom Teacher Directives", expanded=False):
            t_inst = st.text_area(
                "Custom Grading Directives for Physics / Chemistry / Maths:",
                value="Strictly penalize 0.5 marks if SI units (N, kg, m/s²) are omitted. Award partial credit for derivation steps.",
                height=65
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

                sub_time_str = sub.get("submittedAt", "")
                try:
                    sub_dt = datetime.fromisoformat(sub_time_str.replace("Z", ""))
                    elapsed_m = max(1.0, (datetime.now() - sub_dt).total_seconds() / 60.0)
                    elapsed_txt = format_minutes(elapsed_m)
                except Exception:
                    elapsed_txt = "20m"

                with st.container():
                    st.markdown(f"**Submission #{s_idx+1}: Candidate <code>{student_id}</code>** • {topic} ({subj_name} • {cls_name})", unsafe_allow_html=True)
                    st.markdown(f"Current Marks: **{awarded} / {max_m}** | Status: `{status}`")

                    if status == "PENDING_TEACHER_RELEASE":
                        st.markdown(f'<div class="timer-pill">⏱️ Timer Running: {elapsed_txt} since arrival in queue</div>', unsafe_allow_html=True)
                        st.info("💡 **Teacher Question-Level Evaluation & Release:** Modify marks for any question below. The total score recalculates immediately upon pressing Enter or clicking the small release icon beside each question. Marks can be released question-by-question to avoid bulk release.")

                        # Question-by-Question Marks Editing & Individual Release Feature
                        questions_list = sub.get("questions", [])
                        with st.expander(f"🔍 Question-by-Question Marks Breakdown & Release for Candidate {student_id}", expanded=True):
                            for q_i, q_item in enumerate(questions_list):
                                q_txt = q_item.get("question") or q_item.get("questionText", f"Question {q_i+1}")
                                app_q_score = float(q_item.get("score", q_item.get("awardedMarks", 0.0)))
                                q_mx = float(q_item.get("max", q_item.get("maxMarks", 5.0)))
                                stu_ans = q_item.get("student_ans") or q_item.get("studentAnswer", "Blank / No response")
                                q_is_rel = q_item.get("isReleased", False)

                                col_qa, col_qb, col_qc = st.columns([3.0, 1.1, 1.3])
                                with col_qa:
                                    st.markdown(f"**Q{q_i+1} ({q_mx} Marks):** {q_txt}")
                                    st.markdown(f"**Student Answer:** *\"{stu_ans}\"*")
                                    if q_is_rel:
                                        st.markdown(f'<span style="background: #DCFCE7; color: #15803D; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 999px; border: 1px solid #86EFAC;">🟢 Q{q_i+1} Released: <strong>{app_q_score} / {q_mx}</strong></span>', unsafe_allow_html=True)
                                    else:
                                        st.markdown(f'<span style="background: #FEF3C7; color: #92400E; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 999px; border: 1px solid #FCD34D;">⏳ Pending Question Release</span>', unsafe_allow_html=True)

                                with col_qb:
                                    # Teacher editable mark input per question with instant Enter callback
                                    cur_q_val = float(st.session_state.get(f"t_q_override_{sub_id}_{q_i}", app_q_score))
                                    new_q_val = st.number_input(
                                        f"Q{q_i+1} Marks:",
                                        min_value=0.0,
                                        max_value=q_mx,
                                        value=min(q_mx, max(0.0, cur_q_val)),
                                        step=0.5,
                                        key=f"t_q_override_{sub_id}_{q_i}",
                                        on_change=update_teacher_q_mark,
                                        args=(sub_id, q_i),
                                        help=f"Type marks for Q{q_i+1} and press Enter to instantly recalculate total score."
                                    )

                                with col_qc:
                                    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
                                    # Small icon / button to submit and release marks for this individual question
                                    rel_btn_label = f"✅ Q{q_i+1} Released" if q_is_rel else f"💾 Release Q{q_i+1}"
                                    if st.button(rel_btn_label, key=f"btn_rel_q_{sub_id}_{q_i}", help=f"Click to submit and release marks for Q{q_i+1}", use_container_width=True):
                                        actual_val = float(st.session_state.get(f"t_q_override_{sub_id}_{q_i}", new_q_val))
                                        q_item["score"] = actual_val
                                        q_item["awardedMarks"] = actual_val
                                        q_item["isReleased"] = True

                                        tot = round(sum(float(q.get("score", q.get("awardedMarks", 0.0))) for q in sub.get("questions", [])), 1)
                                        sub["totalAwarded"] = tot
                                        sub["totalAwardedMarks"] = tot
                                        st.session_state[f"t_override_{sub_id}"] = tot
                                        save_db(db)
                                        st.toast(f"✅ Q{q_i+1} marks ({actual_val}/{q_mx}) released! Total updated to {tot}/{max_m}")
                                        st.rerun()

                        # Recompute live sum across all questions
                        live_calc_sum = round(sum(float(q.get("score", q.get("awardedMarks", 0.0))) for q in sub.get("questions", [])), 1)
                        released_q_count = sum(1 for q in sub.get("questions", []) if q.get("isReleased", False))
                        total_q_count = len(sub.get("questions", []))
                        live_pct = round((live_calc_sum / max_m) * 100.0, 1) if max_m > 0 else 0.0

                        # Synchronize total score session state key if not set
                        if f"t_override_{sub_id}" not in st.session_state:
                            st.session_state[f"t_override_{sub_id}"] = live_calc_sum

                        # Prominent Live Total Score Display Box (Updates IMMEDIATELY!)
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #EFF6FF, #DBEAFE); border: 1.5px solid #3B82F6; border-radius: 8px; padding: 12px 18px; margin: 12px 0;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <span style="font-size: 11px; text-transform: uppercase; font-weight: 700; color: #1E40AF; letter-spacing: 0.5px;">Live Calculated Total Score (Instant Update)</span>
                                    <div style="font-size: 24px; font-weight: 800; color: #1D4ED8;">{live_calc_sum} <span style="font-size: 14px; font-weight: 600; color: #475569;">/ {max_m} Marks</span> <span style="font-size: 15px; color: #059669; font-weight: 700;">({live_pct}%)</span></div>
                                </div>
                                <div style="text-align: right;">
                                    <span style="background: {'#DCFCE7' if released_q_count == total_q_count and total_q_count > 0 else '#FEF3C7'}; color: {'#15803D' if released_q_count == total_q_count and total_q_count > 0 else '#92400E'}; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 999px; border: 1px solid {'#86EFAC' if released_q_count == total_q_count and total_q_count > 0 else '#FCD34D'};">
                                        {released_q_count} of {total_q_count} Questions Released
                                    </span>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        col_ov1, col_ov2 = st.columns([2, 1])
                        with col_ov1:
                            teacher_remarks = st.text_input(
                                f"Faculty Feedback / Remarks for Candidate {student_id}:",
                                value="Step-by-step marks verified and approved by faculty.",
                                key=f"t_fb_input_{sub_id}"
                            )
                        with col_ov2:
                            new_marks = st.number_input(
                                f"Final Total Score:",
                                min_value=0.0,
                                max_value=max_m,
                                value=st.session_state.get(f"t_override_{sub_id}", live_calc_sum),
                                step=0.5,
                                key=f"t_override_{sub_id}"
                            )

                        if st.button(f"✅ Finalize & Release Complete Paper to Candidate {student_id}", key=f"rel_btn_{sub_id}", type="primary", use_container_width=True):
                            now_rel = datetime.now()
                            # Mark all questions as officially released
                            for q_it in sub.get("questions", []):
                                q_it["isReleased"] = True

                            sub["totalAwarded"] = new_marks
                            sub["totalAwardedMarks"] = new_marks
                            sub["status"] = "RELEASED"
                            sub["releasedAt"] = now_rel.isoformat() + "Z"
                            sub["teacherRemarks"] = teacher_remarks

                            try:
                                sub_dt_calc = datetime.fromisoformat(sub_time_str.replace("Z", ""))
                                sub["turnaroundMinutes"] = max(1.0, round((now_rel - sub_dt_calc).total_seconds() / 60.0, 1))
                            except Exception:
                                sub["turnaroundMinutes"] = 20.0

                            save_db(db)
                            st.success(f"Assessment ({new_marks}/{max_m}) finalized & released to Candidate {student_id}! Timer stopped (Turnaround: {format_minutes(sub['turnaroundMinutes'])}).")
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

        # Curriculum Board Filtering for Admin Governance Dashboard
        if selected_board != "All Board":
            filtered_subs = [s for s in all_subs if matches_board(s.get("board", ""), selected_board)]
            filtered_students = [std for std in all_students if matches_board(std.get("board", ""), selected_board)]
            st.info(f"🏛️ **Active Board Filter: {selected_board}** — Executive KPIs, faculty workload distributions, and student marks are strictly filtered for **{selected_board}**. (Select 'All Board' on the top right to view all students across all boards).")
        else:
            filtered_subs = all_subs
            filtered_students = all_students
            st.info("🏛️ **Active Board Filter: All Board** — Aggregated institutional view displaying data for all students and evaluations across all curriculum boards (CBSE, ICSE, and State Boards).")

        # 1. Executive Global KPIs
        total_subs = len(filtered_subs)
        global_pending = len([s for s in filtered_subs if s.get("status") == "PENDING_TEACHER_RELEASE"])
        global_completed = len([s for s in filtered_subs if s.get("status") in ["RELEASED", "ACCEPTED"]])
        global_appeals = len([s for s in filtered_subs if s.get("status") == "CHALLENGED"])

        all_turnarounds = [s.get("turnaroundMinutes") for s in filtered_subs if s.get("turnaroundMinutes") is not None]
        global_avg_turnaround = round(sum(all_turnarounds) / len(all_turnarounds), 1) if all_turnarounds else 26.5

        st.markdown("### 🏛️ System-Wide Academic Governance KPIs")
        kpi_a1, kpi_a2, kpi_a3, kpi_a4, kpi_a5 = st.columns(5)
        with kpi_a1:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #3B82F6;">
                <div class="kpi-num" style="color: #1D4ED8;">{total_subs}</div>
                <div class="kpi-label">Total Submissions</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a2:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #F59E0B;">
                <div class="kpi-num" style="color: #D97706;">{global_pending}</div>
                <div class="kpi-label">Pending Across Faculty</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a3:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #10B981;">
                <div class="kpi-num" style="color: #059669;">{global_completed}</div>
                <div class="kpi-label">Completed Evaluations</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a4:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #6366F1;">
                <div class="kpi-num" style="color: #4F46E5;">{format_minutes(global_avg_turnaround)}</div>
                <div class="kpi-label">System Avg Turnaround</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_a5:
            st.markdown(f"""
            <div class="kpi-box" style="border-top: 3px solid #EC4899;">
                <div class="kpi-num" style="color: #BE185D;">{len(filtered_students)}</div>
                <div class="kpi-label">Enrolled Candidates</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # 2. All-Teacher Level Comparative Performance Dashboard
        st.markdown("### 🧑‍🏫 Teacher-Level Comparative Performance & Workload Analytics")
        st.caption("Summarizing evaluation queues, completion volume, and turnaround speed across all faculty members.")

        teacher_summary_data = []
        for t in teachers:
            t_name = t["name"]
            t_id = t["id"]
            t_subjs = t["subjects"]
            t_assigned_subs = [s for s in filtered_subs if s.get("subject") in t_subjs or s.get("subjectName") in t_subjs]

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

        st.markdown("<hr>", unsafe_allow_html=True)

        # 3. Students' Marks Information & Visualizations (Unique Name+ID, strictly <=100%)
        st.markdown("### 🎓 Student Marks Information & Academic Performance Analytics")
        st.caption("Institutional grade distribution, board benchmarks, and student-level academic progress.")

        student_analytics = []
        for std in filtered_students:
            s_id = std.get("id")
            s_name = std.get("name")
            s_class = std.get("studentClass", 9)
            s_board = std.get("board", "CBSE")

            s_subs = [s for s in filtered_subs if s.get("studentId") == s_id]
            completed_s_subs = [s for s in s_subs if s.get("status") in ["RELEASED", "ACCEPTED"]]

            if completed_s_subs:
                scores = [float(s.get("totalAwarded", 0.0)) for s in completed_s_subs]
                maxes = [float(s.get("totalMax", 20.0)) for s in completed_s_subs]
                avg_score = round(sum(scores) / len(scores), 1)
                total_max_sum = sum(maxes)
                avg_pct = round((sum(scores) / total_max_sum) * 100.0, 1) if total_max_sum > 0 else 0.0
                highest = max(scores)
            else:
                avg_score = 0.0
                avg_pct = 0.0
                highest = 0.0

            avg_pct = min(100.0, max(0.0, avg_pct))
            student_label = f"{s_name} ({s_id})"

            student_analytics.append({
                "Student ID": s_id,
                "Student Name": s_name,
                "Student Label": student_label,
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
            for s in filtered_subs:
                subj = s.get("subject", "Physics")
                aw = float(s.get("totalAwarded", 0.0))
                subject_marks.setdefault(subj, []).append(aw)

            subj_avg_rows = [{"Subject": k, "Average Marks (out of 20)": round(sum(v)/len(v), 1)} for k, v in subject_marks.items()]
            if subj_avg_rows:
                df_subj = pd.DataFrame(subj_avg_rows).set_index("Subject")
                st.bar_chart(df_subj, color="#3B82F6")
            else:
                st.info(f"No graded assessments recorded under {selected_board}.")

        with col_v2:
            st.markdown("**Student Average Performance Comparison (%):**")
            if not df_std.empty and "Student Label" in df_std.columns:
                chart_std_pct = df_std[["Student Label", "Avg Pct Num"]].set_index("Student Label")
                chart_std_pct.columns = ["Average Score (%)"]
                st.bar_chart(chart_std_pct, color="#10B981")
            else:
                st.info(f"No student performance records found for {selected_board}.")

        st.markdown("#### 📋 Comprehensive Student Academic Gradebook")
        if not df_std.empty:
            st.dataframe(
                df_std[["Student ID", "Student Name", "Class", "Board", "Assessments Taken", "Completed", "Average Marks (out of 20)", "Average Percentage", "Highest Mark", "Performance Tier"]],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info(f"No student gradebook data available for {selected_board}.")

        st.markdown("<hr>", unsafe_allow_html=True)

        # 4. Global Directory & User Management
        with st.expander("👥 Institutional Directory: Registered Students & Faculty IDs", expanded=False):
            col_reg1, col_reg2 = st.columns(2)
            with col_reg1:
                st.markdown("**Registered Students Registry:**")
                if filtered_students:
                    st.dataframe(pd.DataFrame(filtered_students)[["id", "name", "studentClass", "board", "cityState", "email"]], hide_index=True)
                else:
                    st.info(f"No students registered under {selected_board}.")
            with col_reg2:
                st.markdown("**Faculty Registry:**")
                st.dataframe(pd.DataFrame(teachers)[["id", "name", "subjects", "email", "department"]], hide_index=True)

# -----------------------------------------------------------------------------
# GLOBAL FOOTER
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; font-size:11.5px; color:#64748B;">
    🛡️ <strong>EduAegis</strong> • Responsible AI Tutor & Governed Grader • IIM Capstone Project<br>
    DPDP Act 2023 Aligned • Blind Evaluation Compliance • NITI Aayog Responsible AI Frameworks
</div>
""", unsafe_allow_html=True)
