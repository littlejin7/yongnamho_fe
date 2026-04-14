"""
styles.py — 수묵화 스타일 공통 CSS
"""

import streamlit as st


def apply_styles():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

/* ── 메인 배경 ───────────────────────────────────── */
.stApp { background-color: #f5f0e8; color: #2c1810; }
.main  { background-color: #f5f0e8; }
[data-testid="stAppViewContainer"] { background-color: #f5f0e8; }
[data-testid="stMain"] { background-color: #f5f0e8; }

/* ── 사이드바 ────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #ede8de;
    border-right: 1px solid #c9b99a;
}
[data-testid="stSidebar"] * { color: #2c1810 !important; }
[data-testid="stSidebar"] .stTextInput input {
    background-color: #f5f0e8 !important;
    border: 1px solid #c9b99a !important;
    color: #2c1810 !important;
    border-radius: 20px;
    padding: 6px 14px;
}
[data-testid="stSidebar"] .stSelectbox > div > div {
    background-color: #f5f0e8 !important;
    border: 1px solid #c9b99a !important;
    border-radius: 8px;
}

/* ── 탭 ──────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background-color: #ede8de;
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid #c9b99a;
}
.stTabs [data-baseweb="tab"] {
    background-color: transparent;
    border-radius: 8px;
    color: #8b7355;
    font-weight: 700;
    padding: 8px 20px;
}
.stTabs [aria-selected="true"] {
    background-color: #2c1810 !important;
    color: #f5f0e8 !important;
}

/* ── 컨테이너 카드 ───────────────────────────────── */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff;
    border: 1px solid #d4c4a8 !important;
    border-radius: 12px;
    transition: border-color 0.2s, box-shadow 0.2s;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #8b4513 !important;
    box-shadow: 0 2px 12px rgba(139,69,19,0.08);
}

/* ── 버튼 ────────────────────────────────────────── */
.stButton > button {
    background-color: #ede8de;
    color: #2c1810;
    border: 1px solid #c9b99a;
    border-radius: 8px;
    font-weight: 700;
    font-family: 'Noto Sans KR', sans-serif;
    transition: all 0.2s;
}
.stButton > button:hover {
    background-color: #2c1810;
    color: #f5f0e8;
    border-color: #2c1810;
}

/* ── 링크 버튼 ───────────────────────────────────── */
.stLinkButton > a {
    background-color: #ede8de !important;
    color: #8b4513 !important;
    border: 1px solid #c9b99a !important;
    border-radius: 8px;
    font-weight: 700;
}
.stLinkButton > a:hover {
    background-color: #2c1810 !important;
    color: #f5f0e8 !important;
}

/* ── 메트릭 ──────────────────────────────────────── */
[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #d4c4a8;
    border-radius: 12px;
    padding: 16px 20px;
}

/* ── info 박스 ───────────────────────────────────── */
.stAlert {
    background-color: #fdf6ec !important;
    border-left-color: #8b4513 !important;
    color: #5c3317 !important;
    border-radius: 8px;
}

/* ── 데이터프레임 ────────────────────────────────── */
.stDataFrame { background-color: #ffffff; border-radius: 10px; }

/* ── 제목 ────────────────────────────────────────── */
h1, h2, h3 { color: #2c1810 !important; font-weight: 900 !important; }

/* ── 이미지 ──────────────────────────────────────── */
img { border-radius: 8px; }

/* ── 스크롤바 ────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #f5f0e8; }
::-webkit-scrollbar-thumb { background: #c9b99a; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #8b4513; }

/* ───── 커스텀 컴포넌트 ───────────────────────────── */

/* 뉴스 카드 */
.news-card {
    background: #ffffff;
    border: 1px solid #d4c4a8;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.news-card:hover {
    border-color: #8b4513;
    box-shadow: 0 2px 12px rgba(139,69,19,0.08);
}

/* 랭킹 번호 */
.rank-num       { font-size: 28px; font-weight: 900; color: #8b4513; line-height: 1; font-family: 'Noto Serif KR', serif; }
.rank-num.top3  { color: #c0392b; }

/* 아티스트/헤드라인 */
.artist-name  { font-size: 15px; font-weight: 700; color: #2c1810; margin: 0; }
.headline     { font-size: 13px; color: #6b5c4c; margin: 2px 0 6px 0; }
.summary-text {
    font-size: 12px; color: #8b7355;
    border-left: 2px solid #8b4513;
    padding-left: 8px; margin: 6px 0;
}

/* 감성 배지 */
.badge-pos { background:#d4edda; color:#155724; padding:2px 8px; border-radius:20px; font-size:11px; font-weight:700; }
.badge-neg { background:#f8d7da; color:#721c24; padding:2px 8px; border-radius:20px; font-size:11px; font-weight:700; }
.badge-neu { background:#d1ecf1; color:#0c5460; padding:2px 8px; border-radius:20px; font-size:11px; font-weight:700; }

/* 변화 배지 */
.change-up   { color:#155724; font-size:11px; font-weight:700; }
.change-down { color:#721c24; font-size:11px; font-weight:700; }
.change-new  { background:#8b4513; color:#fff; padding:1px 6px; border-radius:10px; font-size:10px; font-weight:700; }
.change-same { color:#8b7355; font-size:11px; }

/* featured 카드 */
.featured-card {
    background: linear-gradient(135deg, #fdf6ec 0%, #f0e6d0 100%);
    border: 2px solid #c9b99a;
    border-radius: 16px;
    padding: 28px;
    height: 100%;
    position: relative;
    overflow: hidden;
}
.featured-card::before {
    content: '';
    position: absolute;
    top: -20px; right: -20px;
    width: 120px; height: 120px;
    background: radial-gradient(circle, rgba(139,69,19,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.featured-rank    { font-size: 56px; font-weight: 900; color: #c0392b; line-height:1; font-family: 'Noto Serif KR', serif; }
.featured-artist  { font-size: 28px; font-weight: 900; color: #2c1810; margin: 8px 0 4px; font-family: 'Noto Serif KR', serif; }
.featured-headline{ font-size: 16px; color: #8b4513; margin-bottom: 12px; font-weight: 700; }
.featured-summary { font-size: 14px; color: #5c4a3a; line-height: 1.7; }

/* 메트릭 카드 */
.metric-card {
    background: #ffffff;
    border: 1px solid #d4c4a8;
    border-radius: 12px;
    padding: 16px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.metric-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #8b4513, #c0392b);
    border-radius: 0 0 12px 12px;
}
.metric-label { font-size: 12px; color: #8b7355; margin-bottom: 4px; }
.metric-value { font-size: 26px; font-weight: 900; color: #2c1810; font-family: 'Noto Serif KR', serif; }
.metric-delta { font-size: 12px; margin-top: 2px; }

/* 섹션 타이틀 */
.section-title {
    font-size: 18px; font-weight: 900; color: #2c1810;
    border-left: 4px solid #8b4513;
    padding-left: 10px; margin: 20px 0 12px;
    font-family: 'Noto Serif KR', serif;
}

/* 날짜 배지 */
.date-badge {
    background: #ffffff;
    border: 1px solid #d4c4a8;
    border-radius: 8px;
    padding: 4px 12px;
    font-size: 13px; color: #6b5c4c;
    display: inline-block;
}

/* 카테고리 버튼 (사이드바) */
.cat-btn {
    display: inline-block;
    background: #f5f0e8;
    border: 1px solid #c9b99a;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 13px; font-weight: 700; color: #2c1810;
    margin: 3px;
    cursor: pointer;
    transition: all 0.15s;
}
.cat-btn:hover, .cat-btn.active {
    background: #2c1810;
    color: #f5f0e8;
    border-color: #2c1810;
}

/* 인용구 */
.quote-text {
    font-size: 13px; color: #8b7355;
    font-style: italic;
    line-height: 1.8;
    font-family: 'Noto Serif KR', serif;
    border-left: 2px solid #c9b99a;
    padding-left: 10px;
    margin-top: 16px;
}
</style>
""", unsafe_allow_html=True)