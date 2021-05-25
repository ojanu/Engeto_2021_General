start = int(input("START: "))
stop = int(input("STOP: "))
divisor = int(input("DIVISOR: "))
pr_list = []
if divisor == 0:
  print("Cannot divide by zero")
  exit()
# generování sbírky
print("Numbers in range", (start, (stop + 1)), "divisible by", divisor, ":")
for i in range(start, (stop + 1)):
  if i % divisor == 0:
    pr_list.append(i)
    print(pr_list)