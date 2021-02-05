from . import views
from django.conf.urls import url

app_name = 'sistema'

urlpatterns = [
    url(r'base', views.base, name='base'),
    url(r'based/', views.based, name='based'),
    url(r'blank/', views.blank, name='blank'),
    url(r'charts/', views.charts, name='charts'),
    url(r'error404/', views.error404, name='error404'),
    url(r'^$', views.index, name='index'),
    url(r'tables/', views.tables, name='tables'),

    url(r'channels/', views.channels, name='channels'),
    url(r'publics/', views.publics, name='publics'),
    url(r'watcheds/', views.watcheds, name='watcheds'),

    url(r'accessibility/', views.accessibility, name='accessibility'),
    url(r'acquisition/', views.acquisition, name='acquisition'),
    url(r'file_upload/', views.file_upload, name='file_upload'),
    url(r'data_upload/', views.data_upload, name='data_upload'),
    url(r'read_files/', views.read_files, name='read_files'),
    url(r'storage/', views.storage, name='storage'),
    url(r'synchronization/', views.synchronization, name='synchronization'),

    url(r'components/', views.components, name='components'),
    url(r'projects/', views.projects, name='projects'),
    url(r'technologies/', views.technologies, name='technologies'),
    url(r'users/', views.users, name='users'),
]