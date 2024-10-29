import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove

def capture_image():
    global img
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cap.release()
    if ret:
        show_image(img)
# Hàm để mở và chọn ảnh
def open_image():
    global img, img_display
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
    if filepath:
        img = cv2.imread(filepath)
        show_image(img)

# Hàm hiển thị ảnh gốc lên giao diện
def show_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)
    panel_original.config(image=img_tk)
    panel_original.image = img_tk

# Hàm xử lý và hiển thị ảnh sau khi áp dụng bộ lọc
def apply_filter(filter_type):
    if img is not None:
        if filter_type == "blur":
            processed_img = cv2.GaussianBlur(img, (15, 15), 0)
        elif filter_type == "sharpen":
            kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
            processed_img = cv2.filter2D(img, -1, kernel)
        elif filter_type == "gray":
            processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            processed_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)

        show_processed_image(processed_img)

# Hiển thị ảnh đã xử lý lên giao diện
def show_processed_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)
    panel_processed.config(image=img_tk)
    panel_processed.image = img_tk

# Hàm để lưu ảnh đã xử lý
def save_image():
    if img is not None:
        filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if filepath:
            cv2.imwrite(filepath, img)
            print(f"Ảnh đã được lưu tại {filepath}")

def remove_background():
    global img
    if img is not None:
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # rect = (10, 10, img.shape[1] - 20, img.shape[0] - 20)  # Vùng chọn bao quanh đối tượng chính
        # cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
       
      


        # mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        # img_nobg = img * mask2[:, :, np.newaxis]  # Xóa nền
        img_nobg=remove(img)


        show_processed_image(img_nobg)  # Hiển thị ảnh đã xử lý


# Giao diện Tkinter
root = Tk()
root.title("Ứng dụng xử lý ảnh")

# Panel hiển thị ảnh gốc
panel_original = Label(root)
panel_original.grid(row=0, column=0)

# Panel hiển thị ảnh đã xử lý
panel_processed = Label(root)
panel_processed.grid(row=0, column=1)

# Các nút chức năng
btn_open = Button(root, text="Chọn ảnh", command=open_image)
btn_open.grid(row=1, column=0, padx=10, pady=10)

btn_blur = Button(root, text="Làm mờ", command=lambda: apply_filter("blur"))
btn_blur.grid(row=1, column=1, padx=10, pady=10)

btn_sharpen = Button(root, text="Tăng độ nét", command=lambda: apply_filter("sharpen"))
btn_sharpen.grid(row=2, column=1, padx=10, pady=10)

btn_gray = Button(root, text="Chuyển trắng đen", command=lambda: apply_filter("gray"))
btn_gray.grid(row=3, column=1, padx=10, pady=10)
btn_capture = Button(root, text="Chụp ảnh", command=capture_image)
btn_capture.grid(row=1, column=2, padx=10, pady=10)
btn_remove_bg = Button(root, text="Xóa phông", command=remove_background)
btn_remove_bg.grid(row=4, column=0, padx=10, pady=10)


btn_save = Button(root, text="Lưu ảnh", command=save_image)
btn_save.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
