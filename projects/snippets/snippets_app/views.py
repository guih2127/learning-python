from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

# Uma das melhores vantagens de se utilizar Class Based Views é que elasnos permitem
# compor pedaços reutilizáveis de comportamento.
# As operações de create/retrieve/update/delete que estamos utilizando até agora são
# bem parecidas em várias Web APIs que criamos. Esses comportamentos comuns são implementados
# nas classes MIXIN do DRF.

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Analisando por um momento, nossa classe agora herda de 2 mixins, ListModel e CreateModel,
# além da classe GenericAPIView. A classe genérica provém a funcionalidade raíz e as outras duas
# proporcionam as ações list() e create().

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Similar ao caso acima, estamos utilizando a classe GenericAPIView e outros classes
# Mixins para prover as ações .retrieve(), .update() e .destroy().