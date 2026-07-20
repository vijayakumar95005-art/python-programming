cost_price=int(input())
selling_price=int(input())
if cost_price>selling_price:
    print("Loss:",selling_price-cost_price)
elif cost_price<selling_price:
    print("Profit:",selling_price-cost_price)
else:
    print("No profit No Loss")

