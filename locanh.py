import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.root.geometry("800x600")
        
        self.original_image = None
        self.processed_image = None
        self.cap = None
        
        self.create_widgets()

    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text="Chọn Ảnh", command=self.upload_image, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.upload_button.pack(pady=10)

        self.capture_button = tk.Button(self.root, text="Bắt Đầu Camera", command=self.open_camera, bg="#2196F3", fg="white", font=("Arial", 12))
        self.capture_button.pack(pady=10)

        self.stop_camera_button = tk.Button(self.root, text="Kết Thúc Camera", command=self.stop_camera, bg="#f44336", fg="white", font=("Arial", 12))
        self.stop_camera_button.pack(pady=10)

        self.clear_button = tk.Button(self.root, text="Xóa Tất Cả Dữ Liệu", command=self.clear_data, bg="#f44336", fg="white", font=("Arial", 12))
        self.clear_button.pack(pady=10)

        self.filter_frame = tk.Frame(self.root)
        self.filter_frame.pack(pady=10)

        self.blur_button = tk.Button(self.filter_frame, text="Làm Mờ", command=self.apply_blur, bg="#FFC107", font=("Arial", 10))
        self.blur_button.grid(row=0, column=0, padx=5)

        self.sharp_button = tk.Button(self.filter_frame, text="Tạo Độ Nét", command=self.apply_sharpen, bg="#FFC107", font=("Arial", 10))
        self.sharp_button.grid(row=0, column=1, padx=5)

        self.bw_button = tk.Button(self.filter_frame, text="Đen Trắng", command=self.apply_bw, bg="#FFC107", font=("Arial", 10))
        self.bw_button.grid(row=0, column=2, padx=5)

        self.remove_bg_button = tk.Button(self.filter_frame, text="Xóa Phông (GrabCut)", command=self.remove_background, bg="#FFC107", font=("Arial", 10))
        self.remove_bg_button.grid(row=0, column=3, padx=5)

        self.resize_frame = tk.Frame(self.root)
        self.resize_frame.pack(pady=10)

        self.width_label = tk.Label(self.resize_frame, text="Chiều Rộng (px):", font=("Arial", 10))
        self.width_label.grid(row=0, column=0)

        self.width_entry = tk.Entry(self.resize_frame, width=5)
        self.width_entry.grid(row=0, column=1)

        self.length_label = tk.Label(self.resize_frame, text="Chiều Dài (px):", font=("Arial", 10))
        self.length_label.grid(row=0, column=2)

        self.length_entry = tk.Entry(self.resize_frame, width=5)
        self.length_entry.grid(row=0, column=3)

        self.resize_button = tk.Button(self.resize_frame, text="Thay Đổi Kích Thước", command=self.adjust_size, bg="#FFC107", font=("Arial", 10))
        self.resize_button.grid(row=0, column=4, padx=5)

        self.save_button = tk.Button(self.root, text="Lưu Ảnh", command=self.save_image, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.save_button.pack(pady=10)

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        self.original_label = tk.Label(self.image_frame, text="Ảnh Gốc:", font=("Arial", 14))
        self.original_label.grid(row=0, column=0)

        self.original_canvas = tk.Canvas(self.image_frame, width=400, height=400, bg="lightgray")
        self.original_canvas.grid(row=1, column=0)

        self.processed_label = tk.Label(self.image_frame, text="Ảnh Sau Xử Lý:", font=("Arial", 14))
        self.processed_label.grid(row=0, column=1)

        self.processed_canvas = tk.Canvas(self.image_frame, width=400, height=400, bg="lightgray")
        self.processed_canvas.grid(row=1, column=1)

        self.root.bind("<space>", self.capture_image)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image, self.original_canvas)

    def open_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Lỗi", "Không thể mở camera.")
            return
        
        self.show_camera()

    def show_camera(self):
        ret, frame = self.cap.read()
        if ret:
            self.display_image(frame, self.original_canvas)
            self.root.after(10, self.show_camera)

    def capture_image(self, event=None):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                self.original_image = frame
                self.display_image(self.original_image, self.original_canvas)
                self.processed_image = frame
                self.display_image(self.processed_image, self.processed_canvas)

    def stop_camera(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            messagebox.showinfo("Thông báo", "Camera đã kết thúc.")

    def display_image(self, image, canvas):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(image_rgb, (400, 400))
        img_pil = Image.fromarray(img_resized)
        img_tk = ImageTk.PhotoImage(img_pil)
        canvas.create_image(200, 200, image=img_tk)
        canvas.image = img_tk

    def apply_blur(self):
        if self.original_image is not None:
            self.processed_image = cv2.GaussianBlur(self.original_image, (15, 15), 0)
            self.display_image(self.processed_image, self.processed_canvas)

    def apply_sharpen(self):
        if self.original_image is not None:
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            self.processed_image = cv2.filter2D(self.original_image, -1, kernel)
            self.display_image(self.processed_image, self.processed_canvas)

    def apply_bw(self):
        if self.original_image is not None:
            self.processed_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            self.display_image(self.processed_image, self.processed_canvas)

    def remove_background(self):
        if self.original_image is not None:
            mask = np.zeros(self.original_image.shape[:2], np.uint8)
            bgd_model = np.zeros((1, 65), np.float64)
            fgd_model = np.zeros((1, 65), np.float64)

            # Định nghĩa hình chữ nhật cho vùng foreground
            rect = (10, 10, self.original_image.shape[1]-10, self.original_image.shape[0]-10)

            # Áp dụng GrabCut
            cv2.grabCut(self.original_image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

            # Tạo mặt nạ cho vùng foreground
            mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            self.processed_image = self.original_image * mask2[:, :, np.newaxis]
            self.display_image(self.processed_image, self.processed_canvas)

    def adjust_size(self):
        if self.original_image is not None:
            try:
                width = int(self.width_entry.get())
                length = int(self.length_entry.get())
                self.processed_image = cv2.resize(self.original_image, (width, length))
                self.display_image(self.processed_image, self.processed_canvas)
            except ValueError:
                messagebox.showwarning("Cảnh Báo", "Vui lòng nhập kích thước hợp lệ.")

    def save_image(self):
        if self.processed_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
            if file_path:
                cv2.imwrite(file_path, self.processed_image)
                messagebox.showinfo("Lưu Ảnh", "Ảnh đã được lưu thành công!")

    def clear_data(self):
        self.original_image = None
        self.processed_image = None
        self.original_canvas.delete("all")
        self.processed_canvas.delete("all")
        self.width_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)

        messagebox.showinfo("Xóa Dữ Liệu", "Đã xóa tất cả dữ liệu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
