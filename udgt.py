import sympy as sp
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Tạo cửa sổ chính của ứng dụng
root = Tk()
root.title("Ứng dụng hỗ trợ học Giải Tích")
root.geometry("800x600")

# Hàm xử lý biến số tùy chọn
def get_variable():
    var = nhap_bien.get().strip()
    if not var:
        messagebox.showerror("Lỗi", "Hãy nhập biến số trước khi thực hiện phép tính.")
        return None
    try:
        return sp.symbols(var)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi nhận dạng biến số: {e}")
        return None

# Hàm tính đạo hàm
def tinh_dao_ham():
    bien_so = get_variable()
    if not bien_so:
        return
    ham_so = nhap_ham.get().strip()
    if not ham_so:
        messagebox.showerror("Lỗi", "Hãy nhập hàm số trước khi tính đạo hàm.")
        return
    try:
        ham_sympy = sp.sympify(ham_so)
        dao_ham = sp.diff(ham_sympy, bien_so)
        ket_qua.set(f"Đạo hàm theo {bien_so}: {dao_ham}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi tính đạo hàm: {e}")

# Hàm tính nguyên hàm (tích phân bất định)
def tinh_nguyen_ham():
    bien_so = get_variable()
    if not bien_so:
        return
    ham_so = nhap_ham.get().strip()
    if not ham_so:
        messagebox.showerror("Lỗi", "Hãy nhập hàm số trước khi tính nguyên hàm.")
        return
    try:
        ham_sympy = sp.sympify(ham_so)
        nguyen_ham = sp.integrate(ham_sympy, bien_so)
        ket_qua.set(f"Nguyên hàm theo {bien_so}: {nguyen_ham} + C")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi tính nguyên hàm: {e}")

# Hàm tính tích phân có cận
def tinh_tich_phan():
    bien_so = get_variable()
    if not bien_so:
        return
    ham_so = nhap_ham.get().strip()
    if not ham_so:
        messagebox.showerror("Lỗi", "Hãy nhập hàm số trước khi tính tích phân.")
        return
    try:
        ham_sympy = sp.sympify(ham_so)
        a = nhap_can_duoi.get().strip()
        b = nhap_can_tren.get().strip()

        if a and b:
            a = float(a)
            b = float(b)
            tich_phan = sp.integrate(ham_sympy, (bien_so, a, b))
            ket_qua.set(f"Tích phân từ {a} đến {b} theo {bien_so}: {tich_phan}")
        else:
            messagebox.showerror("Lỗi", "Hãy nhập cả cận trên và cận dưới để tính tích phân có cận.")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi tính tích phân: {e}")

# Hàm vẽ đồ thị
def ve_do_thi():
    bien_so = get_variable()
    if not bien_so:
        return
    ham_so = nhap_ham.get().strip()
    if not ham_so:
        messagebox.showerror("Lỗi", "Hãy nhập hàm số trước khi vẽ đồ thị.")
        return
    try:
        ham_sympy = sp.sympify(ham_so)
        ham_lambdify = sp.lambdify(bien_so, ham_sympy, 'numpy')

        fig, ax = plt.subplots(figsize=(5, 4))
        x_vals = np.linspace(-10, 10, 400)
        y_vals = ham_lambdify(x_vals)

        ax.plot(x_vals, y_vals, label=f'Đồ thị của {ham_so} theo {bien_so}')
        ax.axhline(0, color='black',linewidth=0.5)
        ax.axvline(0, color='black',linewidth=0.5)
        ax.grid(True)
        ax.legend()

        # Vẽ đồ thị trong giao diện
        canvas = FigureCanvasTkAgg(fig, master=frame_do_thi)  
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi vẽ đồ thị: {e}")

# Hàm xóa dữ liệu nhập
def xoa_du_lieu():
    nhap_ham.delete(0, END)
    nhap_bien.delete(0, END)
    nhap_can_duoi.delete(0, END)
    nhap_can_tren.delete(0, END)
    ket_qua.set("")
    # Xóa đồ thị nếu có
    for widget in frame_do_thi.winfo_children():
        widget.destroy()

# Giao diện người dùng
Label(root, text="Nhập hàm số:", font=("Arial", 14)).pack(pady=10)
nhap_ham = Entry(root, font=("Arial", 14), width=30)
nhap_ham.pack(pady=10)

Label(root, text="Nhập biến số (ví dụ: x, y):", font=("Arial", 12)).pack(pady=5)
nhap_bien = Entry(root, font=("Arial", 12), width=10)
nhap_bien.pack(pady=5)

# Cận trên và cận dưới
Label(root, text="Nhập cận dưới (a):", font=("Arial", 12)).pack(pady=5)
nhap_can_duoi = Entry(root, font=("Arial", 12), width=10)
nhap_can_duoi.pack(pady=5)

Label(root, text="Nhập cận trên (b):", font=("Arial", 12)).pack(pady=5)
nhap_can_tren = Entry(root, font=("Arial", 12), width=10)
nhap_can_tren.pack(pady=5)

# Kết quả hiển thị
ket_qua = StringVar()
Label(root, textvariable=ket_qua, font=("Arial", 14), fg="blue").pack(pady=10)

# Khung cho các nút chức năng
frame_nut = Frame(root)
frame_nut.pack(pady=10)

Button(frame_nut, text="Tính đạo hàm", command=tinh_dao_ham, font=("Arial", 12), width=15).grid(row=0, column=0, padx=10, pady=5)
Button(frame_nut, text="Nguyên hàm", command=tinh_nguyen_ham, font=("Arial", 12), width=15).grid(row=0, column=1, padx=10, pady=5)
Button(frame_nut, text="Tích phân có cận", command=tinh_tich_phan, font=("Arial", 12), width=15).grid(row=0, column=2, padx=10, pady=5)
Button(frame_nut, text="Vẽ đồ thị", command=ve_do_thi, font=("Arial", 12), width=15).grid(row=0, column=3, padx=10, pady=5)
Button(frame_nut, text="Xóa dữ liệu", command=xoa_du_lieu, font=("Arial", 12), width=15).grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Khung hiển thị đồ thị
frame_do_thi = Frame(root)
frame_do_thi.pack(pady=10, fill=BOTH, expand=True)

# Khởi chạy ứng dụng
root.mainloop()
