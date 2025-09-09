# 8. Nhập một số nguyên, đếm xem số đó có bao nhiêu chữ số và tính tổng các chữ số
# Nhập số nguyên
num = int(input("Nhập một số nguyên: "))

# Đếm số chữ số và tính tổng các chữ số
num_str = str(abs(num))  # Lấy giá trị tuyệt đối để tránh dấu âm
num_digits = len(num_str)
digit_sum = sum(int(digit) for digit in num_str)

print(f"Số {num} có {num_digits} chữ số và tổng các chữ số là {digit_sum}")
