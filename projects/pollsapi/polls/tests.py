from django.test import TestCase

# o DRF provém classes que torna a criação de testes mais simples.

# APIRequestFactory: Permite criar requisições com qualquer metódo HTTP,
# que então pode ser passado para uma view para que possamos comparar as respostas.
	# factory = APIRequestFactory()
	# request = factory.post(uri, post data)

# APIClient: Podemos dar um GET ou POST na URL e comparar as respostas.

# APITestCase: A maioria dos testes vão subclassear essa classe.

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from polls import views

# 1
class TestPoll(APITestCase):
	def setUp(self):
		self.client = APIClient()
		self.factory = APIRequestFactory()
		self.view = views.PollViewSet.as_view({'get': 'list'})
		self.uri = '/polls/'
		self.user = self.setup_user()

	@staticmethod
	def setup_user():
	    User = get_user_model()
	    return User.objects.create_user(
	        'test',
	        email='testuser@test.com',
	        password='test'
	    )

	def test_list(self):
	    request = self.factory.get(self.uri)
	    request.user = self.user
	    response = self.view(request)
	    self.assertEqual(response.status_code, 200,
	                     'Expected Response Code 200, received {0} instead.'
	                     .format(response.status_code)
	    )

# 2 podemos fazer os mesmos testes com APIClient, invés de criar as requisições primeiro,
# podemos dar um POST ou um GET diretamente e obter uma resposta.

	def test_list2(self):
		self.client.login(username="test", password="test")
		response = self.client.get(self.uri)
		self.assertEqual(response.status_code, 200,
		                 'Expected Response Code 200, received {0} instead.'
		                 .format(response.status_code))

# 3 agora sabemos testar nossa API, vamos ver como fica com o metódo POST.

	def test_create(self):
	    self.client.login(username="test", password="test")
	    params = {
	        "question": "How are you?",
	        "created_by": 1
	        }
	    response = self.client.post(self.uri, params)
	    self.assertEqual(response.status_code, 201,
	                     'Expected Response Code 201, received {0} instead.'
	                     .format(response.status_code))