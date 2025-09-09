# 1. Viết chương trình nhập vào một số nguyên n. Kiểm tra xem số đó có phải là số nguyên tố, số đối xứng,
# số hoàn chỉnh, số chính phương hay không?
import math

# Kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
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
    if n <= 1:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

# Kiểm tra số chính phương
def is_square_number(n):
    return int(math.sqrt(n)) ** 2 == n

# Nhập vào một số nguyên n
n = int(input("Nhập một số nguyên n: "))

# Kiểm tra các điều kiện
print(f"Số {n} có phải là số nguyên tố không? {is_prime(n)}")
print(f"Số {n} có phải là số đối xứng không? {is_palindrome(n)}")
print(f"Số {n} có phải là số hoàn chỉnh không? {is_perfect_number(n)}")
print(f"Số {n} có phải là số chính phương không? {is_square_number(n)}")
