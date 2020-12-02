
def encode(string):
    ascii = []
    for letter in string:
        ascii.append(ord(letter))
    bits = []
    for num in ascii:
        n = 7
        bit = ''
        while n != -1:
            if 2**n > num:
                bit += '0'
            else:
                bit += '1'
                num -= 2**n
            n -= 1
        bits.append(bit)
    triple_bits = []
    for bit in bits:
        trip_bit = ''
        for num in bit:
            trip_bit += 3*num
        triple_bits.append(trip_bit)
    return ''.join(triple_bits)




def decode(bits):
    check_error = []
    for num in range(3,len(bits)+1,3):
        check_error.append(bits[num-3:num])
    corrected_bits = []
    for trip in check_error:
        if trip.count('0') >= 2:
            corrected_bits.append('0')
        else:
            corrected_bits.append('1')
    corrected_bin = []
    for num in range(8,len(corrected_bits)+1,8):
        corrected_bin.append(''.join(corrected_bits[num-8:num]))
    asci_list = []
    for num in corrected_bin:
        asci_val = 0
        n=7
        for bin in num:
            asci_val += (2**n)*int(bin)
            n-=1
        asci_list.append(asci_val)
    output = ''
    for asci in asci_list:
        output += chr(asci)
    return output


print(decode(encode('the cat+')))

