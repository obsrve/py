def make_car(car_mark, car_model, **car_info):
    car_info['Mark'] = car_mark
    car_info['Model'] = car_model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)