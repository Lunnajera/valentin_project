from django.urls import path
from .views import quiz_view, valentine_view, accept_view,foto,video

urlpatterns = [
    path("", quiz_view, name="quiz"),
    path("valentine/", valentine_view, name="valentine"),
    path("accept/", accept_view, name="accept"),
    path('foto/', foto, name='foto'),
    path('video/', video, name='video'),
]
