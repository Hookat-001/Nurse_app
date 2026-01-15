import streamlit as st
import time

# --- 1. CẤU HÌNH TRANG & GIAO DIỆN ---
st.set_page_config(
    page_title="Nurse Path App",
    page_icon="👩‍⚕️",
    layout="wide", # Chuyển sang wide để có không gian cho Sidebar và Workshop
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh giao diện
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; }
    .job-card { padding: 15px; border-radius: 8px; background-color: #f0f2f6; margin-bottom: 10px; }
    /* Highlight cho phần Test ở cuối */
    .test-feedback { border: 2px dashed #ff4b4b; padding: 10px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR: HƯỚNG DẪN & GIÁ TRỊ CỐT LÕI (BỔ SUNG) ---
# Phần này giải quyết [cite: 83-99]
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=100)
    st.title("NURSE PATH")
    st.caption("Giải pháp giảm lo âu thất nghiệp cho sinh viên Điều dưỡng")
    
    st.divider()
    
    # Hướng dẫn sử dụng 
    st.header("📖 Hướng dẫn nhanh")
    st.info("Mục tiêu: Dùng được ngay – không cần hướng dẫn dài")
    st.markdown("""
    1. 📥 Tải bộ công cụ
    2. 📝 Tự đánh giá năng lực (Tab 1)
    3. 📅 Thực hiện lộ trình 90 ngày (Tab 2)
    4. ✅ Theo dõi tiến độ hàng tuần
    5. 🔄 Điều chỉnh thực tế
    """)
    
    st.divider()
    
    # Giá trị cốt lõi [cite: 93-98]
    st.header("💎 Giá trị cốt lõi")
    st.markdown("""
    * ✅ **Thực tế:** Dựa trên nhu cầu tuyển dụng
    * ✅ **Dễ sử dụng:** Triển khai ngay
    * ✅ **Độc lập:** Dùng mọi lúc, mọi nơi
    """)

# --- 3. HEADER CHÍNH ---
st.title("👩‍⚕️ LỘ TRÌNH NGHỀ NGHIỆP ĐIỀU DƯỠNG")
st.markdown("**Kết nối sinh viên với việc làm phù hợp trình độ [cite: 27]**")
st.divider()

# Tạo 4 Tab chức năng
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 1. Đánh giá Năng lực", 
    "📅 2. Lộ trình 90 ngày", 
    "🏥 3. Việc làm", 
    "💬 4. Mentor & Workshop"
])

# --- TAB 1: ĐÁNH GIÁ NĂNG LỰC (GIỮ NGUYÊN LOGIC CỦA BẠN) ---
with tab1:
    st.header("📋 Đánh giá Năng lực Toàn diện")
    st.markdown("Hệ thống đánh giá dựa trên chuẩn năng lực cơ bản[cite: 30].")
    
    with st.form("assessment_form"):
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.subheader("1. Kỹ năng & Kinh nghiệm")
            clinical_skills = st.multiselect(
                "Kỹ năng lâm sàng đã làm được[cite: 32]:",
                ["Tiêm tĩnh mạch/Lấy ven", "Tiêm bắp/Dưới da", "Đặt thông tiểu", "Thay băng/Cắt chỉ", "CPR (Sơ cứu)", "Đo sinh hiệu", "Ghi hồ sơ"]
            )
            weakness = st.text_input("Điểm còn yếu cần cải thiện[cite: 33]:")
            
        with col_b:
            st.subheader("2. Định hướng & Chứng chỉ")
            internship_duration = st.slider("Tháng thực tập[cite: 34]:", 0, 12, 3)
            career_goal = st.selectbox("Dự định làm việc[cite: 35]:", 
                ["Lâm sàng chuyên khoa (BV lớn)", "Phòng khám tư/Thẩm mỹ", "Chăm sóc tại nhà", "Đi nước ngoài"])
            certificates = st.multiselect("Chứng chỉ đã có[cite: 36]:", 
                ["Tin học văn phòng", "Ngoại ngữ", "CPR", "Chứng chỉ hành nghề"])

        submit_btn = st.form_submit_button("📊 PHÂN TÍCH KẾT QUẢ")

    if submit_btn:
        st.divider()
        # Logic tính điểm (Giữ nguyên logic thông minh của bạn)
        score = 0
        if len(clinical_skills) > 4: score += 4
        else: score += len(clinical_skills) * 0.5
        
        if internship_duration >= 3: score += 2
        if len(certificates) >= 2: score += 2
        
        # Logic kiểm tra điều kiện đặc biệt (Rất hay!)
        missing = []
        if "Đi nước ngoài" in career_goal and "Ngoại ngữ" not in certificates:
            score = min(score, 5)
            missing.append("Thiếu Chứng chỉ Ngoại ngữ (Bắt buộc đi nước ngoài)")
        
        percentage = int(min((score / 8) * 100, 100)) # Thang điểm 8
        
        st.metric("Mức độ sẵn sàng [cite: 38]", f"{percentage}%")
        st.progress(percentage)
        
        if percentage < 60:
            st.error("⚠️ Bạn thiếu kỹ năng thực tế. Hãy qua Tab 2 xem lộ trình ngay!")
        elif percentage < 80:
            st.warning("ℹ️ Tạm ổn. Cần trau dồi thêm kỹ năng mũi nhọn.")
        else:
            st.success("✅ Tuyệt vời! Bạn đã sẵn sàng ứng tuyển.")
            
        if missing:
            for m in missing: st.error(f"❗ {m}")

# --- TAB 2: LỘ TRÌNH 90 NGÀY (GIỮ NGUYÊN LOGIC CỦA BẠN) ---
with tab2:
    st.header("📅 Kế hoạch hành động 90 ngày")
    st.write("Làm theo từng tuần để giảm lo âu[cite: 20].")

    # Giai đoạn 1 [cite: 42]
    with st.expander("🌱 Giai đoạn 1 (0-30 ngày): CHUẨN BỊ", expanded=True):
        st.markdown("### 🎯 Mục tiêu: Hoàn thiện hồ sơ")
        st.checkbox("Hoàn thiện CV 1 trang đúng ngành")
        st.checkbox("Xây dựng Portfolio (Kỹ năng, Ca bệnh, Nhận xét)")
        st.checkbox("Học 1 kỹ năng mũi nhọn (Khóa ngắn hạn/Tự học)")
        st.info("💡 Mẹo: Xin nhận xét từ người hướng dẫn để cải thiện Portfolio.")
        
        st.divider()
        if st.button("📝 Test củng cố Giai đoạn 1"):
            st.success("Đã hoàn thành bài test kiến thức hồ sơ!")

    # Giai đoạn 2 [cite: 57]
    with st.expander("🚀 Giai đoạn 2 (31-60 ngày): TIẾP CẬN"):
        st.markdown("### 🎯 Mục tiêu: Luyện phỏng vấn")
        st.checkbox("Xin việc tại nơi thực tập cũ")
        st.checkbox("Luyện phỏng vấn: Giới thiệu bản thân & Tình huống")
        st.checkbox("Luyện trả lời câu hỏi Đạo đức nghề nghiệp")
        
        st.divider()
        if st.button("📝 Test kỹ năng Phỏng vấn"):
            st.info("Hệ thống đang giả lập tình huống phỏng vấn...")

    # Giai đoạn 3 [cite: 65]
    with st.expander("⭐ Giai đoạn 3 (61-90 ngày): ỔN ĐỊNH"):
        st.markdown("### 🎯 Mục tiêu: Ứng tuyển thực tế")
        st.checkbox("Gửi hồ sơ & Đi phỏng vấn thực tế")
        st.checkbox("Đánh dấu tiến độ mỗi tuần (Checklist)")
        st.success("👉 Theo dõi tiến độ giúp tạo cảm giác kiểm soát tương lai [cite: 67]")

# --- TAB 3: VIỆC LÀM (GIỮ NGUYÊN) ---
with tab3:
    st.header("🏥 Việc làm gợi ý")
    st.write("Nơi chấp nhận sinh viên mới ra trường [cite: 70]")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Bệnh viện Quận (Đa khoa)")
            st.caption("TP.HCM - Lương Thỏa thuận")
            if st.button("Ứng tuyển BV"): st.toast("Đã lưu!")
    with col2:
        with st.container(border=True):
            st.subheader("Phòng khám Tư (Home Care)")
            st.caption("Hà Nội - 8-10 triệu")
            if st.button("Ứng tuyển PK"): st.toast("Đã lưu!")

# --- TAB 4: MENTOR & WORKSHOP (NÂNG CẤP) ---
# Bổ sung Workshop theo 
with tab4:
    st.header("💬 Kết nối & Tư vấn")
    st.write("Giải pháp cho sinh viên ở xa: Nghe - Hỏi - Giải đáp Online ")
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.subheader("📺 Workshop Online")
        st.info("Tham gia các buổi chia sẻ chuyên môn từ xa.")
        with st.container(border=True):
            st.markdown("**Chủ đề: Xử lý tình huống khó với bệnh nhân**")
            st.caption("⏰ 19:00 Chủ nhật tuần này")
            st.button("Đăng ký tham gia")
            
    with c2:
        st.subheader("🙋‍♀️ Hỏi đáp Chuyên gia")
        with st.form("mentor_form"):
            st.text_input("Tên của bạn:")
            st.selectbox("Chủ đề:", ["Sửa CV", "Phỏng vấn", "Chuyên môn"])
            st.text_area("Câu hỏi của bạn:")
            if st.form_submit_button("Gửi câu hỏi"):
                st.success("Mentor sẽ trả lời trong 24h.")

# --- PHẦN CUỐI: KHẢO SÁT THỬ NGHIỆM (BỔ SUNG) ---
# Phần này cực quan trọng để hoàn thiện bài toán 
st.divider()
with st.expander("📝 GÓP Ý THỬ NGHIỆM (Dành cho Sinh viên năm cuối)"):
    st.write("Nhóm mong muốn lắng nghe ý kiến của bạn [cite: 76]")
    
    with st.form("feedback_form"):
        # 3 câu hỏi cốt lõi [cite: 79-81]
        st.slider("1. Ứng dụng có DỄ DÙNG không?", 1, 5, 5)
        st.radio("2. Ứng dụng có giúp bạn GIẢM LO ÂU không?", ["Có", "Một chút", "Không"])
        st.radio("3. Ứng dụng có thúc đẩy bạn HÀNH ĐỘNG không?", ["Có", "Chưa"])
        
        if st.form_submit_button("Gửi Góp ý"):
            st.balloons()
            st.success("Cảm ơn bạn! Ý kiến của bạn giúp hoàn thiện giải pháp.")
