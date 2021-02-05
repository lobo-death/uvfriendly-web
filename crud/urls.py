from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'crud'

urlpatterns = [
    # Create a new register
    url(r'newp/', views.ProjetosCreate.as_view(), name='form_projs'),
    url(r'newc/', views.ComponentesCreate.as_view(), name='form_comps'),
    url(r'newt/', views.TecnologiasCreate.as_view(), name='form_techs'),
    url(r'newu/', views.UsuariosCreate.as_view(), name='form_users'),

    # Update an existent register
    path(r'editp/<int:pk>', views.ProjetosUpdate.as_view(), name='form_projs'),
    path(r'editc/<int:pk>', views.ComponentesUpdate.as_view(), name='form_comps'),
    path(r'editt/<int:pk>', views.TecnologiasUpdate.as_view(), name='form_techs'),
    path(r'editu/<int:pk>', views.UsuariosUpdate.as_view(), name='form_users'),

    # Delete an existent register
    path(r'delep/<int:pk>', views.ProjetosDelete.as_view(), name='dele_projs'),
    path(r'delec/<int:pk>', views.ComponentesDelete.as_view(), name='dele_comps'),
    path(r'delet/<int:pk>', views.TecnologiasDelete.as_view(), name='dele_techs'),
    path(r'deleu/<int:pk>', views.UsuariosDelete.as_view(), name='dele_users'),

    # Detail of an existent register
    path(r'viewp/<int:pk>', views.ProjetosView.as_view(), name='view_projs'),
    path(r'viewc/<int:pk>', views.ComponentesView.as_view(), name='view_comps'),
    path(r'viewt/<int:pk>', views.TecnologiasView.as_view(), name='view_techs'),
    path(r'viewu/<int:pk>', views.UsuariosView.as_view(), name='view_users'),
]
