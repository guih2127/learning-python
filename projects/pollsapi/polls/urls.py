# aqui ficam as urls que utilizaremos para mapear a API
# inicialmente, a API terá dois endpoints que retornarão dados
# em JSON, /polls/ e /polls/<id>/

# from django.urls import path
# from .views import polls_list, polls_detail

# 1.
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]

# 2.
from rest_framework.routers import DefaultRouter
from .views import PollViewSet
from django.urls import path
from .views import ChoiceList, CreateVote, UserCreate, LoginView

# 3.
# até agora, temos três endpoints na API, /polls/, /polls/<pk>/,
# /choices/ e /vote/. podemos, e muito, melhorar os endpoints de nossa
# api.

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]

urlpatterns += router.urls