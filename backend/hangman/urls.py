from django.urls import include, path
from rest_framework import routers

from hangman.views import WordViewset

router = routers.DefaultRouter()
router.register(r'words', WordViewset)

urlpatterns = [
    path('', include(router.urls)),
]