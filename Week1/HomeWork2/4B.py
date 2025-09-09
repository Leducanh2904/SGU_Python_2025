# 4. Liệt kê tất cả các số nguyên tố nhỏ hơn N ( N nhập từ bàn phím)
import math

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Nhập N từ bàn phím
N = int(input("Nhập số N: "))

# Liệt kê các số nguyên tố nhỏ hơn N
print(f"Các số nguyên tố nhỏ hơn {N}:")
for i in range(2, N):
    if is_prime(i):
        print(i, end=" ")
print()
