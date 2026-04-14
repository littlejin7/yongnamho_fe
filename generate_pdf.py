"""워크프레임 PDF 생성 스크립트 (1회용)"""
from fpdf import FPDF
import os


class WorkframePDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font("Pretendard", "B", 22)
            self.cell(0, 14, "K-Enter News Dashboard", align="C", new_x="LMARGIN", new_y="NEXT")
            self.set_font("Pretendard", "", 12)
            self.set_text_color(100, 100, 100)
            self.cell(0, 8, "전체 워크프레임  |  2026.04.07 ~ 04.28", align="C", new_x="LMARGIN", new_y="NEXT")
            self.set_text_color(0, 0, 0)
            self.ln(4)
            self.set_draw_color(70, 130, 180)
            self.set_line_width(0.8)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Pretendard", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"- {self.page_no()} -", align="C")

    def section_title(self, title):
        self.ln(4)
        self.set_font("Pretendard", "B", 14)
        self.set_fill_color(70, 130, 180)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"  {title}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def sub_title(self, title):
        self.set_font("Pretendard", "B", 11)
        self.set_text_color(70, 130, 180)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def body_text(self, text):
        self.set_font("Pretendard", "", 10)
        self.multi_cell(0, 6, text)

    def bullet(self, text):
        self.set_font("Pretendard", "", 10)
        x = self.get_x()
        self.cell(6, 6, "•")
        self.multi_cell(0, 6, text)


def build_pdf():
    pdf = WorkframePDF()
    pdf.set_auto_page_break(auto=True, margin=20)

    # 한글 폰트 등록 (Windows 기본 맑은고딕 사용)
    font_dir = "C:/Windows/Fonts"
    # Pretendard가 있으면 사용, 없으면 맑은고딕
    if os.path.exists(os.path.join(font_dir, "malgun.ttf")):
        pdf.add_font("Pretendard", "", os.path.join(font_dir, "malgun.ttf"))
        pdf.add_font("Pretendard", "B", os.path.join(font_dir, "malgunbd.ttf"))
    pdf.set_font("Pretendard", "", 10)

    pdf.add_page()

    # ── 프로젝트 개요 ──
    pdf.section_title("프로젝트 개요")
    pdf.bullet("목표 : K-엔터 뉴스 크롤링 → LLM 요약/가공 → Streamlit 대시보드")
    pdf.bullet("기간 : 4/7(월) ~ 4/28(월)  |  평일 16일")
    pdf.bullet("팀 구성 : BE 3명  ·  FE 2명  ·  PE(프롬프트) 3명")
    pdf.ln(2)

    # ── 아키텍처 ──
    pdf.section_title("전체 아키텍처")
    arch = (
        "  [Tavily API 크롤링]\n"
        "         ↓\n"
        "  [raw_news — SQLite 저장]\n"
        "         ↓\n"
        "  [LLM 가공 — LangChain + Pydantic]\n"
        "         ↓\n"
        "  [processed_news — SQLite 저장]\n"
        "         ↓\n"
        "  [ChromaDB 임베딩 — RAG 검색]\n"
        "         ↓\n"
        "  [Streamlit 대시보드 + TTS]"
    )
    pdf.set_font("Pretendard", "", 10)
    pdf.multi_cell(0, 6, arch)
    pdf.ln(2)

    # ── PHASE 1 ──
    pdf.section_title("PHASE 1  |  데이터 파이프라인 뼈대  (4/7 ~ 4/11)")
    pdf.sub_title("▶ BE (백엔드)")
    pdf.bullet("BE-1 : 크롤러 안정화 (날짜 필터, 에러 핸들링, 도메인 확장)")
    pdf.bullet("BE-2 : DB 스키마 확정 + Pydantic 모델 정의 (입출력 검증)")
    pdf.bullet("BE-3 : LLM 가공 파이프라인 구축 (raw → processed 변환 로직)")
    pdf.ln(1)
    pdf.sub_title("▶ PE (프롬프트)")
    pdf.bullet("PE-1,2 : 뉴스 요약/분류 프롬프트 설계 및 테스트 (카테고리, 감성, 키워드)")
    pdf.bullet("PE-3 : 프롬프트 출력 → Pydantic 스키마 매핑 검증")
    pdf.ln(1)
    pdf.sub_title("▶ FE (프론트엔드)")
    pdf.bullet("FE-1,2 : Streamlit 페이지 구조 설계 + 와이어프레임 확정")
    pdf.ln(1)
    pdf.set_font("Pretendard", "B", 10)
    pdf.set_text_color(0, 128, 0)
    pdf.cell(0, 7, "✓ 체크포인트 : 크롤링 → 가공 → DB 저장 파이프라인이 돌아가는가?", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    # ── PHASE 2 ──
    pdf.section_title("PHASE 2  |  핵심 기능 개발  (4/14 ~ 4/18)")
    pdf.sub_title("▶ BE (백엔드)")
    pdf.bullet("BE-1 : 자동 크롤링 스케줄러 구현 (주기적 실행)")
    pdf.bullet("BE-2 : ChromaDB 연동 — processed_news 임베딩 저장")
    pdf.bullet("BE-3 : RAG 검색 API 구현 (질의 → 관련 뉴스 검색 → 답변 생성)")
    pdf.ln(1)
    pdf.sub_title("▶ PE (프롬프트)")
    pdf.bullet("PE-1,2 : RAG 질의 프롬프트 최적화 + 답변 생성 프롬프트")
    pdf.bullet("PE-3 : TTS용 텍스트 전처리 프롬프트 (자연스러운 읽기 스크립트)")
    pdf.ln(1)
    pdf.sub_title("▶ FE (프론트엔드)")
    pdf.bullet("FE-1 : 대시보드 메인 — 카테고리별 뉴스 카드, 감성/키워드 차트")
    pdf.bullet("FE-2 : 뉴스 상세 페이지 + RAG 검색 UI")
    pdf.ln(1)
    pdf.set_font("Pretendard", "B", 10)
    pdf.set_text_color(0, 128, 0)
    pdf.cell(0, 7, "✓ 체크포인트 : 대시보드에서 뉴스/차트가 보이고, RAG 검색이 되는가?", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    # ── PHASE 3 ──
    pdf.section_title("PHASE 3  |  부가기능 + 통합  (4/21 ~ 4/25)")
    pdf.sub_title("▶ BE (백엔드)")
    pdf.bullet("BE-1,2 : TTS 기능 구현 (API 연동 + 오디오 재생)")
    pdf.bullet("BE-3 : 전체 파이프라인 통합 테스트 + 버그 수정")
    pdf.ln(1)
    pdf.sub_title("▶ PE (프롬프트)")
    pdf.bullet("PE-1,2,3 : 전체 프롬프트 최종 튜닝 + 엣지케이스 대응")
    pdf.ln(1)
    pdf.sub_title("▶ FE (프론트엔드)")
    pdf.bullet("FE-1 : TTS 재생 버튼 UI + 대시보드 시각화 보강")
    pdf.bullet("FE-2 : 반응형 레이아웃 + CSS 디자인 마무리")
    pdf.ln(1)
    pdf.set_font("Pretendard", "B", 10)
    pdf.set_text_color(0, 128, 0)
    pdf.cell(0, 7, "✓ 체크포인트 : TTS 재생 되는가? 전체 흐름에 버그 없는가?", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    # ── PHASE 4 ──
    pdf.section_title("PHASE 4  |  최종 마무리  (4/28)")
    pdf.bullet("전원 : 최종 통합 테스트 + 버그 핫픽스 + 발표자료/데모 준비")
    pdf.ln(1)
    pdf.set_font("Pretendard", "B", 10)
    pdf.set_text_color(0, 128, 0)
    pdf.cell(0, 7, "✓ 체크포인트 : 데모 시연 가능한 상태인가?", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    # ── 파일 구조 ──
    pdf.section_title("예상 파일 구조")
    structure = (
        "P01/\n"
        "├── main.py                # 진입점\n"
        "├── crawler.py             # 크롤링 (완료)\n"
        "├── database.py            # DB 테이블 (완료)\n"
        "├── schemas.py             # Pydantic 입출력 모델\n"
        "├── processor.py           # LLM 가공 파이프라인\n"
        "├── vectorstore.py         # ChromaDB 임베딩/검색\n"
        "├── rag_search.py          # RAG 질의 처리\n"
        "├── tts.py                 # TTS 음성 변환\n"
        "├── scheduler.py           # 자동 크롤링 스케줄러\n"
        "├── app.py                 # Streamlit 메인 앱\n"
        "├── pages/                 # Streamlit 멀티페이지\n"
        "│   ├── dashboard.py\n"
        "│   ├── detail.py\n"
        "│   └── search.py\n"
        "└── prompts/               # 프롬프트 템플릿\n"
        "    ├── summary.py\n"
        "    ├── classify.py\n"
        "    └── tts_script.py"
    )
    pdf.set_font("Pretendard", "", 9)
    pdf.multi_cell(0, 5.5, structure)

    # ── 보류 기능 ──
    pdf.section_title("보류 기능 (여유 시 진행)")
    pdf.bullet("PDF 보고서 출력 — 프롬프트 복잡 + 오류 잦음, 추후 개발")
    pdf.bullet("이미지/웹툰 생성 — 퀄리티 유지 어려움, 시간 여유 시 재검토")

    # 저장
    output_path = "c:/Users/User/Desktop/P01/K-Enter_워크프레임.pdf"
    pdf.output(output_path)
    print(f"PDF 생성 완료: {output_path}")


if __name__ == "__main__":
    build_pdf()
