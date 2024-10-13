age = int(input('what is your age?'))
rate = int(input('heart rate?'))

def zone(age,rate):
    m=208-1.7*age
    if rate>=0.9*m:
        print ('training zone = interval')
    elif 0.7*m<=rate<0.9*m:
        print('training zone = threshold')
    elif 0.5*m<=rate<0.7*m:
        print('aerobic training')
    else:
        print('couch potato')

zone(age, rate)
