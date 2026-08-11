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
    data.append(print(get_random_weather()))