

def currency(fn):
    def wrapper(*arg, **kwargs):
        check = fn(*arg, **kwargs)
        if type(check) != int:
            raise Exception('NotINT')
        return check
    return wrapper

@currency
def price_tax(price, tax, type):
    if type == str:
        a = str(price*(1+tax))
    elif type == int:
        a = int(price*(1+tax))
    else:
        a = float(price*(1+tax))
    return a

print(price_tax(7,0.15, int))
print(price_tax(7,0.15, float))