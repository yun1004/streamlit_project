import streamlit as st

st.title("🔮 MBTI 직업 & 궁합 분석기 🔮")

mbti_types = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", 
              "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

def get_mbti_info(mbti):
    info = {
        "ISTJ": {
            "job": "회계사 💼, 법률가 ⚖️, 경찰관 👮‍♂️",
            "match": "ESFP 🎭, ESTP 🏄‍♂️"
        },
        "ENFP": {
            "job": "작가 ✍️, 배우 🎭, 심리상담사 🧠",
            "match": "INTJ 🧠, INFJ 🔮"
        },
        # 나머지 MBTI 유형들에 대한 정보도 이와 같이 추가...
    }
    return info.get(mbti, {"job": "정보 없음", "match": "정보 없음"})

if st.button("분석하기 🚀"):
    info = get_mbti_info(selected_mbti)
    st.write(f"## {selected_mbti}님을 위한 분석 결과 🌟")
    st.write(f"### 추천 직업 💼")
    st.write(info["job"])
    st.write(f"### 잘 맞는 MBTI 💖")
    st.write(info["match"])
    st.write(f"""
    {selected_mbti}님! 당신은 독특한 성격의 소유자예요. 🌈 
    추천 직업들을 살펴보면, 당신의 강점을 잘 살릴 수 있는 분야들이죠. 
    이 직업들에서 당신의 {selected_mbti} 특성이 빛을 발할 거예요! ✨

    그리고 잘 맞는 MBTI 유형들과 만나면, 마치 퍼즐 조각이 맞춰지는 것처럼 
    환상의 팀워크를 이룰 수 있어요. 🧩 서로의 장단점을 보완하며 
    더 나은 결과를 만들어낼 수 있죠.

    하지만 기억하세요, 이건 단순한 가이드일 뿐이에요. 
    당신의 진정한 잠재력은 MBTI의 경계를 넘어서는 법이죠. 
    항상 새로운 도전을 두려워하지 마세요. 
    당신만의 특별한 재능으로 세상을 놀라게 할 준비가 되었나요? 🚀🌟
    """)

st.write("---")
st.write("© 2025 MBTI 분석기 | 당신의 잠재력을 발견하세요! 🔍✨")
