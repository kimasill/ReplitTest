n, m = map(int, input().split())

result = 0
line = 0
temp = 10000
  
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(m):
    if data[j]< temp: 
      temp = data[j]
      line = temp
  temp = 10000
  if line > result : 
    result = line
  
print(result)