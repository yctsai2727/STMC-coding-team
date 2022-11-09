# Eligibility code using or 

math = float(input('Maths: '))
phy = float(input('Physics: '))
chem = float(input('Chemistry: '))

if (math+phy >= 140) or (math >= 65 and phy >= 55 and chem >= 50 and (math+phy+chem) >= 190):
    print('You are in!')
else:
    print('Sorry, you are not eligible :(')