# nas views ficam a "lógica" que utilizaremos no projeto,
# inicialmente, escrevermos duas view functions para os
# dois endpoints que definimos.

from rest_framework import viewsets

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

# 1.
""" def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data) """

# # inicialmente, escrevemos views utilizando o django, normal, sem utilizar o DRF,
# # essas views utilizam o JsonResponse para retornar os dados em JSON.
# # porém, precisaremos utilizar o DRF, que provém para nós um conjunto enorme de 
# # componentes e coisas convenientes para criar APIs.

# 2.
""" class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data) """

# Utilizamos a classe APIView, já uma classe do Django Rest, para criarmos
# nossa API de forma mais limpa.
# porém, podemos ir um pouco mais, e utilizar as views genéricas do DRF
# para criar as views da nossa API.

# aqui, podemos melhorar ainda mais utilizando Viewsets,
# as views PollList e PollDetail utilizam o mesmo serializer
# e a mesma queryset base, então podemos agrupá-las em uma viewset
# e conectá-las nas urls utilizando um router.

""" class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer """

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

""" class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer """

# aqui, definimos uma queryset, que determina a queryset inicial,
# e posteriormente pode ser filtrada, ordenada, etc.
# a serializer_class é o serializer que iremos utilizar para serializar
# a nossa saída e desserializar a entrada de dados.

# quanto as classes genéricas, elas tem algumas diferenças entre si:
# ListCreateAPIView: Permite apenas GET e POST, permite listar entidades ou criar uma.
# RetrieveDestroyAPIView: Permite apenas GET e DELETE, ou seja, ver ou deletar uma entidade.
# CreateAPIView: Permite apenas o metódo POST, ou seja, permite criação de entidades mas
# não permite listá-las.

# agora que definimos melhor os endpoints da API, vamos editar as views.
# como /polls e /polls/<pk> não irão mudar, essas views serão mantidas.

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

# ...
# PollList and PollDetail views

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

# sobrescrevmos o metódo get_queryset, para filtrar apenas as choices
# com o poll.id passado na url. obtemos essa id com self.kwargs["pk"]


class CreateVote(APIView):
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# aqui, criamos uma classe baseada na classe APIView, porque desejamos
# customizar completamente o nosso comportamento. novamente, obtêmos <pk>
# e <choice_pk> da url.

# COMO ESCOLHER O MELHOR TIPO DE VIEW?
# vimos 4 tipos de views que podemos utilizar para criar a API, sendo elas
# views normais do django, APIViews, views genéricas e ModelViewSets.

# ModelViewSet: Deve ser utilizada quando desejarmos permitir todas ou quase
# todas as operações CRUD no model.

# Views Genéricas: Quando desejarmos permitir apenas algumas operações
# no model.

# APIViews: Quando desejarmos editar completamente o comportamento da view.