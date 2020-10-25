def kadane(pizza,n):
	max_atual = 0
	max_total = -1
	for i in xrange(n):
		max_atual = max_atual + pizza[i]
		if max_atual < 0:
			max_atual = 0
		if max_atual > max_total:
			max_total = max_atual
	return max_total

n = int(raw_input())
pizza = list(map(int,raw_input().split()))
for i in xrange(n):
	pizza[i]*=-1
circular = kadane(pizza,n)
for i in xrange(n):
	pizza[i]*=-1
soma_normal = sum(pizza)
kadane_circular = soma_normal + circular
kadane_normal = kadane(pizza,n)
print(max(kadane_circular,kadane_normal))
