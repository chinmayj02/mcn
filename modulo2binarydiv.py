# for i in range(len(dividend)-len(divisor)+1):
#         if dividend[i] == 1:
#             for j in range(len(divisor)):
#                 dividend[i+j] = dividend[i+j] ^ divisor[j]
    
# remainder = ''.join(str(bit) for bit in dividend[-len(divisor)+1:])
# print(remainder)