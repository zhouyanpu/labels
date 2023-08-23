from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.getData),
    path('clear/', views.clear),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('allusers/', views.allUsers),
    path('alllabels/', views.allLabels),
    path('labels/', views.addLabel),
    path('mylabels/', views.myLabels),
    path('dellabels/', views.delLabels),
    path('editlabels/', views.EditLabels),
    path('register/', views.addUser),
    path('login/', views.login),

]