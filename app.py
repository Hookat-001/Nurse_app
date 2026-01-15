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

# --- 2. HÀM XỬ LÝ ẢNH NỀN (BASE64) ---
# Hàm này giúp đưa ảnh từ máy tính lên làm nền web
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- 3. QUẢN LÝ TRẠNG THÁI ---
if 'show_splash' not in st.session_state:
    st.session_state.show_splash = True
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# =========================================================
# PHẦN 1: TRANG CHÀO (SPLASH SCREEN) - GIAO DIỆN KHUNG ẢNH
# =========================================================
if st.session_state.show_splash:
    
    # ⚠️ Đảm bảo file ảnh 'image_8a6388.jpg' nằm cùng thư mục với app.py
    try:
        img_base64 = get_base64_of_bin_file("z7434843704046_810c2c91c80bba353a689637e23727d7.jpg")
        
        # CSS ĐẶC BIỆT:
        # 1. Đặt ảnh làm nền, căn giữa.
        # 2. Biến nút bấm thành chữ to đẹp nằm giữa màn hình.
        st.markdown(f"""
            <style>
            /* Ẩn header/footer mặc định của Streamlit cho đẹp */
            [data-testid="stHeader"] {{visibility: hidden;}}
            
            /* Thiết lập ảnh nền */
            .stApp {{
                background-image: url("data:image/jpg;base64,{img_base64}");
                background-size: contain; /* Hoặc cover nếu muốn tràn màn hình */
                background-position: center;
                background-repeat: no-repeat;
                background-color: #ffffff; /* Màu nền trắng cho phần thừa */
            }}
            
            /* Căn chỉnh nút bấm vào giữa màn hình (tương đối) */
            .stButton {{
                display: flex;
                justify_content: center;
                align-items: center;
                height: 60vh; /* Chiều cao vùng bấm */
            }}
            
            /* Biến hóa nút bấm thường thành Chữ tiêu đề đẹp */
            .stButton > button {{
                background-color: rgba(255, 255, 255, 0.8) !important; /* Nền trắng mờ nhẹ */
                color: #00ADB5 !important;
                font-size: 50px !important;
                font-weight: 900 !important;
                border: 4px solid #00ADB5 !important;
                border-radius: 20px !important;
                padding: 20px 60px !important;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.2) !important;
                transition: all 0.3s ease;
            }}
            
            /* Hiệu ứng khi di chuột vào */
            .stButton > button:hover {{
                transform: scale(1.1);
                color: #ff4b4b !important;
                border-color: #ff4b4b !important;
                cursor: pointer;
            }}
            
            /* Dòng chữ nhỏ hướng dẫn bên dưới */
            .click-hint {{
                text-align: center;
                color: #555;
                font-size: 18px;
                margin-top: -50px;
                font-weight: bold;
                animation: blink 2s infinite;
            }}
            
            @keyframes blink {{
                0% {{opacity: 1;}}
                50% {{opacity: 0.5;}}
                100% {{opacity: 1;}}
            }}
            </style>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error("⚠️ Không tìm thấy file ảnh 'image_8a6388.jpg'. Hãy upload ảnh lên GitHub hoặc để cùng thư mục!")
        st.stop()

    # --- NÚT BẤM CHÍNH ---
    # Chúng ta tạo 3 cột để nút nằm giữa
    c1, c2, c3 = st.columns([1, 4, 1])
    
    with c2:
        st.write("") # Khoảng trống đệm phía trên
        st.write("") 
        st.write("") 
        
        # Nút bấm chính là TÊN APP
        if st.button("NURSE PATH 🚀"):
            st.session_state.show_splash = False
            st.rerun()
            
        st.markdown('<p class="click-hint">👆 Bấm vào tên để bắt đầu</p>', unsafe_allow_html=True)

    st.stop()

# =========================================================
# PHẦN 2: ỨNG DỤNG CHÍNH (SAU KHI BẤM VÀO)
# =========================================================

# --- CSS CHO APP CHÍNH (Khôi phục giao diện chuẩn) ---
st.markdown("""
    <style>
    /* Hiện lại header nhưng ẩn nút deploy */
    [data-testid="stHeader"] {visibility: visible;}
    .stAppDeployButton {display: none;}
    
    /* CSS Tùy chỉnh các tab và card */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; }
    .job-card { padding: 15px; border-radius: 8px; background-color: #f0f2f6; margin-bottom: 10px; border-left: 5px solid #00ADB5; }
    .cv-tip { background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 5px solid #43a047; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- MÀN HÌNH ĐĂNG NHẬP / NHẬN CÔNG CỤ ---
if not st.session_state.logged_in:
    # Hiển thị sidebar trở lại
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
    
    st.header("💡 Vì sao chọn App này?")
    st.markdown("""
    * ✅ **Thực tế:** Sát nhu cầu tuyển dụng
    * ✅ **Dễ dùng:** Giao diện thân thiện
    * ✅ **Hiệu quả:** Giảm lo âu tức thì
    """)
    
    st.divider()
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.show_splash = True # Về trang chào
        st.rerun()

# --- NỘI DUNG CHÍNH ---
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
                <h3>👋 Chào bạn mới!</h3>
                <p>Bạn đang ở vạch xuất phát. Hãy bắt đầu từ <b>Giai đoạn 1</b> của lộ trình nhé.</p>
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
    st.header("📅 Lộ trình Cá nhân hóa")
    tasks = ["t1_1", "t1_2", "t1_3", "t1_4", "t2_1", "t2_2", "t2_3", "t2_4", "t3_1", "t3_2", "t3_3", "t3_4"]
    done = sum(1 for t in tasks if st.session_state.get(t, False))
    prog = int((done/len(tasks))*100)
    
    st.write(f"**Tiến độ tổng thể:** {prog}%")
    st.progress(prog)
    st.divider()

    with st.expander("🌱 Giai đoạn 1: CHUẨN BỊ (Nền tảng)", expanded=True):
        st.checkbox("Ôn tập kiến thức chuyên khoa", key="t1_1")
        st.checkbox("Thực hành thành thạo kỹ năng cơ bản", key="t1_2")
        st.checkbox("Rèn luyện kỹ năng mềm", key="t1_3")
        st.checkbox("Chuẩn bị hồ sơ (Nháp)", key="t1_4")

    with st.expander("🚀 Giai đoạn 2: TIẾP CẬN"):
        st.checkbox("Tìm hiểu quy trình tại BV thực tập", key="t2_1")
        st.checkbox("Hoàn tất chứng chỉ bắt buộc", key="t2_2")
        st.checkbox("Đăng ký khóa học ngắn hạn", key="t2_3")
        st.checkbox("Xin nhận xét từ người hướng dẫn", key="t2_4")

    with st.expander("⭐ Giai đoạn 3: VỀ ĐÍCH"):
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

# --- TAB 4 & 5 (GIỮ NGUYÊN NHƯ CŨ) ---
with tab4:
    st.header("🏥 Việc làm")
    st.info("Chọn khu vực để xem việc làm phù hợp (Chức năng Demo)")
    st.selectbox("Khu vực:", ["TP.HCM", "Hà Nội"])
    st.button("Tìm kiếm ngay")

with tab5:
    st.header("💬 Mentor")
    st.text_area("Đặt câu hỏi cho chuyên gia:")
    st.button("Gửi câu hỏi")

