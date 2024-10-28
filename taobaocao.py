import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt

class StudentReportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Tạo Báo Cáo Học Phần")

        # Dữ liệu sinh viên
        self.data = pd.DataFrame()  # Thay đổi để sử dụng DataFrame

        # Giao diện báo cáo
        self.create_report_frame()

    def create_report_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Nhập Dữ Liệu Từ CSV", command=self.import_csv).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Xem Báo Cáo", command=self.view_report).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Xuất Báo Cáo", command=self.export_report).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Vẽ Biểu Đồ", command=self.plot_chart).grid(row=0, column=3, padx=5)

    def view_report(self):
        report_window = tk.Toplevel(self.root)
        report_window.title("Báo Cáo Học Phần")

        if not self.data.empty:
            for index, entry in self.data.iterrows():
                tk.Label(report_window, text=f"{index + 1}: {entry.to_dict()}").pack()
        else:
            tk.Label(report_window, text="Chưa có dữ liệu nào.").pack()

    def export_report(self):
        if not self.data.empty:
            self.data.to_csv("report.csv", index=False)
            messagebox.showinfo("Thông Báo", "Báo cáo đã được xuất ra file report.csv!")
        else:
            messagebox.showwarning("Cảnh Báo", "Chưa có dữ liệu để xuất!")

    def import_csv(self):
        file_path = filedialog.askopenfilename(title="Chọn File CSV", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                # Đổi tên cột
                self.data.rename(columns={'Điểm': 'Số Lượng Sinh Viên', 'Sinh Viên': 'Số Thứ Tự'}, inplace=True)
                messagebox.showinfo("Thông Báo", "Dữ liệu đã được nhập thành công!")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể nhập dữ liệu: {e}")

    def plot_chart(self):
        if not self.data.empty:
            try:
                # Lấy các cột từ D đến L (cột 3 đến 11 nếu bắt đầu từ 0)
                cols_to_plot = self.data.columns[3:12]
                self.data[cols_to_plot].plot(kind='bar')
                plt.title("Biểu Đồ Học Phần")
                plt.xlabel("Số Thứ Tự")
                plt.ylabel("Số Lượng Sinh Viên")
                plt.legend(title='Môn Học')
                plt.show()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể vẽ biểu đồ: {e}")
        else:
            messagebox.showwarning("Cảnh Báo", "Chưa có dữ liệu để vẽ biểu đồ!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentReportApp(root)
    root.mainloop()
