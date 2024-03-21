"""
Muc tieu
1. Loai bo cac cot (column) co gia tri hoan toan rong
2. Loai bo cac hang co gia tri rong
3. Xoa dau SPACE nam o phia truoc ten moi cot (column)
"""


import pandas as pd

# co the thuc hien thay doi file_name de cleaning nhieu file cung luc
# dien ten file vao day de thuc hien tien xu ly du lieu
file_name = "hanoi-us-embassy-air-quality"
file_path = "/home/lehoang/Desktop/Project_airPollution/" + file_name + ".csv"
df = pd.read_csv(file_path)

if " aqi" in df.columns:
    df.drop(columns=" aqi", inplace= True)

# Loại bỏ cột 'co' và 'aqi' từ DataFrame
#df.drop(columns=['co', 'aqi'], inplace=True)

# Tìm và xóa các cột có tất cả giá trị là rỗng
df = df.dropna(axis=1, how='all')

# Loại bỏ các hàng trùng lặp
df.drop_duplicates(inplace=True)

# Loại bỏ các hàng có giá trị cột "Nitrogen_Dioxide" là NaN hoặc rỗng
df = df[~df[" no2"].isna() & (df[" no2"] != ' ')]

# Loại bỏ các hàng có giá trị cột "Sulfur_Dioxide" là NaN hoặc rỗng
df = df[~df[" so2"].isna() & (df[" so2"] != ' ')]

# Loại bỏ các hàng có giá trị cột "Ozon" là rỗng
df = df[~df[" o3"].isna() & (df[" o3"] != ' ')]

# Loại bỏ các hàng có giá trị cột "pm25" là rỗng
df = df[~df[" pm25"].isna() & (df[" pm25"] != ' ')]

# Loại bỏ các hàng có giá trị cột "Date" là rỗng
df = df[df["date"] != ' ']

#loai bo cac hang co gia tri cot "pm10" la rong
if " pm10" in df.columns:
    df = df[~df[" pm10"].isna() & (df[" pm10"] != ' ')]


#loai bo cac hang co gia tri cot "co" la rong
df = df[~df[" co"].isna() & (df[" co"] != ' ')]

# Loại bỏ khoảng trắng từ tên các cột
df.rename(columns=lambda x: x.strip(), inplace=True)


# Lưu file sau khi đã hoàn thành tiền xử lý dữ liệu
output_file_path = "/home/lehoang/Desktop/Project_airPollution/" + file_name + "-after-cleaning" + ".csv"
df.to_csv(output_file_path, index=False)
