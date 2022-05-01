N=input()
y=[]
x = [int(a) for a in str(N)] #把整數拆成數字
for i in range(len(x)):
  if i %2==0: #如果是i是偶數就放入y
    y.append(x[i])
    x[i]=0 #再把放入y的數改成0
xs,ys=sum(x),sum(y) #計算它們倆list的和
print(abs(xs-ys)) #再用abs()取絕對值