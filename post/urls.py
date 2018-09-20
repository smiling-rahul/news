from django.urls import path,include
from .views import index,post,Indian_News,Entertainment,World_News,\
    Economics,Sports,Technology,Life_Style,Science_and_Environment
app_name ='post'
urlpatterns = [
    path('',index,name='index'),
    path('Indian_News/',Indian_News,name='Indian_News'),
    path('World_News/',World_News,name='World_News'),
    path('Economics/',Economics,name='Economics'),
    path('Sports/',Sports,name='Sports'),
    path('entertainment/',Entertainment,name='Entertainment'),
    path('Technology/',Technology,name='Technology'),
    path('Life_Style/',Life_Style,name='Life_Style'),
    path('Science_and_Environment/',Science_and_Environment,name='Science_and_Environment'),

    path('post/<pk>',post,name='post'),


]