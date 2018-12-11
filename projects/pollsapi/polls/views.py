# nas views ficam a "lógica" que utilizaremos no projeto,
# inicialmente, escrevermos duas view functions para os
# dois endpoints que definimos.

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

def polls_list(request):
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
    return JsonResponse(data)

# inicialmente, escrevemos views utilizando o django, normal, sem utilizar o DRF,
# essas views utilizam o JsonResponse para retornar os dados em JSON.
# porém, precisaremos utilizar o DRF, que provém para nós um conjunto enorme de 
# componentes e coisas convenientes para criar APIs.