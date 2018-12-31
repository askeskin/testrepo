 

 
asalOlmayanlar=[]
carpanlar=[]
sayi =29299141
#302053
print("sayi:",sayi)
for i in range(2,(sayi//2)+1):
  kalan=sayi%i
  if kalan!=0 or i in asalOlmayanlar:
    continue
  t = 0
  for k in carpanlar:
    if i%k==0:
      t = k

  if t != 0 :
    #asalOlmayanlar.append(t)
    continue

  carpanlar.append(i)

  #asalCarpanlar.append(i)  
  for j in carpanlar:  
    if( i*j < sayi):
      asalOlmayanlar.append(i*j)

if len(carpanlar) == 0:
  print(sayi," asal sayıdır.")
else:
  print(carpanlar) 
  print(asalOlmayanlar)

