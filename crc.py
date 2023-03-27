def mod2bindiv():
    remainder=[]
    for i in range(d):
        remainder.append(dividend.pop(0))
    for i in range(m+d-5):
        if 1 not in remainder:
            break
        if len(remainder)<len(divisor):
            break
        for i in range(d):
            remainder[i]=remainder[i]^divisor[i]
        if not dividend:
            break
        while True:
            if remainder and remainder[0]==0:
                remainder.pop(0)
            else:
                break
        while len(remainder)!=d:
            if dividend:
                remainder.append(dividend.pop(0))
            else:
                break
    if len(remainder)!=d-1:
        while len(remainder)>d-1:
            remainder.pop(0)
        while len(remainder)<d-1:
            remainder.insert(0,0)
    return remainder

print("\n***** CRC Program *****\n\n----SenderSide----\n")
m=int(input("Enter length of message to transmitted: "))
msg=[x for x in input("Enter the message(bit stream): ")]
while len(msg)!=m:
    print("Invalid message entered, try again!")
    msg=[x for x in input("Enter the message(bit stream): ")]
dividend=[i for i in msg]
d=int(input("Enter length of generator: "))
divisor=[int(x) for x in input("Enter the generator(bits): ")]
while len(divisor)!=d:
    print("Invalid generator entered, try again!")
    divisor=[int(x) for x in input("Enter the generator(bits): ")]
dividend+=list(x for x in str('0'*(d-1)))
print(f"Dividend after adding zeros: {''.join(dividend)}")
dividend=[int(x) for x in dividend]
remainder=mod2bindiv()
print(f"CRC generated is: {''.join(map(str,remainder))}")
msg_transmitted=msg+remainder
print(f"Message transmitted is: {''.join(map(str,msg_transmitted))}")

print("\n----ReceiverSide----\n")
choice=input("Has any bit in the message changed? [y/n]: ")
while choice not in ['y','Y','n','N']:
    print("Invalid choice, try again!")
    choice=input("Has any bit in the message changed? [y/n]: ")
if choice in ['y','Y']:
    changed_index=int(input("Which bit is in error? (from left to right): "))-1
    while changed_index<0:
        print("Invalid position, try again!")
        changed_index=int(input("Which bit is in error? (from left to right): "))-1
else:
    changed_index=-1
msg_received=[int(x) for x in msg_transmitted]
if changed_index>-1:
    if msg_received[changed_index]==0:
        msg_received[changed_index]=1
    else:
        msg_received[changed_index]=0
print(f"Message received is: {''.join(map(str,msg_received))}")
msg_received=[int(x) for x in msg_received]
dividend=[i for i in msg_received]
remainder=mod2bindiv()
print(f"Remainder is: {''.join(map(str,remainder))}")
remainder=[int(x) for x in remainder]
if all(bits == 0 for bits in remainder):
    print("No Error")
else:
    print("Error Detected")


# ***** CRC Program *****

# ----SenderSide----

# Enter length of message to transmitted: 10
# Enter the message(bit stream): 1101011011
# Enter length of generator: 5
# Enter the generator(bits): 10011
# Dividend after adding zeros: 11010110110000
# CRC generated is: 1110
# Message transmitted is: 11010110111110

# ----ReceiverSide----

# Has any bit in the message changed? [y/n]: n
# Message received is: 11010110111110
# Remainder is: 0000
# No Error