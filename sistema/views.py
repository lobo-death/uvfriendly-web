from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from matplotlib import pyplot as plt
import pandas as pd

from uvfriendly.models import Componentes, Projetos, Tecnologias, Usuarios
from uvfriendly.forms import DocumentForm

template_name = 'sistema'

# Create your views here.
def base(request):
    return render(request, 'sistema/base.html')


def based(request):
    return render(request, 'sistema/based.html')


def blank(request):
    return render(request, 'sistema/blank.html')


def charts(request):
    return render(request, 'sistema/charts.html')


def error404(request):
    return render(request, 'sistema/error404.html')


def index(request):
    return render(request, 'sistema/index.html')


def tables(request):
    tabela = pd.read_csv("media/documents/german_credit.csv")
    contexto = {
        'tabela': tabela.to_html(index=False)
    }
    return render(request, 'sistema/tables.html', contexto)

#====================================================

# Channels ===================================================
def channels(request):
    return render(request, 'sistema/channels/channels.html')


def publics(request):
    return render(request, 'sistema/channels/publics.html')


def watcheds(request):
    return render(request, 'sistema/channels/watcheds.html')

#=============================================================

# Tasks ==========================================================
def accessibility(request):
    return render(request, 'sistema/tasks/accessibility.html')


def acquisition(request):
    return render(request, 'sistema/tasks/acquisition.html')


def storage(request):
    return render(request, 'sistema/tasks/storage.html')


def synchronization(request):
    return render(request, 'sistema/tasks/synchronization.html')

#=================================================================

# Tools ===================================================================================
def components(request):
    componentes = Componentes.objetos.all()
    contexto = {
        'componentes': componentes
    }
    return render(request, 'sistema/tools/components.html', contexto)

#__________________________________________________________________________________________
def projects(request):
    projetos = Projetos.objetos.all()
    contexto = {
        'projetos': projetos
    }
    return render(request, 'sistema/tools/projects.html', contexto)

#_______________________________________________________________________________________________________________________
def technologies(request):
    tecnologias = Tecnologias.objetos.all()
    contexto = {
        'tecnologias': tecnologias
    }
    return render(request, 'sistema/tools/technologies.html', contexto)

#_______________________________________________________________________________________________________________________
def users(request):
    usuarios = Usuarios.objetos.all()
    contexto = {
        'usuarios':usuarios
    }
    return render(request, 'sistema/tools/users.html', contexto)

#=======================================================================================================================
def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'sistema/tasks/file_upload.html',{
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'sistema/tasks/file_upload.html')

#=======================================================================================================================
def data_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sistema/tasks/data_upload.html')
    else:
        form = DocumentForm()
    return render(request, 'sistema/tasks/data_upload.html', {
        'form': form
    })

#=======================================================================================================================
def read_files(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # myfile = "media/documents/german_credit.csv"
        # df = pd.DataFrame()
        df = pd.read_csv(myfile, sep=",")
        data1 = df.iloc[1000:2136,2]
        plt.plot(data1, label='tempearatura')
        plt.title("Temperatura")
        plt.xlabel("Quantidade de Amostras")
        plt.ylabel("Temperatura em Graus Celsius")
        show1 = plt.show()
        data2 = df.iloc[1000:2136, 3]
        plt.plot(data2, label='umidade')
        plt.title("Umidade")
        plt.xlabel("Quantidade de Amostras")
        plt.ylabel("Umidade Relativa do Ar em %")
        show2 = plt.show()
        df = df.iloc[1000:2136,[0,1,2,3]]
        contexto = {
            'df': df.to_html(index=False),
            'show1': show1,
            'show2': show2,
        }
        return render(request, 'sistema/tasks/read_files.html', contexto)
    return render(request, 'sistema/tasks/read_files.html')