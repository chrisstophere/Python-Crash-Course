def make_car(manufacturer, model_name, **car_info):
    car_info['make'] = manufacturer
    car_info['model'] = model_name
    return car_info
car_profile = make_car('ford', 'f150', color='blue', tow_package=True)
print(car_profile)