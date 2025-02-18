import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 불러오기
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("age2411.csv", encoding="utf-8")
        return df
    except UnicodeDecodeError:
        st.error("CSV 파일 인코딩에 문제가 있습니다. UTF-8 인코딩을 확인하거나 다른 인코딩 방식을 시도해보세요.")
        return None
    except FileNotFoundError:
        st.error("CSV 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
        return None

df = load_data()

if df is not None:
    # Streamlit 앱 제목 설정
    st.title("우리 동네 인구 탐험대! 🏡")
    st.subheader("궁금한 동네를 선택하면 인구 구조를 보여줄게!")

    # 지역 선택을 위한 selectbox 생성
    selected_area = st.selectbox(
        "어느 동네의 인구 구조가 궁금한가요?",
        df['행정구역'].unique()
    )

    # 선택된 지역의 데이터 필터링
    filtered_df = df[df['행정구역'] == selected_area]

    # 연령별 인구수 데이터 추출 (정규 표현식 사용)
    import re
    age_columns = [col for col in df.columns if re.match(r'2024년11월_계_\d+세', col)]
    age_data = filtered_df[age_columns].iloc[0]

    # 데이터프레임 생성 (Plotly Express 호환용)
    plot_df = pd.DataFrame({'연령': age_data.index, '인구수': age_data.values})
    plot_df['연령'] = plot_df['연령'].str.replace('2024년11월_계_', '').str.replace('세', '')

    # 막대 그래프 생성
    fig = px.bar(plot_df, x='연령', y='인구수', title=f'{selected_area} 인구 구조')
    st.plotly_chart(fig, use_container_width=True)

    # 추가 설명
    st.markdown("""
    **인구 구조 분석:**

    *   그래프를 통해 우리 동네의 연령별 인구 분포를 확인할 수 있어요.
    *   어린이, 청소년, 어른, 어르신 중 누가 가장 많은지 비교해 보세요.
    *   우리 동네의 인구 구조는 다른 동네와 어떻게 다른지 생각해 보세요.

    **프로젝트 더 알아보기:**

    *   이 데이터를 활용해서 우리 동네에 필요한 시설이나 서비스는 무엇이 있을지 아이디어를 내볼 수 있어요.
    *   인구 변화 추이를 조사해서 우리 동네의 미래 모습을 예측해 볼 수도 있답니다!
    """)
else:
    st.warning("데이터를 불러오는 데 실패했습니다. requirements.txt 파일과 CSV 파일 설정을 확인해주세요.")
