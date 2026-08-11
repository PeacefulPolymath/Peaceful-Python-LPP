import random

def get_random_weather():
    temp = random.uniform(-50 , 50)
    temp = round(temp , 2)
    feels_like = random.uniform(temp + 10 , temp -10)
    feels_like = round(feels_like , 2)
    humidity = random.randint(0 , 100)
    pressure = random.randint(990 , 1010)
    dict = {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity,
        'pressure': pressure
    }
    return dict
data = []
for i in range(100):
    weather = get_random_weather()
    data.append(weather)

def get_average_temperature(weather_data):
    total = 0
    counter = 0
    for i in weather_data:
        total += i['temp']
        counter += 1
    average = total /counter
    return average
print(get_average_temperature(data))