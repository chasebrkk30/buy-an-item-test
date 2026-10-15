adventurer_name = input('What is your name?')
item_name = input('What item do you want to buy?')
item_quantity = int(input(f'How many of {item_name} do you want to buy?'))
price_per_item = float(input("What is your PPI (Price per Item)?"))
vip_discount = None

subtotal_cost = item_quantity * price_per_item

if subtotal_cost >= 100.0:
    vip_discount = 0.20
elif 50.0 <= subtotal_cost <= 99.9:
    vip_discount = 0.10
else:
    vip_discount = 0.00

discount_amount = subtotal_cost * vip_discount

total_cost = subtotal_cost - discount_amount

print(f"Your total cost is {total_cost} gold, with a discount of {vip_discount}!")


