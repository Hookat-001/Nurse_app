import streamlit as st

st.title("Tool Mã Hóa Online")
text_input = st.text_input("Nhập nội dung:")

if st.button("Mã hóa ngay"):
    # Giả lập mã hóa đơn giản (đảo ngược chuỗi)
    # Bạn thay logic của bạn vào đây
    result = text_input[::-1] 
    st.success(f"Kết quả: {result}")
    st.balloons() # Hiệu ứng bóng bay cho vui