from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer
from rest_framework import generics

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