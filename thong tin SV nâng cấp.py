import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog


def load_data(file_path):
    """Load data from a CSV file into a numpy array."""
    try:
        data = np.genfromtxt(file_path, delimiter=',', dtype=str, encoding='utf-8', skip_header=1)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return np.array([])


def search_student(data, student_id):
    """Search for a student's information by ID."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    student_data = data[data[:, 0] == student_id]
    print( student_data)
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có ID {student_id}."
    else:
        return "\n".join([", ".join(row) for row in student_data])

def populate_table(tree, data):
    """Populate the Treeview with student data."""
    # Clear any previous rows
    for row in tree.get_children():
        tree.delete(row)

    # Insert new rows from the data
    for row in data:
        tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

def search_subject(data, subject_name):
    """Search for grades of a specific subject."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    subject_data = data[data[:, 2] == subject_name]
    print(subject_data)
    if subject_data.size == 0:
        return f"Không tìm thấy điểm cho môn học {subject_name}."
    else:
        return "\n".join([f"ID: {row[0]}, Tên: {row[1]}, Điểm: {row[3]}" for row in subject_data])


def calculate_average(data, student_id):
    """Calculate the average grade for a specific student using numpy."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    student_data = data[data[:, 0] == student_id]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có ID {student_id}."
    else:
        try:
            grades = student_data[:, 3].astype(float)  # Convert grades to float
            average_grade = np.mean(grades)
            return f"Trung bình cộng điểm của sinh viên có ID {student_id} là {average_grade:.2f}."
        except ValueError:
            return "Có lỗi khi chuyển đổi điểm sang số thực. Vui lòng kiểm tra dữ liệu."

def search_class(data,class_search):
    list_name=[]
    if data.size == 0:
        return "Dữ liệu không được tải."
    
    student_data = data[data[:, 4] == class_search]
    for row in student_data:
        if row[1] in list_name:
            pass
        else:
            list_name.append(row[1])
    str_std="\n".join(list_name)
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có lop {class_search}."
    else:
        return f"Sinh viên trong lớp {class_search} là {str_std}."
def search_low(data,subject_name):
    listname=[]
    if data.size == 0:
        return "Dữ liệu không được tải."
    student_data = data[data[:, 2] == subject_name]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên trong mon {subject_name}."
    else:
        maxpoint=11
        for row in student_data:
            if float(row[3]) <maxpoint:
                maxpoint=float(row[3])
        for row in student_data:
            if float(row[3]) ==maxpoint:
                listname.append(row)
        return "\n".join([f"ID: {r[0]}, Tên: {r[1]}, Điểm: {r[3]},Lớp: {r[4]}" for r in listname])
        
def search_high(data,subject_name):
    listname=[]
    if data.size == 0:
        return "Dữ liệu không được tải."
    student_data = data[data[:, 2] == subject_name]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên trong mon {subject_name}."
    else:
        maxpoint=0
        for row in student_data:
            if float(row[3]) >maxpoint:
                maxpoint=float(row[3])
        for row in student_data:
            if float(row[3]) ==maxpoint:
                listname.append(row)
        return "\n".join([f"ID: {r[0]}, Tên: {r[1]}, Điểm: {r[3]},Lớp: {r[4]}" for r in listname])
            

def search_action():
    choice = choice_var.get()
    student_id = id_entry.get()
    subject_name = subject_entry.get()
    class_search=class_entry.get()

    if choice == '1':  # Tìm kiếm thông tin sinh viên
        result = search_student(data, student_id)
    elif choice == '2':  # Tìm kiếm điểm môn học
        result = search_subject(data, subject_name)
    elif choice == '3':  # Tính TBC điểm của sinh viên
        result = calculate_average(data, student_id)
    elif choice == '4':
        result = search_class(data,class_search)
    elif choice == '5':
        result = search_low(data,subject_name)
    elif choice == '6':
        result = search_high(data,subject_name)
    else:
        result = "Lựa chọn không hợp lệ."

    messagebox.showinfo("Kết quả", result)


def main():
    global data
    file_path = 'New folder\data.csv'  # Đặt đường dẫn đến file dữ liệu của bạn
    data = load_data(file_path)

    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Tìm kiếm thông tin sinh viên")
    # Thêm bảng hiển thị danh sách sinh viên
    tree = ttk.Treeview(root, columns=("ID", "Tên", "Môn học", "Điểm", "Lớp"), show='headings')
    tree.heading("ID", text="ID Sinh viên")
    tree.heading("Tên", text="Tên Sinh viên")
    tree.heading("Môn học", text="Môn học")
    tree.heading("Điểm", text="Điểm")
    tree.heading("Lớp", text="Lớp")
    tree.pack(pady=10, fill='x')

    # Nạp dữ liệu vào bảng
    populate_table(tree, data)

    # Thêm các widget
    tk.Label(root, text="Chọn hành động:").pack(pady=5)

    global choice_var
    choice_var = tk.StringVar(value='1')

    tk.Radiobutton(root, text="Tìm kiếm thông tin sinh viên", variable=choice_var, value='1').pack(anchor='w')
    tk.Radiobutton(root, text="Tìm kiếm điểm môn học", variable=choice_var, value='2').pack(anchor='w')
    tk.Radiobutton(root, text="Tính TBC điểm của sinh viên", variable=choice_var, value='3').pack(anchor='w')
    tk.Radiobutton(root, text="Tìm kiếm theo lớp", variable=choice_var, value='4').pack(anchor='w')
    tk.Radiobutton(root, text="Tìm kiếm sinh viên có điểm thấp nhất của môn học", variable=choice_var, value='5').pack(anchor='w')
    tk.Radiobutton(root, text="Tìm kiếm sinh viên có điểm cao nhất của môn học", variable=choice_var, value='6').pack(anchor='w')
    tk.Label(root, text="ID sinh viên:").pack(pady=5)
    global id_entry
    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    tk.Label(root, text="Tên môn học (nếu có):").pack(pady=5)
    global subject_entry
    subject_entry = tk.Entry(root)
    subject_entry.pack(pady=5)

    tk.Label(root, text="Lớp :").pack(pady=5)
    global class_entry
    class_entry = tk.Entry(root)
    class_entry.pack(pady=5)

    tk.Button(root, text="Tìm kiếm", command=search_action).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
