# para nossa API, a primeira coisa que precisamos é de um modo de 
# serializar as instâncias dos modelsem representações, esse processo é
# denominado serialização, ou seja, criar a representação dos dados
# que possamos transferir para algum lugar. Desserialização é o processo
# inverso.

from rest_framework import serializers

from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

# em detalhes, um ModelSerializer cria um serializer automaticamente,
# baseado na Model, como o Django forms faz com formulários. ele inclui
# implementações básicas dos metódos create() e update() e gera validações
# para os serializers automaticamente. o metódo save(), que também está incluído,
# sabe como criar ou atualizar uma instância.