from rest_framework import serializers
from snippets_app.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# A primeira coisa a se fazer para criar uma Web API é criar um SERIALIZER. Serializers
# provém modo para serializar e deserializar instâncias em representações como json. 
# Ou seja, o processo de serialização consiste em transformar as instâncias, escritas em Python,
# e convertê-las no formato json.

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # A primeira parte do serializer consiste em especificar os campos que serão serializados
    # ou deserializados.

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    
    # Os metódos create e update definem como as instâncias serão criadas ou modificadas utilizando
    # serializer.save(). Uma classe serializer é bem parecida com uma classe do Django Form.