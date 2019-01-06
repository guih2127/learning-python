from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer

# Agora estamos realmente utilizando funcionalidades do DRF para criar views.
# Refatoramos as views existentes com function based views (@api_view), deixando o código
# um pouco mais conciso e utilizando status codes nomeados.

# Incluímos o argumento format nas views, que permitirá que a nossa Web API lide com
# diversos tipos de dados, e não apenas json.

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Ambos os exemplos ainda são parecidos com as views utilizadas anteriormente.
# Uma das principais diferenças é a presença do objeto Response, que determina o
# tipo correto de conteúdo para retornar para o cliente.
# Além disso, nós não estamos mais prendendo nossas requisições e respostas a um
# determinado tipo de conteúdo, request.data consegue lidar com requisições json,
# mas também consegue lidar com outros formatos.