from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from uvfriendly.models import Componentes, Projetos, Tecnologias, Usuarios, Canais

# Create your views here.
# Channels CRUD
class CanaisList(ListView):
    model = Canais


# Tools CRUD ===========================================================================================================
class ProjetosList(ListView):
    model = Projetos


class ProjetosView(DetailView):
    template_name = 'crud/view_projs.html'
    model = Projetos


class ProjetosCreate(CreateView):
    template_name = 'crud/form_projs.html'
    model = Projetos
    fields = ['nome', 'descricao', 'classe', 'status']
    success_url = reverse_lazy('sistema:projects')


class ProjetosUpdate(UpdateView):
    template_name = 'crud/form_projs.html'
    model = Projetos
    fields = ['nome', 'descricao', 'classe', 'status']
    success_url = reverse_lazy('sistema:projects')


class ProjetosDelete(DeleteView):
    template_name = 'crud/dele_projs.html'
    model = Projetos
    success_url = reverse_lazy('sistema:projects')

#_______________________________________________________________________________________________________________________
class ComponentesList(ListView):
    model = Componentes


class ComponentesView(DetailView):
    template_name = 'crud/view_comps.html'
    model = Componentes


class ComponentesCreate(CreateView):
    template_name = 'crud/form_comps.html'
    model = Componentes
    fields = ['nome', 'descricao', 'fullsize', 'thumbnails', 'status']
    success_url = reverse_lazy('sistema:components')


class ComponentesUpdate(UpdateView):
    template_name = 'crud/form_comps.html'
    model = Componentes
    fields = ['nome', 'descricao', 'fullsize', 'thumbnails', 'status']
    success_url = reverse_lazy('sistema:components')


class ComponentesDelete(DeleteView):
    template_name = 'crud/dele_comps.html'
    model = Componentes
    success_url = reverse_lazy('sistema:components')


#_______________________________________________________________________________________________________________________
class TecnologiasList(ListView):
    model = Tecnologias


class TecnologiasView(DetailView):
    template_name = 'crud/view_techs.html'
    model = Tecnologias


class TecnologiasCreate(CreateView):
    template_name = 'crud/form_techs.html'
    model = Tecnologias
    fields = ['nome', 'alt', 'classe', 'status']
    success_url = reverse_lazy('sistema:technologies')


class TecnologiasUpdate(UpdateView):
    template_name = 'crud/form_techs.html'
    model = Tecnologias
    fields = ['nome', 'alt', 'classe', 'status']
    success_url = reverse_lazy('sistema:technologies')


class TecnologiasDelete(DeleteView):
    template_name = 'crud/dele_techs.html'
    model = Tecnologias
    success_url = reverse_lazy('sistema:technologies')

#_______________________________________________________________________________________________________________________
class UsuariosList(ListView):
    model = Usuarios


class UsuariosView(DetailView):
    template_name = 'crud/view_users.html'
    model = Usuarios


class UsuariosCreate(CreateView):
    template_name = 'crud/form_users.html'
    model = Usuarios
    fields = ['cpf', 'nome', 'sobrenome', 'email', 'senha1', 'senha2', 'status', 'level']
    success_url = reverse_lazy('sistema:users')


class UsuariosUpdate(UpdateView):
    template_name = 'crud/form_users.html'
    model = Usuarios
    fields = ['cpf', 'nome', 'sobrenome', 'email', 'senha1', 'senha2', 'status', 'level']
    success_url = reverse_lazy('sistema:users')


class UsuariosDelete(DeleteView):
    template_name = 'crud/dele_users.html'
    model = Usuarios
    success_url = reverse_lazy('sistema:users')

#_______________________________________________________________________________________________________________________