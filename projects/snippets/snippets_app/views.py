from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer

# Inicialmente vamos criar as Views sem utilizar nenhuma funcionalidade do DRF.
# A raiz da nossa API vai ser uma view que suporta a listagem de todos os snippets
# ou a criação de um novo.

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# Também precisamos de uma view que corresponda à um snippet individual, e pode ser
# utilizada para obter, atualizar ou deletar um snippet existente.

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

# É bom constatar que, por enquanto, tem vários casos que ainda não estamos lidando no momento.
# Por exemplo, se a requisição for feita com um metódo que a view não suporta, retornaremos uma
# resposta 500 "Server Error". Ainda assim, por enquanto isso aqui serve.
