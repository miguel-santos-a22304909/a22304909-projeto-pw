from django import forms    # formulários Django
from .models import Banda
from .models import Musica

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe.

    help_texts = {
            'nome': 'Insira o nome da banda.',
            'ano_criacao': 'Insira o ano de criação da banda.',
            'biografia': 'Insira uma breve biografia da banda.',
            'nacionalidade': 'Insira a nacionalidade da banda.',
            'descricao': 'Insira a descrição da banda.',
            'foto': 'Insira uma foto da banda'

        }

class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe.