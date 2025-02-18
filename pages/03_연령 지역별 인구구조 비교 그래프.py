import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("age2411.csv", encoding="utf-8")
    return df

df = load_data()

# Streamlit 앱 제목 설정
st.title("지역별 인구 구조 분석 📊")
st.subheader("선택한 연령대의 비율이 가장 높은/낮은 지역 비교")

# 연령 선택을 위한 selectbox 생성
age_options = [col.replace('2024년11월_계_', '').replace('세', '').replace('_', ' ') for col in df.columns if '2024년11월_계_' in col and '세' in col]
selected_age = st.selectbox(
    "어떤 연령대의 비율을 비교하고 싶으세요?",
    age_options
)

# 선택한 연령대의 컬럼명 찾기
selected_age_col = f"2024년11월_계_{selected_age.replace(' ', '_')}세"

# 선택한 연령대의 비율 계산
total_population_col = '2024년11월_계_총인구수'
df['비율'] = df[selected_age_col] / df[total_population_col] * 100

# 비율이 가장 높은/낮은 지역 찾기
max_ratio_area = df.loc[df['비율'].idxmax()]
min_ratio_area = df.loc[df['비율'].idxmin()]

# 인구 구조 데이터 추출 함수
def get_population_data(area_data):
    age_cols = [col for col in df.columns if '2024년11월_계_' in col and '세' in col]
    population_data = area_data[age_cols]
    plot_df = pd.DataFrame({'연령': population_data.index, '인구수': population_data.values})
    plot_df['연령'] = plot_df['연령'].str.replace('2024년11월_계_', '').str.replace('세', '').str.replace('_', ' ')
    return plot_df

# 데이터 준비
max_ratio_df = get_population_data(max_ratio_area)
min_ratio_df = get_population_data(min_ratio_area)

# 그래프 생성을 위한 데이터 병합
max_ratio_df['지역'] = f"{max_ratio_area['행정구역']} (최고 비율)"
min_ratio_df['지역'] = f"{min_ratio_area['행정구역']} (최저 비율)"
combined_df = pd.concat([max_ratio_df, min_ratio_df])

# 선 그래프 생성
fig = px.line(combined_df, x='연령', y='인구수', color='지역',
              title=f"{selected_age} 비율이 가장 높은/낮은 지역 인구 구조 비교")
st.plotly_chart(fig, use_container_width=True)

# 결과 요약
st.subheader("결과 요약 📝")
st.write(f"**{selected_age}** 비율이 가장 높은 지역: **{max_ratio_area['행정구역']}** ({max_ratio_area['비율']:.2f}%)")
st.write(f"**{selected_age}** 비율이 가장 낮은 지역: **{min_ratio_area['행정구역']}** ({min_ratio_area['비율']:.2f}%)")
