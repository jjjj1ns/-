import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="훈민정음 리롤 게임",
    page_icon="🟥",
    layout="centered"
)

# 초성 리스트 (된소리 제거)
chosung_list = [
    'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ',
    'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# 이름 리스트
names = ['안', '김', '최', '주', '임', '이']

# 세션 상태 초기화
for name in names:
    if f'count_{name}' not in st.session_state:
        st.session_state[f'count_{name}'] = 0

# 타이틀
st.markdown("<h1 style='text-align: center;'>🟥 훈민정음 게임</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🎲 아래 버튼을 눌러 무작위 초성 2개를 뽑아보세요!</p>", unsafe_allow_html=True)

# 리롤 버튼
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    reroll = st.button("🔁 리롤", use_container_width=True)

# 초성 출력
if reroll:
    c1 = random.choice(chosung_list)
    c2 = random.choice(chosung_list)

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🎯 오늘의 초성</h3>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"<div style='font-size: 60px; text-align: center;'>{c1}</div>", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"<div style='font-size: 60px; text-align: center;'>{c2}</div>", unsafe_allow_html=True)

    st.markdown("---")

# 카운터 영역
st.markdown("<h4 style='text-align: center;'>👥 인원 카운트</h4>", unsafe_allow_html=True)

# 각 이름별로 세로 배치
for name in names:
    col1, col2, col3 = st.columns([1, 1, 1.5])

    # 이름 표시
    with col1:
        st.markdown(f"<div style='font-size: 24px; text-align: center; font-weight: bold;'>{name}</div>", unsafe_allow_html=True)

    # 숫자 표시
    with col2:
        st.markdown(f"<div style='font-size: 36px; text-align: center;'>{st.session_state[f'count_{name}']}</div>", unsafe_allow_html=True)

    # 버튼 세트 (세로 정렬)
    with col3:
        plus = st.button(f"➕1", key=f"plus_{name}")
        minus = st.button(f"➖1", key=f"minus_{name}")
        if plus:
            st.session_state[f'count_{name}'] += 1
        if minus:
            st.session_state[f'count_{name}'] -= 1
