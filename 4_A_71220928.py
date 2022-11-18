print("===================CAFE===================")
print("==========MASUKKAN JUMLAH PESANAN=========")
q = input("CAPPUCINO         DISKON 50%      Rp 25.000       :")
w = input("VANILLA LATTE     DISKON 65%      Rp 22.000       :")
e = input("AMERICANO         DISKON 35%      Rp 30.000       :")
r = input("BREWED COFFEE     DISKON 40%      Rp 20.000       :")

a = int(q)*25.000*50/100
s = int(w)*22.000*65/100
d = int(e)*30.000*35/100
f = int(r)*20.000*40/100

z = int(a) + int(s) + int(d) + int(f) 

print("=================TOTAL=================")
print("TOTAL CAPPUCINO         : Rp ",a)
print("TOTAL VANILLA LATTE     : Rp ",s)
print("TOTAL AMERICANO         : Rp ",d)
print("TOTAL BREWED COFFEE     : Rp ",f)
print("Jumlah total biaya yang harus dibayar adalah Rp ",z,".0")
