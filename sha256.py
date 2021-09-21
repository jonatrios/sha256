from hash_utils import *

h_list = [0x6A09E667, 0xBB67AE85, 
             0x3C6EF372, 0xA54FF53A, 
             0x510E527F, 0x9B05688C, 
             0x1F83D9AB, 0x5BE0CD19]

k_list = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

h_bit_list = [num_to_bit(h,32) for h in h_list]


class SHA256():

    def __init__(self, msg=''.encode()) -> None:
        self.msg : bytes = msg
        if isinstance(msg, bytes) == False:
            raise TypeError('Unicode-objects must be encoded before hashing')
    
    def update(self, msg : bytes) -> None:
        self.msg = msg + self.msg
        if isinstance(msg, bytes) == False:
            raise TypeError('Unicode-objects must be encoded before hashing')
    
    def msg_to_bin(self) -> str:
        b = ''
        for i in self.msg:
            b = b + num_to_bit(i)
        return b
    
    def msg_size(self) -> int:
        return len(self.msg_to_bin())


    def hexdigest(self) -> str:
        msg_f = fill_step(self.msg_to_bin())
        msg_list_f = bin_blocks512(msg_f)
        msg_32_f = bin_subBlocks32(msg_list_f)
        
        h_0 = h_bit_list[0]
        h_1 = h_bit_list[1]
        h_2 = h_bit_list[2]
        h_3 = h_bit_list[3]
        h_4 = h_bit_list[4]
        h_5 = h_bit_list[5]
        h_6 = h_bit_list[6]
        h_7 = h_bit_list[7]
            
            
        for n in range(0,len(msg_32_f)):
            
            a = h_0
            b = h_1
            c = h_2
            d = h_3
            e = h_4
            f = h_5
            g = h_6
            h = h_7
            
            w = []
            
            for i in range(0,16):
                w.append(msg_32_f[n][i])
                
            for j in range(16,64):
                term1 = sigma1(w[j-2])
                term2 = w[j-7]
                term3 = sigma0(w[j-15])
                term4 = w[j-16]
                term1 = int(term1,2)
                term2 = int(term2,2)
                term3 = int(term3,2)
                term4 = int(term4,2)
                final_t = S_mod(term1 + term2 + term3 + term4)
                w.append(final_t)
                
                        
            for m in range(0,64):
                T1 = (int(h,2) + int(gamma1(e),2) + int(Ch(e,f,g),2) + int(k_list[m]) + int(w[m],2)) % 2**32
                T2 = (int(gamma0(a),2) + int(Maj(a,b,c),2)) % 2**32
                h = g
                g = f
                f = e
                e = num_to_bit((int(d ,2)+ T1) % 2**32,32)
                d = c
                c = b
                b = a
                a = num_to_bit((T1 + T2) % 2**32,32)
            
            h_0 = num_to_bit((int(a,2) + int(h_0,2) ) % 2**32,32)
            h_1 = num_to_bit((int(b,2) + int(h_1,2) ) % 2**32,32)
            h_2 = num_to_bit((int(c,2) + int(h_2,2) ) % 2**32,32)
            h_3 = num_to_bit((int(d,2) + int(h_3,2) ) % 2**32,32)
            h_4 = num_to_bit((int(e,2) + int(h_4,2) ) % 2**32,32)
            h_5 = num_to_bit((int(f,2) + int(h_5,2) ) % 2**32,32)
            h_6 = num_to_bit((int(g,2) + int(h_6,2) ) % 2**32,32)
            h_7 = num_to_bit((int(h,2) + int(h_7,2) ) % 2**32,32)
            
        hex_str0 = str(format(int(h_0,2),'x'))
        hex_str1 = str(format(int(h_1,2),'x'))
        hex_str2 = str(format(int(h_2,2),'x'))
        hex_str3 = str(format(int(h_3,2),'x'))
        hex_str4 = str(format(int(h_4,2),'x'))
        hex_str5 = str(format(int(h_5,2),'x'))
        hex_str6 = str(format(int(h_6,2),'x'))
        hex_str7 = str(format(int(h_7,2),'x'))
        
        hex_str_list = [hex_str0,hex_str1,hex_str2,hex_str3,hex_str4,hex_str5,hex_str6,
                        hex_str7]
        hex_concat = ''
        for i in range(8):
            if len(hex_str_list[i]) < 8:
                hex_str_list[i] = '0' + hex_str_list[i]
            hex_concat = hex_concat + hex_str_list[i]

        return hex_concat