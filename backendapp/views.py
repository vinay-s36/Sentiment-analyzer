from django.shortcuts import render
from backendapp.spice import inputfunction
from backendapp.image import text
from .models import image
import random


def index(request):
    return render(request, 'index.html')


def sentiment(request):
    tweetinp = request.POST['tweetInput']
    tweetinp1 = inputfunction(tweetinp)
    return render(request, 'index.html', {'tweetinput': tweetinp, 'tweetoutput': tweetinp1})


def sentiment1(request):
    image2 = request.FILES['image']
    x = random.randint(1, 1000)
    print(x)
    image4 = image2.name
    image3 = image(name=x, image1=image2)
    image3.save()
    res = text(image4)
    res1 = inputfunction(res)
    return render(request, 'index.html', {'imageinput': res, 'imageoutput': res1})
