import requests

def Weather(city):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&lang=pt_br&q='
    # city = input('Enter the City Name :')
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    text = ("O tempo está {0} Temperatura mínima {1} Temperatura máxima {2} ".format(
        json_data['weather'][0]['description'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return text