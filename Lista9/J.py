n = int(input())
k = int(input())

l1 = []
qtd = 0

for i in range(n):
    n1 = int(input())
    l1.append(n1)
l1.sort(reverse=True)
for i in range(len(l1)):
    limite = l1[k-1]
    if l1[i] >= limite:
        qtd +=1
print(qtd)

