import streamlit as st
import random

st.set_page_config(page_title="훈민정음 게임", page_icon="🟥", layout="centered")

# 초성 리스트 (된소리 제거)
chosung_list = [
    'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ',
    'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

names = ['안', '김', '최', '주', '임', '이']

# 초기화
for name in names:
    st.session_state.setdefault(f'count_{name}', 0)

# 타이틀
st.title("🟥 훈민정음 게임")
st.markdown("🎲 무작위 초성 2개를 뽑아보세요!")

# 리롤 버튼
if st.button("🔁 리롤"):
    st.session_state['chosung1'] = random.choice(chosung_list)
    st.session_state['chosung2'] = random.choice(chosung_list)

# 초성 출력 (수정된 부분)
if 'chosung1' in st.session_state and 'chosung2' in st.session_state:
    st.markdown("---")
    st.markdown("### 🎯 오늘의 초성")

    # ✅ 수정: 가로 정렬을 위한 HTML + CSS
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center; gap: 40px; margin-top: 20px;'>
            <div style='font-size: 60px;'>{st.session_state['chosung1']}</div>
            <div style='font-size: 60px;'>{st.session_state['chosung2']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

# 👥 인원 카운트 UI
st.markdown("### 👥 인원 카운트")

# 버튼 클릭 먼저 처리
for name in names:
    plus_key = f"{name}_plus"
    minus_key = f"{name}_minus"

    if st.session_state.get(plus_key):
        st.session_state[f'count_{name}'] += 1
        st.session_state[plus_key] = False  # reset

    if st.session_state.get(minus_key):
        st.session_state[f'count_{name}'] -= 1
        st.session_state[minus_key] = False  # reset

# 실제 UI 출력
for name in names:
    col1, col2, col3 = st.columns([1.5, 1, 2])  # 이름, 숫자, 버튼

    with col1:
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:20px'>{name}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div style='font-size:32px; text-align:center'>{st.session_state[f'count_{name}']}</div>", unsafe_allow_html=True)

    with col3:
        st.checkbox("➕1", key=f"{name}_plus")
        st.checkbox("➖1", key=f"{name}_minus")
