from string import Template

def main():
    cart = []
    cart.append(dict(item="butter", price=8, qty=3))
    cart.append(dict(item="milk", price=5, qty=90))
    cart.append(dict(item="rice", price=1, qty=7))
    template = Template("$item X $qty = $price")
    total = 0
    
    for item in cart:
        print('{}'.format(template.safe_substitute(item)))
        total += item["price"] * item["qty"]
    print('Total is: {}'.format(total))

if __name__ == "__main__":
    main()