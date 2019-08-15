
def stru(data):
  f = " "
  op = [
  '+',
  '-',
  'x',
  'X',
  '/'
  ]
  for  i in range(0,len(data),1):
    x = data.find(op[i])
    go = False
    if x != -1:
      go = True
      a = data[x-1]
      b = data[x+1]
      if b == f:
        if a == f :
          pass
      else:
        print(float(a)+float(b))
