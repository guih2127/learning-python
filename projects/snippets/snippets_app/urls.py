from django.urls import path
from snippets_app import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# Importamos e utilizamos format_suffix_patterns para dar a opção de escolha
# do tipo de formato que nossa Web API irá receber e retornar as requisições
# e respostas.

# Atualizamos nossas urls já que agora estamos utilizando class based views.