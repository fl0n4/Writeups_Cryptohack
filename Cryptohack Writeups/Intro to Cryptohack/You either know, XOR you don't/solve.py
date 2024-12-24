

enc_flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

x = bytearray(bytes.fromhex(enc_flag))

print(xor(x,b"crypto{"))  
#b'myXORke+y......
# So lets try myXORkey as a key

print(xor(x,b"myXORkey"))  
#crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
# Here you go 

