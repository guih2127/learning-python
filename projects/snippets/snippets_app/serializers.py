from rest_framework import serializers
from snippets_app.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# A primeira coisa a se fazer para criar uma Web API é criar um SERIALIZER. Serializers
# provém modo para serializar e deserializar instâncias em representações como json. 
# Ou seja, o processo de serialização consiste em transformar as instâncias, escritas em Python,
# e convertê-las no formato json.

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

# Nosso código com serializers.Serializer estava replicando muita coisa da Model, então
# herdamos de ModelSerializer para deixar o código mais conciso. A classe ModelSerializer
# funciona de forma semelhante ao ModelForm do Django.
# ModelSerializers não fazem nada mágico, são somente um atalho para criar um serializer,
# já que determinam automaticamente um conjunto de campos e possui implementações básicas padrão
# para os metódos create e update.