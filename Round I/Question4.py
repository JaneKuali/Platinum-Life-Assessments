import sys
def main():
    qty = None
    cost = None

def fetch_quantity():

#Returns a number, any number
    try:
        num = 5
        return num/0
    except Exception as e:
        print("\nOperation error:",e)

def fetch_cost():
    try:
        num = 60
        return num
    except Exception:
        pass
#Returns a number, any number

def compute_cost_per_quantity():
        qty = fetch_quantity()
        cost = fetch_cost()
        try:
            cost_per_quantity = cost/qty
            return cost_per_quantity
        except Exception as e:
            print("\nOperation error:",e)
            sys.exit(1)


cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)
