import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split
from sklearn import neighbors, linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Khởi tạo biến toàn cục
df = None
x = None
y = None
model = None

# Hàm để load dữ liệu từ file CSV
def load_data():
    global df, x, y
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        x = df.iloc[:200, 0:5].values.astype(np.float64)  # Dữ liệu đầu vào
        y = df.iloc[:200, 5].values.astype(np.float64)    # Performance Index
        messagebox.showinfo("Load Data", "Data loaded successfully.")

# Hàm huấn luyện mô hình
def train_model(algorithm):
    global model
    if df is None:
        messagebox.showerror("Error", "Please load data first.")
        return
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    
    if algorithm == "KNN":
        model = neighbors.KNeighborsRegressor(n_neighbors=3,p=2)
    elif algorithm == "Linear Regression":
        model = linear_model.LinearRegression()

    model.fit(X_train, y_train)
    messagebox.showinfo("Train Model", f"Model trained using {algorithm}.")

# Hàm để kiểm tra mô hình, tính tỷ lệ so sánh và vẽ đồ thị
def test_model():
    if model is None:
        messagebox.showerror("Error", "Please train the model first.")
        return
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    y_predict = model.predict(X_test)

    mse = mean_squared_error(y_test, y_predict)
    mae = mean_absolute_error(y_test,y_predict)
    rmse = np.sqrt(mse)

    # Tính tỷ lệ so sánh
    greater_than_2 = np.sum(abs(y_test - y_predict) > 2)
    between_1_and_2 = np.sum((abs(y_test - y_predict) > 1) & (abs(y_test - y_predict) <= 2))
    less_than_1 = np.sum(abs(y_test - y_predict) <= 1)

    # Hiển thị sai số và tỷ lệ so sánh
    messagebox.showinfo("Test Result", 
        f"MSE: {mse:.2f}\nMAE: {mae:.2f}\nRMSE: {rmse:.2f}\n\n"
        f"Comparisons:\n> 2 points: {greater_than_2}\n1 to 2 points: {between_1_and_2}\n< 1 point: {less_than_1}"
    )

    # Vẽ biểu đồ cột cho MSE, RMSE, MAE
    metrics = ['MSE', 'RMSE', 'MAE']
    values = [mse, rmse, mae]
    
    plt.figure(figsize=(8, 6))
    plt.bar(metrics, values, color=['blue', 'green', 'red'])
    plt.title('Error Metrics')
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.show()

# Hàm dự đoán kết quả
def predict_performance():
    if model is None:
        messagebox.showerror("Error", "Please train the model first.")
        return
    
    try:
        hours = float(hours_studied_entry.get())
        scores = float(previous_scores_entry.get())
        activities = int(extracurricular_entry.get())
        sleep = float(sleep_hours_entry.get())
        papers = int(sample_papers_entry.get())

        input_data = np.array([[hours, scores, activities, sleep, papers]]).astype(np.float64)
        prediction = model.predict(input_data)[0]
        messagebox.showinfo("Prediction Result", f"Predicted Performance Index: {prediction:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Tạo giao diện bằng Tkinter
def create_gui():
    window = tk.Tk()
    window.title("Student Performance Predictor")

    # Nút Load Data
    load_button = tk.Button(window, text="Load Data", command=load_data)
    load_button.grid(row=0, column=0, pady=5)

    # Nút Train với lựa chọn thuật toán
    train_label = tk.Label(window, text="Choose Algorithm:")
    train_label.grid(row=1, column=0)
    
    algorithm_var = tk.StringVar(value="KNN")
    knn_radio = tk.Radiobutton(window, text="KNN", variable=algorithm_var, value="KNN")
    lr_radio = tk.Radiobutton(window, text="Linear Regression", variable=algorithm_var, value="Linear Regression")
    
    knn_radio.grid(row=1, column=1)
    lr_radio.grid(row=1, column=2)

    train_button = tk.Button(window, text="Train", command=lambda: train_model(algorithm_var.get()))
    train_button.grid(row=1, column=3, pady=5)

    # Nút Test
    test_button = tk.Button(window, text="Test Model", command=test_model)
    test_button.grid(row=2, column=0, pady=5)

    # Nhập dữ liệu cho dự đoán
    tk.Label(window, text="Hours Studied").grid(row=3, column=0)
    global hours_studied_entry
    hours_studied_entry = tk.Entry(window)
    hours_studied_entry.grid(row=3, column=1)

    tk.Label(window, text="Previous Scores").grid(row=4, column=0)
    global previous_scores_entry
    previous_scores_entry = tk.Entry(window)
    previous_scores_entry.grid(row=4, column=1)

    tk.Label(window, text="Extracurricular Activities (0 or 1)").grid(row=5, column=0)
    global extracurricular_entry
    extracurricular_entry = tk.Entry(window)
    extracurricular_entry.grid(row=5, column=1)

    tk.Label(window, text="Sleep Hours").grid(row=6, column=0)
    global sleep_hours_entry
    sleep_hours_entry = tk.Entry(window)
    sleep_hours_entry.grid(row=6, column=1)

    tk.Label(window, text="Sample Question Papers Practiced").grid(row=7, column=0)
    global sample_papers_entry
    sample_papers_entry = tk.Entry(window)
    sample_papers_entry.grid(row=7, column=1)

    # Nút dự đoán
    predict_button = tk.Button(window, text="Predict Performance Index", command=predict_performance)
    predict_button.grid(row=8, columnspan=2, pady=10)

    # Khởi chạy giao diện
    window.mainloop()

# Chạy giao diện
create_gui()
