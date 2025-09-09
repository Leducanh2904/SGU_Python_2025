# 7. Tìm số đầu tiên chia hết cho 9 và chia hết cho 7 nằm trong đoạn [M,N]
M = int(input("Nhập số M: "))
N = int(input("Nhập số N: "))

found = False
for i in range(M, N + 1):
    if i % 9 == 0 and i % 7 == 0:
        print(f"Số đầu tiên chia hết cho 9 và chia hết cho 7 trong đoạn [{M}, {N}] là: {i}")
        found = True
        break

if not found:
    print(f"Không có số nào chia hết cho 9 và 7 trong đoạn [{M}, {N}]")
