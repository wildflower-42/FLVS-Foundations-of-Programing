#The Purpose of this program is to list addition tables up to 20:
def main():
  
  ans = 0
  add = 0
  for ans in range(0,20):
    add = (str("1 + ")+str(ans)+" = ")
    ans = ans + 1
    print(str(add)+str(ans))
main()
