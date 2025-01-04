from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request): 
    if request.method == 'POST': 
        city = request.POST.get('city', '').strip()  # Obtiene la ciudad y elimina espacios extra.
        
        if city:  # Verifica que el campo no esté vacío.
            try:
                # API URL con la clave proporcionada
                api_url = (
                    f'http://api.openweathermap.org/data/2.5/weather?q={city}'
                    f'&appid=a889b385b5042bfe532ec0eff4a344f8'
                )
                
                # Obtiene los datos de la API
                source = urllib.request.urlopen(api_url).read()
                list_of_data = json.loads(source)
                
                # Extrae y organiza los datos
                data = { 
                    "city": city,
                    "country_code": str(list_of_data['sys']['country']), 
                    "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}", 
                    "temp": f"{round(list_of_data['main']['temp'] - 273.15, 2)}°C", 
                    "pressure": str(list_of_data['main']['pressure']), 
                    "humidity": str(list_of_data['main']['humidity']), 
                }
            except Exception as e:
                # Maneja errores en la solicitud o la conversión de datos
                data = {"error": "No se pudieron obtener los datos. Verifica el nombre de la ciudad."}
        else:
            data = {"error": "El campo de la ciudad está vacío. Por favor, ingresa una ciudad válida."}
    else: 
        data = {}

    return render(request, "main/index.html", data)