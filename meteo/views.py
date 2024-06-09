from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.


def tempo_lisboa_view(request):
    response_distritos = requests.get("https://api.ipma.pt/open-data/distrits-islands.json")
    response_clima = requests.get("https://api.ipma.pt/open-data/weather-type-classe.json")

    distritos = response_distritos.json()["data"]
    clima = response_clima.json()["data"]

    lisboa = None

    for distrito in distritos:
        if distrito["local"] == "Lisboa":
            lisboa = distrito
            break

    if lisboa:
        global_id_local = lisboa["globalIdLocal"]
        response_previsao = requests.get(f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json")
        previsao_meteorologica = response_previsao.json()["data"]

        # Lista para armazenar os dados dos próximos 5 dias
        dados_proximos_dias = []


        for previsao in previsao_meteorologica:

            temperatura_minima = previsao["tMin"]
            temperatura_maxima = previsao["tMax"]
            data = previsao["forecastDate"]
            id_tipo_clima = previsao["idWeatherType"]

            # Encontrar a descrição do tempo com base no id
            descricao_tempo = None
            for clima_tipo in clima:
                if clima_tipo["idWeatherType"] == id_tipo_clima:
                    descricao_tempo = clima_tipo["descWeatherTypePT"]
                    break

            # Se encontrarmos uma descrição de tempo válida, construímos o URL do ícone correspondente
            if descricao_tempo:
                icone_tempo = "meteo/w_ic_d_" + (str(id_tipo_clima) if int(id_tipo_clima) > 9 else "0" + str(id_tipo_clima)) + "anim.svg"


            dados_proximos_dias.append({
                "data": data,
                "temperatura_minima": temperatura_minima,
                "temperatura_maxima": temperatura_maxima,
                "descricao_tempo": descricao_tempo,
                "icone_tempo": icone_tempo if descricao_tempo else None
            })


        context = {
            "dados_proximos_dias": dados_proximos_dias
        }

        # Renderizar o template com os dados
        return render(request, "meteo/lisboa.html", context)

    else:
        return render(request, "error.html", {"message": "Lisboa não encontrada nos distritos."})