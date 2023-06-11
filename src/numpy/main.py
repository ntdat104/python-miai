import numpy as np

# Tạo numpy array từ Python list
print(np.array([1, 2, 3, 4]))
print(np.array([1.1, 2, 3.4, 4]))
print(np.array([1, 2, 3, 4], dtype='float32'))

a1 = np.array([1, 2, 3, 4])
print(type(a1))

a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
print(a2.shape) # 2 dòng và 3 cột
print(a2.ndim) # 2 chiều
print(a2.dtype)
print(a2.size) # Tổng số thành phần

# Tạo numpy array từ hàm có sẵn
print(np.zeros([2, 4], dtype=int)) # 2 hàng và 4 cột
print(np.ones((3, 6), dtype=float))
print(np.arange(0, 20, 2)) # duyệt từ 0 -> 20 với khoảng cách là 2
print(np.full((3,5), 6.9))
print(np.linspace(0, 1, 5))

# Tạo random
print(np.random.random((4, 4)))

# Seed for reproducibility
np.random.seed(0)
print(np.random.random((4, 4)))
print(np.random.normal(0, 1, (3,3)))
print(np.random.randint(0, 10, (4,5)))
print(np.random.rand(4, 4))