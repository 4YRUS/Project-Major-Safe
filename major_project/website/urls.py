from . import views
from django.urls import path,include


urlpatterns = [

    path('', views.home, name='home'),
    path('about-us/', views.aboutUs, name='aboutUs'),

    path('aiCanvas/', views.aiCanvas, name='aiCanvas'),
    path('canvasResponse/',views.return_canvas_response,name="canvas"),

    path('path-finder/',views.pathFinder, name="pathFinder"),
    
]