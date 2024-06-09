from bandas.models import *
import json

print("Loader iniciado!")

with open('bandas/json/bandas.json') as bandas_ficheiro:
    bandas = json.load(bandas_ficheiro)

    for banda_info in bandas['bandas']:
            Banda.objects.create(
                nome=banda_info['nome'],
                nacionalidade=banda_info['nacionalidade'],
                ano_criacao=banda_info['ano_criacao']
            )
print("Dados das bandas carregados!")
with open('bandas/json/discos.json') as discos_ficheiro:
        albuns = json.load(discos_ficheiro)

        for disco_info in albuns['discos']:
            banda = Banda.objects.get(nome=disco_info['banda'])
            album = Album.objects.create(
                titulo=disco_info['titulo'],
                banda=banda,
            )

            for musica_info in disco_info['musicas']:
                Musica.objects.create(
                    titulo=musica_info['titulo'],
                    duracao=musica_info['duracao'],
                    banda=banda,
                    album=album,
                )
print("Dados dos discos carregados!")
print("Dados carregados com sucesso!")

