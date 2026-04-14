"""
components/sidebar.py — 사이드바 필터 컴포넌트
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
import streamlit.components.v1 as components
from categories import all_majors, subs_for_majors


def render_sidebar() -> tuple[str, str, str, list[str], bool]:
    with st.sidebar:
        # ── 로고 ──────────────────────────────────────
        st.markdown("""
        <div style="padding:20px 0 16px 0; border-bottom:1px solid #c9b99a; margin-bottom:20px;">
            <div style="display:flex;align-items:center;gap:10px;">
                <div style="width:36px;height:36px;background:#2c1810;border-radius:50%;
                    display:flex;align-items:center;justify-content:center;
                    font-size:16px;">🎵</div>
                <div>
                    <div style="font-size:16px;font-weight:900;color:#2c1810;font-family:'Noto Serif KR',serif;">K-ENT Now</div>
                    <div style="font-size:11px;color:#8b7355;">오늘의 트렌드 보기</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── 대분류 ─────────────────────────────────────
        st.markdown('<div style="font-size:13px;font-weight:700;color:#5c4a3a;margin-bottom:8px;">카테고리</div>', unsafe_allow_html=True)
        major_options = ["전체"] + all_majors()
        major = st.selectbox(
            label="대분류",
            options=major_options,
            label_visibility="collapsed",
        )

        # ── 중분류 버튼형 ──────────────────────────────
        selected_majors = [] if major == "전체" else [major]
        sub_options = ["전체"] + subs_for_majors(selected_majors)

        st.markdown('<div style="font-size:13px;font-weight:700;color:#5c4a3a;margin:12px 0 8px;">중분류</div>', unsafe_allow_html=True)
        sub = st.selectbox(
            label="중분류",
            options=sub_options,
            label_visibility="collapsed",
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── 감성 필터 버튼형 ───────────────────────────
        st.markdown('<div style="font-size:13px;font-weight:700;color:#5c4a3a;margin-bottom:8px;">감성 필터</div>', unsafe_allow_html=True)
        sentiments = st.multiselect(
            label="감성",
            options=["긍정", "부정", "중립"],
            default=["긍정", "부정", "중립"],
            label_visibility="collapsed",
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── 아티스트 검색 ──────────────────────────────
        st.markdown('<div style="font-size:13px;font-weight:700;color:#5c4a3a;margin-bottom:8px;">아티스트 검색</div>', unsafe_allow_html=True)
        keyword = st.text_input(
            label="검색어",
            placeholder="예: BTS, aespa…",
            label_visibility="collapsed",
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── 자동 새로고침 ──────────────────────────────
        st.markdown("---")
        st.markdown('<div style="font-size:13px;font-weight:700;color:#5c4a3a;margin-bottom:6px;">자동 새로고침</div>', unsafe_allow_html=True)
        auto_refresh = st.toggle("ON / OFF", value=False)
        if auto_refresh:
            components.html(
                '<script>setTimeout(()=>window.location.reload(),60000)</script>',
                height=0,
            )
            st.caption("⏱️ 60초마다 자동 갱신")

        # ── 인용구 ─────────────────────────────────────
        st.markdown("---")
        st.markdown("""
        <div class="quote-text">
            "좋은 음악은<br>마음을 물들이고,<br>이야기는 세상을 잇는다."
        </div>
        """, unsafe_allow_html=True)

    return keyword, major, sub, sentiments, auto_refresh