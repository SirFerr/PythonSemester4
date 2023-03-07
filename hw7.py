def main(num):
    t0 = (num >> 14) & 1
    t3 = (num >> 6) & 0xFF
    t2 = (num >> 2) & 0xF
    t1 = num & 0x3
    return str((t0 << 14) | (t1 << 12) | (t3 << 4) | t2)


print(main(870))  # '8409'
print(main(9855))  # '14751'
print(main(8002))  # '10192'
print(main(8780))  # '2195'
