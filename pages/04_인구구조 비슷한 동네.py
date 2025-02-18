import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 데이터 불러오기 및 오류 처리
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("age2411.csv", encoding="utf-8")
        return df
    except FileNotFoundError:
        st.error("CSV 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
        return None
    except UnicodeDecodeError:
        st.error("CSV 파일 인코딩에 문제가 있습니다. UTF-8 인코딩을 확인하거나 다른 인코딩 방식을 시도해보세요.")
        return None

df = load_data()

if df is not None:
    # Streamlit 앱 제목 설정
    st.title("인구 구조 유사도 분석 🏘️")
    st.subheader("선택한 지역과 가장 비슷한 인구 구조를 가진 동네 비교")

    # 지역 선택을 위한 selectbox 생성
    available_areas = df['행정구역'].unique()
    selected_area = st.selectbox(
        "어느 동네와 비슷한 인구 구조를 찾고 싶으세요?",
        available_areas
    )

    # 연령대별 인구수 컬럼 추출
    age_cols = [col for col in df.columns if '2024년11월_계_' in col and '세' in col]

    # 선택된 지역의 인구 구조 데이터 추출
    selected_area_data = df[df['행정구역'] == selected_area][age_cols]

    # 유사도 계산을 위한 데이터 준비
    population_data = df[age_cols].fillna(0) # NaN 값을 0으로 채우기

    # 코사인 유사도 계산
    similarity_scores = cosine_similarity(selected_area_data, population_data)

    # 유사도 점수 DataFrame 생성
    similarity_df = pd.DataFrame(similarity_scores.T, index=df['행정구역'], columns=['유사도'])

    # 자기 자신을 제외하고 가장 유사한 지역 찾기
    similarity_df = similarity_df.drop(selected_area, errors='ignore')
    most_similar_area = similarity_df.sort_values(by='유사도', ascending=False).iloc[0]

    # 가장 유사한 지역의 인구 구조 데이터 추출
    most_similar_area_name = most_similar_area.name
    most_similar_area_data = df[df['행정구역'] == most_similar_area_name][age_cols]

    # 인구 구조 데이터 정제 함수
    def get_population_data(area_data, area_name):
        plot_df = pd.DataFrame({
            '연령': age_cols,
            '인구수': area_data.iloc[0].values,
            '지역': area_name
        })
        plot_df['연령'] = plot_df['연령'].str.replace('2024년11월_계_', '').str.replace('세', '').str.replace('_', ' ')
        return plot_df

    # 데이터 준비
    selected_plot_df = get_population_data(selected_area_data, selected_area)
    similar_plot_df = get_population_data(most_similar_area_data, most_similar_area_name)

    # 그래프 생성을 위한 데이터 병합
    combined_df = pd.concat([selected_plot_df, similar_plot_df])

    # 선 그래프 생성
    fig = px.line(combined_df, x='연령', y='인구수', color='지역',
                  title=f"{selected_area}와 가장 유사한 {most_similar_area_name} 인구 구조 비교")
    st.plotly_chart(fig, use_container_width=True)

    # 결과 요약
    st.subheader("결과 요약 📝")
    st.write(f"**{selected_area}**와 가장 유사한 지역: **{most_similar_area_name}** (유사도: {most_similar_area['유사도']:.4f})")

    # 추가 설명
    st.markdown("""
    **[인구 구조 분석](pplx://action/followup):**

    *   선택한 지역과 가장 유사한 지역의 인구 구조를 비교해 보세요.
    *   두 지역의 연령별 인구 분포가 어떻게 다른지 확인할 수 있습니다.

    **[프로젝트 더 알아보기](pplx://action/followup):**

    *   인구 구조 유사도를 활용하여, 비슷한 특징을 가진 지역들을 그룹으로 묶어볼 수 있습니다.
    *   지역 간 유사성을 기반으로, 새로운 상권이나 시설을 배치하는 아이디어를 생각해 볼 수 있습니다.
    """)
else:
    st.warning("데이터를 불러오는 데 실패했습니다. CSV 파일과 경로를 확인해주세요.")
