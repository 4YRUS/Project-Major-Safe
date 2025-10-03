from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Images
import json 
import base64
from .imagereader import read_image
from django.core.files.base import ContentFile
import time

# Home Page
def home(request):
	return render(request,'home.html')

# About Us Page 
def aboutUs(request):
	return render(request,'aboutUs.html')

# aiCanvas
def aiCanvas(request):
	return render(request,'aiCanvas.html')

# Calls the external function.
def read_canvas(path):
    text = read_image(path)
    print(text)
    return text

# returns response for aiCanvas
def return_canvas_response(request):
    message = "Hey Ssup??!! Draw or Write any thing, let me solve."
    if request.method=='POST':
        try:
            message = "HELLO IT HAS COME HERE"

            print(f"\n\n\n {message} \n\n\n")

            imagedata = json.loads(request.body).get('image')

            a,imagestring = imagedata.split(';base64,')

            image = ContentFile(base64.b64decode(imagestring),name='firstimage.png')

            obj1 = Images.objects.create(image = image)

            image_url = obj1.image.url

            print('\n\n\n',image_url,"\n\n\n")

            try:

                message = read_canvas("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\MAJOR PROJECT\\major_project" + image_url)
                # message = read_canvas("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\work\\" + image_url)
                # message = "THIS IS A TEMPORARY RESPONSE"
                # print(f"\n\n\n {message} \n\n\n")
                # time.sleep(10)
                obj1.delete()

                return JsonResponse({"message": message})
            except:
                obj1.delete()
                return JsonResponse({"message":"Sorry, There was an error. "})
        except:
            return JsonResponse({"Error" : "Not Valid Form"})


    return JsonResponse({"message":message})


#Path Finder
def pathFinder(request):
	return render(request,"pathFinder.html")