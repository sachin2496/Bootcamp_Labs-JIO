import sys

# Access the passed arguments
if len(sys.argv) == 1 :
    print("NO argument passed")
    exit()
else:
    args = sys.argv[1:]
    print(args)
    a = args[0]


class compfactorial:
    def compute(self, n) -> int:
        res = 1
        for i in range(1, n + 1):
            res = res * i
        return res


obj = compfactorial()
print("a : " + a)
print(type(a))
try:
    a_int = int(a)
    output = obj.compute(a_int)
    print(output)
except ValueError:
    print("Invalid input: cannot convert an empty string to an integer")
