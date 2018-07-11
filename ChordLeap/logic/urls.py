from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from django.conf.urls import url
from logic import views, auth, controllers
from django.views import generic
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import views, serializers, status
from rest_framework.routers import DefaultRouter
from logic.serializers import EchoView


urlpatterns = [
  url(r'^$', generic.RedirectView.as_view(
      url='/api/', permanent=False)),
  url(r'^api/$', get_schema_view()),
  url(r'^api/auth/', include(
      'rest_framework.urls', namespace='rest_framework')),
  url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
  url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
  url(r'^api/echo/$', EchoView.as_view()),
  url(r'api/chords/$', controllers.ChordList.as_view()),
]
