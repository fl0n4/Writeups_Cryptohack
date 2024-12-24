

enc_flag = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

x = bytearray(bytes.fromhex(enc_flag))

for i in range(256):
    flag = "".join( chr(i^j) for j in x)    
    if flag.startswith('crypto'):
        print(flag)

#crypto{0x10_15_my_f4v0ur173_by7e}