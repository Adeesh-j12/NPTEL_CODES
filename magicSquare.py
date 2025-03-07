#MAGIC SQUARE
def magic_square(n):
  # we have taken matrix input.
  magicSquare=[]
  for i in range(n):
    l=[]
    for j in range(n):
      l.append(0)
    magicSquare.append(l)
  # another way to form matrix of 0.
  #magic=[[0 for i in range(n)] for j in range(n)]
  i=n//2
  j=n-1
  num=n*n
  count=1

  while(count<=num):
    if(i==-1 and j==n):     #condition 4
      j=n-2
      i=0
    else:
      if(j==n):   #column value is exceeding
        j=0
      if(i<0):    #row is becoming -1
        i=n-1
    if(magicSquare[i][j]!=0):    # condition 3
      j=j-2
      i=i+1
      continue
    else:
      magicSquare[i][j]=count
      count=count+1
    j=j+1
    i=i-1
# Here we done now we have to print element.
  for i in range(n):
    for j in range(n):
      print(magicSquare[i][j], end=" ")
    print()
  print("The sum of each row/column/digonal is: "+str(n*(n**2+1)/2))
magic_square(3)
