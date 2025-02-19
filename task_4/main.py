def count_bits(n):
    return bin(n).count('1')

print(count_bits(0))
print()
print(count_bits(4))
print()
print(count_bits(7))

n=7
print(n.bit_count())