# 9. Viết chương trình tính lũy thừa nhanh a^b dùng đệ quy và chia để trị
# Tính lũy thừa nhanh a^b
def fast_power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = fast_power(a, b // 2)
        return half * half
    else:
        half = fast_power(a, (b - 1) // 2)
        return half * half * a

# Nhập a và b từ bàn phím
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

result = fast_power(a, b)
print(f"Kết quả của {a}^{b} là: {result}")
