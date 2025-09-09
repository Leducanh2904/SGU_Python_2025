# 6. Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn [99;999] (tính cả 99
# và 999)
print("Các số chia hết cho 7 nhưng không phải bội số của 5 trong đoạn [99, 999]:")
for i in range(99, 1000):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=" ")
print()
