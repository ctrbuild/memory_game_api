from django.urls import path
from . import views

urlpatterns=[
    path('cards/', views.getCard),
    path('addcard/', views.addCard),
    path('scores/', views.getScores),
    path('addscore/', views.addScores)
]
