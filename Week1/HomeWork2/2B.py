# 2. Viết chương trình nhập vào hai số M, N. In ra tất cả các số nguyên tố, số đối xứng, số hoàn chỉnh, số
# chính phương trong khoảng [M,N] (nếu có)
import math
# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra số đối xứng
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Kiểm tra số hoàn chỉnh
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

# Kiểm tra số chính phương
def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

# Nhập vào hai số M và N
M = int(input("Nhập vào số M: "))
N = int(input("Nhập vào số N: "))

# In ra các số nguyên tố trong khoảng [M, N]
print(f"Các số nguyên tố trong khoảng [{M}, {N}]:")
for i in range(M, N + 1):
    if is_prime(i):
        print(i, end=" ")
print()

# In ra các số đối xứng trong khoảng [M, N]
print(f"Các số đối xứng trong khoảng [{M}, {N}]:")
for i in range(M, N + 1):
    if is_palindrome(i):
        print(i, end=" ")
print()

# In ra các số hoàn chỉnh trong khoảng [M, N]
print(f"Các số hoàn chỉnh trong khoảng [{M}, {N}]:")
for i in range(M, N + 1):
    if is_perfect_number(i):
        print(i, end=" ")
print()

# In ra các số chính phương trong khoảng [M, N]
print(f"Các số chính phương trong khoảng [{M}, {N}]:")
for i in range(M, N + 1):
    if is_perfect_square(i):
        print(i, end=" ")
print()
