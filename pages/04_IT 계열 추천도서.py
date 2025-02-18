import streamlit as st

# 책 정보를 담은 딕셔너리
books = {
    "처음 떠나는 컴퓨터과학 산책": {
        "출판연도": "2023",
        "출판사": "한빛미디어",
        "저자": "이광근",
        "요약": "컴퓨터 과학의 핵심 개념을 쉽고 재미있게 설명하는 입문서입니다.",
        "평점": "4.5/5"
    },
    "시간순삭 파이썬": {
        "출판연도": "2022",
        "출판사": "길벗",
        "저자": "박응용",
        "요약": "10대를 위한 파이썬 프로그래밍 입문서로, 실용적인 예제를 통해 학습합니다.",
        "평점": "4.3/5"
    },
    "거의 모든 IT의 역사": {
        "출판연도": "2021",
        "출판사": "메디치미디어",
        "저자": "정지훈",
        "요약": "IT 산업의 발전 과정과 주요 사건들을 흥미롭게 다룬 책입니다.",
        "평점": "4.7/5"
    },
    "구글 엔지니어는 이렇게 일한다": {
        "출판연도": "2020",
        "출판사": "한빛미디어",
        "저자": "타이터스 원터스",
        "요약": "구글의 소프트웨어 엔지니어링 문화와 실제 업무 방식을 소개합니다.",
        "평점": "4.6/5"
    },
    "AI 최강의 수업": {
        "출판연도": "2024",
        "출판사": "매일경제신문사",
        "저자": "김진형",
        "요약": "인공지능의 현재와 미래, 그리고 우리 삶에 미칠 영향을 다룹니다.",
        "평점": "4.8/5"
    },
    "Between Humanities and the Digital": {
        "출판연도": "2015",
        "출판사": "MIT Press",
        "저자": "Patrik Svensson, David Theo Goldberg",
        "요약": "디지털 시대의 인문학과 기술의 접점을 탐구합니다.",
        "평점": "4.2/5"
    },
    "Philosophy in Culture: A Cross-Cultural Perspective": {
        "출판연도": "2016",
        "출판사": "Springer",
        "저자": "Mbih J. Tosam, Peter Takov",
        "요약": "문화와 기술의 철학적 접근을 다양한 관점에서 살펴봅니다.",
        "평점": "4.0/5"
    },
    "The Age of A.I.": {
        "출판연도": "2021",
        "출판사": "Little, Brown and Company",
        "저자": "Henry Kissinger, Eric Schmidt, Daniel Huttenlocher",
        "요약": "AI가 인류의 미래에 미칠 영향을 다각도로 분석합니다.",
        "평점": "4.4/5"
    },
    "Everyday Chaos": {
        "출판연도": "2019",
        "출판사": "Harvard Business Review Press",
        "저자": "David Weinberger",
        "요약": "복잡성과 기술이 현대 사회에 미치는 영향을 탐구합니다.",
        "평점": "4.3/5"
    },
    "You Are Not a Gadget": {
        "출판연도": "2010",
        "출판사": "Knopf",
        "저자": "Jaron Lanier",
        "요약": "디지털 기술이 인간성에 미치는 영향에 대한 비판적 시각을 제시합니다.",
        "평점": "4.1/5"
    },
    "Alone Together": {
        "출판연도": "2011",
        "출판사": "Basic Books",
        "저자": "Sherry Turkle",
        "요약": "기술 발전이 인간 관계에 미치는 영향을 심도 있게 분석합니다.",
        "평점": "4.2/5"
    },
    "Weapons of Math Destruction": {
        "출판연도": "2016",
        "출판사": "Crown",
        "저자": "Cathy O'Neil",
        "요약": "빅데이터와 알고리즘이 사회 불평등에 미치는 영향을 다룹니다.",
        "평점": "4.5/5"
    },
    "Here Comes Everybody": {
        "출판연도": "2008",
        "출판사": "Penguin Press",
        "저자": "Clay Shirky",
        "요약": "인터넷이 가져온 사회적 조직의 변화를 탐구합니다.",
        "평점": "4.3/5"
    },
    "The Myth of Artificial Intelligence": {
        "출판연도": "2021",
        "출판사": "Belknap Press",
        "저자": "Erik J. Larson",
        "요약": "AI의 현재 한계와 미래 가능성에 대한 비판적 분석을 제공합니다.",
        "평점": "4.4/5"
    },
    "Business Meets the Humanities": {
        "출판연도": "2023",
        "출판사": "Springer",
        "저자": "Martina Skrubbeltrang Mahnke 외",
        "요약": "비즈니스와 인문학의 융합을 통한 새로운 가치 창출을 탐구합니다.",
        "평점": "4.1/5"
    },
    "The Age of Algorithms": {
        "출판연도": "2020",
        "출판사": "Cambridge University Press",
        "저자": "Serge Abiteboul, Gilles Dowek",
        "요약": "알고리즘이 현대 사회에 미치는 영향을 종합적으로 분석합니다.",
        "평점": "4.3/5"
    },
    "인공지능의 철학": {
