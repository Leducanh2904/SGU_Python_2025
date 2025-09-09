# In ra M số nguyên tố đầu tiên
M = int(input("Nhập số M: "))

count = 0
i = 2
print(f"{M} số nguyên tố đầu tiên:")
while count < M:
    if is_prime(i):
        print(i, end=" ")
        count += 1
    i += 1
print()
