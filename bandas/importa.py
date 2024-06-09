import json


def importa(ficheiro):

    for banda_info in bandas_de_rock:
        banda = Banda.objects.create(
            nome=banda_info['nome'],
            nacionalidade=banda_info['nacionalidade'],
            ano_de_criacao=banda_info['ano_de_criacao']
        )