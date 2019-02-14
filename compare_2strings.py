s1,s2=input().split()
if len(s1)>len(s2):
	print(s1)
elif len(s1)==len(s2) or len(s2)>len(s1):
	print(s2)
