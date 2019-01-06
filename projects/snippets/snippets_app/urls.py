from django.urls import path
from snippets_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# Importamos e utilizamos format_suffix_patterns para dar a opção de escolha
# do tipo de formato que nossa Web API irá receber e retornar as requisições
# e respostas.