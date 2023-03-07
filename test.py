def main(input_data):
    x1 = input_data & 0x3FF
    x2 = (input_data >> 10) & 0x3
    x3 = (input_data >> 12) & 0x7
    x4 = (input_data >> 15) & 0x1

    output_data = (x3 << 13) | (x4 << 12) | (x1 << 2) | x2

    return str(output_data)


print(main(40773))
