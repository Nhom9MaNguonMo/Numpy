import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

# Đọc dữ liệu từ file CSV
df = pd.read_csv('diemPython.csv', index_col=0, header=0)

# Hàm hiển thị tổng số sinh viên
def tong_sv():
    tong_sv = df['Số SV'].sum()
    messagebox.showinfo("Tổng số sinh viên", f'Tổng số sinh viên đi thi: {tong_sv}')

# Hàm tìm lớp có nhiều sinh viên đạt điểm A nhất
def lop_nhieu_diemA():
    diemA = df['Loại A']
    lop_nhieu_diemA_nhat = df.loc[diemA.idxmax(), 'Mã lớp']
    so_sv_diemA_nhat = diemA.max()
    messagebox.showinfo("Lớp có nhiều điểm A nhất", 
                        f'Lớp {lop_nhieu_diemA_nhat} có {so_sv_diemA_nhat} sinh viên đạt điểm A')

# Hàm vẽ đồ thị phân bố điểm A và B+
def ve_do_thi():
    plt.plot(df['Mã lớp'], df['Loại A'], 'r-', label="Điểm A")
    plt.plot(df['Mã lớp'], df['Loại B+'], 'g-', label="Điểm B+")
    plt.xlabel('Mã lớp')
    plt.ylabel('Số sinh viên đạt điểm')
    plt.legend(loc='upper right')
    plt.xticks(rotation=90)
    plt.title("Phân bố điểm A và B+ theo Mã lớp")
    plt.show()

# Hàm vẽ đồ thị cột cho các loại điểm
def ve_do_thi_loai_diem():
    phan_loai_diem = ['Loại A+', 'Loại A', 'Loại B+', 'Loại B', 'Loại C+', 'Loại C', 'Loại D+', 'Loại D', 'Loại F']
    so_luong_sinh_vien = df[phan_loai_diem].sum().values

    # Tạo đồ thị cột
    plt.bar(phan_loai_diem, so_luong_sinh_vien, color=['gold', 'green', 'blue', 'cyan', 'purple', 'orange', 'pink', 'red', 'brown'])
    plt.xlabel('Loại điểm')
    plt.ylabel('Số sinh viên')
    plt.title('Số sinh viên đạt các loại điểm')
    plt.xticks(rotation=45)
    plt.show()

# Hàm hiển thị báo cáo dạng bảng với thanh cuộn ngang và tính tổng
def show_table_with_scroll(data, columns, title):
    # Tạo cửa sổ mới để hiển thị bảng
    table_window = tk.Toplevel()
    table_window.title(title)

    # Tạo frame để chứa bảng và thanh cuộn
    frame = ttk.Frame(table_window)
    frame.pack(fill='both', expand=True)

    # Tạo thanh cuộn ngang
    x_scrollbar = ttk.Scrollbar(frame, orient="horizontal")
    x_scrollbar.pack(side="bottom", fill="x")

    # Tạo Treeview để hiển thị bảng
    tree = ttk.Treeview(frame, columns=columns, show='headings', xscrollcommand=x_scrollbar.set)
    tree.pack(expand=True, fill='both')

    # Kết nối thanh cuộn ngang với bảng
    x_scrollbar.config(command=tree.xview)

    # Đặt tiêu đề cho các cột
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    # Thêm dữ liệu vào bảng
    for idx, row in data.iterrows():
        tree.insert('', 'end', values=list(row))

    # Thêm dòng tổng số sinh viên vào đầu cột
    totals = data.sum(numeric_only=True)
    total_row = ['Tổng'] + list(totals)  # Tạo danh sách tổng với 'Tổng' ở cột đầu tiên
    total_row = [total_row[0]] + [str(totals[col]) for col in columns[1:]]  # Chuyển đổi thành chuỗi và căn trái
    tree.insert('', 'end', values=total_row)

# Hàm báo cáo thống kê dạng bảng theo phân loại điểm
def bao_cao_phan_loai_diem():
    phan_loai_diem = ['Loại A+', 'Loại A', 'Loại B+', 'Loại B', 'Loại C+', 'Loại C', 'Loại D+', 'Loại D', 'Loại F']
    bao_cao_diem = df[['Mã lớp'] + phan_loai_diem]
    show_table_with_scroll(bao_cao_diem, ['Mã lớp'] + phan_loai_diem, "Báo cáo phân loại điểm")

# Hàm báo cáo thống kê theo chuẩn đầu ra
def bao_cao_chuan_dau_ra():
    chuan_dau_ra = ['L1', 'L2']
    bao_cao_chuan = df[['Mã lớp'] + chuan_dau_ra]
    show_table_with_scroll(bao_cao_chuan, ['Mã lớp'] + chuan_dau_ra, "Báo cáo chuẩn đầu ra")

# Hàm báo cáo thống kê theo bài kiểm tra TX1, TX2
def bao_cao_kiem_tra():
    bai_kiem_tra = ['TX1', 'TX2']
    bao_cao_kt = df[['Mã lớp'] + bai_kiem_tra]
    show_table_with_scroll(bao_cao_kt, ['Mã lớp'] + bai_kiem_tra, "Báo cáo bài kiểm tra")

# Tạo giao diện chính
root = tk.Tk()
root.title("Phân tích điểm môn Python")

# Tạo các nút cho từng chức năng
btn_tong_sv = ttk.Button(root, text="Tổng số sinh viên", command=tong_sv)
btn_tong_sv.grid(row=0, column=0, padx=10, pady=10)

btn_lop_nhieu_diemA = ttk.Button(root, text="Lớp có nhiều điểm A", command=lop_nhieu_diemA)
btn_lop_nhieu_diemA.grid(row=0, column=1, padx=10, pady=10)

btn_do_thi = ttk.Button(root, text="Vẽ đồ thị A và B+", command=ve_do_thi)
btn_do_thi.grid(row=1, column=0, padx=10, pady=10)

btn_do_thi_loai_diem = ttk.Button(root, text="Vẽ đồ thị loại điểm", command=ve_do_thi_loai_diem)
btn_do_thi_loai_diem.grid(row=1, column=1, padx=10, pady=10)

btn_bao_cao_diem = ttk.Button(root, text="Báo cáo phân loại điểm", command=bao_cao_phan_loai_diem)
btn_bao_cao_diem.grid(row=2, column=0, padx=10, pady=10)

btn_bao_cao_chuan = ttk.Button(root, text="Báo cáo chuẩn đầu ra", command=bao_cao_chuan_dau_ra)
btn_bao_cao_chuan.grid(row=2, column=1, padx=10, pady=10)

btn_bao_cao_kt = ttk.Button(root, text="Báo cáo bài kiểm tra", command=bao_cao_kiem_tra)
btn_bao_cao_kt.grid(row=3, column=0, padx=10, pady=10)

# Chạy giao diện
root.mainloop()
