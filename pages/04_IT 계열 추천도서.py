import streamlit as st

st.title("IT 계열 진학 희망 고등학생을 위한 추천도서 10선")

books = [
    {"title": "처음 떠나는 컴퓨터과학 산책", "author": "저자 미상", "description": "컴퓨터 과학의 기초를 쉽게 설명하는 입문서입니다."},
    {"title": "시간순삭 파이썬", "author": "저자 미상", "description": "실용적인 문제를 통해 파이썬을 배우는 10대를 위한 책입니다."},
    {"title": "시간순삭 인공지능 with 스크래치", "author": "저자 미상", "description": "스크래치를 통해 인공지능의 기본 개념을 배웁니다."},
    {"title": "컴퓨터과학 알고리즘 스크래치 3.0", "author": "저자 미상", "description": "스크래치를 이용해 알고리즘을 학습할 수 있는 책입니다."},
    {"title": "비버챌린지 2(고등학생용)", "author": "저자 미상", "description": "컴퓨팅 사고력을 기르는 문제집입니다."},
    {"title": "거의 모든 IT의 역사", "author": "정지훈", "description": "IT 산업의 역사를 통해 미래를 전망합니다."},
    {"title": "알고리즘, 인생을 계산하다", "author": "브라이언 크리스천", "description": "일상 속 알고리즘의 영향을 살펴봅니다."},
    {"title": "1일 1로그 100일 완성 IT 지식", "author": "브라이언 커니핸", "description": "IT 기초 지식을 100일 동안 학습합니다."},
    {"title": "구글 엔지니어는 이렇게 일한다", "author": "타이터스 원터스", "description": "실제 IT 기업의 업무 방식을 소개합니다."},
    {"title": "AI 최강의 수업", "author": "김진형", "description": "인공지능의 현재와 미래에 대해 알아봅니다."}
]

for i, book in enumerate(books, 1):
    st.subheader(f"{i}. {book['title']}")
    st.write(f"저자: {book['author']}")
    st.write(book['description'])
    st.write("---")

st.info("이 책들은 IT 기초, 프로그래밍, 인공지능, 알고리즘 등 다양한 주제를 다루고 있습니다. 관심 있는 분야의 책부터 시작해보세요!")
