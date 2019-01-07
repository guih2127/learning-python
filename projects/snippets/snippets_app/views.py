from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

# Indo um passo a frente, o DRF já nós dá um conjunto de generic views
# já preparadas, que possuem mixed in implementados. Ou seja, podemos escrever
# bem menos código do que estavamos escrevendo.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# ListCreate é uma classe que disponibiliza apenas os metódos .list() e .create().
# RetrieveUpdateDestroy nos disponibiliza os metódos .retrieve(), .update() e .destroy().

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Criamos as views para User e UserDetail, nada muito diferente do que fizemos anteriormente.
# UserList herda de ListAPIView e UserDetail herda de RetrieveAPIView, pois as listas de usuários
# e detalhe de um usuário em específico será apenas read-only. É bom lembrar que List lista uma queryset,
# e retrieve retorna uma instância da model.