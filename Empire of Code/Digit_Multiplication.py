def golf(n):
 r
 while n:
  if n%10:
   r*=n%10
  n//=10
 return r
