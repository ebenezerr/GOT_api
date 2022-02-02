from django.urls import path

from apps.cast.views import CharacterViewSet

app_name = "cast"
urlpatterns = [
    path('characters/', CharacterViewSet.as_view({"get": "list", "post": "create"}), name="character-list"),
]
