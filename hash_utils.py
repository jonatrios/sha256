
def text_to_bin(text):
    b = ''
    for i in text.encode():
        b = b + num_to_bit(i)
    return b
        
def num_to_bit(n,base_bit=8):
    bin_n = ''
    m = 0
    while n // 2 != m:
        bin_n = str(n % 2) + bin_n
        n = n // 2
    if base_bit == 8:
        if len(str(n) + bin_n) % 2 !=0 or (len(str(n) + bin_n) // 8) % 2 !=0:
            z = (8 - (len(str(n) + bin_n) % 8))
            if z == 8:
                return str(n) + bin_n
            else:
                add = '0' * z
                return add + str(n) + bin_n
        elif len(str(n) + bin_n) <= 6:
            z = (8 - (len(str(n) + bin_n) % 8))
            add = '0' * z
            return add + str(n) + bin_n 
        else:
            return str(n) + bin_n
    if base_bit == 32:
        if len(str(n) + bin_n) < 32:
            z = (32 - (len(str(n) + bin_n) % 32))
            add = '0' * z    
            return add + str(n) + bin_n
        else:
            return str(n) + bin_n
      
def fill_step(msg_bin):
    msg_bin_extend = msg_bin + '1'
    x = (448 -  len(msg_bin) - 1) % 512
    y_64 = '0' * (64 - len(num_to_bit(len(msg_bin)))) + num_to_bit(len(msg_bin))
    msg_bin_extend =msg_bin_extend + ('0' * x)
    msg_bin_extend = msg_bin_extend + y_64
    return msg_bin_extend

def bin_blocks512(fill_text):
    parts = [fill_text[i:i+512] for i in range(0, len(fill_text), 512)]
    return parts

def bin_subBlocks32(block_list):
    sub_parts = [elem[j:j+32] for elem in block_list for j in range(0, len(elem), 32)]
    s = [sub_parts[i:i+16] for i in range(0,len(sub_parts),16) ]
    return s



def bin_and(x,y):
    z = ''
    for i in range(0,32):
        z = z + str(int(x[i]) * int(y[i]))
    return z

def bin_not(x):
    z = ''
    for i in range(0,32):
        z = z + str( int(not int(x[i])))
    return z

def bin_xor(x,y):
    z = ''
    for i in range(0,32):
        if x[i] == y[i]:
            z = z + '0'
        else:
            z = z + '1'
    return z

def rotate(elem, y=1, shift_d='r'):
    if len(elem) == 0: 
        return '0' * 32
    if shift_d == 'l':
        y = y % len(elem)
    else:
        y = -y % len(elem) 
    return elem[y:] + elem[:y]

def shift(elem, y=1, shift_d='r'):
    if len(elem) == 0: 
        return '0' * 32
    if shift_d == 'l':
        return  elem[y:] + '0' * y
    else:
        return '0' * y + elem[:len(elem)-y]

S_mod = lambda x: num_to_bit( ((x) % 4294967296),32)    
sigma0 = lambda x: bin_xor(bin_xor(rotate(x,7), rotate(x,18)), shift(x,3))
sigma1 = lambda x: bin_xor(bin_xor(rotate(x,17), rotate(x,19)), shift(x,10))


gamma0 = lambda x: bin_xor(bin_xor(rotate(x,2), rotate(x,13)), rotate(x,22))
gamma1 = lambda x: bin_xor(bin_xor(rotate(x,6), rotate(x,11)), rotate(x,25))
Ch = lambda x,y,z: bin_xor(bin_and(x,y), bin_and(bin_not(x), z))
Maj = lambda x,y,z: bin_xor(bin_xor(bin_and(x,y) , bin_and(x,z)) , bin_and(y,z))





