from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [

    path("", views.index, name="index"),

    path("basket/", views.basket, name="basket"),

    path("user/<str:name>/" , views.user, name="user") , 

    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

