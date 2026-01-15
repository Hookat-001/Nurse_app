import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Nurse Path", page_icon="👩‍⚕️")

# Tiêu đề
st.title("👩‍⚕️ NURSE PATH - Lộ Trình Nghề Nghiệp")
st.write("Giải pháp giảm lo âu thất nghiệp cho sinh viên Điều dưỡng")

# Tạo 4 Tab chức năng như thiết kế của bạn
tab1, tab2, tab3, tab4 = st.tabs(["📊 Đánh giá", "📅 Lộ trình 90 ngày", "🏥 Việc làm", "👤 Hồ sơ"])

# --- TAB 1: ĐÁNH GIÁ NĂNG LỰC ---
with tab1:
    st.header("Kiểm tra mức độ sẵn sàng")
    st.write("Chọn những kỹ năng bạn ĐÃ làm được:")
    
    # Danh sách kỹ năng dựa trên tài liệu [cite: 32, 36]
    skills = {
        "Tiêm tĩnh mạch / Lấy ven": False,
        "Sơ cấp cứu cơ bản": False,
        "Giao tiếp & CS người bệnh": False,
        "Tin học văn phòng": False,
        "Tiếng Anh chuyên ngành": False,
        "Đã từng đi thực tập lâm sàng": False
    }

    # Tạo checkbox
    score = 0
    total = len(skills)
    
    # Hiển thị checkbox và tính điểm
    selected_skills = []
    for skill in skills.keys():
        if st.checkbox(skill):
            score += 1
            selected_skills.append(skill)
            
    # Tính phần trăm 
    percentage = int((score / total) * 100)
    
    st.divider()
    st.subheader(f"Mức độ sẵn sàng của bạn: {percentage}%")
    st.progress(percentage)

    # Logic đưa ra lời khuyên [cite: 39]
    if percentage < 50:
        st.warning("⚠️ Bạn còn thiếu nhiều kỹ năng thực tế. Hãy qua Tab 'Lộ trình' để xem kế hoạch bổ sung ngay!")
    elif percentage < 80:
        st.info("ℹ️ Tạm ổn, nhưng cần trau dồi thêm kỹ năng mũi nhọn.")
    else:
        st.success("✅ Tuyệt vời! Bạn đã sẵn sàng ứng tuyển.")

# --- TAB 2: LỘ TRÌNH 90 NGÀY ---
with tab2:
    st.header("Kế hoạch hành động 90 ngày")
    st.write("Làm theo từng tuần để giảm lo âu thất nghiệp [cite: 20]")

    # Giai đoạn 1 [cite: 42]
    with st.expander("Giai đoạn 1 (0-30 ngày): CHUẨN BỊ", expanded=True):
        st.write("Mục tiêu: Hoàn thiện hồ sơ & Kỹ năng nền")
        st.checkbox("Hoàn thiện CV 1 trang đúng ngành [cite: 45]")
        st.checkbox("Xây dựng Portfolio (Ca bệnh tiêu biểu) [cite: 46]")
        st.checkbox("Chọn 1 kỹ năng mũi nhọn để học thêm [cite: 50]")
        st.info("💡 Mẹo: Xin nhận xét từ người hướng dẫn thực tập để cải thiện Portfolio.")

    # Giai đoạn 2 [cite: 57]
    with st.expander("Giai đoạn 2 (31-60 ngày): TIẾP CẬN"):
        st.write("Mục tiêu: Kết nối & Luyện phỏng vấn")
        st.checkbox("Xin việc tại nơi thực tập cũ [cite: 58]")
        st.checkbox("Luyện tập trả lời phỏng vấn (Giới thiệu, Tình huống) [cite: 59]")
        st.checkbox("Tìm hiểu về Đạo đức nghề nghiệp [cite: 62]")

    # Giai đoạn 3 [cite: 65]
    with st.expander("Giai đoạn 3 (61-90 ngày): ỔN ĐỊNH"):
        st.write("Mục tiêu: Ứng tuyển thực tế")
        st.checkbox("Gửi hồ sơ đến các Bệnh viện/Phòng khám [cite: 69]")
        st.checkbox("Đi phỏng vấn thực tế")
        st.checkbox("Điều chỉnh hồ sơ nếu chưa đạt [cite: 67]")

# --- TAB 3: VIỆC LÀM PHÙ HỢP ---
with tab3:
    st.header("Việc làm gợi ý cho sinh viên mới")
    st.write("Nơi chấp nhận sinh viên chưa có nhiều kinh nghiệm [cite: 70]")
    
    # Giả lập danh sách việc làm giống hình vẽ
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("🏥 Bệnh viện Quận A")
        st.write("**Vị trí:** Điều dưỡng đa khoa")
        st.write("**Yêu cầu:** Tốt nghiệp CĐ/ĐH, nhanh nhẹn.")
        st.button("Ứng tuyển ngay", key="btn1")

    with col2:
        st.info("🏥 Phòng khám Tư nhân B")
        st.write("**Vị trí:** Điều dưỡng chăm sóc tại nhà")
        st.write("**Yêu cầu:** Có xe máy, chịu khó.")
        st.button("Ứng tuyển ngay", key="btn2")

# --- TAB 4: HỒ SƠ & MENTOR ---
with tab4:
    st.header("Kết nối Mentor")
    st.write("Hỏi đáp online với chuyên gia [cite: 91]")
    
    text_question = st.text_area("Đặt câu hỏi cho Mentor:")
    if st.button("Gửi câu hỏi"):
        st.success("Câu hỏi đã được gửi! Chuyên gia sẽ trả lời trong 24h.")
