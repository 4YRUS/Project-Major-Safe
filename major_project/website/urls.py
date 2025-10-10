from . import views
from django.urls import path,include


urlpatterns = [

    path('', views.home, name='home'),
    path('about-us/', views.aboutUs, name='aboutUs'),

    path('aiCanvas/', views.aiCanvas, name='aiCanvas'),
    path('canvasResponse/',views.return_canvas_response,name="canvas"),

    path('path-finder/',views.pathFinder, name="pathFinder"),

    path('mcq-test-home/',views.mcqTestHome, name="mcqTestHome"),
    path('mcq-test/',views.mcqTest, name="mcqTest"),
    path('pdf-data/',views.getPdfs,name="GetPdfs"),
    path("extract-existing-pdfs/<int:pk>/",views.extractExistingPdf,name="ExtractExistingPdfs"),
    path('extract-mcqs/',views.extractMcqs,name="ExtractMcqs"),

    
]