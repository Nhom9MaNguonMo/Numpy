import sympy as sym
import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog


def main():

    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Ung dung mon giai tich")

    # Thêm các widget
    tk.Label(root, text="Chọn hành động:").pack(pady=5)

    global choice_var
    choice_var = tk.StringVar(value='1')

    tk.Radiobutton(root, text="Đạo hàm", variable=choice_var, value='1').pack(anchor='w')
    tk.Radiobutton(root, text="Tích phân", variable=choice_var, value='2').pack(anchor='w')
    tk.Radiobutton(root, text="Tìm lim", variable=choice_var, value='3').pack(anchor='w')
    tk.Radiobutton(root, text="Khai triển phương trình", variable=choice_var, value='4').pack(anchor='w')
    tk.Radiobutton(root, text="Rút gon phương trình", variable=choice_var, value='5').pack(anchor='w')
    tk.Radiobutton(root, text="Giải phuong trình", variable=choice_var, value='6').pack(anchor='w')
    tk.Label(root, text="Nhập phương trình:").pack(pady=5)
    global id_entry6
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    tk.Label(root, text="Tên môn học (nếu có):").pack(pady=5)
    global subject_entry
    subject_entry = tk.Entry(root)
    subject_entry.pack(pady=5)

    tk.Button(root, text="Confirm").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()