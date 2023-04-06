import math

def main():
    den = input("Denary: ")
    print(decimalToBinary(int(den)))
    binary = input("Binary: ")
    print(binaryToHex(binary))
    print(binaryToDecimal(binary))

def decimalToBinary(num):
    num = int(num)
    numBits = (math.floor(math.log(num, 2)))+1

    binary = ""
    cumNum = num
    for j in range(numBits):
        i = numBits - j
        binaryPower = pow(2, i-1)
        if cumNum >= binaryPower:
            binary += "1"
            cumNum -= binaryPower
        elif cumNum < binaryPower:
            binary += "0"
            
    return binary

def binaryToDecimal(binary):
    binary = str(binary)
    while not len(binary)%4 == 0:
        binary = "0" + binary

    total = 0
    index = 1
    for bit in binary:
        value = pow(2, len(binary) - index)
        if bit == "1":
            total += value
        index += 1

    return total   

def binaryToHex(binary):
    binary = str(binary)
    while not len(binary)%4 == 0:
        binary = "0" + binary

    chunks = []
    numChunks = int(len(binary)/4)
    for i in range(numChunks):
        index = i*4
        chunks.append(binary[index:index+4])

    hexComplete = ""
    for chunk in chunks:
        chunkBinary = binaryToDecimal(chunk)
        if chunkBinary <= 9:
            hexComplete += f"{chunkBinary}"
        elif chunkBinary > 9:
            asciiDecimal = chunkBinary + 55
            letter = chr(asciiDecimal)
            hexComplete += letter

    return hexComplete

main()
