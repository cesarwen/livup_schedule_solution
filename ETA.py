import requests
import json

def ETA(origin, destination):

    origin = "Rua Amaro Carvalheiro, 158 - Pinheiros"
    destination = "rua verbo de vino 1061"
    api_link = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&mode=driving&key=AIzaSyChknhNuJvPardLC2t_gwOjOgZk1gVOxJ8".format(origin, destination)

    route = requests.get(api_link)

    msg = json.loads(route.text)
    duration = int(msg["routes"][0]['legs'][0]['duration']['value'])
    return(duration)
    #print('Viagem [min] = {}\nViagem [s]   = {}'.format(round(duration/60,0), duration))