import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split
from sklearn import neighbors, linear_model, tree, svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Khởi tạo biến toàn cục
df = None
x = None
y = None
models = {}
scaler = None

# Hàm làm sạch dữ liệu
def clean_data(data):
    # Điền giá trị thiếu (missing values) bằng trung bình của từng cột
    data.fillna(data.mean(), inplace=True)
    return data

# Hàm chuẩn hóa dữ liệu
def normalize_data(X):
    global scaler
    scaler = StandardScaler()  # Sử dụng chuẩn hóa StandardScaler
    X_scaled = scaler.fit_transform(X)
    return X_scaled

# Hàm để load dữ liệu từ file CSV
def load_data():
    global df, x, y
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        
        # Làm sạch dữ liệu
        df = clean_data(df)
        
        # Lấy dữ liệu đầu vào (9 cột đầu)
        x = df.iloc[:, 0:9].values.astype(np.float64)
        
        # Chuẩn hóa dữ liệu
        x = normalize_data(x)
        
        # Dữ liệu Potability (Cột thứ 10 - Đầu ra)
        y = df.iloc[:, 9].values.astype(np.float64)
        
        messagebox.showinfo("Tải dữ liệu", "Dữ liệu đã được làm sạch và chuẩn hóa.")
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
    knn_model = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn_model.fit(X_train, y_train)
    models['KNN'] = knn_model
    
    # Logistic Regression
    lr_model = linear_model.LogisticRegression()
    lr_model.fit(X_train, y_train)
    models['Hồi quy Logistic'] = lr_model
    
    # Decision Tree Classifier
    dtr_model = tree.DecisionTreeClassifier()
    dtr_model.fit(X_train, y_train)
    models['Cây quyết định'] = dtr_model
    
    # Support Vector Classifier
    svr_model = svm.SVC()
    svr_model.fit(X_train, y_train)
    models['SVC'] = svr_model
    
    messagebox.showinfo("Huấn luyện mô hình", "Tất cả các mô hình đã được huấn luyện thành công.")

# Hàm để kiểm tra và so sánh các thuật toán bằng Accuracy
def compare_models():
    if df is None or x is None or y is None:
        messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước.")
        return
    
    if not models:
        messagebox.showerror("Lỗi", "Vui lòng huấn luyện mô hình trước.")
        return
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    
    accuracy_scores = {}
    
    for model_name, model in models.items():
        y_predict = model.predict(X_test)
        
        # Tính accuracy
        accuracy = accuracy_score(y_test, y_predict) * 100  # Chuyển sang phần trăm
        accuracy_scores[model_name] = accuracy
    
    # Hiển thị kết quả accuracy
    result_message = "So sánh độ chính xác giữa các mô hình (Accuracy %):\n\n"
    for model_name in models.keys():
        result_message += f"{model_name} - Accuracy: {accuracy_scores[model_name]:.2f}%\n"
    
    messagebox.showinfo("So sánh mô hình", result_message)
    
    # Vẽ đồ thị so sánh accuracy
    labels = list(models.keys())
    x_axis = np.arange(len(labels))  # Số lượng các mô hình

    fig, ax = plt.subplots(figsize=(10, 6))

    rects = ax.bar(x_axis, accuracy_scores.values(), color='blue')

    # Thêm nhãn và tiêu đề
    ax.set_xlabel('Mô hình')
    ax.set_ylabel('Độ chính xác (%)')
    ax.set_title('So sánh độ chính xác giữa các mô hình')
    ax.set_xticks(x_axis)
    ax.set_xticklabels(labels)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Hàm dự đoán kết quả với một mô hình cụ thể
def predict_potability(model_name):
    if df is None or x is None or y is None:
        messagebox.showerror("Lỗi", "Vui lòng tải dữ liệu trước.")
        return
    
    if model_name not in models:
        messagebox.showerror("Lỗi", f"Vui lòng huấn luyện mô hình {model_name} trước.")
        return
    
    try:
        ph = float(ph_entry.get())
        hardness = float(hardness_entry.get())
        solids = float(solids_entry.get())
        chloramines = float(chloramines_entry.get())
        sulfate = float(sulfate_entry.get())
        conductivity = float(conductivity_entry.get())
        organic_carbon = float(organic_carbon_entry.get())
        trihalomethanes = float(trihalomethanes_entry.get())
        turbidity = float(turbidity_entry.get())

        input_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]).astype(np.float64)
        input_data = scaler.transform(input_data)  # Chuẩn hóa dữ liệu đầu vào trước khi dự đoán
        prediction = models[model_name].predict(input_data)[0]
        
        if prediction == 1:
            messagebox.showinfo("Kết quả dự đoán", f"{model_name} dự đoán khả năng sử dụng nước: Uống được")
        else:
            messagebox.showinfo("Kết quả dự đoán", f"{model_name} dự đoán khả năng sử dụng nước: Không uống được")
            
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đúng các giá trị số.")

# Tạo giao diện bằng Tkinter
def create_gui():
    window = tk.Tk()
    window.title("Xác định khả năng sử dụng nước")

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
    tk.Label(frame, text="pH").grid(row=3, column=0)
    global ph_entry
    ph_entry = tk.Entry(frame)
    ph_entry.grid(row=3, column=1)

    tk.Label(frame, text="Độ cứng (Hardness)").grid(row=4, column=0)
    global hardness_entry
    hardness_entry = tk.Entry(frame)
    hardness_entry.grid(row=4, column=1)

    tk.Label(frame, text="Chất rắn (Solids)").grid(row=5, column=0)
    global solids_entry
    solids_entry = tk.Entry(frame)
    solids_entry.grid(row=5, column=1)

    tk.Label(frame, text="Chloramines").grid(row=6, column=0)
    global chloramines_entry
    chloramines_entry = tk.Entry(frame)
    chloramines_entry.grid(row=6, column=1)

    tk.Label(frame, text="Sulfate").grid(row=7, column=0)
    global sulfate_entry
    sulfate_entry = tk.Entry(frame)
    sulfate_entry.grid(row=7, column=1)

    tk.Label(frame, text="Độ dẫn điện (Conductivity)").grid(row=8, column=0)
    global conductivity_entry
    conductivity_entry = tk.Entry(frame)
    conductivity_entry.grid(row=8, column=1)

    tk.Label(frame, text="Carbon hữu cơ (Organic Carbon)").grid(row=9, column=0)
    global organic_carbon_entry
    organic_carbon_entry = tk.Entry(frame)
    organic_carbon_entry.grid(row=9, column=1)

    tk.Label(frame, text="Trihalomethanes").grid(row=10, column=0)
    global trihalomethanes_entry
    trihalomethanes_entry = tk.Entry(frame)
    trihalomethanes_entry.grid(row=10, column=1)

    tk.Label(frame, text="Độ đục (Turbidity)").grid(row=11, column=0)
    global turbidity_entry
    turbidity_entry = tk.Entry(frame)
    turbidity_entry.grid(row=11, column=1)

    # Nút Dự đoán bằng KNN
    predict_knn_button = tk.Button(frame, text="Dự đoán bằng KNN", command=lambda: predict_potability('KNN'))
    predict_knn_button.grid(row=12, column=0, columnspan=2, pady=5, ipadx=20)

    # Nút Dự đoán bằng Logistic Regression
    predict_lr_button = tk.Button(frame, text="Dự đoán bằng Hồi quy Logistic", command=lambda: predict_potability('Hồi quy Logistic'))
    predict_lr_button.grid(row=12, column=2, columnspan=2, pady=5, ipadx=20)

    # Nút Dự đoán bằng Decision Tree
    predict_dtr_button = tk.Button(frame, text="Dự đoán bằng Cây quyết định", command=lambda: predict_potability('Cây quyết định'))
    predict_dtr_button.grid(row=13, column=0, columnspan=2, pady=5, ipadx=20)

    # Nút Dự đoán bằng SVR
    predict_svr_button = tk.Button(frame, text="Dự đoán bằng SVC", command=lambda: predict_potability('SVC'))
    predict_svr_button.grid(row=13, column=2, columnspan=2, pady=5, ipadx=20)

    window.mainloop()

# Gọi hàm tạo giao diện
create_gui()
