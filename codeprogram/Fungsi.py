# perpangkatan
#def a (x):
#    return x ** 2
a = lambda x : x ** 2

# perpangkatan dengan penjumlahan
#def b (x,y)
#    return x,y : x ** 2 + y ** 2
b = lambda x,y : x ** 2 + y ** 2

# Menghitung rata-rata
#def c (*args)
#    return sum(args)/len(args)
c = lambda *args : sum (args)/len(args)

#Membuat huruf acak
#def d (s)
# return "".join(set(s))
d = lambda s: " ".join(set(s))

print(a(20))
print(b(5,10))
print(c(4, 5, 6,-1))
print(d("ardelino"))

