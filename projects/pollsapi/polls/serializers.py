# para nossa API, a primeira coisa que precisamos é de um modo de 
# serializar as instâncias dos modelsem representações, esse processo é
# denominado serialização, ou seja, criar a representação dos dados
# que possamos transferir para algum lugar. Desserialização é o processo
# inverso.

from rest_framework import serializers

from .models import Poll, Choice, Vote
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

# sobrescrevemos o metódo create do ModelSerializer de User. como não temos
# que obter o password na resposta, utilizamos write_only=True.
# além disso, certificamos que não salvaremos o password cru, com a função
# set_password.
# agora, quando criarmos um usuário, um token também será criado para ele.