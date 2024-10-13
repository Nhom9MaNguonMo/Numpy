import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split
from sklearn import neighbors, linear_model, tree, svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Khởi tạo biến toàn cục
df = None
x = None
y = None
models = {}

# Hàm để load dữ liệu từ file CSV
def load_data():
    global df, x, y
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        x = df.iloc[:, 0:5].values.astype(np.float64)  # Dữ liệu đầu vào
        y = df.iloc[:, 5].values.astype(np.float64)    # Performance Index
        messagebox.showinfo("Tải dữ liệu", "Dữ liệu đã được tải thành công.")
    else:
        messagebox.showerror("Lỗi", "Chưa chọn file dữ liệu!")

# Hàm huấn luyện tất cả các mô hình
def train_all_models():
    global models
    if df is None or x is None or y is None:
        messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước.")
        return
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    
    # KNN
    knn_model = neighbors.KNeighborsRegressor(n_neighbors=3)
    knn_model.fit(X_train, y_train)
    models['KNN'] = knn_model
    
    # Linear Regression
    lr_model = linear_model.LinearRegression()
    lr_model.fit(X_train, y_train)
    models['Hồi quy tuyến tính'] = lr_model
    
    # Decision Tree Regressor
    dtr_model = tree.DecisionTreeRegressor()
    dtr_model.fit(X_train, y_train)
    models['Cây quyết định'] = dtr_model
    
    # Support Vector Regressor
    svr_model = svm.SVR()
    svr_model.fit(X_train, y_train)
    models['SVR'] = svr_model
    
    messagebox.showinfo("Huấn luyện mô hình", "Tất cả các mô hình đã được huấn luyện thành công.")

# Hàm để kiểm tra và so sánh các thuật toán
def compare_models():
    if df is None or x is None or y is None:
        messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước.")
        return
    
    if not models:
        messagebox.showerror("Lỗi", "Vui lòng huấn luyện mô hình trước.")
        return
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    
    mse_scores = {}
    rmse_scores = {}
    mae_scores = {}
    
    for model_name, model in models.items():
        y_predict = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_predict)
        mae = mean_absolute_error(y_test, y_predict)
        rmse = np.sqrt(mse)

        mse_scores[model_name] = mse
        mae_scores[model_name] = mae
        rmse_scores[model_name] = rmse
    
    # Hiển thị kết quả sai số
    result_message = "So sánh các mô hình:\n\n"
    for model_name in models.keys():
        result_message += f"{model_name} - MSE: {mse_scores[model_name]:.2f}, RMSE: {rmse_scores[model_name]:.2f}, MAE: {mae_scores[model_name]:.2f}\n"
    
    messagebox.showinfo("So sánh mô hình", result_message)
    
    # Vẽ đồ thị gộp
    labels = list(models.keys())
    x_axis = np.arange(len(labels))  # Số lượng các mô hình
    width = 0.2  # Độ rộng của các thanh

    fig, ax = plt.subplots(figsize=(10, 6))

    rects1 = ax.bar(x_axis - width, mse_scores.values(), width, label='MSE', color='blue')
    rects2 = ax.bar(x_axis, rmse_scores.values(), width, label='RMSE', color='green')
    rects3 = ax.bar(x_axis + width, mae_scores.values(), width, label='MAE', color='red')

    # Thêm nhãn và tiêu đề
    ax.set_xlabel('Mô hình')
    ax.set_ylabel('Giá trị')
    ax.set_title('So sánh MSE, RMSE, MAE giữa các mô hình')
    ax.set_xticks(x_axis)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Hàm dự đoán kết quả với một mô hình cụ thể
def predict_performance(model_name):
    if df is None or x is None or y is None:
        messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước.")
        return
    
    if model_name not in models:
        messagebox.showerror("Lỗi", f"Vui lòng huấn luyện mô hình {model_name} trước.")
        return
    
    try:
        hours = float(hours_studied_entry.get())
        scores = float(previous_scores_entry.get())
        activities = int(extracurricular_entry.get())
        sleep = float(sleep_hours_entry.get())
        papers = int(sample_papers_entry.get())

        input_data = np.array([[hours, scores, activities, sleep, papers]]).astype(np.float64)
        prediction = models[model_name].predict(input_data)[0]
        messagebox.showinfo("Kết quả dự đoán", f"{model_name} dự đoán chỉ số hiệu suất: {prediction:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đúng các giá trị số.")

# Tạo giao diện bằng Tkinter
def create_gui():
    window = tk.Tk()
    window.title("Dự đoán kết quả học tập sinh viên")

    # Tạo một khung chứa tất cả các phần tử để căn giữa
    frame = tk.Frame(window)
    frame.grid(row=0, column=0, padx=10, pady=10)

    # Nút Load Data
    load_button = tk.Button(frame, text="Tải dữ liệu", command=load_data)
    load_button.grid(row=0, column=0, columnspan=4, pady=5, ipadx=50)

    # Nút Train tất cả các mô hình
    train_button = tk.Button(frame, text="Huấn luyện tất cả mô hình", command=train_all_models)
    train_button.grid(row=1, column=0, columnspan=4, pady=5, ipadx=50)

    # Nút Test và So sánh mô hình
    compare_button = tk.Button(frame, text="So sánh các mô hình", command=compare_models)
    compare_button.grid(row=2, column=0, columnspan=4, pady=5, ipadx=50)

    # Nhập dữ liệu cho dự đoán
    tk.Label(frame, text="Giờ học").grid(row=3, column=0)
    global hours_studied_entry
    hours_studied_entry = tk.Entry(frame)
    hours_studied_entry.grid(row=3, column=1)

    tk.Label(frame, text="Điểm trước đó").grid(row=4, column=0)
    global previous_scores_entry
    previous_scores_entry = tk.Entry(frame)
    previous_scores_entry.grid(row=4, column=1)

    tk.Label(frame, text="Hoạt động ngoại khóa (0 hoặc 1)").grid(row=5, column=0)
    global extracurricular_entry
    extracurricular_entry = tk.Entry(frame)
    extracurricular_entry.grid(row=5, column=1)

    tk.Label(frame, text="Giờ ngủ").grid(row=6, column=0)
    global sleep_hours_entry
    sleep_hours_entry = tk.Entry(frame)
    sleep_hours_entry.grid(row=6, column=1)

    tk.Label(frame, text="Số lượng bài mẫu đã làm").grid(row=7, column=0)
    global sample_papers_entry
    sample_papers_entry = tk.Entry(frame)
    sample_papers_entry.grid(row=7, column=1)

    # Nút dự đoán với các mô hình khác nhau
    knn_button = tk.Button(frame, text="Dự đoán với KNN", command=lambda: predict_performance('KNN'))
    knn_button.grid(row=8, column=0, pady=5, ipadx=10)

    lr_button = tk.Button(frame, text="Dự đoán với Hồi quy tuyến tính", command=lambda: predict_performance('Hồi quy tuyến tính'))
    lr_button.grid(row=8, column=1, pady=5, ipadx=10)

    dtr_button = tk.Button(frame, text="Dự đoán với Cây quyết định", command=lambda: predict_performance('Cây quyết định'))
    dtr_button.grid(row=8, column=2, pady=5, ipadx=10)

    svr_button = tk.Button(frame, text="Dự đoán với SVR", command=lambda: predict_performance('SVR'))
    svr_button.grid(row=8, column=3, pady=5, ipadx=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
