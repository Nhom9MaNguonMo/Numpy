import tkinter as tk
from tkinter import messagebox
import numpy as np

# Hàm mở cửa sổ cộng hai ma trận
def open_addition_window():
    new_window = tk.Toplevel(root)
    new_window.title("Cộng hai ma trận")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số nguyên
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số nguyên.")
                row.append(int(value))  # Chuyển đổi thành số nguyên
            matrix.append(row)
        return np.array(matrix)

    def calculate_addition():
        try:
            rows_A = entry_rows_A.get()
            cols_A = entry_cols_A.get()
            rows_B = entry_rows_B.get()
            cols_B = entry_cols_B.get()

            # Kiểm tra không để trống và chỉ nhập số
            if not rows_A.isdigit() or not cols_A.isdigit() or not rows_B.isdigit() or not cols_B.isdigit():
                raise ValueError("Số dòng và số cột phải là số và không được để trống.")

            rows_A = int(rows_A)
            cols_A = int(cols_A)
            rows_B = int(rows_B)
            cols_B = int(cols_B)

            # Kiểm tra kích thước ma trận
            if (rows_A, cols_A) != (rows_B, cols_B):
                raise ValueError("Hai ma trận phải có cùng kích thước để cộng.")

            A = get_matrix_from_entries(matrix_A_entries)
            B = get_matrix_from_entries(matrix_B_entries)

            result = A + B
            label_result.config(text=f"Kết quả:\n{result}")
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))
        except Exception as e:
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi không xác định.")

    matrix_A_entries = []
    matrix_B_entries = []

    label_size_A = tk.Label(new_window, text="Nhập kích thước ma trận A:")
    label_size_A.grid(row=0, column=0, columnspan=2)

    label_rows_A = tk.Label(new_window, text="Số dòng:")
    label_rows_A.grid(row=1, column=0)
    entry_rows_A = tk.Entry(new_window, width=5)
    entry_rows_A.grid(row=1, column=1)

    label_cols_A = tk.Label(new_window, text="Số cột:")
    label_cols_A.grid(row=1, column=2)
    entry_cols_A = tk.Entry(new_window, width=5)
    entry_cols_A.grid(row=1, column=3)

    label_size_B = tk.Label(new_window, text="Nhập kích thước ma trận B (cùng kích thước với A):")
    label_size_B.grid(row=2, column=0, columnspan=2)

    label_rows_B = tk.Label(new_window, text="Số dòng:")
    label_rows_B.grid(row=3, column=0)
    entry_rows_B = tk.Entry(new_window, width=5)
    entry_rows_B.grid(row=3, column=1)

    label_cols_B = tk.Label(new_window, text="Số cột:")
    label_cols_B.grid(row=3, column=2)
    entry_cols_B = tk.Entry(new_window, width=5)
    entry_cols_B.grid(row=3, column=3)

    def generate_matrix_entries():
        nonlocal matrix_A_entries, matrix_B_entries
        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            rows_B = int(entry_rows_B.get())
            cols_B = int(entry_cols_B.get())

            if (rows_A, cols_A) != (rows_B, cols_B):
                messagebox.showerror("Lỗi", "Kích thước hai ma trận phải giống nhau.")
                return

            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=5, column=0, columnspan=4)
            tk.Label(frame_matrix_A, text="Nhập ma trận A:").grid(row=0, column=0, columnspan=cols_A)
            matrix_A_entries = create_matrix_entries(rows_A, cols_A, frame_matrix_A)

            frame_matrix_B = tk.Frame(new_window)
            frame_matrix_B.grid(row=6, column=0, columnspan=4)
            tk.Label(frame_matrix_B, text="Nhập ma trận B:").grid(row=0, column=0, columnspan=cols_B)
            matrix_B_entries = create_matrix_entries(rows_B, cols_B, frame_matrix_B)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số dòng và số cột.")

    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=4, column=0, columnspan=4)

    button_calculate = tk.Button(new_window, text="Tính toán", command=calculate_addition)
    button_calculate.grid(row=7, column=0, columnspan=4)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=8, column=0, columnspan=4)

# Hàm mở cửa sổ trừ hai ma trận
def open_subtraction_window():
    new_window = tk.Toplevel(root)
    new_window.title("Trừ hai ma trận")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số nguyên
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số nguyên.")
                row.append(int(value))  # Chuyển đổi thành số nguyên
            matrix.append(row)
        return np.array(matrix)

    def calculate_subtraction():
        try:
            rows_A = entry_rows_A.get()
            cols_A = entry_cols_A.get()
            rows_B = entry_rows_B.get()
            cols_B = entry_cols_B.get()

            # Kiểm tra không để trống và chỉ nhập số
            if not rows_A.isdigit() or not cols_A.isdigit() or not rows_B.isdigit() or not cols_B.isdigit():
                raise ValueError("Số dòng và số cột phải là số và không được để trống.")

            rows_A = int(rows_A)
            cols_A = int(cols_A)
            rows_B = int(rows_B)
            cols_B = int(cols_B)

            # Kiểm tra kích thước ma trận
            if (rows_A, cols_A) != (rows_B, cols_B):
                raise ValueError("Hai ma trận phải có cùng kích thước để cộng.")

            A = get_matrix_from_entries(matrix_A_entries)
            B = get_matrix_from_entries(matrix_B_entries)
            result = A - B
            label_result.config(text=f"Kết quả:\n{result}")
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))
        except Exception as e:
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi không xác định.")

    matrix_A_entries = []
    matrix_B_entries = []

    label_size_A = tk.Label(new_window, text="Nhập kích thước ma trận A:")
    label_size_A.grid(row=0, column=0, columnspan=2)

    label_rows_A = tk.Label(new_window, text="Số dòng:")
    label_rows_A.grid(row=1, column=0)
    entry_rows_A = tk.Entry(new_window, width=5)
    entry_rows_A.grid(row=1, column=1)

    label_cols_A = tk.Label(new_window, text="Số cột:")
    label_cols_A.grid(row=1, column=2)
    entry_cols_A = tk.Entry(new_window, width=5)
    entry_cols_A.grid(row=1, column=3)

    label_size_B = tk.Label(new_window, text="Nhập kích thước ma trận B (cùng kích thước với A):")
    label_size_B.grid(row=2, column=0, columnspan=2)

    label_rows_B = tk.Label(new_window, text="Số dòng:")
    label_rows_B.grid(row=3, column=0)
    entry_rows_B = tk.Entry(new_window, width=5)
    entry_rows_B.grid(row=3, column=1)

    label_cols_B = tk.Label(new_window, text="Số cột:")
    label_cols_B.grid(row=3, column=2)
    entry_cols_B = tk.Entry(new_window, width=5)
    entry_cols_B.grid(row=3, column=3)

    def generate_matrix_entries():
        nonlocal matrix_A_entries, matrix_B_entries
        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            rows_B = int(entry_rows_B.get())
            cols_B = int(entry_cols_B.get())

            if (rows_A, cols_A) != (rows_B, cols_B):
                messagebox.showerror("Lỗi", "Kích thước hai ma trận phải giống nhau.")
                return

            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=5, column=0, columnspan=4)
            tk.Label(frame_matrix_A, text="Nhập ma trận A:").grid(row=0, column=0, columnspan=cols_A)
            matrix_A_entries = create_matrix_entries(rows_A, cols_A, frame_matrix_A)

            frame_matrix_B = tk.Frame(new_window)
            frame_matrix_B.grid(row=6, column=0, columnspan=4)
            tk.Label(frame_matrix_B, text="Nhập ma trận B:").grid(row=0, column=0, columnspan=cols_B)
            matrix_B_entries = create_matrix_entries(rows_B, cols_B, frame_matrix_B)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số dòng và số cột.")

    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=4, column=0, columnspan=4)

    button_calculate = tk.Button(new_window, text="Tính toán", command=calculate_subtraction)
    button_calculate.grid(row=7, column=0, columnspan=4)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=8, column=0, columnspan=4)

# Hàm mở cửa sổ nhân hai ma trận
def open_multiplication_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nhân hai ma trận")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số nguyên
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số nguyên.")
                row.append(int(value))  # Chuyển đổi thành số nguyên
            matrix.append(row)
        return np.array(matrix)

    def calculate_multiplication():
        try:
            rows_A = entry_rows_A.get()
            cols_A = entry_cols_A.get()
            rows_B = entry_rows_B.get()
            cols_B = entry_cols_B.get()

            # Kiểm tra không để trống và chỉ nhập số
            if not rows_A.isdigit() or not cols_A.isdigit() or not rows_B.isdigit() or not cols_B.isdigit():
                raise ValueError("Số dòng và số cột phải là số và không được để trống.")

            rows_A = int(rows_A)
            cols_A = int(cols_A)
            rows_B = int(rows_B)
            cols_B = int(cols_B)

            # Kiểm tra kích thước ma trận
            if  cols_A != rows_B:
                raise ValueError("Cột ma trận A và ma trận B không giống nhau.")

            A = get_matrix_from_entries(matrix_A_entries)
            B = get_matrix_from_entries(matrix_B_entries)

            result = A @ B
            label_result.config(text=f"Kết quả nhân:\n{result}")
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))
        except Exception as e:
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi không xác định.")


    matrix_A_entries = []
    matrix_B_entries = []

    label_size_A = tk.Label(new_window, text="Nhập kích thước ma trận A:")
    label_size_A.grid(row=0, column=0, columnspan=2)

    label_rows_A = tk.Label(new_window, text="Số dòng:")
    label_rows_A.grid(row=1, column=0)
    entry_rows_A = tk.Entry(new_window, width=5)
    entry_rows_A.grid(row=1, column=1)

    label_cols_A = tk.Label(new_window, text="Số cột:")
    label_cols_A.grid(row=1, column=2)
    entry_cols_A = tk.Entry(new_window, width=5)
    entry_cols_A.grid(row=1, column=3)

    label_size_B = tk.Label(new_window, text="Nhập kích thước ma trận B:")
    label_size_B.grid(row=2, column=0, columnspan=2)

    label_rows_B = tk.Label(new_window, text="Số dòng:")
    label_rows_B.grid(row=3, column=0)
    entry_rows_B = tk.Entry(new_window, width=5)
    entry_rows_B.grid(row=3, column=1)

    label_cols_B = tk.Label(new_window, text="Số cột:")
    label_cols_B.grid(row=3, column=2)
    entry_cols_B = tk.Entry(new_window, width=5)
    entry_cols_B.grid(row=3, column=3)

    def generate_matrix_entries():
        nonlocal matrix_A_entries, matrix_B_entries

        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            rows_B = int(entry_rows_B.get())
            cols_B = int(entry_cols_B.get())

            if cols_A != rows_B:
                messagebox.showerror("Lỗi", "Cột ma trận A và ma trận B không giống nhau.")
                return

            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=5, column=0, columnspan=4)
            tk.Label(frame_matrix_A, text="Nhập ma trận A:").grid(row=0, column=0, columnspan=cols_A)
            matrix_A_entries = create_matrix_entries(rows_A, cols_A, frame_matrix_A)

            frame_matrix_B = tk.Frame(new_window)
            frame_matrix_B.grid(row=6, column=0, columnspan=4)
            tk.Label(frame_matrix_B, text="Nhập ma trận B:").grid(row=0, column=0, columnspan=cols_B)
            matrix_B_entries = create_matrix_entries(rows_B, cols_B, frame_matrix_B)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số dòng và số cột.")


    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=4, column=0, columnspan=4)

    button_calculate = tk.Button(new_window, text="Tính toán", command=calculate_multiplication)
    button_calculate.grid(row=7, column=0, columnspan=4)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=8, column=0, columnspan=4)

# Hàm mở cửa sổ chia hai ma trận
def open_division_window():
    new_window = tk.Toplevel(root)
    new_window.title("Chia hai ma trận")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số.")
                row.append(float(value))  # Chuyển đổi thành số
            matrix.append(row)
        return np.array(matrix)

    def calculate_division():
        try:
            rows_A = entry_rows_A.get().strip()
            cols_A = entry_cols_A.get().strip()
            rows_B = entry_rows_B.get().strip()
            cols_B = entry_cols_B.get().strip()

            # Kiểm tra không để trống và chỉ nhập số
            if rows_A == "" or cols_A == "" or rows_B == "" or cols_B == "":
                raise ValueError("Số dòng và số cột không được để trống.")
            
            if not (rows_A.lstrip('-').isdigit() and cols_A.lstrip('-').isdigit() and 
                    rows_B.lstrip('-').isdigit() and cols_B.lstrip('-').isdigit()):
                raise ValueError("Số dòng và số cột phải là số nguyên.")

            rows_A = int(rows_A)
            cols_A = int(cols_A)
            rows_B = int(rows_B)
            cols_B = int(cols_B)
            
            if cols_A != rows_B:
                raise ValueError("Kích thước cột A và hàng B không khớp.")

            A = get_matrix_from_entries(matrix_A_entries)
            B = get_matrix_from_entries(matrix_B_entries)

            if B.shape[0] != B.shape[1]:
                raise ValueError("Ma trận B phải là hình vuông.")

            B_inv = np.linalg.inv(B)
            # Tính toán A / B phần tử
            result = np.dot(A, B_inv)
            label_result.config(text=f"Kết quả chia:\n{result}")
        except np.linalg.LinAlgError:
            messagebox.showerror("Lỗi", "Ma trận B không khả nghịch. Không thực hiện được phép chia.")
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))
        except Exception as e:
            messagebox.showerror("Lỗi", "Đã xảy ra lỗi không xác định.")

    matrix_A_entries = []
    matrix_B_entries = []

    label_size_A = tk.Label(new_window, text="Nhập kích thước ma trận A:")
    label_size_A.grid(row=0, column=0, columnspan=2)

    label_rows_A = tk.Label(new_window, text="Số dòng:")
    label_rows_A.grid(row=1, column=0)
    entry_rows_A = tk.Entry(new_window, width=5)
    entry_rows_A.grid(row=1, column=1)

    label_cols_A = tk.Label(new_window, text="Số cột:")
    label_cols_A.grid(row=1, column=2)
    entry_cols_A = tk.Entry(new_window, width=5)
    entry_cols_A.grid(row=1, column=3)

    label_size_B = tk.Label(new_window, text="Nhập kích thước ma trận B:")
    label_size_B.grid(row=2, column=0, columnspan=2)

    label_rows_B = tk.Label(new_window, text="Số dòng:")
    label_rows_B.grid(row=3, column=0)
    entry_rows_B = tk.Entry(new_window, width=5)
    entry_rows_B.grid(row=3, column=1)

    label_cols_B = tk.Label(new_window, text="Số cột:")
    label_cols_B.grid(row=3, column=2)
    entry_cols_B = tk.Entry(new_window, width=5)
    entry_cols_B.grid(row=3, column=3)

    def generate_matrix_entries():
        nonlocal matrix_A_entries, matrix_B_entries

        try:
            rows_A = int(entry_rows_A.get().strip())
            cols_A = int(entry_cols_A.get().strip())
            rows_B = int(entry_rows_B.get().strip())
            cols_B = int(entry_cols_B.get().strip())

            if cols_A != rows_B:
                messagebox.showerror("Lỗi", "Kích thước cột A và hàng B không khớp.")
                return

            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=5, column=0, columnspan=4)
            tk.Label(frame_matrix_A, text="Nhập ma trận A:").grid(row=0, column=0, columnspan=cols_A)
            matrix_A_entries = create_matrix_entries(rows_A, cols_A, frame_matrix_A)

            frame_matrix_B = tk.Frame(new_window)
            frame_matrix_B.grid(row=6, column=0, columnspan=4)
            tk.Label(frame_matrix_B, text="Nhập ma trận B:").grid(row=0, column=0, columnspan=cols_B)
            matrix_B_entries = create_matrix_entries(rows_B, cols_B, frame_matrix_B)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số dòng và số cột và không để trống.")

    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=4, column=0, columnspan=4)

    button_calculate = tk.Button(new_window, text="Tính toán", command=calculate_division)
    button_calculate.grid(row=7, column=0, columnspan=4)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=8, column=0, columnspan=4)

# Hàm mở cửa sổ tìm hạng ma trận
def open_rank_window():
    new_window = tk.Toplevel(root)
    new_window.title("Tìm hạng ma trận")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số nguyên
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số nguyên.")
                row.append(int(value))  # Chuyển đổi thành số nguyên
            matrix.append(row)
        return np.array(matrix)
           

    def calculate_rank():
        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            # Kiểm tra không để trống và chỉ nhập số
            rows_A = entry_rows_A.get().strip()
            cols_A = entry_cols_A.get().strip()

            # Kiểm tra không để trống và chỉ nhập số
            if rows_A == "" or cols_A == "":
                raise ValueError("Số dòng và số cột không được để trống.")
            if not (rows_A.isdigit() and cols_A.isdigit()):
                raise ValueError("Số dòng và số cột phải là số.")

            rows_A = int(rows_A)
            cols_A = int(cols_A)

            A = get_matrix_from_entries(matrix_A_entries)

            # Kiểm tra kích thước ma trận
            if A.shape[0] != rows_A or A.shape[1] != cols_A:
                raise ValueError("Kích thước ma trận không hợp lệ.")

            rank = np.linalg.matrix_rank(A)
            label_result.config(text=f"Hạng của ma trận là: {rank}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    matrix_A_entries = []

    label_size_A = tk.Label(new_window, text="Nhập kích thước ma trận:")
    label_size_A.grid(row=0, column=0, columnspan=2)

    label_rows_A = tk.Label(new_window, text="Số dòng:")
    label_rows_A.grid(row=1, column=0)
    entry_rows_A = tk.Entry(new_window, width=5)
    entry_rows_A.grid(row=1, column=1)

    label_cols_A = tk.Label(new_window, text="Số cột:")
    label_cols_A.grid(row=1, column=2)
    entry_cols_A = tk.Entry(new_window, width=5)
    entry_cols_A.grid(row=1, column=3)

    def generate_matrix_entries():
        nonlocal matrix_A_entries
        
        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            
            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=5, column=0, columnspan=4)
            tk.Label(frame_matrix_A, text="Nhập ma trận A:").grid(row=0, column=0, columnspan=cols_A)
            matrix_A_entries = create_matrix_entries(rows_A, cols_A, frame_matrix_A)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số dòng và số cột và không để trống.")

    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=4, column=0, columnspan=4)

    button_calculate = tk.Button(new_window, text="Tính hạng", command=calculate_rank)
    button_calculate.grid(row=7, column=0, columnspan=4)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=8, column=0, columnspan=4)

# Hàm mở cửa sổ tìm ma trận nghịch đảo
def open_inverse_window():
    new_window = tk.Toplevel(root)
    new_window.title("Tìm ma trận nghịch đảo")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số nguyên
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số nguyên.")
                row.append(int(value))  # Chuyển đổi thành số nguyên
            matrix.append(row)
        return np.array(matrix)

    def calculate_inverse():
        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            # Kiểm tra không để trống và chỉ nhập số
            rows_A = entry_rows_A.get().strip()
            cols_A = entry_cols_A.get().strip()

            # Kiểm tra không để trống và chỉ nhập số
            if rows_A == "" or cols_A == "":
                raise ValueError("Số dòng và số cột không được để trống.")
            if not (rows_A.isdigit() and cols_A.isdigit()):
                raise ValueError("Số dòng và số cột phải là số.")

            rows_A = int(rows_A)
            cols_A = int(cols_A)

            A = get_matrix_from_entries(matrix_A_entries)

            # Kiểm tra kích thước ma trận
            if A.shape[0] != rows_A or A.shape[1] != cols_A:
                raise ValueError("Kích thước ma trận không hợp lệ.")

            inv_A = np.linalg.inv(A)
            label_result.config(text=f"Ma trận nghịch đảo là:\n{inv_A}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    matrix_A_entries = []

    label_size_A = tk.Label(new_window, text="Nhập kích thước ma trận:")
    label_size_A.grid(row=0, column=0, columnspan=2)

    label_rows_A = tk.Label(new_window, text="Số dòng:")
    label_rows_A.grid(row=1, column=0)
    entry_rows_A = tk.Entry(new_window, width=5)
    entry_rows_A.grid(row=1, column=1)

    label_cols_A = tk.Label(new_window, text="Số cột:")
    label_cols_A.grid(row=1, column=2)
    entry_cols_A = tk.Entry(new_window, width=5)
    entry_cols_A.grid(row=1, column=3)

    def generate_matrix_entries():
        nonlocal matrix_A_entries

        try:
            rows_A = int(entry_rows_A.get())
            cols_A = int(entry_cols_A.get())
            
            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=5, column=0, columnspan=4)
            tk.Label(frame_matrix_A, text="Nhập ma trận A:").grid(row=0, column=0, columnspan=cols_A)
            matrix_A_entries = create_matrix_entries(rows_A, cols_A, frame_matrix_A)

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho số dòng và số cột và không để trống.")

    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=4, column=0, columnspan=4)

    button_calculate = tk.Button(new_window, text="Tính nghịch đảo", command=calculate_inverse)
    button_calculate.grid(row=7, column=0, columnspan=4)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=8, column=0, columnspan=4)

# Hàm mở cửa sổ giải hệ phương trình
def open_solve_system_window():
    new_window = tk.Toplevel(root)
    new_window.title("Giải hệ phương trình")

    def create_matrix_entries(rows, cols, frame):
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get().strip()  # Xóa khoảng trắng
                # Kiểm tra không được để trống và phải là số nguyên
                if value == "" or not value.lstrip('-').isdigit():  
                    raise ValueError("Các ô nhập ma trận không được để trống và phải là số nguyên.")
                row.append(int(value))  # Chuyển đổi thành số nguyên
            matrix.append(row)
        return np.array(matrix)

    def calculate_system():
        try:
            n = entry_unknowns.get().strip()
            if n == "":
                raise ValueError("Số ẩn không được để trống.")

            # Kiểm tra nếu n là số nguyên
            if not n.lstrip('-').isdigit():
                raise ValueError("Số ẩn phải là số nguyên.")

            n = int(n)  # Chuyển đổi thành số nguyên
            A = get_matrix_from_entries(matrix_A_entries)
            B = get_matrix_from_entries(matrix_B_entries)

            if A.shape[0] != n or A.shape[1] != n:
                raise ValueError("Ma trận hệ số phải là hình vuông và có kích thước n x n.")
            if B.shape[0] != n or B.shape[1] != 1:
                raise ValueError("Ma trận hằng số phải có kích thước n x 1.")

            solution = np.linalg.solve(A, B)
            label_result.config(text=f"Kết quả:\n{solution}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    matrix_A_entries = []
    matrix_B_entries = []

    label_size = tk.Label(new_window, text="Nhập số ẩn:")
    label_size.grid(row=0, column=0)

    entry_unknowns = tk.Entry(new_window, width=5)
    entry_unknowns.grid(row=0, column=1)

    def generate_matrix_entries():
        nonlocal matrix_A_entries, matrix_B_entries
        try:
            n = entry_unknowns.get().strip()
            if n == "" or not n.lstrip('-').isdigit():
                raise ValueError("Số ẩn phải là số nguyên dương và không được để trống.")
            
            n = int(n)  # Chuyển đổi thành số nguyên

            frame_matrix_A = tk.Frame(new_window)
            frame_matrix_A.grid(row=2, column=0, columnspan=2)
            tk.Label(frame_matrix_A, text="Nhập ma trận hệ số A:").grid(row=0, column=0, columnspan=n)
            matrix_A_entries = create_matrix_entries(n, n, frame_matrix_A)

            frame_matrix_B = tk.Frame(new_window)
            frame_matrix_B.grid(row=3, column=0, columnspan=2)
            tk.Label(frame_matrix_B, text="Nhập ma trận hằng số B:").grid(row=0, column=0, columnspan=1)
            matrix_B_entries = create_matrix_entries(n, 1, frame_matrix_B)

        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    button_generate_matrix = tk.Button(new_window, text="Nhập ma trận", command=generate_matrix_entries)
    button_generate_matrix.grid(row=1, column=0, columnspan=2)

    button_calculate = tk.Button(new_window, text="Giải hệ phương trình", command=calculate_system)
    button_calculate.grid(row=4, column=0, columnspan=2)

    label_result = tk.Label(new_window, text="Kết quả:")
    label_result.grid(row=5, column=0, columnspan=2)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng học tập đại số")

# Tạo các nút để mở các chức năng
button_add = tk.Button(root, text="Cộng hai ma trận", command=open_addition_window)
button_add.pack(pady=5)

button_subtract = tk.Button(root, text="Trừ hai ma trận", command=open_subtraction_window)
button_subtract.pack(pady=5)

button_multiply = tk.Button(root, text="Nhân hai ma trận", command=open_multiplication_window)
button_multiply.pack(pady=5)

button_divide = tk.Button(root, text="Chia hai ma trận", command=open_division_window)
button_divide.pack(pady=5)

button_rank = tk.Button(root, text="Tìm hạng ma trận", command=open_rank_window)
button_rank.pack(pady=5)

button_inverse = tk.Button(root, text="Tìm ma trận nghịch đảo", command=open_inverse_window)
button_inverse.pack(pady=5)

button_solve_system = tk.Button(root, text="Giải hệ phương trình", command=open_solve_system_window)
button_solve_system.pack(pady=5)

root.mainloop()
