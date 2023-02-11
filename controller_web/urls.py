from .views import InstagramView, FacebookView
from django.urls import path


urlpatterns = [
    path('dfg45dfg45gdf/', FacebookView.as_view(), name='facebook'),
    path('asd5a5s4f65as/', InstagramView.as_view(), name='instagram'),
]
