import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Hàm vẽ đường thẳng
def draw_line():
    try:
        x1, y1 = float(entry_x1.get()), float(entry_y1.get())
        x2, y2 = float(entry_x2.get()), float(entry_y2.get())
        plt.figure()
        plt.plot([x1, x2], [y1, y2], marker='o')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Đường thẳng')
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm vẽ tam giác
def draw_triangle():
    try:
        x1, y1 = float(entry_x1.get()), float(entry_y1.get())
        x2, y2 = float(entry_x2.get()), float(entry_y2.get())
        x3, y3 = float(entry_x3.get()), float(entry_y3.get())
        plt.figure()
        plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], marker='o')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Tam giác')
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Hàm vẽ hình tròn
def draw_circle():
    try:
        x, y = float(entry_x.get()), float(entry_y.get())
        radius = float(entry_radius.get())
        circle = plt.Circle((x, y), radius, fill=False)
        plt.gca().add_patch(circle)
        plt.axis('scaled')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Hình tròn')
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Giao diện chính
root = tk.Tk()
root.title("Phần mềm Hỗ trợ Học tập Hình học")

# Nhập tọa độ cho đường thẳng
tk.Label(root, text="Tọa độ điểm 1: x1, y1").grid(row=0, column=0)
entry_x1 = tk.Entry(root, width=5)
entry_x1.grid(row=0, column=1)
entry_y1 = tk.Entry(root, width=5)
entry_y1.grid(row=0, column=2)

tk.Label(root, text="Tọa độ điểm 2: x2, y2").grid(row=1, column=0)
entry_x2 = tk.Entry(root, width=5)
entry_x2.grid(row=1, column=1)
entry_y2 = tk.Entry(root, width=5)
entry_y2.grid(row=1, column=2)

tk.Button(root, text="Vẽ Đường Thẳng", command=draw_line).grid(row=2, column=0, columnspan=3)

# Nhập tọa độ cho tam giác
tk.Label(root, text="Tọa độ điểm 1: x1, y1").grid(row=3, column=0)
entry_x1.grid(row=3, column=1)
entry_y1.grid(row=3, column=2)

tk.Label(root, text="Tọa độ điểm 2: x2, y2").grid(row=4, column=0)
entry_x2.grid(row=4, column=1)
entry_y2.grid(row=4, column=2)

tk.Label(root, text="Tọa độ điểm 3: x3, y3").grid(row=5, column=0)
entry_x3 = tk.Entry(root, width=5)
entry_x3.grid(row=5, column=1)
entry_y3 = tk.Entry(root, width=5)
entry_y3.grid(row=5, column=2)

tk.Button(root, text="Vẽ Tam Giác", command=draw_triangle).grid(row=6, column=0, columnspan=3)

# Nhập tọa độ và bán kính cho hình tròn
tk.Label(root, text="Tọa độ tâm: x, y").grid(row=7, column=0)
entry_x = tk.Entry(root, width=5)
entry_x.grid(row=7, column=1)
entry_y = tk.Entry(root, width=5)
entry_y.grid(row=7, column=2)

tk.Label(root, text="Bán kính: r").grid(row=8, column=0)
entry_radius = tk.Entry(root, width=5)
entry_radius.grid(row=8, column=1)

tk.Button(root, text="Vẽ Hình Tròn", command=draw_circle).grid(row=9, column=0, columnspan=3)

# Chạy giao diện
root.mainloop()
