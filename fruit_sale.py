#banana = 3 per kg, + 4.99, if over 50 then 4.99-1.5 

weight = int(input('how many kg of banana?'))

def order_cost(weight):
    banana_price = weight*3 
    if banana_price>50:
        post_packing = 3.49
    else:
        post_packing = 4.99
    total_cost=banana_price+post_packing
    print(total_cost)

order_cost(weight)