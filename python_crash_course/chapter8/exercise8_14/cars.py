def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car1 = make_car("ford", "ka", color= "white")
car2 = make_car("chevrollet", "onix", color= "black", four_door= True)

print(car1)
print(car2)