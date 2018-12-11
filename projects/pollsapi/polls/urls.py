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
from django.urls import path
from .views import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]
