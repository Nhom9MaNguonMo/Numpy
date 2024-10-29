import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, \
                            mean_absolute_error
import tkinter as tk
from tkinter import messagebox, simpledialog





def search_action():
    hour_study=hour_entry.get()
    previous_mark=previous_entry.get()
    activity=activity_entry.get()
    sleep_hour=sleep_entry.get()
    paper_mark=pp_entry.get()
    t=[]
    test=[]
    t.append(hour_study)
    t.append(previous_mark)
    t.append(activity)
    t.append(sleep_hour)
    t.append(paper_mark)
    t=np.array(t).astype(np.float64)
    test.append(t)


    df=pd.read_csv('hocmay\Student_Performance.csv')#,index_col=0,header = 0)
    x = array(df.iloc[:200,0:5]).astype(np.float64)
    y = array(df.iloc[:200,4:5]).astype(np.float64)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    knn = neighbors.KNeighborsRegressor(n_neighbors = 3,p=2)
    knn.fit(X_train, y_train)
    y_predict=knn.predict(test)
    messagebox.showinfo("Điểm dự đoán : ", y_predict)

root = tk.Tk()
root.title("App du doan diem cho sinh vien")
tk.Label(root, text="Nhap số giờ học").pack(pady=5)
global hour_entry
hour_entry = tk.Entry(root)
hour_entry.pack(pady=5)

tk.Label(root, text="Nhập điểm kỳ trước").pack(pady=5)
global previous_entry
previous_entry = tk.Entry(root)
previous_entry.pack(pady=5)

tk.Label(root, text="Nhập số hoat động ngoại khóa tham gia").pack(pady=5)
global activity_entry
activity_entry = tk.Entry(root)
activity_entry.pack(pady=5)

tk.Label(root, text="Nhập số giờ ngủ ").pack(pady=5)
global sleep_entry
sleep_entry = tk.Entry(root)
sleep_entry.pack(pady=5)

tk.Label(root, text="Nhập điểm kiểm tra giấy ").pack(pady=5)
global pp_entry
pp_entry = tk.Entry(root)
pp_entry.pack(pady=5)
tk.Button(root, text="Dự đoán", command=search_action).pack(pady=10)

root.mainloop()

