import pandas as pd

file_path = "/home/lehoang/Desktop/Project_airPollution/hanoi-us-embassy-air-quality.csv"
df = pd.read_csv(file_path)

# Loại bỏ cột 'co' và 'aqi' từ DataFrame
df.drop(columns=[' co', ' aqi'], inplace=True)


# Loại bỏ các hàng trùng lặp
df.drop_duplicates(inplace=True)

# Loại bỏ các hàng có giá trị cột "Nitrogen_Dioxide" là NaN hoặc rỗng
df = df[~df["Nitrogen_Dioxide"].isna() & (df["Nitrogen_Dioxide"] != ' ')]

# Loại bỏ các hàng có giá trị cột "Sulfur_Dioxide" là NaN hoặc rỗng
df = df[~df["Sulfur_Dioxide"].isna() & (df["Sulfur_Dioxide"] != ' ')]

# Loại bỏ các hàng có giá trị cột "Ozon" là rỗng
df = df[df["Ozon"] != ' ']

# Loại bỏ các hàng có giá trị cột "Particulate_Matter" là rỗng
df = df[df["Particulate_Matter"] != ' ']

# Loại bỏ các hàng có giá trị cột "Date" là rỗng
df = df[df["Date"] != ' ']

# Chuyển đổi dữ liệu của các cột sang kiểu chuỗi
df['Particulate_Matter'] = df['Particulate_Matter'].astype(str)
df['Nitrogen_Dioxide'] = df['Nitrogen_Dioxide'].astype(str)
df['Ozon'] = df['Ozon'].astype(str)
df['Sulfur_Dioxide'] = df['Sulfur_Dioxide'].astype(str)

# Loại bỏ khoảng trắng và dấu "'" không mong muốn
df["Particulate_Matter"] = df["Particulate_Matter"].str.replace("'", '').str.replace(' ', '')
df["Nitrogen_Dioxide"] = df["Nitrogen_Dioxide"].str.replace("'", '').str.replace(' ', '')
df["Ozon"] = df["Ozon"].str.replace("'", '').str.replace(' ', '')
df["Sulfur_Dioxide"] = df["Sulfur_Dioxide"].str.replace("'", '').str.replace(' ', '')

# Lưu file sau khi đã hoàn thành tiền xử lý dữ liệu
output_file_path = "/home/lehoang/Desktop/Project_airPollution/hanoi-us-embassy-air-quality-after-cleaning.csv"
df.to_csv(output_file_path, index=False)
