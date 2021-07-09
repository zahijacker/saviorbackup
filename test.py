numbers = input('what are you trying to raise "?/?"?>')
base, power =  map(int, numbers.split(sep="/"))
def raise_to_power(base,power):
    print (base**power)

raise_to_power(base, power)
