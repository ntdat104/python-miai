import pandas as pd
import numpy as np
import constants
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file csv
df = pd.read_csv(constants.DATA_CSV)
print(df)

# Ghi dữ liệu df ra file csv
df.to_csv('src/pandas/assets/data.csv')

# Xem thông tin dataframe
print(df.info())

# Lấy thông tin cột
print(df[['<Ticker>', '<Close>', '<Volume>']])

# Lấy theo dòng
print(df.head(10))
print(df.tail(5))
print(df[100:105])
print(df[100:])
print(df[:100])
print(df[:])

# Lấy theo điều kiện
print(df[df['<Close>'] > 90000])
print(df[df['<Close>'] == 90000])
print(df[(df['<Close>'] > 90000) & (df['<Close>'] == 93000)])

# Thêm cột Close = Close * 2
df['<Double_Close>'] = df['<Close>'] * 2
print(df)

# Thêm cột nếu Close > 90000 thì pass = 1 còn ko thì pass = 0
df['<Pass>'] = np.where(df['<Close>'] > 90000, 1, 0)
print(df[df['<Pass>'] == 1])

# Sửa cột = gán lại
df['<Double_Close>'] = df['<Close>'] * 3
print(df)

# Xóa cột
df = df.drop(columns=['<Double_Close>'])
df.drop(columns=['<Pass>'], inplace=True)
print(df)

# Xóa hàng
print(df.drop(index=[2, 3, 4]))

# Sắp xếp
print(df.sort_values(by=['<Volume>']))
print(df.sort_values(by=['<Volume>'], ascending=False))
print(df.describe())

# Làm sạch dữ liệu
print(df.describe())
print(df.info())
print(df['<Volume>'].fillna(0))

# Vẽ biểu đồ
df['<Close>'].plot.area()
plt.show()