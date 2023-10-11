N, M, K = 5, 8, 3
Array = [2,4,5,4,6]
temp = 0
sum = 0

for i in range(N):
  for y in range(i):
    if Array[i] < Array[y]:
      temp = Array[i]
      Array[i] = Array[y]
      Array[y] = temp

num = K
for i in range(M):
  if num > 0:
    sum += Array[N-1]
    num -= 1
  else :
    sum += Array[N-2]
    num = K

print(sum)
  

      
  
  
    
