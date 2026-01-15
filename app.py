import streamlit as st
import time

# --- 1. CẤU HÌNH TRANG & GIAO DIỆN ---
st.set_page_config(
    page_title="Nurse Path App",
    page_icon="👩‍⚕️",
    layout="centered"
)

# CSS tùy chỉnh để làm đẹp các khung nội dung (Card)
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0px 0px;
        font-weight: 600;
    }
    .job-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background-color: #f9f9f9;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.title("👩‍⚕️ NURSE PATH")
st.markdown("**Lộ trình nghề nghiệp & Giảm lo âu thất nghiệp cho sinh viên Điều dưỡng**")
st.divider()

# Tạo 4 Tab chính
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Đánh giá Năng lực", 
    "📅 Lộ trình 90 ngày", 
    "🏥 Việc làm", 
    "👤 Mentor & Hồ sơ"
])

# --- TAB 1: ĐÁNH GIÁ NĂNG LỰC ---
# Logic dựa trên [cite: 29] và [cite: 38]
with tab1:
    st.header("Kiểm tra mức độ sẵn sàng")
    st.write("Hãy chọn trung thực các kỹ năng bạn ĐÃ làm được:")

    # Phân nhóm kỹ năng để dễ nhìn hơn
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Chuyên môn")
        # Dựa trên [cite: 32]
        s1 = st.checkbox("Tiêm tĩnh mạch / Lấy ven")
        s2 = st.checkbox("Sơ cấp cứu cơ bản")
        s3 = st.checkbox("Đã từng đi thực tập lâm sàng")
        
    with col_b:
        st.subheader("Kỹ năng mềm & Chứng chỉ")
        # Dựa trên [cite: 36]
        s4 = st.checkbox("Giao tiếp & CS người bệnh")
        s5 = st.checkbox("Tin học văn phòng")
        s6 = st.checkbox("Tiếng Anh chuyên ngành")

    # Tính toán điểm số
    skills_list = [s1, s2, s3, s4, s5, s6]
    score = sum(skills_list)
    total = len(skills_list)
    percentage = int((score / total) * 100)

    st.divider()
    
    # Hiển thị kết quả sinh động bằng st.metric
    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric(label="Điểm sẵn sàng", value=f"{percentage}%")
    
    with c2:
        st.write("Tiến độ của bạn:")
        st.progress(percentage)

    # Logic lời khuyên [cite: 38, 39]
    if percentage < 50:
        st.error(f"⚠️ Mức độ: {percentage}% - Cần cố gắng nhiều!")
        st.write("👉 Bạn đang thiếu kỹ năng thực tế. Hãy chuyển sang Tab **Lộ trình** để bắt đầu giai đoạn 1 ngay.")
    elif percentage < 80:
        st.warning(f"ℹ️ Mức độ: {percentage}% - Khá ổn!")
        st.write("👉 Bạn cần trau dồi thêm 1 kỹ năng mũi nhọn để cạnh tranh tốt hơn.")
    else:
        st.success(f"✅ Mức độ: {percentage}% - Tuyệt vời!")
        st.write("👉 Hồ sơ của bạn rất mạnh. Hãy ửng tuyển ngay ở Tab **Việc làm**.")
        if st.button("Nhận huy hiệu sẵn sàng 🏅"):
            st.balloons()

# --- TAB 2: LỘ TRÌNH 90 NGÀY ---
# Logic dựa trên [cite: 20] và [cite: 40]
with tab2:
    st.header("Kế hoạch hành động 90 ngày")
    st.caption("Hoàn thành từng mục nhỏ để giảm bớt lo âu.")

    # Giai đoạn 1 [cite: 42]
    with st.expander("🌱 Giai đoạn 1 (0-30 ngày): CHUẨN BỊ", expanded=True):
        st.markdown("### 🎯 Mục tiêu: Hoàn thiện hồ sơ")
        c_1 = st.checkbox("Viết CV 1 trang đúng chuẩn ngành Y")
        c_2 = st.checkbox("Soạn Portfolio (Các ca bệnh tiêu biểu)") # [cite: 46]
        c_3 = st.checkbox("Học thêm 1 kỹ năng mũi nhọn") # [cite: 50]
        
        if c_1 and c_2 and c_3:
            st.success("Tuyệt vời! Bạn đã xong giai đoạn khởi động.")

    # Giai đoạn 2 [cite: 57]
    with st.expander("🚀 Giai đoạn 2 (31-60 ngày): TIẾP CẬN"):
        st.markdown("### 🎯 Mục tiêu: Kết nối & Phỏng vấn")
        st.checkbox("Liên hệ lại nơi thực tập cũ để xin việc") # [cite: 58]
        st.checkbox("Luyện bộ câu hỏi phỏng vấn (Tình huống, Đạo đức)") # [cite: 59]
        st.checkbox("Tham gia các hội nhóm tuyển dụng điều dưỡng")

    # Giai đoạn 3 [cite: 65]
    with st.expander("⭐ Giai đoạn 3 (61-90 ngày): ỔN ĐỊNH"):
        st.markdown("### 🎯 Mục tiêu: Ứng tuyển thực tế")
        st.checkbox("Gửi hồ sơ đến 5 Bệnh viện/Phòng khám") # 
        st.checkbox("Đi phỏng vấn thực tế")
        st.checkbox("Điều chỉnh lại CV sau mỗi lần phỏng vấn") # [cite: 67]

# --- TAB 3: VIỆC LÀM PHÙ HỢP ---
# Logic dựa trên [cite: 69, 70]
with tab3:
    st.header("Cơ hội việc làm cho sinh viên mới")
    st.info("Danh sách này ưu tiên các nơi chấp nhận đào tạo lại.")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 🏥 Bệnh viện Quận A")
            st.markdown("**Vị trí:** Điều dưỡng Đa khoa")
            st.markdown("📍 **Khu vực:** TP.HCM")
            st.markdown("💰 **Lương:** Thỏa thuận")
            st.caption("Yêu cầu: Tốt nghiệp CĐ/ĐH, nhanh nhẹn.")
            if st.button("Ứng tuyển BV A"):
                st.toast("Đã lưu hồ sơ ứng tuyển!")

    with col2:
        with st.container(border=True):
            st.markdown("### 🏥 Phòng khám Tư nhân B")
            st.markdown("**Vị trí:** Chăm sóc tại nhà")
            st.markdown("📍 **Khu vực:** Hà Nội")
            st.markdown("💰 **Lương:** 8 - 10 triệu")
            st.caption("Yêu cầu: Có xe máy, chịu khó.")
            if st.button("Ứng tuyển PK B"):
                st.toast("Đã lưu hồ sơ ứng tuyển!")

# --- TAB 4: HỒ SƠ & MENTOR ---
# Logic dựa trên [cite: 91, 92]
with tab4:
    st.header("Kết nối Chuyên gia")
    st.write("Đặt câu hỏi để được giải đáp online mà không cần đi xa.")

    with st.form("mentor_form"):
        st.text_input("Họ tên của bạn:")
        topic = st.selectbox("Chủ đề bạn quan tâm:", ["Sửa CV", "Kỹ năng phỏng vấn", "Chuyên môn lâm sàng"])
        question = st.text_area("Nội dung câu hỏi:")
        
        submitted = st.form_submit_button("Gửi câu hỏi")
        if submitted:
            st.success(f"Đã gửi câu hỏi về chủ đề '{topic}'! Mentor sẽ trả lời trong 24h.")
