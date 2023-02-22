a = "1010"
b = "011"
remainder = 0

len_a = len(a)
len_b = len(b)

c = ""

for i in range(max(len_a, len_b)):
    a_i = 0
    b_i = 0
    idx_a = len_a - i - 1
    idx_b = len_b - i - 1
    if idx_a >= 0:
        a_i = int(a[idx_a])
    if idx_b >= 0:
        b_i = int(b[idx_b])

    c_i = a_i + b_i + remainder
    remainder = 0
    if c_i > 1:
        c_i = c_i - 2
        remainder = 1
    c = str(c_i) + c

    print(i)

print("hi")