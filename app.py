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

# --- TAB 1: ĐÁNH GIÁ (CẬP NHẬT CHO NGƯỜI "CHƯA CÓ GÌ") ---
with tab1:
    st.header("📊 Đánh giá mức độ sẵn sàng")
    st.info("💡 Lưu ý: Nếu bạn cảm thấy mình chưa có gì cả, đừng lo lắng. Hãy cứ chọn trung thực, App sẽ chỉ cho bạn cách bắt đầu từ con số 0.")
    
    with st.form("assessment_form"):
        c1, c2 = st.columns(2)
        
        # --- CỘT 1: CHUYÊN MÔN ---
        with c1:
            st.subheader("1. Kỹ năng & Chuyên môn")
            
            # Câu hỏi 1: Kiến thức (Cho phép chọn mức 0)
            score_knowledge = st.slider("Mức độ tự tin về Kiến thức lý thuyết (0 - Rỗng, 10 - Rất tự tin):", 0, 10, 3)
            
            # Câu hỏi 2: Kỹ năng thực hành (Thêm lựa chọn "Chưa có")
            st.write("Kỹ năng thực hành bạn ĐÃ LÀM ĐƯỢC:")
            has_no_skills = st.checkbox("❌ Tôi chưa thạo kỹ năng nào (Sẽ học sau)")
            
            if not has_no_skills:
                skills = st.multiselect("Chọn kỹ năng cụ thể:", 
                    ["Tiêm truyền / Lấy ven", "Đặt thông tiểu / Dạ dày", "Thay băng vết thương", "CPR (Cấp cứu)", "Sử dụng máy y tế"],
                    label_visibility="collapsed")
            else:
                skills = [] # Trả về danh sách rỗng nếu chọn chưa có
            
            # Câu hỏi 3: Kỹ năng mềm
            st.write("Kỹ năng mềm hiện có:")
            soft_skills = st.multiselect("Chọn kỹ năng:", 
                ["Giao tiếp bệnh nhân", "Làm việc nhóm", "Quản lý cảm xúc", "Giải quyết vấn đề"])

        # --- CỘT 2: HỒ SƠ & TÂM LÝ ---
        with c2:
            st.subheader("2. Hồ sơ & Tâm lý")
            
            # Câu hỏi 4: Chứng chỉ (Thêm lựa chọn "Chưa có")
            st.write("Các chứng chỉ đã có trong tay:")
            has_no_certs = st.checkbox("❌ Tôi chưa có chứng chỉ nào cả")
            
            if not has_no_certs:
                certs = st.multiselect("Chọn chứng chỉ:", 
                    ["Tin học", "Ngoại ngữ", "Chứng chỉ hành nghề", "Chứng chỉ Cấp cứu"],
                    label_visibility="collapsed")
            else:
                certs = []

            # Câu hỏi 5: Tâm lý (Quan trọng)
            score_mindset = st.slider("Tâm lý khi nghĩ đến việc đi xin việc (0 - Rất sợ, 10 - Rất sẵn sàng):", 0, 10, 2)
            
        submitted = st.form_submit_button("🔍 PHÂN TÍCH KẾT QUẢ")

    if submitted:
        st.divider()
        # --- LOGIC XỬ LÝ CHO NGƯỜI "CHƯA CÓ GÌ" ---
        
        # Kiểm tra trường hợp đặc biệt: Không có gì cả
        is_blank_sheet = (score_knowledge < 3) and (len(skills) == 0) and (len(certs) == 0)
        
        if is_blank_sheet:
            st.markdown("""
            <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #2196f3;">
                <h3>👋 Chào bạn mới! Đừng hoang mang.</h3>
                <p>Kết quả cho thấy bạn đang ở vạch xuất phát (Giai đoạn Khởi động).</p>
                <p><b>Tin tốt là:</b> Bạn không cần phải sửa sai cái cũ, chỉ cần xây mới từ đầu. Lộ trình của bạn sẽ rất rõ ràng.</p>
                <p>👉 <b>Lời khuyên:</b> Hãy quên việc "đi xin việc" đi. Mục tiêu 30 ngày tới của bạn chỉ là: <b>Học thuộc quy trình Tiêm & Viết xong cái CV nháp.</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.warning("🎯 Hãy chuyển sang **Tab 2 (Lộ trình)** và bắt đầu ngay từ **Giai đoạn 1: CHUẨN BỊ**.")
            
        else:
            # Logic tính điểm bình thường cho người đã có nền tảng
            total_score = score_knowledge + len(skills) + len(soft_skills) + len(certs)*2 + score_mindset
            
            st.markdown("### 📢 KẾT QUẢ CỦA BẠN:")
            if total_score < 15:
                st.error("🔴 TRẠNG THÁI: CẦN BỔ SUNG GẤP")
                st.write("Bạn có một chút nền tảng nhưng chưa đủ để cạnh tranh. Cần tập trung học kỹ năng thực hành.")
            elif total_score < 28:
                st.warning("🟠 TRẠNG THÁI: TƯƠNG ĐỐI SẴN SÀNG")
                st.write("Bạn khá ổn. Hãy tập trung thi nốt chứng chỉ và luyện phỏng vấn.")
            else:
                st.success("🟢 TRẠNG THÁI: SẴN SÀNG ĐI LÀM")
                st.write("Hồ sơ của bạn rất tốt. Hãy tự tin ứng tuyển.")

# --- TAB 2: LỘ TRÌNH CÁ NHÂN HÓA (CÓ THANH TIẾN ĐỘ) ---
with tab2:
    st.header("📅 Lộ trình Cá nhân hóa")
    [cite_start]st.write("Kế hoạch hành động từng bước để giảm lo âu[cite: 20].")

    # --- 1. TÍNH TOÁN TIẾN ĐỘ ---
    # Danh sách các Key (định danh) của checkbox để theo dõi
    tasks = [
        "t1_1", "t1_2", "t1_3", "t1_4", # Giai đoạn 1
        "t2_1", "t2_2", "t2_3", "t2_4", # Giai đoạn 2
        "t3_1", "t3_2", "t3_3", "t3_4"  # Giai đoạn 3
    ]
    
    # Đếm số task đã hoàn thành (Dựa vào session_state)
    completed_count = 0
    for task in tasks:
        if st.session_state.get(task, False): # Nếu checkbox được tick
            completed_count += 1
            
    # Tính phần trăm
    total_tasks = len(tasks)
    progress_percent = int((completed_count / total_tasks) * 100)
    
    # --- 2. HIỂN THỊ THANH TIẾN ĐỘ ---
    st.divider()
    col_prog1, col_prog2 = st.columns([3, 1])
    
    with col_prog1:
        st.write(f"**Tiến độ tổng thể của bạn:** {completed_count}/{total_tasks} công việc")
        st.progress(progress_percent)
    
    with col_prog2:
        st.metric("Hoàn thành", f"{progress_percent}%")
        
    if progress_percent == 100:
        st.success("🏆 CHÚC MỪNG! BẠN ĐÃ SẴN SÀNG 100% ĐỂ ĐI LÀM!")
        st.balloons()
    elif progress_percent >= 50:
        st.info("🔥 Cố lên! Bạn đã đi được một nửa chặng đường.")
    st.divider()

    # --- 3. CHI TIẾT CÁC GIAI ĐOẠN ---
    
    # [cite_start]Giai đoạn 1 [cite: 42]
    with st.expander("🌱 Giai đoạn 1: CHUẨN BỊ (Nền tảng)", expanded=True):
        st.markdown("### 🎯 Mục tiêu: Lấp lỗ hổng kiến thức")
        st.checkbox("Ôn tập kiến thức chuyên khoa (Nội/Ngoại/Nhi...)", key="t1_1")
        st.checkbox("Thực hành thành thạo các kỹ năng cơ bản", key="t1_2")
        st.checkbox("Rèn luyện kỹ năng mềm (Giao tiếp)", key="t1_3")
        st.checkbox("Chuẩn bị hồ sơ cá nhân (Nháp)", key="t1_4")

    # [cite_start]Giai đoạn 2 [cite: 57]
    with st.expander("🚀 Giai đoạn 2: TIẾP CẬN VIỆC LÀM (Thực chiến)"):
        st.markdown("### 🎯 Mục tiêu: Chứng chỉ & Môi trường thực tế")
        st.checkbox("Tìm hiểu quy trình làm việc tại BV thực tập", key="t2_1")
        st.checkbox("Hoàn tất các chứng chỉ bắt buộc (Tin học, Ngoại ngữ)", key="t2_2")
        st.checkbox("Đăng ký 1 khóa học ngắn hạn mũi nhọn", key="t2_3")
        st.checkbox("Xin nhận xét từ người hướng dẫn để cải thiện", key="t2_4")

    # [cite_start]Giai đoạn 3 [cite: 65]
    with st.expander("⭐ Giai đoạn 3: SẴN SÀNG ỨNG TUYỂN (Về đích)"):
        st.markdown("### 🎯 Mục tiêu: Phỏng vấn & Có việc làm")
        st.checkbox("Hoàn thiện CV & Hồ sơ xin việc (Sang Tab 3)", key="t3_1")
        st.checkbox("Luyện bộ câu hỏi phỏng vấn Điều dưỡng", key="t3_2")
        st.checkbox("Role-play: Xử lý tình huống bệnh nhân khó tính", key="t3_3")
        st.checkbox("Nộp hồ sơ vào nơi đã thực tập (Ưu tiên)", key="t3_4")
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

