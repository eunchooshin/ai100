import streamlit as st

st.title('동물 이미지 찾아주기 😎')

name = st.text_input('영어로 동물을 입력하세요')

if st.button('찾아보기'):
    url = 'https://edu.spartacodingclub.kr/random/?'+name
    st.image(url)

key = st.secrets['API_KEY']
st.write(key)
