import streamlit as st
import base64
import time

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Nurse Path App",
    page_icon="👩‍⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. HÀM XỬ LÝ ẢNH NỀN ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- 3. QUẢN LÝ TRẠNG THÁI ---
if 'show_splash' not in st.session_state:
    st.session_state.show_splash = True
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# =========================================================
# PHẦN CSS QUAN TRỌNG: KHẮC PHỤC LỖI DARK MODE & LÀM ĐẸP
# =========================================================
st.markdown("""
    <style>
    /* 1. ÉP BUỘC TRÌNH DUYỆT DÙNG CHẾ ĐỘ SÁNG (Cực quan trọng cho Mobile) */
    :root {
        color-scheme: light !important;
    }
    
    /* 2. Ép buộc màu chữ và màu nền toàn cục */
    html, body, [class*="css"] {
        background-color: #FFFFFF !important;
        color: #000000 !important; /* Chữ đen tuyệt đối */
    }
    
    /* 3. Xử lý Ô Nhập Liệu (Input) để không bị chữ trắng/nền trắng */
    .stTextInput input, .stTextArea textarea {
        color: #000000 !important;       /* Chữ khi gõ vào màu đen */
        background-color: #ffffff !important; /* Nền ô màu trắng */
        -webkit-text-fill-color: #000000 !important; /* Fix cho iPhone/Safari */
        caret-color: #000000 !important; /* Dấu nháy màu đen */
        border: 1px solid #ccc !important;
    }
    
    /* 4. Xử lý Nhãn (Label) của ô nhập liệu */
    .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #31333F !important;
        font-weight: 600 !important;
    }
    
    /* 5. Ẩn nút Deploy và Menu GitHub */
    .stAppDeployButton {display: none;}
    [data-testid="stToolbar"] {visibility: hidden;} 
    [data-testid="stHeader"] {
        visibility: visible !important;
        background-color: rgba(0,0,0,0);
        z-index: 1000;
    }

    /* 6. Sidebar trên mobile */
    [data-testid="stSidebar"] { 
        width: 300px !important;
        background-color: #F0F2F6 !important; 
    }
    [data-testid="stSidebar"] * {
        color: #000000 !important; /* Chữ trong sidebar màu đen */
    }

    /* 7. CSS làm đẹp khác (Card, Tab...) */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; }
    .job-card { padding: 15px; border-radius: 8px; background-color: #f0f2f6; margin-bottom: 10px; border-left: 5px solid #00ADB5; }
    .job-card * { color: #000000 !important; } /* Chữ trong card màu đen */
    
    /* 8. Reset nút bấm thường */
    div.stButton > button:first-child {
        position: static;
        transform: none;
        width: auto !important;
        display: inline-flex !important;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# PHẦN 1: TRANG CHÀO (SPLASH SCREEN)
# =========================================================
if st.session_state.show_splash:
    
    # Sử dụng tên file ảnh bạn vừa cung cấp
    img_name = "z7434843704046_810c2c91c80bba353a689637e23727d7.jpg"
    img_base64 = get_base64_of_bin_file(img_name)
    
    if img_base64:
        bg_style = f"""
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        """
    else:
        bg_style = "background-color: #ffffff;"
        st.error(f"⚠️ Không tìm thấy ảnh '{img_name}'. Hãy kiểm tra lại thư mục!")

    st.markdown(f"""
        <style>
        [data-testid="stHeader"] {{visibility: hidden !important;}}
        [data-testid="stSidebar"] {{display: none !important;}}
        
        .stApp {{
            {bg_style}
        }}
        
        /* CĂN GIỮA NÚT BẤM SPLASH SCREEN */
        div.stButton > button:first-child {{
            position: fixed !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            background-color: rgba(255, 255, 255, 0.95) !important;
            color: #00ADB5 !important;
            font-size: 35px !important;
            font-weight: 900 !important;
            border: 4px solid #00ADB5 !important;
            border-radius: 50px !important;
            padding: 20px 40px !important;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3) !important;
            z-index: 9999;
        }}
        </style>
    """, unsafe_allow_html=True)

    if st.button("NURSE PATH 🚀"):
        st.session_state.show_splash = False
        st.rerun()

    st.stop()

# =========================================================
# PHẦN 2: ỨNG DỤNG CHÍNH
# =========================================================

# --- MÀN HÌNH ĐĂNG NHẬP ---
if not st.session_state.logged_in:
    st.set_page_config(initial_sidebar_state="expanded") 

    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=250)
        st.title("NURSE PATH")
        st.subheader("Lộ trình nghề nghiệp Điều dưỡng")
        st.info("✅ Giảm lo âu - Tăng tự tin - Sẵn sàng đi làm")
    
    with col2:
        st.write("") 
        st.write("")
        with st.form("login_form"):
            st.markdown("### 📝 Đăng ký nhận Bộ công cụ")
            st.write("Nhập thông tin để bắt đầu lộ trình cá nhân hóa của bạn.")
            
            # CSS đặc biệt cho input form đăng nhập
            st.markdown("""<style>input {color: black !important;}</style>""", unsafe_allow_html=True)

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

# --- DASHBOARD CHÍNH ---
with st.sidebar:
    st.title(f"Hi, {st.session_state.user_name} 👋")
    st.caption("Sinh viên Điều dưỡng")
    st.progress(30, text="Tiến độ lộ trình: 30%")
    st.divider()
    
    st.header("📖 Hướng dẫn nhanh")
    st.markdown("""
    1. 📥 Tải bộ công cụ
    2. 📝 Tự đánh giá (Tab 1)
    3. 📅 Lộ trình 90 ngày (Tab 2)
    4. 📄 Chuẩn bị hồ sơ (Tab 3)
    """)
    st.divider()
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.show_splash = True 
        st.rerun()

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

# --- TAB 1: ĐÁNH GIÁ ---
with tab1:
    st.header("📊 Đánh giá mức độ sẵn sàng đi làm")
    st.info("💡 Lưu ý: Nếu bạn cảm thấy mình chưa có gì cả, đừng lo lắng. App sẽ hướng dẫn bạn từ đầu.")
    
    with st.form("assessment_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Năng lực Chuyên môn")
            score_knowledge = st.slider("Tự tin về Kiến thức (0-10):", 0, 10, 3)
            
            st.write("Kỹ năng thực hành ĐÃ LÀM ĐƯỢC:")
            has_no_skills = st.checkbox("❌ Tôi chưa thạo kỹ năng nào")
            if not has_no_skills:
                skills = st.multiselect("Chọn kỹ năng:", 
                    ["Tiêm truyền / Lấy ven", "Đặt thông tiểu", "Thay băng", "CPR", "Sử dụng máy y tế"], label_visibility="collapsed")
            else: skills = [] 
            
            st.write("Kỹ năng mềm:")
            soft_skills = st.multiselect("Chọn kỹ năng:", ["Giao tiếp", "Làm việc nhóm", "Quản lý cảm xúc", "Giải quyết vấn đề"])

        with c2:
            st.subheader("Hồ sơ & Tâm lý")
            st.write("Chứng chỉ đã có:")
            has_no_certs = st.checkbox("❌ Tôi chưa có chứng chỉ nào")
            if not has_no_certs:
                certs = st.multiselect("Chọn chứng chỉ:", ["Tin học", "Ngoại ngữ", "CCHN", "Cấp cứu"], label_visibility="collapsed")
            else: certs = []
            score_mindset = st.slider("Tâm lý vững vàng (0-10):", 0, 10, 2)
            
        submitted = st.form_submit_button("🔍 PHÂN TÍCH KẾT QUẢ")

    if submitted:
        st.divider()
        is_blank = (score_knowledge < 3) and (len(skills) == 0) and (len(certs) == 0)
        
        if is_blank:
            st.markdown("""
            <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #2196f3;">
                <h3 style="color: #000;">👋 Chào bạn mới!</h3>
                <p style="color: #333;">Bạn đang ở vạch xuất phát. Hãy bắt đầu từ <b>Giai đoạn 1</b> của lộ trình nhé.</p>
            </div>""", unsafe_allow_html=True)
            st.warning("👉 Chuyển sang **Tab 2** để xem việc cần làm ngay.")
        else:
            score = score_knowledge + len(skills) + len(soft_skills) + len(certs)*2 + score_mindset
            st.markdown("### 📢 KẾT QUẢ CỦA BẠN:")
            if score < 15: st.error("🔴 MỨC ĐỘ: CHƯA SẴN SÀNG")
            elif score < 28: st.warning("🟠 MỨC ĐỘ: TƯƠNG ĐỐI SẴN SÀNG")
            else: st.success("🟢 MỨC ĐỘ: SẴN SÀNG ĐI LÀM")

# --- TAB 2: LỘ TRÌNH ---
with tab2:
    st.header("📅 Lộ trình 90 ngày")
    tasks = ["t1_1", "t1_2", "t1_3", "t1_4", "t2_1", "t2_2", "t2_3", "t2_4", "t3_1", "t3_2", "t3_3", "t3_4"]
    done = sum(1 for t in tasks if st.session_state.get(t, False))
    prog = int((done/len(tasks))*100)
    
    col_p1, col_p2 = st.columns([3, 1])
    with col_p1:
        st.write(f"**Tiến độ tổng thể:** {prog}%")
        st.progress(prog)
    with col_p2:
        if prog == 100: st.balloons()
    st.divider()

    with st.expander("🌱 Giai đoạn 1 (30 ngày đầu): CHUẨN BỊ (Nền tảng)", expanded=True):
        st.checkbox("Ôn tập kiến thức chuyên khoa", key="t1_1")
        st.checkbox("Thực hành thành thạo kỹ năng cơ bản", key="t1_2")
        st.checkbox("Rèn luyện kỹ năng mềm", key="t1_3")
        st.checkbox("Chuẩn bị hồ sơ (Nháp)", key="t1_4")

    with st.expander("🚀 Giai đoạn 2 (30 ngày tiếp theo): TIẾP CẬN"):
        st.checkbox("Tìm hiểu quy trình tại BV thực tập", key="t2_1")
        st.checkbox("Hoàn tất chứng chỉ bắt buộc", key="t2_2")
        st.checkbox("Đăng ký khóa học ngắn hạn", key="t2_3")
        st.checkbox("Xin nhận xét từ người hướng dẫn", key="t2_4")

    with st.expander("⭐ Giai đoạn 3 (30 ngày cuối): VỀ ĐÍCH"):
        st.checkbox("Hoàn thiện CV & Hồ sơ", key="t3_1")
        st.checkbox("Luyện phỏng vấn", key="t3_2")
        st.checkbox("Role-play tình huống", key="t3_3")
        st.checkbox("Nộp hồ sơ", key="t3_4")

# --- TAB 3: HỖ TRỢ CV ---
with tab3:
    st.header("📄 Trung tâm Hỗ trợ Hồ sơ")
    cv_tasks = ["c1", "c2", "c3", "c4", "c5", "c6"]
    cv_prog = int((sum(1 for t in cv_tasks if st.session_state.get(t, False)) / 6) * 100)
    
    st.markdown(f"**Hoàn thiện hồ sơ: {cv_prog}%**")
    st.progress(cv_prog)
    if cv_prog == 100: st.success("🎉 Đã đầy đủ hồ sơ!")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ Checklist")
        st.checkbox("CV Điều dưỡng", key="c1")
        st.checkbox("Bằng tốt nghiệp", key="c2")
        st.checkbox("Bảng điểm gốc", key="c3")
        st.checkbox("Chứng chỉ hành nghề", key="c4")
        st.checkbox("Giấy khám sức khỏe", key="c5")
        st.checkbox("Sơ yếu lý lịch", key="c6")
    with col2:
        st.subheader("✍️ Mẹo viết CV")
        st.info("💡 Mục tiêu: Đừng viết 'muốn học hỏi'. Hãy viết 'muốn đóng góp kỹ năng chăm sóc'.")
        st.download_button("📥 Tải Mẫu CV", data="Sample CV", file_name="CV_Mau.txt")

# --- TAB 4: VIỆC LÀM ---
with tab4:
    st.header("🏥 Việc làm")
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        area = st.selectbox("Khu vực mong muốn:", ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Cần Thơ"])
    with f_col2:
        job_type = st.selectbox("Loại hình cơ sở:", ["Bệnh viện Công", "Bệnh viện Tư", "Phòng khám Đa khoa", "Chăm sóc tại nhà"])
    
    st.divider()
    st.markdown(f"**Kết quả tìm kiếm: {job_type} tại {area}**")
    st.markdown(f"""
    <div class="job-card">
        <h3>🏥 Điều dưỡng Đa khoa - {job_type} Quận 1</h3>
        <p>📍 <b>Khu vực:</b> {area} | 💰 <b>Lương:</b> Thỏa thuận</p>
        <p>✅ <b>Yêu cầu:</b> Tốt nghiệp CĐ/ĐH, Nhanh nhẹn, Chấp nhận đào tạo lại.</p>
        <button style="background-color: #00ADB5; color: white; border: none; padding: 8px 16px; border-radius: 4px;">Ứng tuyển ngay</button>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 5: MENTOR ---
with tab5:
    st.header("💬 Kết nối Mentor")
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
