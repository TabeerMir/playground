

def imperial_to_kg(stones, pounds):
    kg = (6.35*stones)+(pounds/2.205)
    print(f'{kg} kg')


'''which_measure = input('which measurement would you like to convert?: stones to kg, inches to cm, ounces to ml? ')
if which_measure == 'stones to kg':
    stones = int(input('how many stones'))
    pounds = int(input('how many ounces'))
    imperial_to_kg(stones, pounds)
elif which_measure == 'inches to cm':
    imperial_to_cm()'''

imperial_to_kg(10,9)

