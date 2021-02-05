from django.shortcuts import render
from uvfriendly.models import Componentes, Projetos, Tecnologias

template_name = 'website'

# Create your views here.
def index(request):
    componentes = Componentes.objetos.all()
    projetos = Projetos.objetos.all()
    tecnologias = Tecnologias.objetos.all()

    contexto = {
        'componentes':componentes,
        'projetos':projetos,
        'tecnologias':tecnologias
    }

    return render(request, 'website/index.html', contexto)



