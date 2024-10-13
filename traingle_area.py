def area_triangle():
    a = int(input('give length of first side'))
    b = int(input('give length of second side'))
    c = int(input('give length of third side'))
    s = (a+b+c)/2
    area = float(pow (s*(s-a)*(s-b)*(s-c),1/2))
    print(area)

area_triangle()