# aqui ficam as urls que utilizaremos para mapear a API
# inicialmente, a API terá dois endpoints que retornarão dados
# em JSON, /polls/ e /polls/<id>/

from django.urls import path
from .views import polls_list, polls_detail

urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail")
]