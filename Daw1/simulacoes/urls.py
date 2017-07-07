from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import SimulacoesDetailView, SimulacoesListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', SimulacoesListView.as_view(), name='simulacoes'),
    url(r'^(?P<pk>\d+)/$', SimulacoesDetailView.as_view(), name='simulacoes_detail' ), 
    # url(r'^(?P<id>\d+)', 'simulacoes.views.simulacoes_detail_view_func', name='simulacoes_detail_function' ), 
]