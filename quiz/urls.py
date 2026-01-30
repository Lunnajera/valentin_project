from django.urls import path
from .views import quiz_view, valentine_view, accept_view

urlpatterns = [
    path("", quiz_view, name="quiz"),
    path("valentine/", valentine_view, name="valentine"),
    path("accept/", accept_view, name="accept"),
]
