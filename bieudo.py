import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

csv_path = '/home/lehoang/Desktop/Project_airPollution/hanoi-vietnam-air-quality-after-cleaning.csv'

df = pd.read_csv(csv_path)

df['date'] = pd.to_datetime(df['date'])

# Khoảng thời gian lockdown
lockdown = ('2021-08-01', '2021-09-30')
after_lockdown = ('2021-10-01', '2021-11-30')

pm25_1 = df.loc[(df['date'] >= lockdown[0]) & (df['date'] <= lockdown[1])]
pm25_2 = df.loc[(df['date'] >= after_lockdown[0]) & (df['date'] <= after_lockdown[1])]

# Lấy các giá trị pm2.5 trước và sau lockdown
pm25_1_values = pm25_1['pm25'].tolist()
pm25_2_values = pm25_2['pm25'].tolist()

# Tạo list chứa các giá trị từ 1 đến len(pm25_1_values)
length_1 = [i for i in range(1, len(pm25_1_values) + 1)]

# Tạo list chứa các giá trị từ 1 đến len(pm25_2_values)
length_2 = [i for i in range(1, len(pm25_2_values) + 1)]

# Vẽ biểu đồ so sánh
plt.figure(figsize=(10, 6))

plt.plot(length_1, pm25_1_values, label='In Lockdown', color='blue')
plt.plot(length_2, pm25_2_values, label='After Lockdown', color='red')

plt.xlabel('Time')
plt.ylabel('PM2.5 Value')
plt.title('Comparison of Lockdown vs After Lockdown PM2.5 Values')
plt.legend()
plt.grid(True)

# Tạo con trỏ
cursor = Cursor(plt.gca(), useblit=True, color='black', linewidth=1)

plt.show()
