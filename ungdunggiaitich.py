import tkinter as tk
from tkinter import messagebox, filedialog
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import csv

# Khởi tạo biến x
x = symbols('x')

# Hàm tính đạo hàm
def calculate_derivative():
    try:
        function = function_entry.get()
        derivative = diff(sympify(function), x)
        result_var.set(f"Đạo hàm: {derivative}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm tính tích phân
def calculate_integral():
    try:
        function = function_entry.get()
        integral = integrate(sympify(function), x)
        result_var.set(f"Tích phân: {integral}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm tính tích phân theo cận
def calculate_definite_integral():
    try:
        function = function_entry.get()
        lower_bound = float(lower_bound_entry.get())
        upper_bound = float(upper_bound_entry.get())
        integral = integrate(sympify(function), (x, lower_bound, upper_bound))
        result_var.set(f"Tích phân từ {lower_bound} đến {upper_bound}: {integral}")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm vẽ đồ thị
def plot_graph():
    try:
        function = function_entry.get()
        lower_bound = float(lower_bound_entry.get())
        upper_bound = float(upper_bound_entry.get())

        func = sympify(function)
        f = lambdify(x, func, 'numpy')

        x_vals = np.linspace(lower_bound, upper_bound, 400)
        y_vals = f(x_vals)

        plt.figure()
        plt.plot(x_vals, y_vals, label=str(func))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Đồ thị của hàm số')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm xóa các ô nhập và kết quả
def clear_entries():
    function_entry.delete(0, tk.END)
    lower_bound_entry.delete(0, tk.END)
    upper_bound_entry.delete(0, tk.END)
    result_var.set("")

# Hàm nhập dữ liệu từ file CSV
def load_from_csv():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        if len(data[0]) == 1:  # Nếu chỉ có một cột, giả sử đó là hàm số
            function_entry.delete(0, tk.END)
            function_entry.insert(0, data[0][0])
        elif len(data[0]) == 3:  # Nếu có ba cột, giả sử đó là hàm số và cận trên dưới
            function_entry.delete(0, tk.END)
            function_entry.insert(0, data[0][0])
            lower_bound_entry.delete(0, tk.END)
            lower_bound_entry.insert(0, data[0][1])
            upper_bound_entry.delete(0, tk.END)
            upper_bound_entry.insert(0, data[0][2])
        else:
            messagebox.showerror("Lỗi", "Định dạng file CSV không hợp lệ.")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Khởi tạo giao diện chính
root = tk.Tk()
root.title("Phần mềm Hỗ trợ Học tập Giải tích")

# Frame cho nhập và chức năng
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

# Nhập hàm số
tk.Label(menu_frame, text="Nhập hàm số:").pack(side=tk.LEFT)
function_entry = tk.Entry(menu_frame)
function_entry.pack(side=tk.LEFT)
derivative_button = tk.Button(menu_frame, text="Đạo Hàm", command=calculate_derivative)
derivative_button.pack(side=tk.LEFT)
integral_button = tk.Button(menu_frame, text="Tích Phân", command=calculate_integral)
integral_button.pack(side=tk.LEFT)
definite_integral_button = tk.Button(menu_frame, text="Tích Phân Theo Cận", command=calculate_definite_integral)
definite_integral_button.pack(side=tk.LEFT)

# Nhập cận dưới và cận trên cho vẽ đồ thị và tính tích phân
tk.Label(menu_frame, text="Cận dưới:").pack(side=tk.LEFT)
lower_bound_entry = tk.Entry(menu_frame, width=5)
lower_bound_entry.pack(side=tk.LEFT)
tk.Label(menu_frame, text="Cận trên:").pack(side=tk.LEFT)
upper_bound_entry = tk.Entry(menu_frame, width=5)
upper_bound_entry.pack(side=tk.LEFT)
plot_button = tk.Button(menu_frame, text="Vẽ Đồ Thị", command=plot_graph)
plot_button.pack(side=tk.LEFT)

# Nút để nhập dữ liệu từ file CSV
load_button = tk.Button(root, text="Nhập từ CSV", command=load_from_csv)
load_button.pack(pady=10)

# Kết quả
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

# Nút làm mới
clear_button = tk.Button(root, text="Làm Mới", command=clear_entries)
clear_button.pack(pady=10)

# Chạy giao diện
root.mainloop()
