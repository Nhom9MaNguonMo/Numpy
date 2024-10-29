import numpy as np
import tkinter as tk
from tkinter import messagebox

# Hàm tạo các ô nhập cho hệ số và hằng số
def create_entries():
    try:
        # Xóa các ô nhập trước đó nếu có
        for widget in frame.winfo_children():
            widget.destroy()

        rows = int(num_rows_entry.get())
        if rows <= 0:
            raise ValueError("Số lượng phương trình phải lớn hơn 0")

        global coefficient_entries, constant_entries
        coefficient_entries = []
        constant_entries = []

        # Tạo ô nhập cho từng phương trình
        for i in range(rows):
            row_coeffs = []
            for j in range(rows):  # Tạo ô cho hệ số
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_coeffs.append(entry)
            coefficient_entries.append(row_coeffs)

            constant_entry = tk.Entry(frame, width=5)  # Ô nhập cho hằng số
            constant_entry.grid(row=i, column=rows)
            constant_entries.append(constant_entry)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ.")

# Hàm giải hệ phương trình
def solve_system():
    try:
        rows = len(coefficient_entries)
        coefficients = []
        constants = []

        for i in range(rows):
            coeffs = [float(entry.get()) for entry in coefficient_entries[i]]
            coefficients.append(coeffs)
            constants.append(float(constant_entries[i].get()))

        # Giải hệ phương trình
        A = np.array(coefficients)
        B = np.array(constants)
        solution = np.linalg.solve(A, B)

        result_var.set(f"Nghiệm: {solution}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập các giá trị hợp lệ.")
    except np.linalg.LinAlgError:
        result_var.set("Hệ không có nghiệm hoặc có vô số nghiệm.")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Giao diện
root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")

# Nhập số lượng phương trình
tk.Label(root, text="Số lượng phương trình (n):").grid(row=0, column=0)
num_rows_entry = tk.Entry(root)
num_rows_entry.grid(row=0, column=1)

num_rows_button = tk.Button(root, text="Tạo ô nhập", command=create_entries)
num_rows_button.grid(row=0, column=2)

# Frame để chứa các ô nhập
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=3)

solve_button = tk.Button(root, text="Giải", command=solve_system)
solve_button.grid(row=2, column=0, columnspan=3)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
