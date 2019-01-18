def hcf(m1,m2):
	while(m2!=0):
		t=m2
		m2=m1%m2
		m1=t
	return m1
def main():
	n=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(n):
		l.append(int(input()))
	print(l)
	for c in range(q):
		m1=int(input())
		m2=int(input())
		r.append(hcf(l[m1-1],l[m2-1]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
