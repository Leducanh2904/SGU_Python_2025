# 9. Viết chương trình tính lũy thừa nhanh a^b dùng đệ quy và chia để trị
# Tính lũy thừa nhanh a^b
def fast_power(a, b):
    if b == 0:
        return 1
    half = fast_power(a, b // 2)
    if b % 2 == 0:
        return half * half
    else:
        return half * half * a

# Nhập a và b từ bàn phím
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

result = fast_power(a, b)
print(f"Kết quả của {a}^{b} là: {result}")
