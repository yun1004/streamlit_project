import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.metrics.pairwise import cosine_similarity

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
    st.subheader("선택한 지역과 인구 비율이 가장 비슷한 동네 비교")

    # 지역 선택을 위한 selectbox 생성
    available_areas = df['행정구역'].unique()
    selected_area = st.selectbox(
        "어느 동네와 비슷한 인구 구조를 찾고 싶으세요?",
        available_areas
    )

    # 연령대별 인구수 컬럼 추출
    age_cols = [col for col in df.columns if '2024년11월_계_' in col and '세' in col]

    # 총 인구수 컬럼 추출
    total_population_col = '2024년11월_계_총인구수'

    # 데이터 타입 변경 및 NaN 처리
    df['총인구수'] = pd.to_numeric(df[total_population_col], errors='coerce')
    for col in age_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna(subset=age_cols + ['총인구수'])

    # 인구 비율 계산 함수
    def calculate_population_ratios(data):
        return data[age_cols].div(data['총인구수'], axis=0) * 100

    # 전체 지역의 인구 비율 계산
    population_ratio_data = calculate_population_ratios(df)

    # 선택된 지역의 인구 비율 데이터 추출
    selected_area_ratio_data = population_ratio_data[df['행정구역'] == selected_area]

    # 코사인 유사도 계산
    similarity_scores = cosine_similarity(selected_area_ratio_data, population_ratio_data)

    # 유사도 점수 DataFrame 생성
    similarity_df = pd.DataFrame(similarity_scores.T, index=df['행정구역'], columns=['유사도'])

    # 자기 자신을 제외하고 가장 유사한 지역 찾기
    similarity_df = similarity_df.drop(selected_area, errors='ignore')
    most_similar_area = similarity_df.sort_values(by='유사도', ascending=False).iloc[0]

    # 가장 유사한 지역의 인구 구조 데이터 추출
    most_similar_area_name = most_similar_area.name
    most_similar_area_data = df[df['행정구역'] == most_similar_area_name][age_cols]

    # 인구 구조 데이터 정제 함수 (인구 비율 사용)
    def get_population_data(area_data, area_name, age_cols):
        # 해당 지역의 총 인구수를 가져옴
        total_population = df[df['행정구역'] == area_name]['총인구수'].values[0]

        # 연령별 인구 비율 계산
        population_ratios = area_data[age_cols].iloc[0].values / total_population * 100

        plot_df = pd.DataFrame({
            '연령': age_cols,
            '인구 비율': population_ratios,  # 인구수 대신 비율 사용
            '지역': area_name
