import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="K-ENT Now",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ───────────────────────────────────────────────────────────
# CSS
# ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #0f0f1a;
}
section[data-testid="stSidebar"] {
    background-color: #111122 !important;
}
.block-container { padding-top: 1.2rem !important; }

/* ── 사이드바 pill 버튼 ── */
div[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    padding: 5px 8px;
    border: 1.5px solid #2a2a4a;
    background: #1a1a2e;
    color: #94a3b8;
    transition: all 0.15s;
}
div[data-testid="stSidebar"] .stButton > button:hover {
    border-color: #7c3aed;
    color: #e2e8f0;
}

/* ── 뉴스 카드 ── */
.news-card {
    background: #1a1a2e;
    border: 1px solid #2a2a4a;
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 8px;
    transition: border-color 0.2s;
}
.news-card:hover { border-color: #7c3aed; }

.rank-num       { font-size:24px; font-weight:900; color:#7c3aed; line-height:1; min-width:36px; }
.rank-num.top3  { color:#f59e0b; }
.artist-name    { font-size:14px; font-weight:700; color:#e2e8f0; }
.headline-text  { font-size:12px; color:#94a3b8; margin: 1px 0; }

.dot-pos  { display:inline-block; width:7px; height:7px; border-radius:50%; background:#6ee7b7; margin-right:3px; }
.dot-neg  { display:inline-block; width:7px; height:7px; border-radius:50%; background:#fca5a5; margin-right:3px; }
.dot-neu  { display:inline-block; width:7px; height:7px; border-radius:50%; background:#93c5fd; margin-right:3px; }

.badge-pos { background:#064e3b; color:#6ee7b7; padding:2px 7px; border-radius:20px; font-size:10px; font-weight:700; }
.badge-neg { background:#450a0a; color:#fca5a5; padding:2px 7px; border-radius:20px; font-size:10px; font-weight:700; }
.badge-neu { background:#1e3a5f; color:#93c5fd; padding:2px 7px; border-radius:20px; font-size:10px; font-weight:700; }

.change-up   { color:#6ee7b7; font-size:11px; font-weight:700; }
.change-down { color:#fca5a5; font-size:11px; font-weight:700; }
.change-new  { background:#7c3aed; color:#fff; padding:1px 5px; border-radius:8px; font-size:9px; font-weight:700; }
.change-same { color:#64748b; font-size:11px; }

/* ── Featured 1위 카드 ── */
.featured-card {
    background: #1a1a2e;
    border: 2px solid #7c3aed;
    border-radius: 14px;
    padding: 24px 22px;
}
.featured-rank    { font-size:52px; font-weight:900; color:#f59e0b; line-height:1; }
.featured-artist  { font-size:26px; font-weight:900; color:#fff; margin: 6px 0 2px; }
.featured-headline{ font-size:15px; color:#c4b5fd; font-weight:700; margin-bottom:10px; }
.featured-summary { font-size:13px; color:#94a3b8; line-height:1.7; }

/* ── 메트릭 카드 ── */
.metric-card {
    background: #1a1a2e;
    border: 1px solid #2a2a4a;
    border-radius: 12px;
    padding: 14px 16px;
    text-align: left;
}

/* ── 섹션 타이틀 ── */
.section-title {
    font-size:17px; font-weight:900; color:#e2e8f0;
    border-left:4px solid #7c3aed; padding-left:10px;
    margin: 18px 0 10px;
}

/* ── 날짜 뱃지 ── */
.date-badge {
    background:#1a1a2e; border:1px solid #2a2a4a;
    border-radius:8px; padding:5px 14px;
    font-size:13px; color:#94a3b8; display:inline-block;
}

/* ── 브리핑 바 ── */
.briefing-bar {
    background:#1a1a2e; border:1px solid #2a2a4a;
    border-radius:12px; padding:16px 24px;
    display:flex; align-items:center; justify-content:space-between;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────
# MOCK DATA
# ───────────────────────────────────────────────────────────
NEWS = [
    {"rank":1,  "change":2,   "artist":"세븐틴",            "headline":"전원 재계약",          "summary":"세븐틴이 월드투어 앙코르에서 13명 전원 소속사와 두 번째 재계약을 깜짝 발표했다.", "sentiment":"pos", "score":96, "count":28},
    {"rank":2,  "change":0,   "artist":"엔하이픈",          "headline":"1억 스트리밍 달성",    "summary":"신보 타이틀곡이 발매 3일 만에 스포티파이 1억 스트리밍을 돌파했다.",             "sentiment":"pos", "score":89, "count":17},
    {"rank":3,  "change":-1,  "artist":"방탄소년단",        "headline":"빌보드 신기록",        "summary":"BTS가 빌보드 핫100에서 K팝 솔로 아티스트 최다 진입 기록을 경신했다.",          "sentiment":"pos", "score":94, "count":31},
    {"rank":4,  "change":"N", "artist":"에이비식스",        "headline":"멤버 넷째 임신 발표",  "summary":"에이비식스 멤버가 SNS를 통해 넷째 아이 임신 소식을 전했다.",                   "sentiment":"neu", "score":55, "count":9},
    {"rank":5,  "change":1,   "artist":"소녀시대",          "headline":"티파니 결혼 발표",     "summary":"소녀시대 티파니가 오랜 교제 끝에 결혼을 공식 발표했다.",                       "sentiment":"pos", "score":78, "count":22},
    {"rank":6,  "change":0,   "artist":"에이티즈",          "headline":"아시아·호주 투어 확정","summary":"에이티즈가 아시아 및 호주 10개 도시 투어 일정을 공개했다.",                    "sentiment":"pos", "score":85, "count":14},
    {"rank":7,  "change":3,   "artist":"악뮤",              "headline":"7년 만 신곡 발매",    "summary":"악동뮤지션이 7년 만에 발매한 신곡이 각종 차트 1위를 휩쓸고 있다.",              "sentiment":"pos", "score":91, "count":19},
    {"rank":8,  "change":"N", "artist":"킥플립",            "headline":"마이 퍼스트 킥",      "summary":"신인 그룹 킥플립이 데뷔곡으로 각종 SNS에서 화제를 모으고 있다.",               "sentiment":"pos", "score":72, "count":7},
    {"rank":9,  "change":-3,  "artist":"코르티스",          "headline":"선주문 122만 장",     "summary":"코르티스 신보 선주문이 역대 자체 최고인 122만 장을 기록했다.",                 "sentiment":"pos", "score":88, "count":11},
    {"rank":10, "change":2,   "artist":"아이브",            "headline":"안유진 화보 공개",    "summary":"아이브 안유진의 글로벌 패션지 화보가 공개되며 뜨거운 반응을 얻고 있다.",         "sentiment":"pos", "score":82, "count":16},
    {"rank":11, "change":-1,  "artist":"피원하모니",        "headline":"日 팬미팅 성료",      "summary":"피원하모니가 일본 도쿄 팬미팅을 성공적으로 마쳤다.",                           "sentiment":"pos", "score":79, "count":8},
    {"rank":12, "change":1,   "artist":"엑스디너리히어로즈","headline":"DEAD AND 발매",        "summary":"밴드 엑스디너리히어로즈가 새 EP를 전격 발매했다.",                             "sentiment":"neu", "score":60, "count":6},
    {"rank":13, "change":4,   "artist":"키스오브라이프",    "headline":"뮤비 티저 공개",      "summary":"키스오브라이프가 컴백 뮤직비디오 티저를 공개하며 기대감을 높이고 있다.",          "sentiment":"pos", "score":84, "count":10},
    {"rank":14, "change":"N", "artist":"아일릿",            "headline":"미니 4집 예고",       "summary":"아일릿이 미니 4집 컨셉 이미지를 공개하며 컴백을 예고했다.",                    "sentiment":"pos", "score":77, "count":9},
    {"rank":15, "change":-2,  "artist":"리센느",            "headline":"뮤직비디오 티저",     "summary":"리센느가 신보 뮤직비디오 티저를 공개했다.",                                   "sentiment":"neu", "score":58, "count":5},
]

SENTIMENT_TIME = pd.DataFrame({
    "시간": ["00시","02시","04시","06시","08시","10시","12시","14시","16시","18시","20시","22시"],
    "긍정": [12, 8,  6, 15, 28, 42, 38, 45, 52, 49, 55, 47],
    "부정": [ 3, 2,  1,  4,  7,  9,  8, 10, 11,  9,  8,  7],
    "중립": [ 5, 4,  3,  6, 10, 14, 12, 15, 18, 16, 14, 13],
})

def dot(s):
    cls = {"pos":"dot-pos","neg":"dot-neg","neu":"dot-neu"}.get(s,"dot-neu")
    return f'<span class="{cls}"></span>'

def sent_kr(s):
    return {"pos":"긍정","neg":"부정","neu":"중립"}.get(s,"중립")

def badge(s):
    cls = {"pos":"badge-pos","neg":"badge-neg","neu":"badge-neu"}.get(s,"badge-neu")
    em  = {"pos":"●","neg":"●","neu":"●"}.get(s,"●")
    return f'<span class="{cls}">{em} {sent_kr(s)}</span>'

def change_badge(c):
    if c == "N": return '<span class="change-new">NEW</span>'
    if isinstance(c, int):
        if c > 0:  return f'<span class="change-up">↑</span>'
        if c < 0:  return f'<span class="change-down">↓</span>'
    return '<span class="change-same">→</span>'

# ───────────────────────────────────────────────────────────
# SESSION STATE (pill 버튼용)
# ───────────────────────────────────────────────────────────
if "sel_cats"  not in st.session_state:
    st.session_state.sel_cats  = {"아이돌", "드라마", "영화", "글로벌"}
if "sel_sents" not in st.session_state:
    st.session_state.sel_sents = {"긍정", "부정", "중립"}

# ───────────────────────────────────────────────────────────
# SIDEBAR
# ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:8px 0 16px;">
      <div style="font-size:18px;font-weight:900;color:#e2e8f0;">🎵 K-ENT Now</div>
      <div style="font-size:11px;color:#64748b;margin-top:2px;">오늘의 트렌드 보기</div>
    </div>
    """, unsafe_allow_html=True)

    # 카테고리 pill 버튼
    st.markdown('<div style="font-size:12px;font-weight:700;color:#94a3b8;margin-bottom:6px;">카테고리</div>', unsafe_allow_html=True)
    cat_list = ["아이돌","드라마","영화","글로벌"]
    c1, c2 = st.columns(2)
    for i, cat in enumerate(cat_list):
        col = c1 if i % 2 == 0 else c2
        is_on = cat in st.session_state.sel_cats
        label = f"{'✓ ' if is_on else ''}{cat}"
        with col:
            if st.button(label, key=f"cat_{cat}"):
                if is_on:
                    st.session_state.sel_cats.discard(cat)
                else:
                    st.session_state.sel_cats.add(cat)
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 감성 필터 pill 버튼
    st.markdown('<div style="font-size:12px;font-weight:700;color:#94a3b8;margin-bottom:6px;">감성 필터</div>', unsafe_allow_html=True)
    sent_list = ["긍정","부정","중립"]
    s1, s2, s3 = st.columns(3)
    sent_colors = {"긍정":"#064e3b","부정":"#450a0a","중립":"#1e3a5f"}
    for col, sent in zip([s1, s2, s3], sent_list):
        is_on = sent in st.session_state.sel_sents
        label = f"{'✓' if is_on else ''} {sent}"
        with col:
            if st.button(label, key=f"sent_{sent}"):
                if is_on:
                    st.session_state.sel_sents.discard(sent)
                else:
                    st.session_state.sel_sents.add(sent)
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 아티스트 검색
    st.markdown('<div style="font-size:12px;font-weight:700;color:#94a3b8;margin-bottom:6px;">아티스트 검색</div>', unsafe_allow_html=True)
    search = st.text_input("", placeholder="예: BTS, aespa…", label_visibility="collapsed")

    st.markdown("---")

    # 자동 새로고침
    st.markdown('<div style="font-size:12px;font-weight:700;color:#94a3b8;margin-bottom:6px;">자동 새로고침</div>', unsafe_allow_html=True)
    auto = st.toggle("ON", value=False)
    if auto:
        import streamlit.components.v1 as components
        components.html('<script>setTimeout(()=>window.location.reload(),60000)</script>', height=0)
        st.caption("⏱️ 60초마다 갱신")

# ───────────────────────────────────────────────────────────
# 필터 적용
# ───────────────────────────────────────────────────────────
sent_map = {"긍정":"pos","부정":"neg","중립":"neu"}
active_sents = {sent_map[s] for s in st.session_state.sel_sents}
filtered_news = [
    n for n in NEWS
    if n["sentiment"] in active_sents
    and (not search or search in n["artist"])
]

# ───────────────────────────────────────────────────────────
# HEADER
# ───────────────────────────────────────────────────────────
today = datetime.now().strftime("%Y년 %m월 %d일")
h_left, h_right = st.columns([4, 1])
with h_left:
    st.markdown("""
    <div style="margin-bottom:4px;">
      <span style="font-size:28px;font-weight:900;color:#e2e8f0;">K-ENT Now</span>
      <span style="font-size:13px;color:#64748b;margin-left:10px;">오늘의 트렌드 보기</span>
    </div>
    <div style="height:3px;background:linear-gradient(90deg,#7c3aed,#2d1b69,transparent);border-radius:2px;margin-bottom:16px;"></div>
    """, unsafe_allow_html=True)
with h_right:
    st.markdown(f'<div style="text-align:right;padding-top:6px;"><span class="date-badge">📅 {today}</span></div>', unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────
# METRIC CARDS (아이콘 없음 — 수치만)
# ───────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
metrics = [
    ("오늘 뉴스",    "287건",  "+42 ↑",  "#6ee7b7"),
    ("긍정 기사",    "78%",    "+5%p ↑", "#6ee7b7"),
    ("부정 급등",    "3건",    "+3 ↑",   "#fca5a5"),
    ("핫 아티스트",  "세븐틴", "1위",    "#f59e0b"),
]
for col, (label, val, delta, dcolor) in zip([m1,m2,m3,m4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
          <div style="font-size:11px;color:#64748b;margin-bottom:4px;">{label}</div>
          <div style="font-size:26px;font-weight:900;color:#e2e8f0;line-height:1.2;">{val}</div>
          <div style="font-size:11px;color:{dcolor};margin-top:3px;">{delta}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────
# 오늘의 랭킹
# ───────────────────────────────────────────────────────────
st.markdown('<div class="section-title">오늘의 랭킹</div>', unsafe_allow_html=True)

featured = filtered_news[0] if filtered_news else NEWS[0]
rest     = filtered_news[1:15] if len(filtered_news) > 1 else NEWS[1:15]

left, right = st.columns([1, 2])

with left:
    st.markdown(f"""
    <div class="featured-card">
      <div class="featured-rank">0{featured["rank"]}</div>
      <div style="margin:8px 0 4px;display:flex;align-items:center;gap:8px;">
        {badge(featured["sentiment"])}
        <span style="font-size:11px;color:#64748b;">기사 {featured["count"]}건</span>
      </div>
      <div class="featured-artist">{featured["artist"]}</div>
      <div class="featured-headline">{featured["headline"]}</div>
      <div class="featured-summary">{featured["summary"]}</div>
      <div style="margin-top:18px;padding-top:12px;border-top:1px solid #2a2a4a;">
        <span style="font-size:12px;color:#94a3b8;">감성 스코어</span>
        <span style="font-size:28px;font-weight:900;color:#6ee7b7;margin-left:8px;">{featured["score"]}점</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")
    if st.button("▶ 1위 뉴스 브리핑 듣기", use_container_width=True):
        try:
            from gtts import gTTS
            import io
            tts = gTTS(text=f"1위는 {featured['artist']}입니다. {featured['summary']}", lang="ko")
            fp = io.BytesIO(); tts.write_to_fp(fp); fp.seek(0)
            st.audio(fp, format="audio/mp3")
        except:
            st.info("gTTS 설치 후 사용 가능: pip install gTTS")

with right:
    cols_r = st.columns(2)
    for i, news in enumerate(rest[:14]):
        with cols_r[i % 2]:
            rank_cls = "top3" if news["rank"] <= 3 else ""
            st.markdown(f"""
            <div class="news-card">
              <div style="display:flex;align-items:center;gap:10px;">
                <span class="rank-num {rank_cls}">{str(news["rank"]).zfill(2)}</span>
                <div style="flex:1;min-width:0;">
                  <div style="display:flex;align-items:center;gap:5px;flex-wrap:wrap;">
                    <span class="artist-name">{news["artist"]}</span>
                    {change_badge(news["change"])}
                  </div>
                  <div class="headline-text">{news["headline"]}</div>
                  <div style="display:flex;align-items:center;gap:6px;margin-top:4px;flex-wrap:wrap;">
                    {dot(news["sentiment"])}
                    <span style="font-size:10px;color:#64748b;">{sent_kr(news["sentiment"])} | 기사 {news["count"]}건</span>
                    <span style="font-size:11px;color:#7c3aed;margin-left:auto;font-weight:700;">{news["score"]}점</span>
                  </div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────
# 감성 추이 차트
# ───────────────────────────────────────────────────────────
st.markdown('<div class="section-title">오늘의 감성 추이</div>', unsafe_allow_html=True)

fig = go.Figure()
for col_name, color, kr in [("긍정","#6ee7b7","긍정"),("부정","#fca5a5","부정"),("중립","#93c5fd","중립")]:
    fig.add_trace(go.Scatter(
        x=SENTIMENT_TIME["시간"],
        y=SENTIMENT_TIME[col_name],
        name=kr,
        line=dict(color=color, width=2),
        fill="tozeroy",
        fillcolor=color + "15",
        mode="lines+markers",
        marker=dict(size=4)
    ))
fig.update_layout(
    paper_bgcolor="#0f0f1a",
    plot_bgcolor="#1a1a2e",
    font=dict(color="#94a3b8", family="Noto Sans KR", size=11),
    legend=dict(bgcolor="#1a1a2e", bordercolor="#2a2a4a", orientation="h",
                x=0, y=1.12, font=dict(size=11)),
    xaxis=dict(gridcolor="#2a2a4a", showline=False),
    yaxis=dict(gridcolor="#2a2a4a", showline=False),
    margin=dict(l=10, r=10, t=30, b=10),
    height=260,
)
st.plotly_chart(fig, use_container_width=True)

# ───────────────────────────────────────────────────────────
# 브리핑 바
# ───────────────────────────────────────────────────────────
st.markdown('<div style="height:1px;background:#2a2a4a;margin:8px 0 16px;"></div>', unsafe_allow_html=True)
b_left, b_right = st.columns([3, 1])
with b_left:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:12px;padding:14px 0;">
      <span style="font-size:22px;">🎙️</span>
      <div>
        <div style="font-size:15px;font-weight:700;color:#e2e8f0;">오늘의 K-ENT 뉴스 브리핑</div>
        <div style="font-size:12px;color:#64748b;">Top 5 뉴스를 라디오 브리핑으로 들어보세요</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
with b_right:
    st.markdown("<div style='padding-top:10px;'>", unsafe_allow_html=True)
    if st.button("▶ 전체 브리핑 재생 (Top 5)", use_container_width=True):
        try:
            from gtts import gTTS
            import io
            script = "안녕하세요, 오늘의 K엔터 뉴스 브리핑입니다. "
            for n in NEWS[:5]:
                script += f"{n['rank']}위는 {n['artist']}입니다. {n['summary']} "
            tts = gTTS(text=script, lang="ko")
            fp = io.BytesIO(); tts.write_to_fp(fp); fp.seek(0)
            st.audio(fp, format="audio/mp3")
        except:
            st.info("pip install gTTS 후 사용 가능합니다.")
    st.markdown("</div>", unsafe_allow_html=True)
