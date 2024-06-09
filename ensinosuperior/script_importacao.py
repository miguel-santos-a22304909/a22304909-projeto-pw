from ensinosuperior.models import *
import json


##def importar_curso(file):

with open("ensinosuperior/json/lei.json") as f:
        informacao_curso = json.load(f)
        detalhes_curso = informacao_curso['courseDetail']

        curso = Curso.objects.create (nome = detalhes_curso['courseName'] ,
            horas_contacto_total = informacao_curso['hrContactoSoma'],
            competencias = detalhes_curso['competences'],
            ects = detalhes_curso['courseECTS'],
            objetivos = detalhes_curso['objectives']
            )

        for disciplina_info in informacao_curso['courseFlatPlan']:
                disciplina = Disciplina.objects.create(
                            nome = disciplina_info['curricularUnitName'],
                            ramo = disciplina_info['curricularBranchName'],
                            ano = disciplina_info['curricularYear'],
                            semestre = disciplina_info['semester'],
                            ects = disciplina_info['ects'],
                            horas_contacto = disciplina_info['hrTotalContacto'],
                            curricularIUnitReadableCode =disciplina_info['curricularIUnitReadableCode']
                            )
                disciplina.cursos.add(curso)

print("Dados carregados com sucesso!")

