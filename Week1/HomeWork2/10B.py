# 10. Viết chương trình nhập vào một số nguyên dương n. In ra từng chữ số trong n. Yêu cầu không dùng
# các hàm trong xử lý chuỗi
# Nhập số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# In ra từng chữ số của n
while n > 0:
    digit = n % 10  
    print(digit, end=" ")
    n = n // 10  
print()
