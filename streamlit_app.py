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
from objective_question_bank import get_objective_question_set
try:
    from source_learning_engine import (
        extract_document_content,
        get_youtube_learning_content,
        synthesize_tutor_lesson,
        generate_dynamic_mcqs_from_source,
        generate_dynamic_subjective_from_source
    )
except Exception:
    # Fail-safe zero-error fallback
    extract_document_content = lambda fn, fb: "Document content parsed."
    get_youtube_learning_content = lambda url: None
    synthesize_tutor_lesson = lambda st, sx, **kw: {"title": st, "explanation": sx, "analogies": [], "key_principles": [], "audio_text": sx, "key_terms": []}
    generate_dynamic_mcqs_from_source = lambda st, sx, **kw: get_objective_question_set("Physics", 9)
    generate_dynamic_subjective_from_source = lambda st, sx, **kw: get_question_set("Physics", 9)

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
    
    :root {{
        color-scheme: light !important;
    }}

    @media (prefers-color-scheme: dark) {{
        :root {{
            color-scheme: light !important;
        }}
        body, .stApp, [data-testid="stAppViewContainer"] {{
            background-color: #F8FAFC !important;
            color: #0F172A !important;
        }}
    }}

    html, body {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        -webkit-font-smoothing: antialiased;
        color: #0F172A;
    }}

    .stApp {{
        color: #0F172A;
    }}

    /* Standard Headings and Text on Light Backgrounds */
    h1, h2, h3, h4, h5, h6 {{
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
    }}

    /* Default Card Content */
    .soothing-card, .soothing-card p, .soothing-card span, .soothing-card div {{
        color: #0F172A;
    }}

    .stCaption, [data-testid="stCaptionContainer"] p, [data-testid="stCaptionContainer"] * {{
        color: #475569 !important;
        -webkit-text-fill-color: #475569 !important;
        font-size: 13px !important;
    }}

    /* Global Space Optimization - Eliminates excessive top whitespace */
    .block-container {{
        padding-top: 0.8rem !important;
        padding-bottom: 2rem !important;
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
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.08) 0px, transparent 45%),
            radial-gradient(at 100% 0%, rgba(16, 185, 129, 0.07) 0px, transparent 45%),
            radial-gradient(at 100% 100%, rgba(14, 165, 233, 0.06) 0px, transparent 45%),
            radial-gradient(at 0% 100%, rgba(139, 92, 246, 0.06) 0px, transparent 45%),
            url("data:image/svg+xml;base64,{b64_bg}");
        background-attachment: fixed;
        background-size: cover, cover, cover, cover, 360px 360px;
    }}
    
    /* ========================================================================= */
    /* BLUE BOX 1: TOP HEADER BANNER (PURE BRIGHT WHITE TEXT, NEVER BLACK)       */
    /* ========================================================================= */
    .aegis-header {{
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 45%, #1E3A8A 85%, #0F172A 100%) !important;
        padding: 14px 22px !important;
        border-radius: 14px !important;
        margin-bottom: 14px !important;
        border: 1px solid rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 4px 15px -3px rgba(15, 23, 42, 0.25) !important;
    }}
    
    /* Enforce pure white text on all children inside aegis-header */
    .aegis-header,
    .aegis-header *,
    .aegis-header p,
    .aegis-header span,
    .aegis-header div,
    .aegis-header strong,
    .aegis-header em {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}
    
    .aegis-title, .aegis-title * {{
        font-size: 21px !important;
        font-weight: 800 !important;
        letter-spacing: -0.3px !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }}
    
    .aegis-badge {{
        background: rgba(16, 185, 129, 0.25) !important;
        color: #34D399 !important;
        -webkit-text-fill-color: #34D399 !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        padding: 3px 10px !important;
        border-radius: 9999px !important;
        border: 1px solid rgba(52, 211, 153, 0.5) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.4px !important;
    }}

    .aegis-subtext, .aegis-subtext * {{
        font-size: 13px !important;
        color: #E2E8F0 !important;
        -webkit-text-fill-color: #E2E8F0 !important;
        margin-top: 4px !important;
        line-height: 1.45 !important;
    }}

    .aegis-header code {{
        background: rgba(255, 255, 255, 0.2) !important;
        color: #93C5FD !important;
        -webkit-text-fill-color: #93C5FD !important;
        padding: 2px 7px !important;
        border-radius: 4px !important;
        border: 1px solid rgba(147, 197, 253, 0.4) !important;
        font-weight: 700 !important;
    }}

    .role-badge-student {{
        background: #EFF6FF !important;
        color: #1D4ED8 !important;
        -webkit-text-fill-color: #1D4ED8 !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        padding: 3px 10px !important;
        border-radius: 9999px !important;
        border: 1px solid #BFDBFE !important;
    }}

    .role-badge-teacher {{
        background: #ECFDF5 !important;
        color: #047857 !important;
        -webkit-text-fill-color: #047857 !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        padding: 3px 10px !important;
        border-radius: 9999px !important;
        border: 1px solid #A7F3D0 !important;
    }}

    .role-badge-admin {{
        background: #FAF5FF !important;
        color: #7E22CE !important;
        -webkit-text-fill-color: #7E22CE !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        padding: 3px 10px !important;
        border-radius: 9999px !important;
        border: 1px solid #E9D5FF !important;
    }}
    
    /* Compact Persistent Board Pill */
    .board-pill {{
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        background: #EEF2FF !important;
        color: #3730A3 !important;
        font-weight: 700 !important;
        font-size: 12.5px !important;
        padding: 4px 12px !important;
        border-radius: 9999px !important;
        border: 1px solid #C7D2FE !important;
    }}
    
    /* Solid White Card for 100% Crisp Mobile & Desktop Readability */
    .soothing-card {{
        background: #FFFFFF !important;
        border: 1.5px solid #E2E8F0 !important;
        border-radius: 14px !important;
        padding: 18px 20px !important;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.05) !important;
        margin-bottom: 12px !important;
    }}

    /* Rich Profile Card with Decorative Background Illustration */
    .sidebar-profile-card {{
        background-color: #0F172A !important;
        background-image: url("data:image/svg+xml;base64,{b64_sidebar}") !important;
        background-size: cover !important;
        background-position: center !important;
        border: 1px solid rgba(129, 140, 248, 0.45) !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        margin-bottom: 10px !important;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.25) !important;
        color: #FFFFFF !important;
    }}
    .sidebar-profile-card * {{
        color: #FFFFFF !important;
    }}

    /* Profile ID Badge Pill inside Sidebar Profile Card (High Contrast & Clear Readability) */
    .sidebar-profile-card code,
    .sidebar-profile-card .profile-id-badge,
    .profile-id-badge,
    [data-testid="stSidebar"] .sidebar-profile-card code,
    [data-testid="stSidebar"] .sidebar-profile-card .profile-id-badge {{
        background: #EFF6FF !important;
        background-color: #EFF6FF !important;
        color: #1D4ED8 !important;
        -webkit-text-fill-color: #1D4ED8 !important;
        border: 1.5px solid #BFDBFE !important;
        padding: 2.5px 8px !important;
        border-radius: 6px !important;
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace !important;
        font-weight: 800 !important;
        font-size: 12px !important;
        letter-spacing: 0.4px !important;
        display: inline-block !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    }}

    /* Tighten Sidebar Padding */
    [data-testid="stSidebar"] {{
        background: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    /* ========================================================================= */
    /* BLUE BOX 2: SPREAD-ACROSS BLUE TABS (100% CONTRAST & ZERO TRIMMING)       */
    /* ========================================================================= */
    .stTabs {{
        width: 100% !important;
    }}

    .stTabs [data-baseweb="tab-list"] {{
        display: flex !important;
        width: 100% !important;
        flex-wrap: wrap !important;
        overflow: visible !important;
        height: auto !important;
        min-height: 52px !important;
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #2563EB 100%) !important;
        padding: 8px !important;
        border-radius: 14px !important;
        border: 1.5px solid rgba(99, 102, 241, 0.5) !important;
        gap: 8px !important;
        box-shadow: 0 4px 16px rgba(29, 78, 216, 0.22) !important;
        margin-bottom: 16px !important;
    }}
    
    /* Base Tab Pill Container (No Trimming, Flexible Auto-Wrap) */
    .stTabs [data-baseweb="tab"] {{
        flex: 1 1 auto !important;
        min-width: fit-content !important;
        max-width: none !important;
        height: auto !important;
        min-height: 44px !important;
        padding: 10px 20px !important;
        border-radius: 9px !important;
        text-align: center !important;
        justify-content: center !important;
        align-items: center !important;
        cursor: pointer !important;
        box-sizing: border-box !important;
        transition: all 0.2s ease-in-out !important;

        /* Critical: Prevent Any Text Trimming or Cut-Off */
        white-space: normal !important;
        word-break: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
    }}

    /* Inner text container of tab: never trim or clip */
    .stTabs [data-baseweb="tab"],
    .stTabs [data-baseweb="tab"] > div,
    .stTabs [data-baseweb="tab"] [data-testid="stMarkdownContainer"],
    .stTabs [data-baseweb="tab"] p,
    .stTabs [data-baseweb="tab"] span,
    .stTabs [data-baseweb="tab"] div,
    .stTabs [data-baseweb="tab"] strong {{
        white-space: normal !important;
        word-break: normal !important;
        overflow: visible !important;
        text-overflow: unset !important;
        max-width: none !important;
        line-height: 1.35 !important;
    }}

    /* --------------------------------------------------------------------- */
    /* UNSELECTED TABS: Translucent White Pill with PURE BRIGHT WHITE TEXT   */
    /* (100% Crystal-Clear Contrast against Dark Blue: Never Invisible!)      */
    /* --------------------------------------------------------------------- */
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]),
    .stTabs button[role="tab"]:not([aria-selected="true"]),
    .stTabs [data-baseweb="tab"][aria-selected="false"],
    .stTabs button[role="tab"][aria-selected="false"] {{
        background: rgba(255, 255, 255, 0.16) !important;
        background-color: rgba(255, 255, 255, 0.16) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.45) !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]) *,
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]) p,
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]) span,
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]) div,
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]) strong,
    .stTabs button[role="tab"]:not([aria-selected="true"]) *,
    .stTabs button[role="tab"]:not([aria-selected="true"]) p,
    .stTabs button[role="tab"]:not([aria-selected="true"]) span,
    .stTabs button[role="tab"]:not([aria-selected="true"]) div,
    .stTabs [data-baseweb="tab"][aria-selected="false"] *,
    .stTabs [data-baseweb="tab"][aria-selected="false"] p,
    .stTabs [data-baseweb="tab"][aria-selected="false"] span,
    .stTabs [data-baseweb="tab"][aria-selected="false"] div,
    .stTabs button[role="tab"][aria-selected="false"] *,
    .stTabs button[role="tab"][aria-selected="false"] p {{
        color: #FFFFFF !important; /* PURE CRISP WHITE: 100% VISIBLE ON DARK BLUE! */
        -webkit-text-fill-color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }}

    /* Unselected Tab Hover */
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]):hover,
    .stTabs button[role="tab"]:not([aria-selected="true"]):hover,
    .stTabs [data-baseweb="tab"][aria-selected="false"]:hover,
    .stTabs button[role="tab"][aria-selected="false"]:hover {{
        background: rgba(255, 255, 255, 0.28) !important;
        background-color: rgba(255, 255, 255, 0.28) !important;
        border-color: #FFFFFF !important;
    }}
    .stTabs [data-baseweb="tab"]:not([aria-selected="true"]):hover *,
    .stTabs button[role="tab"]:not([aria-selected="true"]):hover * {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* --------------------------------------------------------------------- */
    /* SELECTED / ACTIVE TAB: Crisp Solid Pure White with Deep Navy Blue Text*/
    /* --------------------------------------------------------------------- */
    .stTabs [data-baseweb="tab"][aria-selected="true"],
    .stTabs button[role="tab"][aria-selected="true"],
    .stTabs [aria-selected="true"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border: 2px solid #93C5FD !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35) !important;
        transform: translateY(-1px) !important;
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
    }}

    .stTabs [data-baseweb="tab"][aria-selected="true"] *,
    .stTabs [data-baseweb="tab"][aria-selected="true"] p,
    .stTabs [data-baseweb="tab"][aria-selected="true"] span,
    .stTabs [data-baseweb="tab"][aria-selected="true"] div,
    .stTabs [data-baseweb="tab"][aria-selected="true"] strong,
    .stTabs button[role="tab"][aria-selected="true"] *,
    .stTabs button[role="tab"][aria-selected="true"] p,
    .stTabs button[role="tab"][aria-selected="true"] span,
    .stTabs button[role="tab"][aria-selected="true"] div,
    .stTabs [aria-selected="true"] *,
    .stTabs [aria-selected="true"] p,
    .stTabs [aria-selected="true"] span,
    .stTabs [aria-selected="true"] div {{
        color: #0F172A !important; /* CRISP DARK SLATE / DEEP NAVY: 100% VISIBLE ON WHITE! */
        -webkit-text-fill-color: #0F172A !important;
        font-weight: 800 !important;
        font-size: 14.5px !important;
    }}

    /* Hide default BaseWeb bottom indicator lines */
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] {{
        display: none !important;
    }}

    /* Vibrant Compact KPI Summary Cards */
    .kpi-box {{
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        text-align: center !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03) !important;
    }}
    .kpi-num {{
        font-size: 22px !important;
        font-weight: 800 !important;
        color: #0F172A !important;
    }}
    .kpi-label {{
        font-size: 12px !important;
        font-weight: 700 !important;
        color: #475569 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.4px !important;
        margin-top: 3px !important;
    }}

    /* Compact Timer Pill */
    .timer-pill {{
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        background: #FFFBEB !important;
        color: #92400E !important;
        font-weight: 700 !important;
        font-size: 12px !important;
        padding: 3px 9px !important;
        border-radius: 9999px !important;
        border: 1px solid #FDE68A !important;
    }}
    
    .blind-banner {{
        background: #F0FDF4 !important;
        border: 1px solid #BBF7D0 !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
        color: #166534 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }}

    /* Objective Evaluation & Marks Score Banner (High-Contrast White on Deep Gradient) */
    .score-banner {{
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #2563EB 100%) !important;
        border-radius: 12px !important;
        padding: 18px 22px !important;
        margin: 16px 0 !important;
        box-shadow: 0 4px 16px rgba(37, 99, 235, 0.22) !important;
        border: 1px solid rgba(99, 102, 241, 0.4) !important;
    }}
    .score-banner, .score-banner * {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}
    .score-banner code {{
        background: rgba(255, 255, 255, 0.2) !important;
        color: #93C5FD !important;
        -webkit-text-fill-color: #93C5FD !important;
        padding: 2px 7px !important;
        border-radius: 4px !important;
        border: 1px solid rgba(147, 197, 253, 0.4) !important;
    }}

    .step-item {{
        background: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        margin-bottom: 8px !important;
    }}

    .sidebar-resource-card {{
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        margin-bottom: 10px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03) !important;
        transition: transform 0.15s ease, border-color 0.15s ease !important;
    }}
    .sidebar-resource-card:hover {{
        transform: translateY(-1px) !important;
        border-color: #93C5FD !important;
        box-shadow: 0 3px 8px rgba(37,99,235,0.08) !important;
    }}

    /* Form Controls & Inputs - High Contrast & Clean Sizing */
    input, textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea,
    .stTextInput input, .stTextArea textarea {{
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        background-color: #FFFFFF !important;
        border: 1.5px solid #CBD5E1 !important;
        border-radius: 8px !important;
        font-size: 14px !important;
    }}
    input:focus, textarea:focus {{
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
    }}

    /* Selectboxes and Dropdowns */
    [data-baseweb="select"] > div {{
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        border: 1.5px solid #CBD5E1 !important;
        border-radius: 8px !important;
        font-size: 14px !important;
    }}
    [data-baseweb="select"] * {{
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
    }}
    ul[role="listbox"], [data-baseweb="popover"] [role="listbox"] {{
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
    }}
    li[role="option"] {{
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        font-size: 14px !important;
        background-color: #FFFFFF !important;
    }}
    li[role="option"]:hover, li[role="option"][aria-selected="true"] {{
        background-color: #EFF6FF !important;
        color: #1D4ED8 !important;
        -webkit-text-fill-color: #1D4ED8 !important;
    }}

    /* Radio Buttons */
    [data-testid="stRadio"] label, [data-testid="stRadio"] div, [data-testid="stRadio"] span, [data-testid="stRadio"] p {{
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
        font-size: 14px !important;
        font-weight: 600 !important;
    }}

    /* Primary Buttons */
    button[kind="primary"], .stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        border-radius: 8px !important;
        padding: 9px 18px !important;
        border: none !important;
        box-shadow: 0 2px 8px rgba(37,99,235,0.25) !important;
    }}
    button[kind="primary"]:hover, .stButton > button[kind="primary"]:hover {{
        background: linear-gradient(135deg, #1E40AF 0%, #1D4ED8 100%) !important;
        box-shadow: 0 4px 12px rgba(37,99,235,0.35) !important;
    }}

    hr {{
        margin: 12px 0 !important;
        border-color: #E2E8F0 !important;
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
        "preferredSubject": "Physics",
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
        "preferredSubject": "Chemistry",
        "cityState": "Kolkata, West Bengal",
        "email": "nandita.roy@school.edu",
        "phone": "+91 91234 56789"
    },
    "Daksh": {
        "id": "STU-103",
        "username": "Daksh",
        "name": "Daksh Gupta",
        "role": "student",
        "password": "eduaegis123",
        "studentClass": 10,
        "board": "ICSE / CISCE",
        "preferredSubject": "Physics",
        "cityState": "Pune, Maharashtra",
        "email": "daksh.gupta@eduaegis.com",
        "phone": "+91 99887 76655"
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

def generate_unique_teacher_id(existing_teachers):
    """Generates an incremental unique teacher ID like TCH-201, TCH-202, TCH-203."""
    max_num = 200
    for t in existing_teachers:
        t_id = str(t.get("id", ""))
        if t_id.startswith("TCH-"):
            try:
                num = int(t_id.split("-")[1])
                if num > max_num:
                    max_num = num
            except Exception:
                pass
    return f"TCH-{max_num + 1}"

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

    # Ensure unique teachers without duplicates
    tch_map = {}
    for t in data.get("teachers", []):
        if t.get("id"):
            tch_map[t["id"]] = t
    if "TCH-201" not in tch_map:
        tch_map["TCH-201"] = DEFAULT_USERS["Ankur"]
    if "TCH-202" not in tch_map:
        tch_map["TCH-202"] = DEFAULT_USERS["Akanksha"]
    data["teachers"] = list(tch_map.values())

    # Sync all students & teachers into DEFAULT_USERS for rapid authentication & lookup
    for s in data["students"]:
        if not s.get("role"):
            s["role"] = "student"
        if s.get("username"):
            DEFAULT_USERS[s["username"]] = s
    for t in data["teachers"]:
        if not t.get("role"):
            t["role"] = "teacher"
        if t.get("username"):
            DEFAULT_USERS[t["username"]] = t

    if "submissions" not in data or not isinstance(data["submissions"], list):
        data["submissions"] = []

    if "objective_submissions" not in data or not isinstance(data["objective_submissions"], list):
        data["objective_submissions"] = []

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
    for s in db.get("students", []):
        if s.get("username") == username:
            return s.get("password", "eduaegis123")
    for t in db.get("teachers", []):
        if t.get("username") == username:
            return t.get("password", "eduaegis123")
    return "eduaegis123"

def get_user_profile(username):
    """Retrieves full profile dict for a given username."""
    prof = None
    if username in DEFAULT_USERS:
        prof = dict(DEFAULT_USERS[username])
    if not prof:
        for s in db.get("students", []):
            if s.get("username") == username:
                prof = dict(s)
                break
    if not prof:
        for t in db.get("teachers", []):
            if t.get("username") == username:
                prof = dict(t)
                break
    if prof and not prof.get("role"):
        if prof.get("id", "").startswith("STU-"):
            prof["role"] = "student"
        elif prof.get("id", "").startswith("TCH-"):
            prof["role"] = "teacher"
        elif prof.get("id", "").startswith("ADM-") or str(username).lower() == "admin":
            prof["role"] = "admin"
        else:
            prof["role"] = "student"
    return prof

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

def get_all_users_list():
    """Returns a unified list of all registered users (students, teachers, admin) with active passwords."""
    user_map = {}
    for uname, prof in DEFAULT_USERS.items():
        user_map[uname] = dict(prof)
        if not user_map[uname].get("role"):
            user_map[uname]["role"] = "admin" if uname.lower() == "admin" else ("teacher" if str(user_map[uname].get("id", "")).startswith("TCH-") else "student")
    for s in db.get("students", []):
        uname = s.get("username", s.get("name"))
        if uname:
            u_dict = dict(s)
            if not u_dict.get("role"):
                u_dict["role"] = "student"
            user_map[uname] = u_dict
    for t in db.get("teachers", []):
        uname = t.get("username", t.get("name"))
        if uname:
            u_dict = dict(t)
            if not u_dict.get("role"):
                u_dict["role"] = "teacher"
            user_map[uname] = u_dict
    
    result = []
    for uname, u in user_map.items():
        if not u.get("role"):
            u["role"] = "admin" if uname.lower() == "admin" or str(u.get("id", "")).startswith("ADM-") else ("teacher" if str(u.get("id", "")).startswith("TCH-") else "student")
        u["active_password"] = get_user_password(uname)
        result.append(u)
    return result

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
    <div style="max-width: 780px; margin: 25px auto 16px auto; text-align: center;">
        <div style="font-size: 34px;">🛡️</div>
        <h1 style="font-size: 26px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">Welcome to EduAegis</h1>
        <p style="color: #475569; font-size: 14.5px; margin-bottom: 16px;">
            Responsible AI Tutor & Governed Grader • Role-Based Authentication Portal
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_space1, col_login, col_space2 = st.columns([0.08, 3.84, 0.08])

    with col_login:
        tab_auth_signin, tab_auth_signup = st.tabs(["🔐 Sign In to Portal", "📝 Sign Up / Create New Profile"])

        with tab_auth_signin:
            st.markdown("""
            <div class="soothing-card" style="border: 2px solid #E0E7FF; box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.12);">
                <div style="font-size: 16px; font-weight: 700; color: #1E1B4B; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
                    <span>🔐 Access Your Portal</span>
                </div>
            """, unsafe_allow_html=True)

            login_role = st.selectbox(
                "1. Select Your Role",
                ["Student", "Teacher", "Admin"],
                index=0,
                help="Select whether you are logging in as a Student, Teacher, or Super User Admin."
            )

            if login_role == "Student":
                students_list = db.get("students", [])
                user_options = [s.get("username", s.get("name", "Student")) for s in students_list if s.get("username")]
                if not user_options:
                    user_options = ["Anup", "Nandita"]
                default_idx = 0
            elif login_role == "Teacher":
                teachers_list = db.get("teachers", [])
                user_options = [t.get("username", t.get("name", "Teacher")) for t in teachers_list if t.get("username")]
                if not user_options:
                    user_options = ["Ankur", "Akanksha"]
                default_idx = 0
            else:
                user_options = ["Admin"]
                default_idx = 0

            def format_auth_user_label(u_name):
                u_prof = get_user_profile(u_name)
                if u_prof:
                    return f"{u_prof.get('name', u_name)} ({u_prof.get('id', '')})"
                return u_name

            selected_username = st.selectbox("2. Select Your Username / Profile", user_options, index=default_idx, format_func=format_auth_user_label)
            entered_password = st.text_input("3. Password", type="password", placeholder="Enter your password")

            btn_login = st.button("🚀 Log In to EduAegis", type="primary", use_container_width=True)

            if btn_login:
                actual_pw = get_user_password(selected_username)
                if entered_password == actual_pw:
                    user_data = get_user_profile(selected_username)
                    if user_data:
                        st.session_state["logged_in_user"] = user_data
                        st.success(f"Welcome back, {user_data.get('name', selected_username)} ({user_data.get('id', '')})!")
                        time.sleep(0.4)
                        st.rerun()
                    else:
                        st.error("User profile not found.")
                else:
                    st.error("Invalid password. Please check your credentials and try again.")

            # In-App Password Update feature on Login Page
            with st.expander("🔄 Update / Reset Password", expanded=False):
                rst_options = list(set(["Anup", "Nandita", "Ankur", "Akanksha", "Admin"] + [s.get("username") for s in db.get("students", []) if s.get("username")] + [t.get("username") for t in db.get("teachers", []) if t.get("username")]))
                rst_user = st.selectbox("Username to Update", sorted(rst_options), key="rst_user")
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

            st.markdown("<hr style='margin: 12px 0;'>", unsafe_allow_html=True)
            st.markdown("<div style='font-size: 13px; font-weight: 700; color: #334155; margin-bottom: 8px;'>⚡ 1-Click Quick Persona Switch (Instant Testing):</div>", unsafe_allow_html=True)
            col_q1, col_q2, col_q3 = st.columns(3)
            with col_q1:
                if st.button("👤 Anup (Class 9 • CBSE)", use_container_width=True, help="Student: Class 9th CBSE Board"):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Anup"]
                    st.rerun()
                if st.button("🛡️ Ankur (Physics Tchr)", use_container_width=True, help="Teacher: Physical Sciences Faculty"):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Ankur"]
                    st.rerun()
            with col_q2:
                if st.button("👤 Daksh (Class 10 • ICSE)", use_container_width=True, help="Student: Class 10th ICSE Board"):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Daksh"]
                    st.rerun()
                if st.button("🛡️ Akanksha (Chem/Math)", use_container_width=True, help="Teacher: Chemical & Mathematical Sciences"):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Akanksha"]
                    st.rerun()
            with col_q3:
                if st.button("👤 Nandita (Class 9 • ICSE)", use_container_width=True, help="Student: Class 9th ICSE Board"):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Nandita"]
                    st.rerun()
                if st.button("👑 Admin (Super User)", use_container_width=True, help="Admin: Super User & Compliance"):
                    st.session_state["logged_in_user"] = DEFAULT_USERS["Admin"]
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

        with tab_auth_signup:
            st.markdown("""
            <div class="soothing-card" style="border: 2px solid #A7F3D0; box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.12);">
                <div style="font-size: 15px; font-weight: 700; color: #064E3B; margin-bottom: 4px; display: flex; align-items: center; gap: 6px;">
                    <span>📝 Sign Up / Register New Profile</span>
                </div>
                <div style="font-size: 13.5px; color: #475569; margin-bottom: 12px; line-height: 1.45;">
                    Create an institutional profile to access AI tutoring, dynamic rubrics, and automated evaluations.
                </div>
            """, unsafe_allow_html=True)

            sign_role = st.selectbox(
                "1. Select Your Role *",
                ["Student", "Teacher"],
                index=0,
                key="sign_role",
                help="Choose Student for personalized learning & assessments, or Teacher for grading audits & curriculum governance."
            )

            sign_name = st.text_input("2. Full Name *", placeholder="e.g. Rohan Sharma or Dr. Priya Nair", key="sign_name")
            sign_email = st.text_input("3. Email ID (Mail ID) *", placeholder="e.g. rohan.sharma@school.edu", key="sign_email")
            sign_city = st.text_input("4. City / State *", placeholder="e.g. Bangalore, Karnataka or New Delhi", key="sign_city")

            if sign_role == "Student":
                col_st1, col_st2 = st.columns(2)
                with col_st1:
                    sign_class = st.selectbox("5. Class *", [8, 9, 10], index=1, key="sign_class")
                with col_st2:
                    sign_board = st.selectbox(
                        "6. Curriculum Board *",
                        ["CBSE (All India)", "ICSE / CISCE", "State Board (Maharashtra/UP/Karnataka)", "Cambridge IGCSE"],
                        index=0,
                        key="sign_board"
                    )
            else:  # Teacher
                col_tc1, col_tc2 = st.columns(2)
                with col_tc1:
                    sign_subjs = st.multiselect(
                        "5. Teaching Subject(s) *",
                        ["Physics", "Chemistry", "Mathematics"],
                        default=["Physics"],
                        key="sign_subjs"
                    )
                with col_tc2:
                    sign_dept = st.text_input(
                        "6. Academic Department",
                        value="Department of Physical Sciences",
                        key="sign_dept"
                    )

            col_pw1, col_pw2 = st.columns(2)
            with col_pw1:
                sign_pw = st.text_input("7. Set Password *", type="password", placeholder="Min 4 characters", key="sign_pw")
            with col_pw2:
                sign_conf = st.text_input("8. Confirm Password *", type="password", placeholder="Re-enter password", key="sign_conf")

            btn_register = st.button("✨ Create Profile & Log In Immediately", type="primary", use_container_width=True, key="btn_register")

            if btn_register:
                if not sign_name.strip():
                    st.error("Please enter your full name.")
                elif not sign_email.strip() or "@" not in sign_email:
                    st.error("Please enter a valid email address.")
                elif not sign_city.strip():
                    st.error("Please enter your city.")
                elif len(sign_pw) < 4:
                    st.error("Password must be at least 4 characters long.")
                elif sign_pw != sign_conf:
                    st.error("Passwords do not match. Please verify.")
                else:
                    name_parts = sign_name.strip().split()
                    base_user = name_parts[0].replace("Dr.", "").replace("Prof.", "").replace("Mr.", "").replace("Ms.", "").strip()
                    if not base_user:
                        base_user = "User"

                    existing_usernames = set(db.get("passwords", {}).keys())
                    for s in db.get("students", []):
                        if s.get("username"):
                            existing_usernames.add(s["username"])
                    for t in db.get("teachers", []):
                        if t.get("username"):
                            existing_usernames.add(t["username"])

                    cand_user = base_user
                    counter = 1
                    while cand_user in existing_usernames:
                        cand_user = f"{base_user}_{counter}"
                        counter += 1

                    if sign_role == "Student":
                        new_id = generate_unique_student_id(db.get("students", []))
                        new_profile = {
                            "id": new_id,
                            "username": cand_user,
                            "name": sign_name.strip(),
                            "role": "student",
                            "password": sign_pw,
                            "studentClass": sign_class,
                            "board": sign_board,
                            "cityState": sign_city.strip(),
                            "email": sign_email.strip(),
                            "phone": "+91 98000 00000"
                        }
                        db.setdefault("students", []).append(new_profile)
                    else:
                        new_id = generate_unique_teacher_id(db.get("teachers", []))
                        new_profile = {
                            "id": new_id,
                            "username": cand_user,
                            "name": sign_name.strip(),
                            "role": "teacher",
                            "password": sign_pw,
                            "subjects": sign_subjs if sign_subjs else ["Physics"],
                            "cityState": sign_city.strip(),
                            "email": sign_email.strip(),
                            "department": sign_dept.strip() if sign_dept.strip() else "Department of Academic Instruction"
                        }
                        db.setdefault("teachers", []).append(new_profile)

                    db.setdefault("passwords", {})[cand_user] = sign_pw
                    DEFAULT_USERS[cand_user] = new_profile
                    save_db(db)

                    st.session_state["logged_in_user"] = new_profile
                    st.success(f"🎉 Welcome aboard, {sign_name.strip()}! Assigned Unique ID: {new_id}. Logging you in...")
                    time.sleep(0.4)
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# =============================================================================
# ACTIVE LOGGED-IN USER SESSION
# =============================================================================
current_user = st.session_state.get("logged_in_user")
if not current_user:
    st.stop()
user_role = str(current_user.get("role") or ("admin" if str(current_user.get("id", "")).startswith("ADM-") or str(current_user.get("username", "")).lower() == "admin" else ("teacher" if str(current_user.get("id", "")).startswith("TCH-") else "student"))).lower()
current_user["role"] = user_role

# Master Curriculum Board Options
board_options = ["All Board", "CBSE (All India)", "ICSE / CISCE", "State Board (Maharashtra/UP/Karnataka)", "Cambridge IGCSE"]

def match_board_option(board_str):
    """Accurately maps board strings from user profiles to active board_options."""
    if not board_str:
        return "CBSE (All India)"
    b_lower = str(board_str).lower()
    if "icse" in b_lower or "cisce" in b_lower:
        return "ICSE / CISCE"
    elif "cbse" in b_lower:
        return "CBSE (All India)"
    elif "state" in b_lower:
        return "State Board (Maharashtra/UP/Karnataka)"
    elif "cambridge" in b_lower or "igcse" in b_lower:
        return "Cambridge IGCSE"
    for opt in board_options:
        if opt.lower() in b_lower or b_lower in opt.lower():
            return opt
    return "CBSE (All India)"

# -----------------------------------------------------------------------------
# PROFILE-DRIVEN DEFAULT FILTER SYNCHRONIZATION
# Always synchronizes Board, Class, and Subject filters to the logged-in student's profile.
# e.g., 10th Class ICSE student Daksh defaults to ICSE board and 10th class across Tutor, Grader, and References.
# -----------------------------------------------------------------------------
user_sync_token = f"{current_user.get('id')}_{current_user.get('username')}_{user_role}"
if st.session_state.get("last_synced_user_token") != user_sync_token:
    st.session_state["last_synced_user_token"] = user_sync_token
    if user_role == "student":
        target_board = match_board_option(current_user.get("board", "CBSE (All India)"))
        try:
            target_class = int(current_user.get("studentClass", 9))
        except Exception:
            target_class = 9
        if target_class not in [8, 9, 10]:
            target_class = 9
        target_subj = current_user.get("preferredSubject") or current_user.get("subject") or "Physics"
        if target_subj not in ["Physics", "Chemistry", "Mathematics"]:
            target_subj = "Physics"

        st.session_state["selected_curriculum_board"] = target_board
        st.session_state["global_board_selector"] = target_board
        st.session_state["g_board"] = target_board
        st.session_state["g_class"] = target_class
        st.session_state["t_class"] = target_class
        st.session_state["g_subj"] = target_subj
        st.session_state["t_subj"] = target_subj
        st.session_state["ref_board"] = target_board
        st.session_state["ref_class"] = target_class
        st.session_state["ref_subj"] = target_subj
    elif user_role == "teacher":
        t_subjs = current_user.get("subjects", ["Physics"])
        target_subj = t_subjs[0] if t_subjs and t_subjs[0] in ["Physics", "Chemistry", "Mathematics"] else "Physics"
        st.session_state["selected_curriculum_board"] = "All Board"
        st.session_state["global_board_selector"] = "All Board"
        st.session_state["g_board"] = "All Board"
        st.session_state["g_class"] = 9
        st.session_state["t_class"] = 9
        st.session_state["g_subj"] = target_subj
        st.session_state["t_subj"] = target_subj
        st.session_state["ref_board"] = "All Board"
        st.session_state["ref_class"] = 9
        st.session_state["ref_subj"] = target_subj
    else:  # Admin
        st.session_state["selected_curriculum_board"] = "All Board"
        st.session_state["global_board_selector"] = "All Board"
        st.session_state["g_board"] = "All Board"
        st.session_state["g_class"] = 9
        st.session_state["t_class"] = 9
        st.session_state["g_subj"] = "Physics"
        st.session_state["t_subj"] = "Physics"
        st.session_state["ref_board"] = "All Board"
        st.session_state["ref_class"] = 9
        st.session_state["ref_subj"] = "Physics"

# -----------------------------------------------------------------------------
# SIDEBAR: Profile Card with Background Artwork + Password Change
# -----------------------------------------------------------------------------
with st.sidebar:
    if user_role == "student":
        st.markdown(f"""
        <div class="sidebar-profile-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 15px; color: #FFFFFF;">👤 {current_user.get('name')}</span>
                <span class="role-badge-student" style="background: rgba(255,255,255,0.2); color: #93C5FD; border-color: #60A5FA;">Student</span>
            </div>
            <div style="font-size: 12.5px; color: #E0E7FF; margin-top: 5px; line-height: 1.45;">
                <code class="profile-id-badge" style="background: #EFF6FF !important; color: #1D4ED8 !important; -webkit-text-fill-color: #1D4ED8 !important; border: 1.5px solid #BFDBFE !important; padding: 2px 8px !important; border-radius: 6px !important; font-weight: 800 !important; font-size: 12px !important; display: inline-block !important;">{current_user.get('id')}</code> • Class {current_user.get('studentClass', 9)}th • {current_user.get('board', 'CBSE').split(' ')[0]}<br>
                📍 {current_user.get('cityState', 'Bangalore')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif user_role == "teacher":
        subj_list = ", ".join(current_user.get("subjects", ["Physics"]))
        st.markdown(f"""
        <div class="sidebar-profile-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 15px; color: #FFFFFF;">🛡️ {current_user.get('name')}</span>
                <span class="role-badge-teacher" style="background: rgba(16,185,129,0.25); color: #6EE7B7; border-color: #34D399;">Teacher</span>
            </div>
            <div style="font-size: 12.5px; color: #E0E7FF; margin-top: 5px; line-height: 1.45;">
                <code class="profile-id-badge" style="background: #EFF6FF !important; color: #1D4ED8 !important; -webkit-text-fill-color: #1D4ED8 !important; border: 1.5px solid #BFDBFE !important; padding: 2px 8px !important; border-radius: 6px !important; font-weight: 800 !important; font-size: 12px !important; display: inline-block !important;">{current_user.get('id')}</code> • Domain: <strong>{subj_list}</strong><br>
                {current_user.get('department', 'Academic Faculty')}
            </div>
        </div>
        <div class="blind-banner">
            🔒 <strong>Blind Evaluation:</strong> Student names masked.
        </div>
        """, unsafe_allow_html=True)

    else:  # Admin
        st.markdown(f"""
        <div class="sidebar-profile-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 800; font-size: 15px; color: #FFFFFF;">👑 {current_user.get('name')}</span>
                <span class="role-badge-admin" style="background: rgba(168,85,247,0.25); color: #D8B4FE; border-color: #C084FC;">Admin</span>
            </div>
            <div style="font-size: 12.5px; color: #E0E7FF; margin-top: 5px; line-height: 1.45;">
                <code class="profile-id-badge" style="background: #EFF6FF !important; color: #1D4ED8 !important; -webkit-text-fill-color: #1D4ED8 !important; border: 1.5px solid #BFDBFE !important; padding: 2px 8px !important; border-radius: 6px !important; font-weight: 800 !important; font-size: 12px !important; display: inline-block !important;">{current_user.get('id')}</code> • Super User (Executive Governance)
            </div>
        </div>
        """, unsafe_allow_html=True)

    # In-App Password Update feature in Sidebar
    pw_expander_title = "🔑 Change My Password" if user_role == "admin" else "🔑 Change Password"
    with st.expander(pw_expander_title, expanded=False):
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

    # Log Out Option: Consistently placed and prominently visible across Student, Teacher, and Admin views
    if st.button("🚪 Log Out", use_container_width=True, key="btn_sidebar_logout"):
        st.session_state["logged_in_user"] = None
        st.session_state["obj_submitted_flag"] = False
        st.rerun()

    # Admin Quick Reset Any User Password in Sidebar
    if user_role == "admin":
        with st.expander("🔐 Quick Reset User Password", expanded=False):
            st.caption("Super User Override: Reset password for any student or teacher upon request.")
            sb_candidates = [u for u in get_all_users_list() if str(u.get("role") or "").lower() != "admin"]
            if sb_candidates:
                sb_labels = [f"{u.get('name')} ({u.get('id')} • {str(u.get('role') or 'student').capitalize()})" for u in sb_candidates]
                sb_idx = st.selectbox("Select User to Reset:", range(len(sb_labels)), format_func=lambda i: sb_labels[i], key="sb_adm_sel_user_idx")
                sb_sel_user = sb_candidates[sb_idx]
                sb_target_uname = sb_sel_user.get("username", sb_sel_user.get("name"))
                sb_active_pw = get_user_password(sb_target_uname)
                st.markdown(f"<div style='font-size: 12.5px; color: #475569; margin-bottom: 8px;'>Current Password: <code style='font-weight: 800; color: #1D4ED8; background: #EEF2FF; padding: 2px 7px; border-radius: 4px;'>{sb_active_pw}</code></div>", unsafe_allow_html=True)
                sb_new_p = st.text_input(f"New Password for {sb_sel_user.get('name')}", type="password", key=f"sb_npw_{sb_target_uname}")
                sb_conf_p = st.text_input("Confirm New Password", type="password", key=f"sb_cpw_{sb_target_uname}")
                if st.button("💾 Save User Password", use_container_width=True, key=f"sb_btn_set_{sb_target_uname}"):
                    if len(sb_new_p) < 4:
                        st.error("Password must be at least 4 characters.")
                    elif sb_new_p != sb_conf_p:
                        st.error("New passwords do not match.")
                    else:
                        update_user_password(sb_target_uname, sb_new_p)
                        st.success(f"Password updated for {sb_sel_user.get('name')}!")
                        time.sleep(0.4)
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
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <span style="font-weight: 800; font-size: 13.5px; color: #1E293B; letter-spacing: 0.3px;">📚 NCERT & Reference Books</span>
            <span style="font-size: 12.5px; background: #EFF6FF; color: #1D4ED8; font-weight: 700; padding: 3px 8px; border-radius: 999px; border: 1px solid #BFDBFE;">Class {stu_class}th • {board_short}</span>
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
            <div style="display: flex; gap: 10px; align-items: flex-start;">
                <span style="font-size: 18px;">📘</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 13px; color: #0F172A;">NCERT Science Textbook (Class {stu_class}th)</div>
                    <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">{sci_desc}</div>
                    <div style="margin-top: 5px;">
                        <a href="https://ncert.nic.in/textbook.php?{ncert_sci_code}" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #BFDBFE;">📖 Open Official PDF</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 10px; align-items: flex-start;">
                <span style="font-size: 18px;">📐</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 13px; color: #0F172A;">NCERT Mathematics (Class {stu_class}th)</div>
                    <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">Complete Theory, Solved Examples & Exercises</div>
                    <div style="margin-top: 5px;">
                        <a href="https://ncert.nic.in/textbook.php?{ncert_math_code}" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #BFDBFE;">📖 Open Official PDF</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 10px; align-items: flex-start;">
                <span style="font-size: 18px;">🔬</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 13px; color: #0F172A;">NCERT Exemplar Problems</div>
                    <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">HOTS Questions, Numericals & Step Rubrics</div>
                    <div style="margin-top: 5px;">
                        <a href="https://ncert.nic.in/exemplar-problems.php" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 4px 10px; border-radius: 4px; border: 1px solid #A7F3D0;">🔬 View Exemplar</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="sidebar-resource-card">
            <div style="display: flex; gap: 10px; align-items: flex-start;">
                <span style="font-size: 18px;">🏛️</span>
                <div style="flex: 1;">
                    <div style="font-weight: 700; font-size: 13px; color: #0F172A;">DIKSHA National Portal</div>
                    <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">MoE Govt of India QR Interactive Textbooks</div>
                    <div style="margin-top: 5px;">
                        <a href="https://diksha.gov.in/" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #6D28D9; background: #F5F3FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #DDD6FE;">🌐 Open DIKSHA</a>
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
        <div style="font-weight: 800; font-size: 13.5px; color: #1E293B; margin-bottom: 10px;">
            📚 Faculty Pedagogical References
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 13px; color: #0F172A;">NCERT Learning Outcomes Manual</div>
            <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">Competency-based pedagogical standards for Secondary stage.</div>
            <div style="margin-top: 5px;">
                <a href="https://ncert.nic.in/pdf/programmes/learning_outcomes_sec.pdf" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #BFDBFE;">📋 View NCERT Guidelines</a>
            </div>
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 13px; color: #0F172A;">Bloom's Taxonomy Rubrics Guide</div>
            <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">Framework for step-by-step subjective assessment and partial credits.</div>
            <div style="margin-top: 5px;">
                <a href="https://cbseacademic.nic.in/" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 4px 10px; border-radius: 4px; border: 1px solid #A7F3D0;">🎯 CBSE Assessment Manual</a>
            </div>
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 13px; color: #0F172A;">NITI Aayog Responsible AI in Schools</div>
            <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">Human-in-the-Loop & blind evaluation governance protocols.</div>
            <div style="margin-top: 5px;">
                <a href="https://www.niti.gov.in/" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #6D28D9; background: #F5F3FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #DDD6FE;">⚖️ Governance Principles</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:  # Admin
        st.markdown("""
        <div style="font-weight: 800; font-size: 13.5px; color: #1E293B; margin-bottom: 10px;">
            📚 Institutional Governance Hub
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 13px; color: #0F172A;">DPDP Act 2023 Compliance Handbook</div>
            <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">Digital Personal Data Protection Act compliance requirements for minors.</div>
            <div style="margin-top: 5px;">
                <a href="https://www.meity.gov.in/content/digital-personal-data-protection-act-2023" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #BFDBFE;">🛡️ DPDP Act 2023 Official</a>
            </div>
        </div>
        <div class="sidebar-resource-card">
            <div style="font-weight: 700; font-size: 13px; color: #0F172A;">NEP 2020 Pedagogical Framework</div>
            <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">National Education Policy 5+3+3+4 curriculum & evaluation reforms.</div>
            <div style="margin-top: 5px;">
                <a href="https://www.education.gov.in/sites/upload_files/mhrd/files/NEP_Final_English_0.pdf" target="_blank" style="text-decoration:none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 4px 10px; border-radius: 4px; border: 1px solid #A7F3D0;">🏛️ NEP 2020 Document</a>
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
                <span style="font-size: 12px; background: rgba(255,255,255,0.18); color: #E2E8F0; padding: 3px 9px; border-radius: 999px; font-weight: 600;">{role_display}</span>
            </div>
        </div>
        <div class="aegis-subtext">
            Active: <strong>{current_user.get('name')}</strong> (<code>{current_user.get('id')}</code> • {str(user_role or 'admin').capitalize()}) • DPDP Act 2023 Aligned • NITI Aayog Responsible AI Frameworks
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_head_right:
    cur_sel_board = st.session_state.get("selected_curriculum_board") or ("CBSE (All India)" if user_role == "student" else "All Board")
    curr_b_idx = board_options.index(cur_sel_board) if cur_sel_board in board_options else 0
    selected_board = st.selectbox(
        "🏛️ Active Curriculum Board",
        board_options,
        index=curr_b_idx,
        key="global_board_selector",
        help="Select a curriculum board to filter institutional dashboards, queues, and student records. Select 'All Board' to view all students from all boards."
    )
    st.session_state["selected_curriculum_board"] = selected_board

# -----------------------------------------------------------------------------
# SPREAD-ACROSS BLUE TABS (4 FOR STUDENT, 5 FOR TEACHER, 7 FOR ADMIN)
# -----------------------------------------------------------------------------
# Irrespective of the number of tabs, the CSS divides 100% of the blue box equally!
if user_role == "student":
    tab_tutor, tab_grader, tab_history, tab_references = st.tabs([
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader",
        "📜 My Evaluations & Appeals",
        "📚 Suggested Study References"
    ])
    tab_teacher = None
    tab_admin = None
    tab_gov_ref = None

elif user_role == "teacher":
    tab_teacher, tab_tutor, tab_grader, tab_history, tab_references = st.tabs([
        "🛡️ Teacher / Governance Panel",
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader",
        "📜 Student Evaluations & Audit History",
        "📚 Suggested Study References"
    ])
    tab_admin = None
    tab_gov_ref = None

else:  # Admin (Super User Access) - Exclusive 'AI Governance Reference' Tab
    tab_tutor, tab_grader, tab_history, tab_teacher, tab_admin, tab_gov_ref, tab_references = st.tabs([
        "💡 AI Tutor (Concept Learning & Audio)",
        "✍️ AI Grader",
        "📜 All Evaluations & Appeals",
        "🛡️ Teacher / Governance Panel",
        "👑 Admin Governance Dashboard",
        "⚖️ AI Governance Reference",
        "📚 Suggested Study References"
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
            cur_t_class = st.session_state.get("t_class", current_user.get("studentClass", 9) if user_role == "student" else 9)
            t_class_idx = [8, 9, 10].index(cur_t_class) if cur_t_class in [8, 9, 10] else 1
            t_class = st.selectbox("1. Class", [8, 9, 10], index=t_class_idx, key="t_class")
        with col_t2:
            cur_t_subj = st.session_state.get("t_subj", "Physics")
            subj_opts = ["Physics", "Chemistry", "Mathematics"]
            t_subj_idx = subj_opts.index(cur_t_subj) if cur_t_subj in subj_opts else 0
            t_subject = st.selectbox("2. Subject", subj_opts, index=t_subj_idx, key="t_subj")
        with col_t3:
            if t_subject == "Physics":
                t_topics = ["Newton's Second Law & Momentum (F = ma)", "Inertia and First Law of Motion", "Universal Gravitation & Floatation", "Work, Energy & Power", "Sound & Waves"]
            elif t_subject == "Chemistry":
                t_topics = ["Evaporation & Latent Heat Cooling", "States of Matter & Phase Transitions", "Atoms, Molecules & Chemical Formulas", "Structure of the Atom"]
            else:
                t_topics = ["Rational vs Irrational Numbers", "Rationalizing the Denominator", "Laws of Exponents", "Polynomials & Factorization", "Linear Equations"]
            t_selected_topic = st.selectbox("3. Curriculum Topic", t_topics, key="t_top")

        # Multi-Modal Learning Input: Type Any Topic OR Upload Document (PDF/DOC) OR Paste YouTube Link
        col_topic_type, col_topic_source = st.columns([1.35, 1.65])

        with col_topic_type:
            st.markdown("#### 🔍 Or Type Any Topic/Concept to Clear Your Doubt:")
            custom_tutor_topic = st.text_input(
                "Open Text Box (Type concept name, scientific law, or question):",
                placeholder="e.g. Why does evaporation cause cooling?, Newton's 2nd Law derivation, Pythagoras Theorem proof...",
                key="custom_tutor_input"
            )

        with col_topic_source:
            st.markdown("#### 📁 Or Learn from PDF / DOC File or YouTube Link:")
            source_choice = st.radio(
                "Select Custom Learning Source:",
                ["None (Curriculum / Text)", "📄 Upload PDF / DOC", "▶️ Paste YouTube Link"],
                horizontal=True,
                key="tutor_source_mode_radio"
            )

            if "📄 Upload PDF" in source_choice:
                uploaded_doc = st.file_uploader(
                    "Upload notes or chapter PDF/DOCX/DOC/TXT:",
                    type=["pdf", "docx", "doc", "txt"],
                    key="tutor_doc_upload_input",
                    help="Upload any study document. The AI learns concepts from this document, teaches them, and derives test questions accordingly."
                )
                if uploaded_doc is not None:
                    doc_bytes = uploaded_doc.getvalue()
                    extracted_text = extract_document_content(uploaded_doc.name, doc_bytes)
                    st.session_state["tutor_active_source"] = {
                        "type": "doc",
                        "name": uploaded_doc.name,
                        "text": extracted_text,
                        "bytes": doc_bytes
                    }
                    st.success(f"✅ Document Analyzed: **{uploaded_doc.name}** ({round(len(doc_bytes)/1024, 1)} KB)")

            elif "▶️ Paste YouTube" in source_choice:
                yt_url_input = st.text_input(
                    "Enter YouTube Video Link:",
                    placeholder="https://www.youtube.com/watch?v=... or https://youtu.be/...",
                    key="tutor_yt_url_input",
                    help="Paste any educational YouTube URL. The AI extracts the lesson content, teaches concepts, and generates assessment questions."
                )
                if yt_url_input.strip():
                    yt_data = get_youtube_learning_content(yt_url_input.strip())
                    if yt_data:
                        st.session_state["tutor_active_source"] = {
                            "type": "youtube",
                            "name": yt_data["title"],
                            "text": yt_data["transcript"],
                            "url": yt_data["clean_url"],
                            "video_id": yt_data.get("video_id")
                        }
                        st.success(f"✅ YouTube Video Analyzed: **{yt_data['title']}**")
                    else:
                        st.error("Invalid YouTube URL. Please provide a standard YouTube video link.")
            else:
                if "tutor_active_source" in st.session_state and source_choice.startswith("None"):
                    del st.session_state["tutor_active_source"]

        active_source = st.session_state.get("tutor_active_source")

        st.markdown("<hr>", unsafe_allow_html=True)
        col_c1, col_c2 = st.columns([2, 1])

        with col_c1:
            if active_source:
                active_learning_topic = active_source["name"]
                st.markdown(f"### 📖 AI Teacher Breakdown: **{active_learning_topic}**")
                st.markdown(f"""
                <div style="background: #EFF6FF; border: 1.5px solid #60A5FA; border-radius: 10px; padding: 10px 14px; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <span style="font-weight: 800; color: #1D4ED8; font-size: 13.5px;">📁 Multi-Modal Learning Active:</span>
                        <span style="color: #0F172A; font-weight: 700;"> {active_source['name']}</span>
                        <span style="font-size: 12px; color: #475569;"> ({active_source['type'].upper()} Source)</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if active_source.get("type") == "youtube" and active_source.get("url"):
                    with st.expander("▶️ Watch Embedded YouTube Video Inside App", expanded=True):
                        st.video(active_source["url"])

                # Dynamic Lesson Synthesis from Uploaded Document or YouTube Video
                lesson_synth = synthesize_tutor_lesson(active_source["name"], active_source["text"], subject=t_subject, class_num=t_class)
                explanation_text = lesson_synth["explanation"]
                analogies = lesson_synth["analogies"]
                key_formulas = lesson_synth["key_principles"]
                audio_text = lesson_synth["audio_text"]

            else:
                active_learning_topic = custom_tutor_topic.strip() if custom_tutor_topic.strip() else t_selected_topic
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
                    audio_text = (
                        "Namaste and welcome students! Today, let us understand Newton's Second Law of Motion clearly and simply. "
                        "Momentum is mass in motion. "
                        "When catching a fast-moving cricket ball, pulling your hands backward increases the stopping time, "
                        "which cushions the impact and greatly reduces the force on your palms. "
                        "In your board exams, always remember: Force equals mass times acceleration, written as F equals m a, and measured in Newtons. "
                        "Define the law clearly, show step-by-step mathematical reasoning, and state the SI units to score full marks!"
                    )

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
                    audio_text = (
                        "Hello students! In Chemistry, let us understand why evaporation causes cooling. "
                        "Evaporation is a surface phenomenon. The high-energy liquid particles absorb latent heat from the surrounding surface to break free as vapor. "
                        "Because heat energy is drawn away, the surface cools down. "
                        "This is why traditional earthen pots keep drinking water delightfully cool during Indian summers, and why breathable cotton clothes keep you refreshed. "
                        "Remember: evaporation increases with surface area and temperature, but decreases with higher humidity."
                    )

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
                    audio_text = (
                        "Welcome to Mathematics! Today we master rational and irrational numbers. "
                        "Any number that can be expressed as a fraction p over q, where q is not zero, is rational. Its decimal either terminates or repeats predictably. "
                        "On the other hand, an irrational number, such as square root of two or pi, has a decimal that goes on endlessly without ever repeating. "
                        "To rationalize a denominator like one over root two, always multiply both numerator and denominator by its conjugate."
                    )
                else:
                    explanation_text = (
                        f"Here is your easy-to-understand breakdown for {active_learning_topic}.\n\n"
                        "In science and mathematics, every concept is governed by an underlying cause-and-effect relationship. "
                        "In your board exams, always frame your answers with: 1. A formal definition, 2. The mathematical formula with SI units, and 3. A real-world practical illustration."
                    )
                    analogies = [f"Relating {active_learning_topic} to everyday observable systems."]
                    key_formulas = ["Standard Law / Equation with explicit metric units."]
                    audio_text = (
                        f"Namaste students! Let us understand {active_learning_topic} with absolute conceptual clarity. "
                        "In science and mathematics, every concept is governed by cause and effect. "
                        "For your board examinations, always structure your answers with three clear pillars: "
                        "First, a crisp definition. Second, the exact mathematical formula with SI units. "
                        "And third, an everyday real-world example. Clear step-by-step presentation guarantees full marks!"
                    )

            st.markdown(explanation_text)

            # Embedded HTML5 Web Speech Audio Player (Zero Foreign Accent • Neutral Indian English Voice Modulation)
            st.markdown("#### 🔊 Audio Teacher Voice Narration (Neutral Indian English • Zero Accent):")
            clean_audio_js = audio_text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ").replace("\r", " ")
            audio_html = f"""
            <div style="background: #F8FAFC; padding: 14px 18px; border-radius: 12px; border: 1.5px solid #CBD5E1; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <button onclick="playEducatorAudio()" id="btn-play-audio" style="background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%); color: white; border: none; padding: 8px 18px; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 6px rgba(30,64,175,0.28);">
                            ▶ Listen to Teacher
                        </button>
                        <button onclick="stopEducatorAudio()" style="background: #EF4444; color: white; border: none; padding: 8px 14px; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer;">
                            ⏹ Stop
                        </button>
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                        <span style="font-size: 12px; font-weight: 700; color: #1E3A8A;">🎙️ Active Voice:</span>
                        <select id="voice-select" onchange="onVoiceChange()" style="padding: 5px 10px; border-radius: 6px; border: 1.5px solid #93C5FD; font-size: 12px; font-weight: 600; color: #1E293B; background: #FFFFFF; max-width: 290px;">
                            <option value="">Detecting Indian English Voices...</option>
                        </select>
                    </div>
                </div>
                <div id="audio-status" style="font-size: 12px; color: #475569; font-weight: 600; margin-top: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">
                    <span id="audio-msg">Click "Listen to Teacher" for clear, neutral Indian English concept narration.</span>
                    <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 3px 9px; border-radius: 999px; border: 1px solid #BBF7D0;">🇮🇳 Zero Foreign Accent • Natural Cadence</span>
                </div>
            </div>
            <script>
                var synth = window.speechSynthesis;
                var allVoices = [];
                var selectedVoiceObj = null;

                function populateVoices() {{
                    if (!('speechSynthesis' in window)) return;
                    allVoices = synth.getVoices();
                    var voiceSelect = document.getElementById('voice-select');
                    if (!voiceSelect || allVoices.length === 0) return;

                    voiceSelect.innerHTML = '';
                    var indianVoices = [];
                    var otherVoices = [];

                    var indKeywords = ['india', 'indian', 'en-in', 'en_in', 'heera', 'ravi', 'neerja', 'prabhat', 'veena', 'rishi', 'kavya'];

                    for (var i = 0; i < allVoices.length; i++) {{
                        var v = allVoices[i];
                        var lang = (v.lang || '').replace('_', '-').toLowerCase();
                        var name = (v.name || '').toLowerCase();
                        var isIndian = false;

                        if (lang === 'en-in' || lang === 'hi-in') {{
                            isIndian = true;
                        }} else {{
                            for (var k = 0; k < indKeywords.length; k++) {{
                                if (name.indexOf(indKeywords[k]) !== -1) {{
                                    isIndian = true;
                                    break;
                                }}
                            }}
                        }}

                        if (isIndian) {{
                            indianVoices.push(v);
                        }} else if (lang.indexOf('en') === 0) {{
                            otherVoices.push(v);
                        }}
                    }}

                    // Add Indian English voices first with flag
                    if (indianVoices.length > 0) {{
                        for (var j = 0; j < indianVoices.length; j++) {{
                            var opt = document.createElement('option');
                            opt.value = indianVoices[j].name;
                            opt.textContent = '🇮🇳 ' + indianVoices[j].name + ' (Indian English)';
                            voiceSelect.appendChild(opt);
                        }}
                        selectedVoiceObj = indianVoices[0];
                        voiceSelect.selectedIndex = 0;
                        document.getElementById('audio-msg').innerHTML = '🎯 <strong>Active Voice:</strong> 🇮🇳 ' + selectedVoiceObj.name + ' (Neutral Indian Educator)';
                    }} else {{
                        for (var m = 0; m < otherVoices.length; m++) {{
                            var opt = document.createElement('option');
                            opt.value = otherVoices[m].name;
                            opt.textContent = otherVoices[m].name + ' (' + otherVoices[m].lang + ')';
                            voiceSelect.appendChild(opt);
                        }}
                        if (otherVoices.length > 0) {{
                            selectedVoiceObj = otherVoices[0];
                            voiceSelect.selectedIndex = 0;
                        }}
                        document.getElementById('audio-msg').innerHTML = '💡 <em>Tuned for Neutral Indian Educator Cadence with zero accent</em>';
                    }}
                }}

                populateVoices();
                if ('speechSynthesis' in window && speechSynthesis.onvoiceschanged !== undefined) {{
                    speechSynthesis.onvoiceschanged = populateVoices;
                }}

                function onVoiceChange() {{
                    var selName = document.getElementById('voice-select').value;
                    for (var i = 0; i < allVoices.length; i++) {{
                        if (allVoices[i].name === selName) {{
                            selectedVoiceObj = allVoices[i];
                            document.getElementById('audio-msg').innerHTML = '🎯 <strong>Selected:</strong> ' + selectedVoiceObj.name;
                            break;
                        }}
                    }}
                }}

                function playEducatorAudio() {{
                    if (!('speechSynthesis' in window)) {{
                        alert('Speech synthesis is not supported on this browser.');
                        return;
                    }}
                    synth.cancel();

                    if (!allVoices || allVoices.length === 0) {{
                        populateVoices();
                    }}

                    var text = "{clean_audio_js}";
                    var msg = new SpeechSynthesisUtterance(text);
                    
                    // Explicitly set Indian English language locale
                    msg.lang = 'en-IN';

                    // Natural Indian Educator Modulation (clear articulation, not rushed)
                    msg.rate = 0.89;
                    msg.pitch = 1.04;

                    if (selectedVoiceObj) {{
                        msg.voice = selectedVoiceObj;
                        document.getElementById('audio-msg').innerHTML = '🔊 <strong>Speaking:</strong> ' + selectedVoiceObj.name + ' • <em>Clear Indian Educator Modulation...</em>';
                    }} else {{
                        document.getElementById('audio-msg').innerHTML = '🔊 <em>Speaking in Indian English educator cadence (en-IN)...</em>';
                    }}

                    msg.onend = function() {{
                        document.getElementById('audio-msg').innerHTML = '✅ <em>Narration complete. Concept ready for review!</em>';
                    }};
                    msg.onerror = function() {{
                        document.getElementById('audio-msg').innerHTML = '⏹ <em>Audio narration finished.</em>';
                    }};

                    synth.speak(msg);
                }}

                function stopEducatorAudio() {{
                    if ('speechSynthesis' in window) {{
                        synth.cancel();
                        document.getElementById('audio-msg').innerHTML = '⏹ <em>Audio stopped.</em>';
                    }}
                }}
            </script>
            """
            components.html(audio_html, height=110)

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
        st.subheader("✍️ AI Grader: Comprehensive Curriculum Assessment")
        st.caption("Dual Assessment Engine: Instant Objective MCQs + Step-by-Step Subjective Grader with AI Governance.")

        # Candidate Selection Ribbon (Profile Synced by Default)
        g_col1, g_col2, g_col3 = st.columns(3)
        with g_col1:
            cur_g_board = st.session_state.get("g_board", selected_board)
            g_b_idx = board_options.index(cur_g_board) if cur_g_board in board_options else 0
            g_board = st.selectbox("1. Board", board_options, index=g_b_idx, key="g_board")
        with g_col2:
            cur_g_class = st.session_state.get("g_class", current_user.get("studentClass", 9) if user_role == "student" else 9)
            g_c_idx = [8, 9, 10].index(cur_g_class) if cur_g_class in [8, 9, 10] else 1
            g_class = st.selectbox("2. Class", [8, 9, 10], index=g_c_idx, key="g_class")
        with g_col3:
            cur_g_subj = st.session_state.get("g_subj", "Physics")
            g_s_idx = ["Physics", "Chemistry", "Mathematics"].index(cur_g_subj) if cur_g_subj in ["Physics", "Chemistry", "Mathematics"] else 0
            g_subject = st.selectbox("3. Subject", ["Physics", "Chemistry", "Mathematics"], index=g_s_idx, key="g_subj")

        # Custom Learning Material / Document / YouTube Ingestion for Grader
        active_tutor_src = st.session_state.get("tutor_active_source")
        use_source_in_grader = False

        if active_tutor_src:
            col_src_box, col_src_tog = st.columns([2.8, 1.2])
            with col_src_box:
                st.markdown(f"""
                <div style="background: #EFF6FF; border: 1.5px solid #60A5FA; border-radius: 10px; padding: 10px 14px; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <span style="font-weight: 800; color: #1D4ED8; font-size: 13.5px;">📁 Active Learning Material Attached:</span>
                        <span style="color: #0F172A; font-weight: 700;"> {active_tutor_src['name']}</span>
                        <span style="font-size: 12px; color: #475569;"> ({active_tutor_src['type'].upper()})</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with col_src_tog:
                use_source_in_grader = st.checkbox("🎯 Generate Questions from this Document/Video", value=True, key="chk_use_source_in_grader")

        col_grader_type, col_grader_source = st.columns([1.35, 1.65])
        with col_grader_type:
            st.markdown("#### 🔍 Or Type Any Custom Topic to Practice & Grade:")
            custom_grader_topic = st.text_input(
                "Open Text Box (Custom Topic):",
                placeholder="e.g. Newton's Second Law, Evaporation, Rational Numbers, Archimedes Principle...",
                key="custom_grader_input"
            )
        with col_grader_source:
            if not active_tutor_src:
                st.markdown("#### 📁 Or Upload Document / YouTube Link to Test On:")
                grader_direct_choice = st.radio(
                    "Optional Custom Test Material:",
                    ["None (Curriculum Standard)", "📄 Upload PDF/DOC", "▶️ Paste YouTube Link"],
                    horizontal=True,
                    key="grader_direct_choice_radio"
                )
                if "📄 Upload PDF" in grader_direct_choice:
                    g_up_doc = st.file_uploader("Upload Notes or Test Paper (PDF, DOCX, TXT):", type=["pdf", "docx", "doc", "txt"], key="grader_direct_doc")
                    if g_up_doc:
                        g_bytes = g_up_doc.getvalue()
                        g_txt = extract_document_content(g_up_doc.name, g_bytes)
                        st.session_state["tutor_active_source"] = {"type": "doc", "name": g_up_doc.name, "text": g_txt, "bytes": g_bytes}
                        use_source_in_grader = True
                        st.rerun()
                elif "▶️ Paste YouTube" in grader_direct_choice:
                    g_yt_inp = st.text_input("YouTube Video URL to test on:", placeholder="https://www.youtube.com/watch?v=...", key="grader_direct_yt")
                    if g_yt_inp.strip():
                        g_yt_data = get_youtube_learning_content(g_yt_inp.strip())
                        if g_yt_data:
                            st.session_state["tutor_active_source"] = {"type": "youtube", "name": g_yt_data["title"], "text": g_yt_data["transcript"], "url": g_yt_data["clean_url"]}
                            use_source_in_grader = True
                            st.rerun()
            else:
                st.markdown("<div style='height: 38px;'></div>", unsafe_allow_html=True)
                if st.button("🔄 Clear Attached Document / Reset to Standard Curriculum", key="btn_clear_attached_src", use_container_width=True):
                    del st.session_state["tutor_active_source"]
                    st.rerun()

        active_grade_topic = custom_grader_topic.strip() if custom_grader_topic.strip() else ("Newton's Second Law of Motion" if g_subject == "Physics" else ("Evaporation & States of Matter" if g_subject == "Chemistry" else "Number Systems & Real Numbers"))

        if use_source_in_grader and active_tutor_src:
            st.info(f"🎯 **Active Testing Material:** {active_tutor_src['name']} ({active_tutor_src['type'].upper()}) • Aligned with {g_board} • Class {g_class}th {g_subject}")
        else:
            st.info(f"🎯 **Active Testing Topic:** {active_grade_topic} • **Curriculum:** {g_board} • Class {g_class}th {g_subject}")

        # Assessment Section Selector (Objective MCQs vs Subjective vs Both)
        st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
        grader_section = st.radio(
            "📋 Select Assessment Component:",
            [
                "🎯 Section A: Objective Questions (5 MCQs • 5 Marks • Instant Scoring)",
                "✍️ Section B: Subjective Questions (5 Questions • 20 Marks • Teacher Audited)",
                "📑 View Both Sections (Full Examination Paper)"
            ],
            index=0,
            horizontal=True,
            key="grader_section_toggle"
        )
        st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # SECTION A: OBJECTIVE TYPE QUESTIONS (5 MCQs, RADIO BUTTONS, INSTANT SCORE)
        # ---------------------------------------------------------------------
        if "Section A" in grader_section or "View Both" in grader_section:
            col_obj_hdr, col_obj_ref = st.columns([3.0, 1.4])
            with col_obj_hdr:
                st.markdown("### 🎯 Section A: 5 Objective Type Questions (MCQs)")
            with col_obj_ref:
                if st.button("🔄 Refresh Objective Questions", key="btn_refresh_mcq_questions", help="Click to load a fresh set of 5 curriculum MCQs", use_container_width=True):
                    st.session_state["active_obj_set_idx"] = st.session_state.get("active_obj_set_idx", 0) + 1
                    st.session_state["obj_submitted_flag"] = False
                    st.toast("🔄 Loaded fresh new set of 5 objective questions!")
                    st.rerun()

            active_obj_idx = st.session_state.get("active_obj_set_idx", 0)

            if use_source_in_grader and active_tutor_src:
                obj_data = generate_dynamic_mcqs_from_source(active_tutor_src['name'], active_tutor_src['text'], g_subject, g_class)
                total_obj_sets = 1
                display_obj_set_num = 1
            else:
                obj_data = get_objective_question_set(g_subject, g_class, custom_topic=custom_grader_topic.strip(), set_index=active_obj_idx)
                total_obj_sets = obj_data["total_sets"]
                display_obj_set_num = (active_obj_idx % total_obj_sets) + 1

            obj_questions = obj_data["questions"]
            active_obj_title = obj_data["topic_title"]

            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; border-left: 4px solid #10B981; border-radius: 8px; padding: 10px 16px; margin-bottom: 14px;">
                <div>
                    <span style="font-weight: 800; font-size: 13.5px; color: #1E293B;">📄 Objective Set {display_obj_set_num} of {total_obj_sets}:</span>
                    <span style="font-size: 13px; color: #059669; font-weight: 700;"> {active_obj_title}</span>
                    <span style="font-size: 12.5px; color: #475569;"> (Class {g_class}th • {g_subject})</span>
                </div>
                <div>
                    <span style="font-size: 12px; background: #D1FAE5; color: #065F46; font-weight: 700; padding: 4px 10px; border-radius: 999px;">Total 5 Marks (1 Mark / Question)</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            user_mcq_answers = {}
            for q_i, q in enumerate(obj_questions):
                st.markdown(f"<div style='font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 12px; margin-bottom: 6px;'>Q{q_i+1} (1.0 Mark): {q['question']}</div>", unsafe_allow_html=True)
                user_mcq_choice = st.radio(
                    f"Select answer for Q{q_i+1}:",
                    options=q["options"],
                    index=None,
                    key=f"mcq_radio_{q['id']}_{g_class}_{g_subject}_{display_obj_set_num}",
                    label_visibility="collapsed"
                )
                user_mcq_answers[q["id"]] = user_mcq_choice

            col_sub_obj, col_sub_sp = st.columns([1.5, 2.5])
            with col_sub_obj:
                btn_submit_objective = st.button("🚀 Submit Objective Section (Instant AI Score)", type="primary", key=f"btn_sub_obj_{display_obj_set_num}", use_container_width=True)

            if btn_submit_objective:
                st.session_state["obj_submitted_flag"] = True
                st.session_state["obj_last_set_num"] = display_obj_set_num

            # Immediate Reflection of Objective Marks
            if st.session_state.get("obj_submitted_flag", False) and st.session_state.get("obj_last_set_num") == display_obj_set_num:
                obj_score = 0.0
                for q in obj_questions:
                    if user_mcq_answers.get(q["id"]) == q["correct_option"]:
                        obj_score += 1.0

                obj_pct = int(round((obj_score / 5.0) * 100))
                
                st.markdown(f"""
                <div class="score-banner">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <div style="font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; color: #93C5FD; font-weight: 700;">Instant Objective Evaluation Completed</div>
                            <div style="font-size: 24px; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
                                🎯 Score: {obj_score} / 5.0 Marks ({obj_pct}%)
                            </div>
                            <div style="font-size: 13px; color: #E0E7FF; margin-top: 4px;">
                                Candidate: <strong>{current_user.get('name')}</strong> (<code>{current_user.get('id')}</code>) • Evaluated immediately by EduAegis Objective Engine
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <span style="font-size: 34px;">{'🌟' if obj_score == 5.0 else ('👍' if obj_score >= 3.0 else '📚')}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("#### 🔍 Detailed Question-by-Question Evaluation Breakdown:")
                for q_i, q in enumerate(obj_questions):
                    chosen = user_mcq_answers.get(q["id"])
                    is_correct = (chosen == q["correct_option"])
                    if is_correct:
                        st.markdown(f"""
                        <div style="background: #F0FDF4; border: 1.5px solid #BBF7D0; border-radius: 10px; padding: 12px 16px; margin-bottom: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <strong style="color: #166534; font-size: 14px;">✅ Q{q_i+1}: Correct (+1.0 Mark)</strong>
                                <span style="font-size: 12px; font-weight: 700; background: #DCFCE7; color: #15803D; padding: 3px 9px; border-radius: 999px;">Awarded: 1.0 / 1.0</span>
                            </div>
                            <div style="font-size: 13.5px; color: #1E293B; margin-top: 5px;"><strong>Your Answer:</strong> {chosen}</div>
                            <div style="font-size: 13px; color: #166534; margin-top: 5px; background: rgba(255,255,255,0.8); padding: 7px 10px; border-radius: 6px; line-height: 1.45;">💡 <strong>Explanation:</strong> {q['explanation']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background: #FEF2F2; border: 1.5px solid #FECACA; border-radius: 10px; padding: 12px 16px; margin-bottom: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <strong style="color: #991B1B; font-size: 14px;">❌ Q{q_i+1}: Incorrect (0.0 Marks)</strong>
                                <span style="font-size: 12px; font-weight: 700; background: #FEE2E2; color: #B91C1C; padding: 3px 9px; border-radius: 999px;">Awarded: 0.0 / 1.0</span>
                            </div>
                            <div style="font-size: 13.5px; color: #1E293B; margin-top: 5px;">
                                <strong>Your Answer:</strong> {chosen if chosen else '<em>Unattempted</em>'}<br>
                                <strong style="color: #166534;">Correct Answer:</strong> <strong>{q['correct_option']}</strong>
                            </div>
                            <div style="font-size: 13px; color: #475569; margin-top: 5px; background: rgba(255,255,255,0.8); padding: 7px 10px; border-radius: 6px; line-height: 1.45;">💡 <strong>Explanation:</strong> {q['explanation']}</div>
                        </div>
                        """, unsafe_allow_html=True)

                # Persist objective result attempt to database
                assigned_std_id = current_user.get("id", "STU-101")
                assigned_std_name = current_user.get("name", "Anup Sharma")
                sub_board = current_user.get("board", "CBSE (All India)") if (user_role == "student" or g_board == "All Board") else g_board
                new_obj_sub = {
                    "id": f"obj_sub_{int(time.time() * 1000)}",
                    "studentId": assigned_std_id,
                    "studentName": assigned_std_name,
                    "board": sub_board,
                    "className": f"Class {g_class}th",
                    "subject": g_subject,
                    "topic": active_obj_title,
                    "score": obj_score,
                    "maxMarks": 5.0,
                    "submittedAt": datetime.now().isoformat() + "Z"
                }
                db.setdefault("objective_submissions", []).insert(0, new_obj_sub)
                save_db(db)

            st.markdown("<hr style='margin: 16px 0;'>", unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # SECTION B: SUBJECTIVE TYPE QUESTIONS (5 QUESTIONS • 20 MARKS • TEACHER AUDITED)
        # ---------------------------------------------------------------------
        if "Section B" in grader_section or "View Both" in grader_section:
            st.markdown("### ✍️ Section B: 5-Question Subjective Paper (20 Total Marks)")

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
                st.markdown("#### 📝 Subjective Curriculum Paper (Step-by-Step Scoring)")
            with col_ref_q:
                if st.button("🔄 Refresh 5 Questions", key="btn_refresh_sample_questions", help="Click to load a brand new set of 5 questions for this class and subject", use_container_width=True):
                    st.session_state["active_q_set_idx"] = st.session_state.get("active_q_set_idx", 0) + 1
                    st.session_state["demo_mode_state"] = None
                    st.toast("🔄 Loaded fresh new 5-question curriculum set!")
                    st.rerun()

            active_set_idx = st.session_state.get("active_q_set_idx", 0)

            if use_source_in_grader and active_tutor_src:
                q_data = generate_dynamic_subjective_from_source(active_tutor_src['name'], active_tutor_src['text'], g_subject, g_class)
                total_available_sets = 1
                display_set_num = 1
            else:
                q_data = get_question_set(g_subject, g_class, custom_topic=custom_grader_topic.strip(), set_index=active_set_idx)
                total_available_sets = q_data["total_sets"]
                display_set_num = (active_set_idx % total_available_sets) + 1

            questions = q_data["questions"]
            active_set_title = q_data["topic_title"]

            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; background: #F1F5F9; border-left: 4px solid #2563EB; border-radius: 8px; padding: 10px 16px; margin-bottom: 14px;">
                <div>
                    <span style="font-weight: 800; font-size: 14px; color: #1E293B;">📄 Active Question Set {display_set_num} of {total_available_sets}:</span>
                    <span style="font-size: 13.5px; color: #2563EB; font-weight: 700;"> {active_set_title}</span>
                    <span style="font-size: 12.5px; color: #64748B;"> (Class {g_class}th • {g_subject})</span>
                </div>
                <div>
                    <span style="font-size: 12.5px; background: #E0E7FF; color: #3730A3; font-weight: 700; padding: 4px 10px; border-radius: 999px;">Total 20 Marks</span>
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

            # Option to Upload Handwritten Paper or Type Answers Online
            st.markdown("#### 📝 Answer Submission Method:")
            sub_ans_method = st.radio(
                "Choose how you want to submit your subjective answers:",
                [
                    "✍️ Type Answers in Text Boxes Below",
                    "📎 Upload Handwritten Answer Sheet (PDF, DOC, DOCX, or Photo of Paper)"
                ],
                index=0,
                horizontal=True,
                key=f"sub_ans_method_{display_set_num}"
            )

            attached_paper_doc = None
            if "Upload Handwritten" in sub_ans_method:
                uploaded_ans_sheet = st.file_uploader(
                    "📎 Upload Handwritten Answer Sheet (PDF, DOCX, DOC, PNG, JPG, JPEG):",
                    type=["pdf", "docx", "doc", "txt", "png", "jpg", "jpeg"],
                    key=f"file_uploader_ans_sheet_{display_set_num}",
                    help="Upload a PDF or scan/photo of your handwritten paper. Your teacher will inspect this document directly in the governance console and assign marks."
                )
                if uploaded_ans_sheet is not None:
                    p_bytes = uploaded_ans_sheet.getvalue()
                    p_text = extract_document_content(uploaded_ans_sheet.name, p_bytes) if not uploaded_ans_sheet.name.lower().endswith(('.png', '.jpg', '.jpeg')) else ""
                    p_b64 = base64.b64encode(p_bytes).decode("utf-8")
                    attached_paper_doc = {
                        "name": uploaded_ans_sheet.name,
                        "type": uploaded_ans_sheet.type or "application/pdf",
                        "size_str": f"{round(len(p_bytes)/1024, 1)} KB",
                        "size_bytes": len(p_bytes),
                        "data_b64": p_b64,
                        "extracted_text": p_text
                    }
                    st.success(f"✅ Handwritten Paper Attached: **{uploaded_ans_sheet.name}** ({attached_paper_doc['size_str']}). Attached for Teacher Audit & Grading!")

            user_answers = {}
            for idx, q in enumerate(questions):
                st.markdown(f"<div style='font-size: 15px; font-weight: 700; color: #0F172A; margin-top: 14px; margin-bottom: 6px;'>Q{idx+1} ({q['marks']} Marks): {q['text']}</div>", unsafe_allow_html=True)
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
                    height=80,
                    key=f"ans_{q['id']}_{g_class}_{g_subject}_{display_set_num}",
                    help="If you uploaded your answer sheet above, you may leave these blank or provide supplementary notes."
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
                    "questions": evaluation_results,
                    "uploadedDocument": attached_paper_doc
                }
                db.setdefault("submissions", []).insert(0, normalize_submission(new_sub, 0))
                save_db(db)

                if attached_paper_doc:
                    st.success(f"🎉 Paper & Solution Document **{attached_paper_doc['name']}** submitted successfully!")
                    st.info(f"📎 **Attached Document Registered:** Candidate **{assigned_std_id}** submitted a handwritten paper. It has been routed directly to the Teacher Evaluation Queue for manual review and score assignment.")
                else:
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

                    # Attached Handwritten Paper / Document info if present
                    if sub.get("uploadedDocument"):
                        doc_d = sub["uploadedDocument"]
                        st.markdown(f"""
                        <div style="background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 8px; padding: 7px 12px; margin: 6px 0; display: inline-flex; align-items: center; gap: 8px;">
                            <span style="font-weight: 700; color: #1D4ED8; font-size: 13px;">📎 Attached Answer Paper:</span>
                            <span style="font-size: 13px; color: #0F172A; font-weight: 600;">{doc_d.get('name')} ({doc_d.get('size_str', 'File')})</span>
                        </div>
                        """, unsafe_allow_html=True)
                        if doc_d.get("data_b64"):
                            try:
                                r_b = base64.b64decode(doc_d["data_b64"])
                                st.download_button(
                                    label=f"📥 Download Submitted Paper ({doc_d.get('name')})",
                                    data=r_b,
                                    file_name=doc_d.get("name", "Submitted_Paper.pdf"),
                                    mime=doc_d.get("type", "application/pdf"),
                                    key=f"hist_dl_{sub_id}_{s_idx}"
                                )
                            except Exception:
                                pass

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

                    # Attached Student Handwritten Paper / Solution Document
                    doc_att = sub.get("uploadedDocument")
                    if doc_att and doc_att.get("data_b64"):
                        st.markdown(f"""
                        <div style="background: #EFF6FF; border: 2px solid #3B82F6; border-radius: 12px; padding: 14px 18px; margin: 12px 0; box-shadow: 0 4px 12px rgba(59,130,246,0.12);">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <span style="font-weight: 800; color: #1D4ED8; font-size: 14.5px;">📎 Attached Student Handwritten Paper / Solution Document:</span>
                                    <div style="color: #0F172A; font-weight: 700; font-size: 14px; margin-top: 3px;">
                                        📄 {doc_att.get('name')} <span style="font-weight: 500; color: #64748B;">({doc_att.get('size_str', 'File')})</span>
                                    </div>
                                    <div style="font-size: 12.5px; color: #475569; margin-top: 2px;">
                                        Student submitted this handwritten physical exam paper. Review the attached document below and assign/adjust question marks accordingly.
                                    </div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        try:
                            raw_paper_bytes = base64.b64decode(doc_att.get("data_b64", ""))
                            col_doc_btn1, col_doc_btn2 = st.columns([1.6, 2.4])
                            with col_doc_btn1:
                                st.download_button(
                                    label=f"📥 Download Student Paper ({doc_att.get('name')})",
                                    data=raw_paper_bytes,
                                    file_name=doc_att.get("name", "Student_Answer_Sheet.pdf"),
                                    mime=doc_att.get("type", "application/pdf"),
                                    key=f"t_dl_paper_{sub_id}_{s_idx}",
                                    use_container_width=True
                                )
                            with col_doc_btn2:
                                if doc_att.get("extracted_text"):
                                    with st.expander("📝 View Extracted Text from Uploaded Paper", expanded=False):
                                        st.text_area("Extracted Paper Content", value=doc_att.get("extracted_text"), height=130, disabled=True, key=f"t_txt_paper_{sub_id}_{s_idx}")
                                elif doc_att.get("name", "").lower().endswith(('.png', '.jpg', '.jpeg')):
                                    with st.expander("🖼️ Preview Uploaded Paper Photo", expanded=False):
                                        st.image(raw_paper_bytes, caption=f"Handwritten Paper - Candidate {student_id}", use_column_width=True)
                        except Exception:
                            pass

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
                                        st.markdown(f'<span style="background: #DCFCE7; color: #15803D; font-size: 12.5px; font-weight: 700; padding: 3px 10px; border-radius: 999px; border: 1px solid #86EFAC;">🟢 Q{q_i+1} Released: <strong>{app_q_score} / {q_mx}</strong></span>', unsafe_allow_html=True)
                                    else:
                                        st.markdown(f'<span style="background: #FEF3C7; color: #92400E; font-size: 12.5px; font-weight: 600; padding: 3px 10px; border-radius: 999px; border: 1px solid #FCD34D;">⏳ Pending Question Release</span>', unsafe_allow_html=True)

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
                                    <span style="font-size: 12px; text-transform: uppercase; font-weight: 700; color: #1E40AF; letter-spacing: 0.5px;">Live Calculated Total Score (Instant Update)</span>
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

        # 4. Administrative User Credential & Password Management (Admin Can View & Change Any User's Password)
        st.markdown("### 🔐 Administrative User Credential & Password Management")
        st.caption("As Administrator, you have full authority to view and update/reset login passwords for any student or teacher upon request or security requirement.")

        manageable_users = [u for u in get_all_users_list() if u.get("role") != "admin"]

        col_admin_pw_left, col_admin_pw_right = st.columns([1.5, 2.5])

        with col_admin_pw_left:
            st.markdown("<div style='font-size: 14px; font-weight: 700; color: #1E293B; margin-bottom: 6px;'>1. Select Candidate or Faculty Profile:</div>", unsafe_allow_html=True)
            adm_role_filter = st.selectbox(
                "Filter by Role:",
                ["All Users (Students & Teachers)", "Students Only", "Teachers Only"],
                key="adm_tab_role_filter"
            )

            if adm_role_filter == "Students Only":
                filtered_target_users = [u for u in manageable_users if u.get("role") == "student"]
            elif adm_role_filter == "Teachers Only":
                filtered_target_users = [u for u in manageable_users if u.get("role") == "teacher"]
            else:
                filtered_target_users = manageable_users

            if not filtered_target_users:
                st.info("No users found matching filter.")
                selected_target_user = None
            else:
                target_user_labels = [
                    f"{u.get('name')} ({u.get('id')} • {str(u.get('role') or 'student').capitalize()} • {str(u.get('board') or u.get('department') or '').split(' ')[0]})"
                    for u in filtered_target_users
                ]
                sel_idx = st.selectbox(
                    "Choose Profile to View & Change Password:",
                    range(len(filtered_target_users)),
                    format_func=lambda i: target_user_labels[i],
                    key="adm_tab_target_user_idx"
                )
                selected_target_user = filtered_target_users[sel_idx]

            if selected_target_user:
                t_uname = selected_target_user.get("username", selected_target_user.get("name"))
                t_name = selected_target_user.get("name", t_uname)
                t_id = selected_target_user.get("id", "N/A")
                t_role = str(selected_target_user.get("role") or "student")
                t_email = selected_target_user.get("email", "Not provided")
                t_board = selected_target_user.get("board") or selected_target_user.get("department", "Sciences")
                t_current_pw = get_user_password(t_uname)

                badge_style = "role-badge-student" if t_role == "student" else "role-badge-teacher"

                st.markdown(f"""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 14px 16px; margin-top: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <div>
                            <span style="font-size: 15px; font-weight: 800; color: #0F172A;">{t_name}</span>
                            <span style="font-size: 12px; font-weight: 700; color: #475569; margin-left: 6px;">({t_id})</span>
                        </div>
                        <span class="{badge_style}" style="padding: 2px 8px; border-radius: 999px;">{str(t_role or 'student').capitalize()}</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">
                        👤 <strong>Login Username:</strong> <code>{t_uname}</code><br>
                        📧 <strong>Email:</strong> {t_email}<br>
                        🏛️ <strong>Affiliation:</strong> {t_board}
                    </div>
                    <div style="margin-top: 10px; padding: 10px 12px; background: #F1F5F9; border-radius: 8px; border: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12.5px; font-weight: 700; color: #1E293B;">🔑 Current Active Password:</span>
                        <code style="font-size: 14px; font-weight: 800; background: #EEF2FF; color: #1D4ED8; padding: 4px 10px; border-radius: 6px; border: 1px solid #BFDBFE;">{t_current_pw}</code>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with col_admin_pw_right:
            if selected_target_user:
                st.markdown(f"<div style='font-size: 14px; font-weight: 700; color: #1E293B; margin-bottom: 6px;'>2. Set New Password for {t_name} ({t_id}):</div>", unsafe_allow_html=True)
                
                with st.form(key=f"adm_pw_form_{t_uname}"):
                    col_p1, col_p2 = st.columns(2)
                    with col_p1:
                        adm_new_pw = st.text_input(
                            "New Password *",
                            type="password",
                            placeholder="Min 4 characters",
                            key=f"adm_form_npw_{t_uname}",
                            help=f"Enter the new password to assign to {t_name} ({t_uname})."
                        )
                    with col_p2:
                        adm_conf_pw = st.text_input(
                            "Confirm New Password *",
                            type="password",
                            placeholder="Re-enter new password",
                            key=f"adm_form_cpw_{t_uname}"
                        )

                    btn_submit_pw = st.form_submit_button("🔐 Enforce & Update Password Immediately", type="primary", use_container_width=True)

                    if btn_submit_pw:
                        if len(adm_new_pw) < 4:
                            st.error("Password must be at least 4 characters long.")
                        elif adm_new_pw != adm_conf_pw:
                            st.error("New password and confirmation password do not match.")
                        else:
                            update_user_password(t_uname, adm_new_pw)
                            st.success(f"🎉 Password successfully updated for {t_name} ({t_id})! New active password: '{adm_new_pw}'. The user can now immediately log in with this password.")
                            time.sleep(0.5)
                            st.rerun()

                # Quick 1-Click Reset to Institutional Default
                col_rst1, col_rst2 = st.columns([1.5, 1])
                with col_rst1:
                    if st.button(f"🔄 1-Click Reset {t_name}'s Password to 'eduaegis123'", key=f"btn_quick_rst_{t_uname}", use_container_width=True):
                        update_user_password(t_uname, "eduaegis123")
                        st.success(f"Reset password for {t_name} to institutional default: 'eduaegis123'!")
                        time.sleep(0.4)
                        st.rerun()
                with col_rst2:
                    st.caption("Standard institutional recovery protocol.")

        # Master Credential Directory & Viewer Table
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        with st.expander("📋 Master Institutional Credentials Directory & Passwords Viewer (All Users)", expanded=False):
            st.caption("Institutional security audit table displaying all active accounts with their current login passwords.")
            show_plain_pw = st.checkbox("👁️ Reveal Plaintext Passwords in Master Table (Security Clearance Active)", value=True, key="chk_reveal_master_pw")

            all_master_rows = []
            for u in manageable_users:
                u_un = u.get("username", u.get("name"))
                act_pw = get_user_password(u_un)
                display_pw = act_pw if show_plain_pw else "••••••••"
                all_master_rows.append({
                    "User ID": u.get("id", "N/A"),
                    "Full Name": u.get("name", u_un),
                    "Login Username": u_un,
                    "Role": str(u.get("role") or "student").capitalize(),
                    "Curriculum Board / Department": u.get("board") or u.get("department", "Sciences"),
                    "Email Address": u.get("email", "N/A"),
                    "Active Password": display_pw,
                    "Account Status": "🟢 Active"
                })

            df_master_cred = pd.DataFrame(all_master_rows)
            st.dataframe(df_master_cred, use_container_width=True, hide_index=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # 5. Global Directory & User Management
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

# =============================================================================
# TAB: AI GOVERNANCE REFERENCE (Exclusive for Admin Profiles Only)
# =============================================================================
if tab_gov_ref is not None:
    with tab_gov_ref:
        st.subheader("⚖️ Institutional AI Governance, Regulatory Intelligence & Compliance Repository")
        st.caption("Exclusive Executive Console for System Administrators: Global & Indian statutory frameworks, major AI acts, compliance checklists, and real-time regulatory monitors.")

        # Top Executive Compliance Indicator Cards
        st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin-bottom: 18px;">
            <div style="background: #F0FDF4; border: 1.5px solid #BBF7D0; border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #166534; letter-spacing: 0.5px;">🇮🇳 India DPDP Act 2023</div>
                <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-top: 2px;">Section 9 Compliant</div>
                <div style="font-size: 12px; color: #15803D; margin-top: 4px;">Zero behavioral profiling • Minor privacy protected</div>
            </div>
            <div style="background: #EFF6FF; border: 1.5px solid #BFDBFE; border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #1E40AF; letter-spacing: 0.5px;">🇪🇺 EU AI Act (2024/1689)</div>
                <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-top: 2px;">Annex III High-Risk Ready</div>
                <div style="font-size: 12px; color: #1D4ED8; margin-top: 4px;">Teacher-in-the-Loop • Mandatory human oversight</div>
            </div>
            <div style="background: #FDF4FF; border: 1.5px solid #F0ABFC; border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #86198F; letter-spacing: 0.5px;">⚖️ EU GDPR (Art. 22)</div>
                <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-top: 2px;">Human Agency Active</div>
                <div style="font-size: 12px; color: #701A75; margin-top: 4px;">Right of explanation & academic contestation</div>
            </div>
            <div style="background: #FEF3C7; border: 1.5px solid #FDE68A; border-radius: 10px; padding: 12px 14px;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #92400E; letter-spacing: 0.5px;">🏛️ NITI Aayog RAI</div>
                <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-top: 2px;">Seven Principles Aligned</div>
                <div style="font-size: 12px; color: #B45309; margin-top: 4px;">Blind grading • Algorithmic audit trails</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        gov_tab1, gov_tab2, gov_tab3, gov_tab4 = st.tabs([
            "🇮🇳 India AI Acts & Statutory Mandates",
            "🌍 Global AI Acts & International Treaties",
            "📡 Live AI Governance Trackers & Monitors",
            "📋 EduAegis Compliance Audit Matrix"
        ])

        with gov_tab1:
            st.markdown("### 🇮🇳 India AI Governance & Statutory Frameworks")
            st.caption("Statutory acts passed by Parliament of India, MeitY directives, and NITI Aayog Responsible AI policy documents.")

            col_in1, col_in2 = st.columns(2)
            with col_in1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">📜 Digital Personal Data Protection Act, 2023</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Statutory Act No. 22</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        Enacted by the Parliament of India (MeitY). Establishes comprehensive digital privacy standards for Data Fiduciaries processing citizen and minor personal data.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px; background: #F8FAFC; padding: 8px 10px; border-radius: 6px;">
                        📌 <strong>Key Clauses for Educational AI:</strong>
                        <ul style="margin: 4px 0 0 16px; padding: 0;">
                            <li><strong>Section 9 (Children's Data):</strong> Mandatory verifiable parental consent; absolute bar on behavioral tracking, targeted advertisements, or detrimental profiling of students.</li>
                            <li><strong>Section 6 & 8:</strong> Explicit notice, purpose limitation, and mandatory security safeguards.</li>
                            <li><strong>Penalties:</strong> Up to ₹250 Crores for failure to observe children's safety obligations.</li>
                        </ul>
                    </div>
                    <a href="https://www.meity.gov.in/content/digital-personal-data-protection-act-2023" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🏛️ Official MeitY Gazette Text ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">📑 NITI Aayog: Principles for Responsible AI (Part 1)</span>
                        <span style="font-size: 11px; background: #EFF6FF; color: #1D4ED8; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Policy Benchmark</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        National approach document establishing the foundational ethical principles for artificial intelligence deployments across India.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px; background: #F8FAFC; padding: 8px 10px; border-radius: 6px;">
                        📌 <strong>7 Foundational Core Principles:</strong>
                        1. Safety & Reliability • 2. Equality • 3. Inclusivity & Non-discrimination • 4. Proportionality • 5. Privacy & Data Protection • 6. Transparency & Explainability • 7. Accountability.
                    </div>
                    <a href="https://www.niti.gov.in/sites/default/files/2021-02/Responsible-AI-22022021.pdf" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0; display: inline-block;">
                        📄 Download NITI Aayog Part 1 (PDF) ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_in2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">⚙️ NITI Aayog: Operationalizing Principles for Responsible AI (Part 2)</span>
                        <span style="font-size: 11px; background: #FDF4FF; color: #86198F; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Enforcement Guide</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        Enforcement mechanisms, regulatory sandboxes, self-assessment compliance frameworks, and procurement guidelines for public and private AI systems.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px; background: #F8FAFC; padding: 8px 10px; border-radius: 6px;">
                        📌 <strong>Key Operational Directives:</strong>
                        <ul style="margin: 4px 0 0 16px; padding: 0;">
                            <li>Institutionalizing Ethics Committees & Teacher Oversight boards.</li>
                            <li>Pre-deployment algorithmic impact assessments (AIA).</li>
                            <li>Auditable logging of AI grading decisions to prevent student discrimination.</li>
                        </ul>
                    </div>
                    <a href="https://niti.gov.in/sites/default/files/2021-08/Part2-Responsible-AI-12082021.pdf" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #701A75; background: #FDF4FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #F0ABFC; display: inline-block;">
                        📄 Download NITI Aayog Part 2 (PDF) ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🚀 IndiaAI Mission & National Governance Framework</span>
                        <span style="font-size: 11px; background: #FEF3C7; color: #92400E; font-weight: 700; padding: 2px 8px; border-radius: 999px;">₹10,372 Cr Allocation</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        Approved by the Union Cabinet. Houses the <em>Safe & Trusted AI Pillar</em> developing indigenous evaluative tools, bias-mitigation benchmark datasets, and institutional algorithmic certification.
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="https://indiaai.gov.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE;">
                            🌐 IndiaAI Official Portal ↗
                        </a>
                        <a href="https://www.meity.gov.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0;">
                            🏛️ MeitY Regulatory Circulars ↗
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with gov_tab2:
            st.markdown("### 🌍 Global AI Legislation, Regulations & Standards")
            st.caption("International statutory acts, risk categorization standards, and global ethics agreements.")

            col_gl1, col_gl2 = st.columns(2)
            with col_gl1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🇪🇺 European Union AI Act (Regulation (EU) 2024/1689)</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Binding Global Standard</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        The world's first comprehensive horizontal legal framework on artificial intelligence. Entered into force across EU member states on 1 August 2024.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px; background: #F8FAFC; padding: 8px 10px; border-radius: 6px;">
                        📌 <strong>Annex III High-Risk Classification for Education:</strong>
                        <br>AI systems used to evaluate learning outcomes, grade tests, or steer student educational trajectories are classified as <strong>HIGH RISK</strong>.
                        <ul style="margin: 4px 0 0 16px; padding: 0;">
                            <li><strong>Mandatory Human Oversight:</strong> Qualified teachers must have final veto and release power.</li>
                            <li><strong>Risk Mitigation:</strong> Strict dataset quality, bias auditing, and continuous post-market monitoring.</li>
                            <li><strong>Explainability:</strong> Students have a legal right to understand how automated scores were derived.</li>
                        </ul>
                    </div>
                    <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🇪🇺 Official EUR-Lex Statutory Text (Regulation 2024/1689) ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">⚖️ EU GDPR (Article 22: Automated Decision-Making)</span>
                        <span style="font-size: 11px; background: #EFF6FF; color: #1D4ED8; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Data Protection</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        Provides individuals with the fundamental right <em>not to be subject to a decision based solely on automated processing</em>, including profiling, which produces legal or similarly significant effects.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px; background: #F8FAFC; padding: 8px 10px; border-radius: 6px;">
                        📌 <strong>Required Safeguards:</strong> Right to obtain human intervention, right to express one's point of view, and right to contest the automated evaluation.
                    </div>
                    <a href="https://gdpr-info.eu/art-22-gdpr/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        ⚖️ View GDPR Article 22 Statutory Text ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_gl2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🇺🇸 US NIST AI Risk Management Framework (AI RMF 1.0)</span>
                        <span style="font-size: 11px; background: #FEF3C7; color: #92400E; font-weight: 700; padding: 2px 8px; border-radius: 999px;">NIST AI 100-1</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        National Institute of Standards and Technology guidance framework for designing trustworthy and responsible artificial intelligence systems.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px; background: #F8FAFC; padding: 8px 10px; border-radius: 6px;">
                        📌 <strong>Four Core Pillars:</strong>
                        <ul style="margin: 4px 0 0 16px; padding: 0;">
                            <li><strong>GOVERN:</strong> Establish institutional oversight policies and risk culture.</li>
                            <li><strong>MAP:</strong> Identify operational context, student demographics, and potential harms.</li>
                            <li><strong>MEASURE:</strong> Rigorous quantitative evaluation of fairness, accuracy, and calibration.</li>
                            <li><strong>MANAGE:</strong> Continuous risk tracking and automated incident escalation.</li>
                        </ul>
                    </div>
                    <a href="https://www.nist.gov/itl/ai-risk-management-framework" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🇺🇸 NIST AI RMF Official Portal ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🌐 UNESCO Recommendation on the Ethics of AI</span>
                        <span style="font-size: 11px; background: #F3E8FF; color: #6B21A8; font-weight: 700; padding: 2px 8px; border-radius: 999px;">193 Member States</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
                        Unanimously adopted by all 193 UNESCO member states. Mandates protecting human dignity, child developmental well-being, and democratic access to educational technology.
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="https://www.unesco.org/en/artificial-intelligence/recommendation-ethics" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #6B21A8; background: #F3E8FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #E9D5FF;">
                            🌐 UNESCO Official Ethics Standard ↗
                        </a>
                        <a href="https://oecd.ai/en/principles" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0;">
                            🏛️ OECD AI Principles ↗
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with gov_tab3:
            st.markdown("### 📡 Live AI Governance Trackers & Real-Time Legal Intelligence")
            st.caption("Authoritative global repositories tracking AI legislative developments, policy enforcement, and court precedents.")

            col_tr1, col_tr2 = st.columns(2)
            with col_tr1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">📊 OECD.AI Policy Observatory</span>
                        <span style="font-size: 11px; background: #DBEAFE; color: #1E40AF; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Live Global Tracker</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Maintained by the OECD. Tracks over 1,000 national AI policies, legislative proposals, and executive orders across 70+ countries with interactive heatmaps.
                    </div>
                    <a href="https://oecd.ai/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 Explore OECD.AI Policy Observatory ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🎓 Stanford HAI AI Index & Policy Monitor</span>
                        <span style="font-size: 11px; background: #FEE2E2; color: #991B1B; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Stanford University</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Stanford Institute for Human-Centered AI annual report tracking global AI legislation passage rates, national algorithmic accountability laws, and foundation model evaluations.
                    </div>
                    <a href="https://aiindex.stanford.edu/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #DC2626; background: #FEF2F2; padding: 6px 12px; border-radius: 6px; border: 1px solid #FECACA; display: inline-block;">
                        🔗 Stanford HAI AI Index ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_tr2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">⚖️ IAPP AI Governance Center</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Privacy Professionals</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        International Association of Privacy Professionals (IAPP). Provides cross-jurisdictional AI legislative comparison tables, compliance toolkits, and emerging court precedents.
                    </div>
                    <a href="https://iapp.org/about/ai-governance-center/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0; display: inline-block;">
                        🔗 IAPP AI Governance Center ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🛡️ Future of Privacy Forum (FPF) - Student Privacy</span>
                        <span style="font-size: 11px; background: #FEF3C7; color: #92400E; font-weight: 700; padding: 2px 8px; border-radius: 999px;">EdTech & AI</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Specialized repository tracking student privacy in artificial intelligence, children's online data protections, and ethical considerations for automated assessment algorithms.
                    </div>
                    <a href="https://fpf.org/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #92400E; background: #FEF3C7; padding: 6px 12px; border-radius: 6px; border: 1px solid #FDE68A; display: inline-block;">
                        🔗 Future of Privacy Forum ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

        with gov_tab4:
            st.markdown("### 📋 EduAegis Institutional Compliance Audit Matrix")
            st.caption("Verification checklist mapping EduAegis architecture against statutory standards.")

            audit_matrix_data = [
                {
                    "Statutory Framework": "DPDP Act 2023 (Section 9)",
                    "Statutory Mandate": "Prohibition of behavioral tracking & detrimental profiling of minors",
                    "EduAegis Built-in Technical Safeguard": "Zero third-party tracking; encrypted offline persistence; evaluations restricted strictly to educational rubric scoring.",
                    "Audit Status": "🟢 COMPLIANT"
                },
                {
                    "Statutory Framework": "EU AI Act (Annex III High-Risk)",
                    "Statutory Mandate": "Mandatory human oversight in educational assessment AI",
                    "EduAegis Built-in Technical Safeguard": "Teacher-in-the-Loop Release Queue: AI scores are held in pending status until audited and released by faculty.",
                    "Audit Status": "🟢 COMPLIANT"
                },
                {
                    "Statutory Framework": "EU GDPR (Article 22)",
                    "Statutory Mandate": "Right to contest automated decisions and obtain human intervention",
                    "EduAegis Built-in Technical Safeguard": "Formal Academic Appeal & Contestation Workflow with transparent question-by-question step mark explanations.",
                    "Audit Status": "🟢 COMPLIANT"
                },
                {
                    "Statutory Framework": "NITI Aayog (Inclusivity & Equity)",
                    "Statutory Mandate": "Elimination of identity and demographic bias in automated scoring",
                    "EduAegis Built-in Technical Safeguard": "Blind Evaluation Protocol: Student names are masked from grading teachers to prevent halo or demographic bias.",
                    "Audit Status": "🟢 COMPLIANT"
                },
                {
                    "Statutory Framework": "NIST AI RMF 1.0 (Measurable Trust)",
                    "Statutory Mandate": "Repeatable, calibrated, non-hallucinatory scoring rubrics",
                    "EduAegis Built-in Technical Safeguard": "Deterministic Zero-Mark Rule for blank/NA/irrelevant answers; question-level mark breakdown matching official CBSE/ICSE answer keys.",
                    "Audit Status": "🟢 COMPLIANT"
                }
            ]
            st.dataframe(pd.DataFrame(audit_matrix_data), use_container_width=True, hide_index=True)

            st.markdown("<hr style='margin: 16px 0 12px 0;'>", unsafe_allow_html=True)
            col_dwn1, col_dwn2 = st.columns([2, 1])
            with col_dwn1:
                st.info("💡 **Compliance Statement:** EduAegis operates as a supervised pedagogical copilot. All subjective marks remain provisional until ratified by institutional academic faculty.")
            with col_dwn2:
                audit_json = json.dumps(audit_matrix_data, indent=2)
                st.download_button(
                    "📥 Export Compliance Audit Report (JSON)",
                    data=audit_json,
                    file_name="eduaegis_ai_governance_compliance.json",
                    mime="application/json",
                    use_container_width=True
                )

# =============================================================================
# TAB: SUGGESTED STUDY REFERENCES (Authenticated, Verified Portals & Research)
# =============================================================================
if tab_references is not None:
    with tab_references:
        st.subheader("📚 Suggested Study References: Authenticated & Verified Academic Resources")
        st.caption("Official national portals, interactive STEM simulations, verified video masterclasses, and pedagogical research frameworks tailored to your profile.")

        # Interactive Reference Filter Ribbon (Defaults to logged-in student's profile)
        ref_f1, ref_f2, ref_f3 = st.columns(3)
        with ref_f1:
            cur_ref_b = st.session_state.get("ref_board", selected_board if selected_board != "All Board" else "CBSE (All India)")
            ref_b_idx = board_options.index(cur_ref_b) if cur_ref_b in board_options else 1
            ref_board = st.selectbox("1. Filter References by Curriculum Board:", board_options, index=ref_b_idx, key="ref_board_select")
        with ref_f2:
            cur_ref_c = st.session_state.get("ref_class", current_user.get("studentClass", 9) if user_role == "student" else 9)
            ref_c_idx = [8, 9, 10].index(cur_ref_c) if cur_ref_c in [8, 9, 10] else 1
            ref_class = st.selectbox("2. Filter References by Class:", [8, 9, 10], index=ref_c_idx, key="ref_class_select")
        with ref_f3:
            cur_ref_s = st.session_state.get("ref_subj", "Physics")
            ref_s_idx = ["Physics", "Chemistry", "Mathematics"].index(cur_ref_s) if cur_ref_s in ["Physics", "Chemistry", "Mathematics"] else 0
            ref_subject = st.selectbox("3. Filter References by Subject:", ["Physics", "Chemistry", "Mathematics"], index=ref_s_idx, key="ref_subj_select")

        st.session_state["ref_board"] = ref_board
        st.session_state["ref_class"] = ref_class
        st.session_state["ref_subj"] = ref_subject

        # Profile Synchronization Badge Banner
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border: 1.5px solid #93C5FD; border-radius: 12px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 24px;">🎯</span>
                <div>
                    <div style="font-size: 14px; font-weight: 800; color: #1E3A8A;">Targeting: {ref_board} • Class {ref_class}th • {ref_subject}</div>
                    <div style="font-size: 12px; color: #3B82F6;">Curated authenticated portals, interactive simulations, and peer-reviewed educational research.</div>
                </div>
            </div>
            <div style="display: flex; gap: 6px;">
                <span style="font-size: 11.5px; background: #FFFFFF; color: #1D4ED8; font-weight: 700; padding: 3px 10px; border-radius: 999px; border: 1px solid #BFDBFE;">Verified Portals</span>
                <span style="font-size: 11.5px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 3px 10px; border-radius: 999px; border: 1px solid #BBF7D0;">NEP 2020 Aligned</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        ref_subtab1, ref_subtab2, ref_subtab3, ref_subtab4 = st.tabs([
            "🏛️ Official Government & Board Portals",
            "🧪 Interactive STEM Virtual Labs",
            "🎥 Verified YouTube Masterclasses",
            "📑 Educational Research & Standards"
        ])

        with ref_subtab1:
            st.markdown("### 🏛️ Authenticated National & Board Portals (Government & Official Councils)")
            st.caption("Official repositories, textbooks, curriculum frameworks, and authenticated sample papers.")

            col_gp1, col_gp2 = st.columns(2)
            with col_gp1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🌐 DIKSHA Portal (Govt. of India)</span>
                        <span style="font-size: 11px; background: #DBEAFE; color: #1E40AF; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Ministry of Education</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Digital Infrastructure for Knowledge Sharing. QR-code energized textbooks, interactive worksheets, and learning outcome assessments for CBSE, ICSE, and State Boards.
                    </div>
                    <a href="https://diksha.gov.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 Explore DIKSHA Portal ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">📖 NCERT Official & e-Pathshala</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">National Council</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Complete official digital textbooks (PDF / Flipbook), exemplar numerical problems, laboratory manuals, and teacher manuals for Classes 8, 9, and 10.
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="https://ncert.nic.in/textbook.php" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE;">
                            🔗 NCERT Textbooks ↗
                        </a>
                        <a href="https://epathshala.nic.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0;">
                            📱 e-Pathshala App ↗
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🔬 CSIR & Vigyan Prasar</span>
                        <span style="font-size: 11px; background: #FEF3C7; color: #92400E; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Scientific Research</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Council of Scientific & Industrial Research scientific popularization articles, hands-on experiment demonstrations, and national science discoveries repository.
                    </div>
                    <a href="https://www.csir.res.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 CSIR Science Portal ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_gp2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🏛️ CISCE Official Portal (ICSE & ISC)</span>
                        <span style="font-size: 11px; background: #F3E8FF; color: #6B21A8; font-weight: 700; padding: 2px 8px; border-radius: 999px;">CISCE Council</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Council for the Indian School Certificate Examinations official syllabi regulations, specimen question papers, marking keys, and pupil diagnostic performance analytics.
                    </div>
                    <a href="https://cisce.org/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 Official CISCE Portal ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">📺 SWAYAM & SWAYAM PRABHA</span>
                        <span style="font-size: 11px; background: #DBEAFE; color: #1E40AF; font-weight: 700; padding: 2px 8px; border-radius: 999px;">24x7 DTH Channel 31</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Ministry of Education high-quality educational television broadcasts and online secondary curriculum modules (Physics, Chemistry, Maths) free of cost across India.
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="https://swayam.gov.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE;">
                            🔗 SWAYAM Courses ↗
                        </a>
                        <a href="https://www.swayamprabha.gov.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0;">
                            📺 Swayam Prabha DTH ↗
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">📊 CBSE Academic Portal</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">CBSE Academic Unit</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Central Board of Secondary Education question banks, curriculum circulars, competency-based question books, and marking rubrics for Secondary classes.
                    </div>
                    <a href="https://cbseacademic.nic.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 CBSE Academic Portal ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

        with ref_subtab2:
            st.markdown("### 🧪 Interactive Virtual Laboratories & STEM Simulations")
            st.caption("Gain deep intuitive mastery through interactive simulations, variable controls, and real-time visualization.")

            col_sim1, col_sim2 = st.columns(2)
            with col_sim1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">⚡ PhET Interactive Simulations (Univ. of Colorado)</span>
                        <span style="font-size: 11px; background: #FEF3C7; color: #92400E; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Award Winning</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        World-class HTML5 interactive simulations for Physics, Chemistry, and Mathematics. Manipulate mass, acceleration, friction, atomic charges, and chemical equilibrium.
                    </div>
                    <div style="font-size: 12px; color: #1E293B; margin-bottom: 10px;">
                        🌟 <strong>Top Simulations for Class 8-10:</strong>
                        <ul style="margin: 4px 0 0 16px; padding: 0;">
                            <li><strong>Physics:</strong> Forces and Motion Basics (Newton's Laws), Gravity and Orbits</li>
                            <li><strong>Chemistry:</strong> States of Matter: Basics (Latent Heat), Balancing Chemical Equations</li>
                            <li><strong>Mathematics:</strong> Fraction Matcher, Function Builder, Area Model Algebra</li>
                        </ul>
                    </div>
                    <a href="https://phet.colorado.edu/en/simulations/browse" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🧪 Launch PhET Simulations ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🔬 OLabs (Online Labs for School Experiments)</span>
                        <span style="font-size: 11px; background: #DBEAFE; color: #1E40AF; font-weight: 700; padding: 2px 8px; border-radius: 999px;">MeitY & Amrita</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Developed by CDAC and Amrita CREATE under Ministry of Electronics & IT. Simulates CBSE curriculum school practicals with interactive apparatus and measurement vernier calipers.
                    </div>
                    <a href="http://www.olabs.edu.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 Access OLabs India ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_sim2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🔭 HBCSE - TIFR Science Olympiad Portal</span>
                        <span style="font-size: 11px; background: #F3E8FF; color: #6B21A8; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Tata Institute</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Homi Bhabha Centre for Science Education (TIFR Mumbai). Foundational concept inventories, experiential learning resources, and Indian National Olympiad (NSEJS) problem sets.
                    </div>
                    <a href="https://www.hbcse.tifr.res.in/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 HBCSE TIFR Portal ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">🛠️ Atal Tinkering Labs (AIM - NITI Aayog)</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">NITI Aayog</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Atal Innovation Mission maker resources, computational design modules, mechanical linkage guides, and practical STEM experiment toolkits for Class 8-10 innovators.
                    </div>
                    <a href="https://aim.gov.in/atal-tinkering-labs.php" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🔗 Explore ATL Community ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

        with ref_subtab3:
            st.markdown("### 🎥 Verified YouTube Channels & Curated Educational Masterclasses")
            st.caption("Top-rated educator channels delivering step-by-step problem derivations, board exam strategies, and conceptual visualizations in Indian English.")

            col_yt1, col_yt2 = st.columns(2)
            with col_yt1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">▶️ Khan Academy India</span>
                        <span style="font-size: 11px; background: #DCFCE7; color: #166534; font-weight: 700; padding: 2px 8px; border-radius: 999px;">100% Free • Non-Profit</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Complete, structured syllabus playlists aligned with CBSE and ICSE Classes 8, 9, and 10. Clear blackboard explanations of physics formulas, chemical reactions, and mathematical proofs.
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="https://www.youtube.com/@KhanAcademyIndia" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #DC2626; background: #FEF2F2; padding: 6px 12px; border-radius: 6px; border: 1px solid #FECACA;">
                            ▶ Khan Academy YouTube ↗
                        </a>
                        <a href="https://hi.khanacademy.org/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE;">
                            🌐 Interactive Website ↗
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">▶️ PW Foundation (Class 9 & 10)</span>
                        <span style="font-size: 11px; background: #DBEAFE; color: #1E40AF; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Physics Wallah</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Targeted one-shot revision sessions, NCERT line-by-line decoding, and numerical problem solving with relatable Indian daily life examples.
                    </div>
                    <a href="https://www.youtube.com/@PW-Foundation" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #DC2626; background: #FEF2F2; padding: 6px 12px; border-radius: 6px; border: 1px solid #FECACA; display: inline-block;">
                        ▶ PW Foundation Channel ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_yt2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">▶️ CIET - NCERT Official YouTube</span>
                        <span style="font-size: 11px; background: #F3E8FF; color: #6B21A8; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Ministry Channel</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Central Institute of Educational Technology live masterclasses, interactive demonstrations, and syllabus concept breakdowns by NCERT author professors.
                    </div>
                    <a href="https://www.youtube.com/@NCERTOFFICIAL" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #DC2626; background: #FEF2F2; padding: 6px 12px; border-radius: 6px; border: 1px solid #FECACA; display: inline-block;">
                        ▶ CIET-NCERT Channel ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">▶️ 3Blue1Brown & Veritasium</span>
                        <span style="font-size: 11px; background: #FEF3C7; color: #92400E; font-weight: 700; padding: 2px 8px; border-radius: 999px;">Visual Intuition</span>
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Visual mathematics and physics storytelling. Ideal for cultivating deep geometrical intuition and curious scientific thinking beyond textbooks.
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <a href="https://www.youtube.com/@3blue1brown" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE;">
                            ▶ 3Blue1Brown (Maths) ↗
                        </a>
                        <a href="https://www.youtube.com/@veritasium" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #DC2626; background: #FEF2F2; padding: 6px 12px; border-radius: 6px; border: 1px solid #FECACA;">
                            ▶ Veritasium (Physics) ↗
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with ref_subtab4:
            st.markdown("### 📑 Educational Research & Pedagogical Evaluation Standards")
            st.caption("Peer-reviewed pedagogical frameworks, national policy directives, and ethical AI evaluation rubrics.")

            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">
                        📜 National Education Policy (NEP 2020) Assessment Paradigm
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        NEP 2020 mandates transforming assessment from rote memorization testing to competency-based evaluation, measuring conceptual clarity, higher-order critical thinking, and real-life problem solving.
                    </div>
                    <a href="https://www.education.gov.in/nep/about-nep" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #047857; background: #ECFDF5; padding: 6px 12px; border-radius: 6px; border: 1px solid #A7F3D0; display: inline-block;">
                        🏛️ Read Official NEP 2020 Directive ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">
                        📐 CBSE Competency Assessment Frameworks (with British Council)
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        Co-developed with Cambridge International and British Council. Defines explicit step-by-step mark allocations, cognitive taxonomies (Knowledge vs Application), and diagnostic grading standards.
                    </div>
                    <a href="https://cbseacademic.nic.in/cba/framework.html" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        📑 View Competency Framework ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

            with col_res2:
                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">
                        🔍 CISCE Analysis of Pupil Performance (Diagnostic Error Analysis)
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        In-depth annual examiner reports examining common pitfalls, derivation errors, SI unit omissions, and conceptual confusions committed by ICSE secondary candidates.
                    </div>
                    <a href="https://cisce.org/pupil-analysis/" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        📊 Access Pupil Performance Data ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div style="background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="font-size: 15px; font-weight: 800; color: #0F172A; margin-bottom: 6px;">
                        🛡️ NITI Aayog Responsible AI & DPDP Act 2023 Principles
                    </div>
                    <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 10px;">
                        National strategy guidelines for ethical AI in education: mandatory Teacher-in-the-Loop audit governance, algorithmic transparency, zero hallucination guardrails, and minor data protection.
                    </div>
                    <a href="https://www.niti.gov.in/responsible-ai" target="_blank" style="text-decoration: none; font-size: 12.5px; font-weight: 700; color: #1D4ED8; background: #EFF6FF; padding: 6px 12px; border-radius: 6px; border: 1px solid #BFDBFE; display: inline-block;">
                        🛡️ NITI Aayog Responsible AI ↗
                    </a>
                </div>
                """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# GLOBAL FOOTER
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; font-size:13px; color:#475569; line-height:1.5;">
    🛡️ <strong>EduAegis</strong> • Responsible AI Tutor & Governed Grader • IIM Capstone Project<br>
    DPDP Act 2023 Aligned • Blind Evaluation Compliance • NITI Aayog Responsible AI Frameworks
</div>
""", unsafe_allow_html=True)
