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

# --- TAB 1: ĐÁNH GIÁ NĂNG LỰC CHUYÊN SÂU ---
with tab1:
    st.header("📋 Đánh giá Năng lực Điều dưỡng Toàn diện")
    st.markdown("Hệ thống đánh giá dựa trên chuẩn năng lực cơ bản cho sinh viên sắp tốt nghiệp.")
    
    with st.form("assessment_form"):
        # --- PHẦN 1: KỸ NĂNG LÂM SÀNG & MỀM [cite: 32, 33] ---
        st.subheader("1. Kỹ năng Lâm sàng & Thực hành")
        st.caption("Bạn tự tin thực hiện thành thạo những kỹ thuật nào dưới đây?")
        
        clinical_skills = st.multiselect(
            "Chọn các kỹ năng bạn đã làm được:",
            [
                "Tiêm tĩnh mạch / Lấy ven", 
                "Tiêm bắp / Tiêm dưới da",
                "Đặt thông tiểu / Thông dạ dày",
                "Thay băng / Cắt chỉ vết thương",
                "Sơ cấp cứu cơ bản (CPR)",
                "Đo dấu hiệu sinh tồn (Mạch, Nhiệt, HA)",
                "Ghi chép hồ sơ bệnh án",
                "Sử dụng máy móc y tế cơ bản"
            ]
        )
        
        weakness = st.text_input("Điểm bạn thấy mình còn yếu nhất cần cải thiện? ", 
                                 placeholder="Ví dụ: Giao tiếp với người nhà bệnh nhân, Kỹ năng lấy ven khó...")

        # --- PHẦN 2: KINH NGHIỆM THỰC TẬP [cite: 34] ---
        st.divider()
        st.subheader("2. Kinh nghiệm Thực tập")
        internship_place = st.text_input("Bạn đã/đang thực tập tại đâu? [cite: 34]", 
                                         placeholder="Ví dụ: Bệnh viện Chợ Rẫy, BV Đa khoa Tỉnh...")
        internship_duration = st.slider("Thời gian thực tập tích lũy (tháng):", 0, 12, 3)

        # --- PHẦN 3: ĐỊNH HƯỚNG NGHỀ NGHIỆP [cite: 35] ---
        st.divider()
        st.subheader("3. Định hướng & Mối quan tâm")
        st.caption("Lựa chọn này sẽ giúp App đưa ra lộ trình phù hợp nhất với bạn.")
        
        career_goal = st.selectbox(
            "Bạn quan tâm/dự định làm việc ở môi trường nào? [cite: 35]",
            [
                "Lâm sàng chuyên khoa (Bệnh viện lớn)",
                "Phòng khám tư nhân / Thẩm mỹ",
                "Chăm sóc tại nhà (Home Care)",
                "Làm việc tại nước ngoài (Đức, Nhật...)"
            ]
        )

        # --- PHẦN 4: CHỨNG CHỈ & BẰNG CẤP [cite: 36] ---
        st.divider()
        st.subheader("4. Chứng chỉ bổ trợ")
        certificates = st.multiselect(
            "Bạn đã có những chứng chỉ nào? [cite: 36]",
            [
                "Chứng chỉ Tin học văn phòng",
                "Chứng chỉ Ngoại ngữ (Tiếng Anh/Đức/Nhật)",
                "Chứng chỉ Ứng cứu khẩn cấp / CPR",
                "Chứng chỉ Hành nghề (đã có hoặc đang đợi)",
                "Chứng chỉ Kỹ năng mềm"
            ]
        )

        submit_btn = st.form_submit_button("📊 PHÂN TÍCH KẾT QUẢ NGAY")

    # --- XỬ LÝ LOGIC ĐÁNH GIÁ [cite: 37, 38, 39] ---
    if submit_btn:
        st.divider()
        st.markdown("### 📢 KẾT QUẢ PHÂN TÍCH CỦA BẠN")
        
        # 1. Tính điểm cơ bản
        score = 0
        total_criteria = 10 # Giả định thang điểm 10
        
        # Điểm kỹ năng (Tối đa 5 điểm)
        if len(clinical_skills) > 5: score += 5
        elif len(clinical_skills) > 3: score += 3
        else: score += 1
        
        # Điểm thực tập (Tối đa 2 điểm)
        if internship_duration >= 3: score += 2
        elif internship_duration > 0: score += 1
        
        # Điểm chứng chỉ (Tối đa 3 điểm)
        if len(certificates) >= 3: score += 3
        elif len(certificates) >= 1: score += 1

        # 2. Logic kiểm tra điều kiện đặc biệt (Dựa trên Định hướng [cite: 35])
        missing_critical = []
        
        # Nếu chọn đi nước ngoài mà thiếu ngoại ngữ
        if "Làm việc tại nước ngoài" in career_goal:
            has_language = any("Ngoại ngữ" in c for c in certificates)
            if not has_language:
                score = min(score, 6) # Bị trừ điểm nặng
                missing_critical.append("Thiếu Chứng chỉ Ngoại ngữ (Bắt buộc cho hướng đi Nước ngoài)")

        # Nếu chọn Bệnh viện lớn mà kỹ năng ít
        if "Lâm sàng chuyên khoa" in career_goal and len(clinical_skills) < 4:
            missing_critical.append("Kỹ năng lâm sàng còn mỏng so với yêu cầu Bệnh viện lớn")

        # 3. Tính phần trăm hiển thị [cite: 38]
        percentage = int((score / total_criteria) * 100)
        
        # Hiển thị mức độ sẵn sàng
        st.progress(percentage)
        
        if percentage >= 95:
            st.success(f"🌟 MỨC ĐỘ SẴN SÀNG: {percentage}% - XUẤT SẮC")
            st.write("Bạn đã sẵn sàng ứng tuyển vào các vị trí tốt nhất.")
        elif percentage >= 80:
            st.info(f"✅ MỨC ĐỘ SẴN SÀNG: {percentage}% - KHÁ TỐT")
            st.write("Bạn có nền tảng tốt, chỉ cần bổ sung thêm các yếu tố phụ.")
        elif percentage >= 60:
            st.warning(f"⚠️ MỨC ĐỘ SẴN SÀNG: {percentage}% - TRUNG BÌNH")
            st.write("Bạn cần nỗ lực nhiều trong 90 ngày tới để tự tin hơn.")
        else:
            st.error(f"🚨 MỨC ĐỘ SẴN SÀNG: {percentage}% - CẦN CẢI THIỆN GẤP")
            st.write("Bạn đang thiếu nhiều yếu tố nền tảng quan trọng.")

        # 4. Đưa ra lời khuyên cụ thể (Kế hoạch tiếp theo) 
        with st.container(border=True):
            st.subheader("💡 Kế hoạch hành động đề xuất cho bạn:")
            
            # Lời khuyên dựa trên cái còn yếu
            if weakness:
                st.write(f"- **Ưu tiên số 1:** Tìm tài liệu hoặc nhờ Mentor hướng dẫn khắc phục điểm yếu: *{weakness}*.")
            
            # Lời khuyên dựa trên cái thiếu
            if missing_critical:
                for item in missing_critical:
                    st.write(f"- ❗ **Bổ sung gấp:** {item}")
            elif len(certificates) == 0:
                st.write("- 🎓 Bạn nên thi lấy ít nhất 1 chứng chỉ (Tin học hoặc Ngoại ngữ) để làm đẹp hồ sơ.")
                
            st.write(f"- 🏥 **Định hướng {career_goal}:** Hãy sang Tab 'Việc làm' để xem các yêu cầu cụ thể của vị trí này.")

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

