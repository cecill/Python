def collatz(t):
 if (t % 2) == 1:
  return (3 * t + 1)
 else:
  return (t // 2)
  
counter = 0
num = 1

while counter <> 0: 
 
 while num <> 100:
    print collatz(num)
    num = collatz(num)
    counter = counter + 1
 print "Number =", num, " Iterations =",counter
 num = num + 1 
 
