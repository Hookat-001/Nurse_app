import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Nurse Path App", page_icon="👩‍⚕️", layout="wide")

# --- QUẢN LÝ TRẠNG THÁI ĐĂNG NHẬP (Luồng III.1) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# --- MÀN HÌNH ĐĂNG NHẬP / NHẬN CÔNG CỤ ---
if not st.session_state.logged_in:
    st.title("👩‍⚕️ CHÀO MỪNG ĐẾN VỚI NURSE PATH")
    st.info("Giải pháp giảm lo âu & Lộ trình nghề nghiệp cho sinh viên Điều dưỡng")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=200)
    with col2:
        with st.form("login_form"):
            st.subheader("📝 Đăng ký nhận bộ công cụ")
            name = st.text_input("Họ và tên sinh viên:")
            email = st.text_input("Gmail:")
            school = st.text_input("Trường đang theo học:")
            
            if st.form_submit_button("🚀 NHẬN BỘ CÔNG CỤ & BẮT ĐẦU"):
                if name and email:
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.rerun() # Tải lại trang để vào giao diện chính
                else:
                    st.error("Vui lòng nhập tên và email!")
    st.stop() # Dừng code tại đây nếu chưa đăng nhập

# =========================================================
# GIAO DIỆN CHÍNH (SAU KHI ĐĂNG NHẬP)
# =========================================================

# CSS Tùy chỉnh
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-weight: 600; }
    .job-card { padding: 15px; border-radius: 8px; background-color: #f0f2f6; margin-bottom: 10px; }
    .cv-tip { border-left: 5px solid #00c853; padding-left: 10px; background-color: #e8f5e9; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: THÔNG TIN & TÍNH KHẢ THI (IV) ---
with st.sidebar:
    st.title(f"Hi, {st.session_state.user_name} 👋")
    st.caption("Sinh viên Điều dưỡng")
    st.divider()
    
    st.header("💡 Vì sao App này hiệu quả?")
    st.success("✅ Nhu cầu thực tế của sinh viên")
    st.success("✅ Giao diện dễ sử dụng")
    st.success("✅ Triển khai thử nghiệm ngay")
    
    st.divider()
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.rerun()

# --- HEADER ---
st.title("👩‍⚕️ LỘ TRÌNH NGHỀ NGHIỆP ĐIỀU DƯỠNG")
st.markdown("**Giảm mơ hồ - Tăng tự nhận thức - Sẵn sàng đi làm**")
st.divider()

# 5 TAB CHỨC NĂNG (Thêm Tab CV riêng biệt)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 1. Đánh giá", 
    "📅 2. Lộ trình", 
    "🏥 3. Việc làm", 
    "📄 4. Hỗ trợ CV",
    "💬 5. Mentor"
])

# --- TAB 1: ĐÁNH GIÁ MỨC ĐỘ SẴN SÀNG (II.1) ---
with tab1:
    st.header("📊 Đánh giá mức độ sẵn sàng đi làm")
    st.write("Trả lời ngắn gọn để biết bạn đang thiếu gì.")
    
    with st.form("assessment_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Chuyên môn & Kỹ năng")
            # Kiến thức chuyên môn & Kỹ năng thực hành
            f1 = st.slider("Mức độ tự tin về Kiến thức chuyên môn:", 0, 10, 5)
            f2 = st.multiselect("Kỹ năng thực hành thành thạo:", 
                ["Tiêm truyền", "Đặt ống thông", "Thay băng", "CPR", "Sử dụng máy y tế"])
            f3 = st.multiselect("Kỹ năng mềm:", 
                ["Giao tiếp", "Làm việc nhóm", "Quản lý cảm xúc", "Giải quyết vấn đề"])
            
        with c2:
            st.subheader("Hồ sơ & Tâm lý")
            # Chứng chỉ & Tâm lý
            f4 = st.multiselect("Chứng chỉ đã có:", ["Ngoại ngữ", "Tin học", "Chứng chỉ hành nghề", "Cấp cứu cơ bản"])
            f5 = st.slider("Tâm lý/Sự tự tin khi nghĩ đến đi làm:", 0, 10, 4) # Mới thêm theo yêu cầu
            
        submitted = st.form_submit_button("🔍 XEM KẾT QUẢ ĐÁNH GIÁ")

    if submitted:
        st.divider()
        # Logic đánh giá
        score = f1 + len(f2) + len(f3) + len(f4) + f5
        # Thang điểm giả định: Max khoảng 35
        
        if score < 15:
            status = "CHƯA SẴN SÀNG"
            color = "red"
            msg = "Bạn cần tập trung bổ sung kiến thức và kỹ năng ngay."
        elif score < 25:
            status = "TƯƠNG ĐỐI SẴN SÀNG"
            color = "orange"
            msg = "Bạn đã có nền tảng, cần trau dồi thêm tâm lý và hồ sơ."
        else:
            status = "SẴN SÀNG ĐI LÀM"
            color = "green"
            msg = "Tuyệt vời! Hãy chuẩn bị ứng tuyển ngay."
            
        st.markdown(f"<h2 style='text-align: center; color: {color};'>{status}</h2>", unsafe_allow_html=True)
        st.info(f"💡 {msg}")
        st.write("👉 **App đã cá nhân hóa lộ trình cho bạn ở Tab 2.**")

# --- TAB 2: LỘ TRÌNH CÁ NHÂN HÓA (II.2) ---
with tab2:
    st.header("📅 Lộ trình nghề nghiệp cá nhân hóa")
    st.write("Dựa trên kết quả đánh giá, dưới đây là kế hoạch 3 giai đoạn:")

    # Giai đoạn 1
    with st.expander("🌱 Giai đoạn 1: CHUẨN BỊ (Nền tảng)", expanded=True):
        st.markdown("### 🎯 Mục tiêu: Bổ sung cái còn thiếu")
        st.checkbox("Ôn tập kiến thức chuyên môn còn hổng")
        st.checkbox("Thực hành thành thạo các kỹ năng cơ bản (Tiêm, Thay băng...)")
        st.checkbox("Rèn luyện kỹ năng mềm (Giao tiếp với bệnh nhân)")
        st.checkbox("Chuẩn bị bản nháp Hồ sơ cá nhân")

    # Giai đoạn 2
    with st.expander("🚀 Giai đoạn 2: TIẾP CẬN VIỆC LÀM (Đi sâu)"):
        st.markdown("### 🎯 Mục tiêu: Chứng chỉ & Thực tế")
        st.checkbox("Tìm hiểu quy trình bệnh viện nơi thực tập")
        st.checkbox("Hoàn thành các Chứng chỉ bắt buộc & Nên có")
        st.checkbox("Đăng ký 1 khóa học ngắn hạn mũi nhọn (có chứng chỉ)")
        st.checkbox("Xin nhận xét từ người hướng dẫn để cải thiện")

    # Giai đoạn 3
    with st.expander("⭐ Giai đoạn 3: SẴN SÀNG ỨNG TUYỂN"):
        st.markdown("### 🎯 Mục tiêu: Phỏng vấn & Việc làm")
        st.checkbox("Hoàn thiện 100% Bộ hồ sơ xin việc")
        st.checkbox("Luyện phỏng vấn (Bộ câu hỏi Điều dưỡng)")
        st.checkbox("Giả định tình huống giao tiếp (Role-play)")
        st.checkbox("Nộp hồ sơ vào nơi đã thực tập (Ưu tiên)")

# --- TAB 3: GỢI Ý VIỆC LÀM (II.3) ---
with tab3:
    st.header("🏥 Gợi ý việc làm phù hợp")
    st.write("Dành cho sinh viên mới tốt nghiệp, ít kinh nghiệm.")
    
    # Bộ lọc theo yêu cầu
    c1, c2 = st.columns(2)
    with c1:
        area = st.selectbox("Khu vực mong muốn:", ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Cần Thơ"])
    with c2:
        type_fac = st.selectbox("Loại hình cơ sở:", ["Bệnh viện Công", "Bệnh viện Tư nhân", "Phòng khám Đa khoa", "Chăm sóc tại nhà"])
    
    st.divider()
    st.subheader(f"Kết quả cho: {type_fac} tại {area}")
    
    # Giả lập kết quả
    with st.container(border=True):
        st.markdown(f"**Điều dưỡng Đa khoa - {type_fac} Quận 1**")
        st.caption(f"📍 {area} | 💰 Thỏa thuận")
        st.write("✅ Yêu cầu: Tốt nghiệp CĐ/ĐH, Chịu khó, Không yêu cầu kinh nghiệm.")
        st.button("Ứng tuyển ngay", key="job1")

# --- TAB 4: HỖ TRỢ CV & HỒ SƠ (II.4 - MỚI HOÀN TOÀN) ---
with tab4:
    st.header("📄 Hỗ trợ Hồ sơ Xin việc Chuẩn ngành")
    st.write("Đừng để thiếu sót giấy tờ làm mất cơ hội của bạn.")

    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("✅ Checklist Hồ sơ cần có")
        st.write("Đánh dấu vào những gì bạn đã chuẩn bị xong:")
        # Danh sách hồ sơ
        st.checkbox("CV Điều dưỡng hoàn chỉnh")
        st.checkbox("Bằng tốt nghiệp / Giấy xác nhận TN")
        st.checkbox("Bảng điểm chi tiết")
        st.checkbox("Chứng chỉ hành nghề/Ngoại ngữ/Tin học")
        st.checkbox("Giấy khám sức khỏe (còn hạn 6 tháng)")
        
        st.divider()
        st.info("💡 Mẹo: Nên photo công chứng sẵn 3-5 bộ để dùng dần.")

    with col_b:
        st.subheader("✍️ Mẹo viết CV Điều dưỡng")
        # Gợi ý câu chữ
        with st.expander("Mục: Mục tiêu nghề nghiệp", expanded=True):
            st.markdown("""
            * **Nên:** 'Mong muốn áp dụng kiến thức điều dưỡng đa khoa để chăm sóc tốt nhất cho bệnh nhân tại BV...'
            * **Không nên:** Viết chung chung 'Muốn học hỏi kinh nghiệm' (Nhà tuyển dụng cần người làm được việc).
            """)
        
        with st.expander("Mục: Kinh nghiệm làm việc"):
            st.markdown("""
            * **Sinh viên mới:** Ghi rõ quá trình **Thực tập lâm sàng**.
            * **Ví dụ:** 'Thực tập sinh khoa Nội - BV Chợ Rẫy (3 tháng): Thực hiện thành thạo lấy ven, thay băng, hỗ trợ bác sĩ...'
            """)
            
        st.download_button("📥 Tải Mẫu CV Điều dưỡng Chuẩn", data="Mau_CV.pdf", file_name="Mau_CV_DieuDuong.pdf")

# --- TAB 5: MENTOR (GIỮ LẠI ĐỂ TĂNG GIÁ TRỊ) ---
with tab5:
    st.header("💬 Kết nối Mentor")
    st.write("Nếu bạn vẫn còn thắc mắc, hãy hỏi chuyên gia.")
    text = st.text_area("Câu hỏi của bạn:")
    if st.button("Gửi câu hỏi"):
        st.success("Đã gửi! Mentor sẽ phản hồi qua Email bạn đăng ký.")
