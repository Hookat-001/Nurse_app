import streamlit as st
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Nurse Path App",
    page_icon="👩‍⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- ẨN LINK GITHUB & MENU MẶC ĐỊNH ---
st.markdown("""
    <style>
    /* Ẩn nút Deploy và Menu hamburger (3 dấu gạch) ở góc phải */
    .stAppDeployButton {display: none;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    
    /* Ẩn Header mặc định (nơi chứa các nút đó) */
    header {visibility: hidden !important;}
    
    /* Ẩn chân trang "Made with Streamlit" nếu muốn */
    footer {visibility: hidden !important;}
    
    /* Kéo giao diện lên cao hơn vì đã ẩn header */
    .block-container {
        padding-top: 1rem !important; 
    }
    </style>
""", unsafe_allow_html=True)

# CSS Tùy chỉnh làm đẹp giao diện
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; }
    .job-card { padding: 15px; border-radius: 8px; background-color: #f0f2f6; margin-bottom: 10px; border-left: 5px solid #00ADB5; }
    .cv-tip { background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 5px solid #43a047; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. QUẢN LÝ TRẠNG THÁI ĐĂNG NHẬP ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# --- MÀN HÌNH 1: ĐĂNG KÝ / NHẬN CÔNG CỤ ---
if not st.session_state.logged_in:
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=250)
        st.title("NURSE PATH")
        st.subheader("Lộ trình nghề nghiệp Điều dưỡng")
        st.info("✅ Giảm lo âu - Tăng tự tin - Sẵn sàng đi làm")
    
    with col2:
        st.write("") # Spacer
        st.write("")
        with st.form("login_form"):
            st.markdown("### 📝 Đăng ký nhận Bộ công cụ")
            st.write("Nhập thông tin để bắt đầu lộ trình cá nhân hóa của bạn.")
            
            name = st.text_input("Họ và tên sinh viên:")
            email = st.text_input("Email (Gmail):")
            school = st.text_input("Trường đang theo học:")
            
            if st.form_submit_button("🚀 NHẬN CÔNG CỤ & BẮT ĐẦU"):
                if name and email:
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.toast(f"Chào mừng {name}!", icon="🎉")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Vui lòng nhập đầy đủ Tên và Email.")
    st.stop() 

# =========================================================
# GIAO DIỆN CHÍNH (SAU KHI ĐĂNG NHẬP)
# =========================================================

# --- SIDEBAR: THÔNG TIN & HƯỚNG DẪN ---
with st.sidebar:
    st.title(f"Hi, {st.session_state.user_name} 👋")
    st.caption("Sinh viên Điều dưỡng")
    
    st.divider()
    
    # Hướng dẫn sử dụng
    st.header("📖 Hướng dẫn nhanh")
    st.info("Mục tiêu: Dùng được ngay – không cần hướng dẫn dài")
    st.markdown("""
    1. 📥 Tải bộ công cụ
    2. 📝 Tự đánh giá năng lực (Tab 1)
    3. 📅 Thực hiện lộ trình 90 ngày (Tab 2)
    4. 📄 Chuẩn bị hồ sơ đầy đủ (Tab 3)
    5. ✅ Ứng tuyển & Phỏng vấn
    """)
    
    st.divider()
    st.header("💎 Giá trị cốt lõi")
    st.markdown("""
    * ✅ **Thực tế:** Sát nhu cầu tuyển dụng
    * ✅ **Dễ dùng:** Giao diện thân thiện
    * ✅ **Hiệu quả:** Giảm lo âu tức thì
    """)
    
    st.divider()
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.rerun()

# --- HEADER ---
st.title("👩‍⚕️ LỘ TRÌNH NGHỀ NGHIỆP CÁ NHÂN")
st.markdown("**Từ Sinh viên mơ hồ ➡️ Ứng viên sáng giá**")
st.divider()

# 5 TAB CHỨC NĂNG
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 1. Đánh giá", 
    "📅 2. Lộ trình", 
    "📄 3. Hỗ trợ CV", 
    "🏥 4. Việc làm", 
    "💬 5. Mentor"
])

# --- TAB 1: ĐÁNH GIÁ MỨC ĐỘ SẴN SÀNG ---
with tab1:
    st.header("📊 Đánh giá mức độ sẵn sàng đi làm")
    st.info("💡 Lưu ý: Nếu bạn cảm thấy mình chưa có gì cả, đừng lo lắng. Hãy chọn trung thực, App sẽ chỉ cho bạn cách bắt đầu từ con số 0.")
    
    with st.form("assessment_form"):
        c1, c2 = st.columns(2)
        
        # --- CỘT 1: CHUYÊN MÔN ---
        with c1:
            st.subheader("1. Kỹ năng & Chuyên môn")
            score_knowledge = st.slider("Mức độ tự tin về Kiến thức lý thuyết (0 - Rỗng, 10 - Rất tự tin):", 0, 10, 3)
            
            st.write("Kỹ năng thực hành bạn ĐÃ LÀM ĐƯỢC:")
            has_no_skills = st.checkbox("❌ Tôi chưa thạo kỹ năng nào (Sẽ học sau)")
            
            if not has_no_skills:
                skills = st.multiselect("Chọn kỹ năng cụ thể:", 
                    ["Tiêm truyền / Lấy ven", "Đặt thông tiểu / Dạ dày", "Thay băng vết thương", "CPR (Cấp cứu)", "Sử dụng máy y tế"],
                    label_visibility="collapsed")
            else:
                skills = [] 
            
            st.write("Kỹ năng mềm hiện có:")
            soft_skills = st.multiselect("Chọn kỹ năng:", 
                ["Giao tiếp bệnh nhân", "Làm việc nhóm", "Quản lý cảm xúc", "Giải quyết vấn đề"])

        # --- CỘT 2: HỒ SƠ & TÂM LÝ ---
        with c2:
            st.subheader("2. Hồ sơ & Tâm lý")
            st.write("Các chứng chỉ đã có trong tay:")
            has_no_certs = st.checkbox("❌ Tôi chưa có chứng chỉ nào cả")
            
            if not has_no_certs:
                certs = st.multiselect("Chọn chứng chỉ:", 
                    ["Tin học", "Ngoại ngữ", "Chứng chỉ hành nghề", "Chứng chỉ Cấp cứu"],
                    label_visibility="collapsed")
            else:
                certs = []

            score_mindset = st.slider("Tâm lý khi nghĩ đến việc đi xin việc (0 - Rất sợ, 10 - Rất sẵn sàng):", 0, 10, 2)
            
        submitted = st.form_submit_button("🔍 PHÂN TÍCH KẾT QUẢ")

    if submitted:
        st.divider()
        is_blank_sheet = (score_knowledge < 3) and (len(skills) == 0) and (len(certs) == 0)
        
        if is_blank_sheet:
            st.markdown("""
            <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #2196f3;">
                <h3>👋 Chào bạn mới! Đừng hoang mang.</h3>
                <p>Kết quả cho thấy bạn đang ở vạch xuất phát.</p>
                <p>👉 <b>Lời khuyên:</b> Hãy quên việc "đi xin việc" đi. Mục tiêu 30 ngày tới của bạn chỉ là: <b>Học thuộc quy trình Tiêm & Viết xong cái CV nháp.</b></p>
            </div>
            """, unsafe_allow_html=True)
            st.warning("🎯 Hãy chuyển sang **Tab 2 (Lộ trình)** và bắt đầu ngay từ **Giai đoạn 1**.")
        else:
            total_score = score_knowledge + len(skills) + len(soft_skills) + len(certs)*2 + score_mindset
            st.markdown("### 📢 KẾT QUẢ CỦA BẠN:")
            if total_score < 15:
                st.error("🔴 MỨC ĐỘ: CHƯA SẴN SÀNG")
                st.write("👉 Bạn cần tập trung vào **Giai đoạn 1** của lộ trình.")
            elif total_score < 28:
                st.warning("🟠 MỨC ĐỘ: TƯƠNG ĐỐI SẴN SÀNG")
                st.write("👉 Bạn đã có nền tảng. Hãy sang **Tab 3** để hoàn thiện hồ sơ.")
            else:
                st.success("🟢 MỨC ĐỘ: SẴN SÀNG ĐI LÀM")
                st.write("👉 Tuyệt vời! Bạn đã đủ điều kiện để ứng tuyển ngay tại **Tab 4**.")

# --- TAB 2: LỘ TRÌNH (CÓ THANH TIẾN ĐỘ) ---
with tab2:
    st.header("📅 Lộ trình Cá nhân hóa")
    st.write("Kế hoạch hành động từng bước để giảm lo âu.")

    # TÍNH TOÁN TIẾN ĐỘ LỘ TRÌNH
    tasks = [
        "t1_1", "t1_2", "t1_3", "t1_4", 
        "t2_1", "t2_2", "t2_3", "t2_4", 
        "t3_1", "t3_2", "t3_3", "t3_4" 
    ]
    completed_count = 0
    for task in tasks:
        if st.session_state.get(task, False):
            completed_count += 1
    progress_percent = int((completed_count / len(tasks)) * 100)
    
    st.divider()
    col_p1, col_p2 = st.columns([3, 1])
    with col_p1:
        st.write(f"**Tiến độ lộ trình:** {progress_percent}%")
        st.progress(progress_percent)
    with col_p2:
        if progress_percent == 100: st.success("🏆 HOÀN THÀNH!")
    st.divider()

    with st.expander("🌱 Giai đoạn 1: CHUẨN BỊ (Nền tảng)", expanded=True):
        st.checkbox("Ôn tập kiến thức chuyên khoa", key="t1_1")
        st.checkbox("Thực hành thành thạo các kỹ năng cơ bản", key="t1_2")
        st.checkbox("Rèn luyện kỹ năng mềm", key="t1_3")
        st.checkbox("Chuẩn bị hồ sơ cá nhân (Nháp)", key="t1_4")

    with st.expander("🚀 Giai đoạn 2: TIẾP CẬN VIỆC LÀM"):
        st.checkbox("Tìm hiểu quy trình làm việc tại BV thực tập", key="t2_1")
        st.checkbox("Hoàn tất các chứng chỉ bắt buộc", key="t2_2")
        st.checkbox("Đăng ký 1 khóa học ngắn hạn mũi nhọn", key="t2_3")
        st.checkbox("Xin nhận xét từ người hướng dẫn", key="t2_4")

    with st.expander("⭐ Giai đoạn 3: SẴN SÀNG ỨNG TUYỂN"):
        st.checkbox("Hoàn thiện CV & Hồ sơ xin việc", key="t3_1")
        st.checkbox("Luyện bộ câu hỏi phỏng vấn", key="t3_2")
        st.checkbox("Role-play: Xử lý tình huống", key="t3_3")
        st.checkbox("Nộp hồ sơ vào nơi đã thực tập", key="t3_4")

# --- TAB 3: HỖ TRỢ CV & HỒ SƠ (ĐÃ CÓ THANH TIẾN ĐỘ %) ---
with tab3:
    st.header("📄 Trung tâm Hỗ trợ Hồ sơ")
    st.write("Đừng để hồ sơ thiếu sót làm mất cơ hội.")

    # --- TÍNH TOÁN TIẾN ĐỘ HỒ SƠ ---
    cv_tasks = ["cv_1", "cv_2", "cv_3", "cv_4", "cv_5", "cv_6"]
    cv_done = 0
    for t in cv_tasks:
        if st.session_state.get(t, False):
            cv_done += 1
    cv_percent = int((cv_done / len(cv_tasks)) * 100)

    # Hiển thị thanh tiến độ CV
    st.markdown(f"**Mức độ hoàn thiện hồ sơ: {cv_percent}%**")
    st.progress(cv_percent)
    
    if cv_percent == 100:
        st.success("🎉 TUYỆT VỜI! Hồ sơ của bạn đã đầy đủ. Hãy tự tin ứng tuyển!")
    elif cv_percent > 0:
        st.info(f"Bạn còn thiếu {len(cv_tasks) - cv_done} loại giấy tờ nữa.")
    st.divider()

    col_cv1, col_cv2 = st.columns(2)
    
    with col_cv1:
        st.subheader("✅ Checklist Giấy tờ")
        st.caption("Hãy tích vào những gì bạn ĐÃ CÓ:")
        st.checkbox("CV Điều dưỡng (đã chỉnh sửa kỹ)", key="cv_1")
        st.checkbox("Bằng tốt nghiệp / Giấy CNTN", key="cv_2")
        st.checkbox("Bảng điểm gốc", key="cv_3")
        st.checkbox("Chứng chỉ hành nghề (hoặc giấy hẹn)", key="cv_4")
        st.checkbox("Giấy khám sức khỏe (còn hạn 6 tháng)", key="cv_5")
        st.checkbox("Sơ yếu lý lịch (Công chứng)", key="cv_6")
        
    with col_cv2:
        st.subheader("✍️ Mẹo viết CV 'Ăn điểm'")
        with st.container():
            st.markdown("""
            <div class="cv-tip">
            <b>Mục Tiêu Nghề Nghiệp:</b><br>
            ❌ Đừng viết: "Muốn học hỏi kinh nghiệm."<br>
            ✅ Hãy viết: "Mong muốn vận dụng kỹ năng CSNB để đóng góp cho khoa Nội..."
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="cv-tip">
            <b>Kinh Nghiệm:</b><br>
            Ví dụ: <i>"Thực tập Khoa Cấp cứu (3 tháng): Thành thạo kỹ thuật ép tim, hỗ trợ đặt nội khí quản..."</i>
            </div>
            """, unsafe_allow_html=True)
            
        st.download_button("📥 Tải Mẫu CV Điều Dưỡng (PDF)", data="Noi dung mau...", file_name="CV_Mau.txt")

# --- TAB 4: VIỆC LÀM ---
with tab4:
    st.header("🏥 Gợi ý Việc làm Phù hợp")
    st.write("Dành cho sinh viên mới tốt nghiệp.")
    
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        area = st.selectbox("Khu vực mong muốn:", ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Cần Thơ"])
    with f_col2:
        job_type = st.selectbox("Loại hình cơ sở:", ["Bệnh viện Công", "Bệnh viện Tư", "Phòng khám Đa khoa", "Chăm sóc tại nhà"])
    
    st.divider()
    st.markdown(f"**Kết quả tìm kiếm: {job_type} tại {area}**")
    
    st.markdown(f"""
    <div class="job-card">
        <h3>🏥 Điều dưỡng Đa khoa - {job_type}</h3>
        <p>📍 <b>Khu vực:</b> {area} | 💰 <b>Lương:</b> Thỏa thuận</p>
        <p>✅ <b>Yêu cầu:</b> Tốt nghiệp CĐ/ĐH, Nhanh nhẹn, Chấp nhận đào tạo lại.</p>
        <button style="background-color: #00ADB5; color: white; border: none; padding: 8px 16px; border-radius: 4px;">Ứng tuyển ngay</button>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 5: MENTOR & GÓP Ý ---
with tab5:
    st.header("💬 Kết nối & Phản hồi")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Hỏi đáp Chuyên gia")
        st.text_area("Nhập câu hỏi của bạn:")
        if st.button("Gửi câu hỏi"):
            st.success("Đã gửi! Mentor sẽ phản hồi qua email.")
    with c2:
        st.subheader("Góp ý Thử nghiệm")
        st.slider("Dễ dùng không?", 1, 5, 5)
        st.radio("Giảm lo âu không?", ["Có", "Không"])
        if st.button("Gửi Góp ý"):
            st.balloons()
            st.success("Cảm ơn bạn!")
