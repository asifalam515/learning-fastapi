cars = ['audi', 'bmw', 'subaru', 'toyota']
 
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

banned_user = ['asif','sakib','naim','tamim']
user = 'marie'
if user not in banned_user:
    print(user.title() + ",You can post a response if you wish")