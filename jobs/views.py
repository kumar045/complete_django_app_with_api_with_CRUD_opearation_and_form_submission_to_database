from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializer

@api_view(['GET', 'PUT', 'DELETE','POST'])

def api(request):
    
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = BlogSerializer(blogs, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def home(request):
    return render(request,'jobs/index.html')


def addbloginfo(request):
    title=request.POST.get('title')
    auther=request.POST.get('author')
    email=request.POST.get('email')
    types=request.POST.get('types')
    signature=request.POST.get('signature')
    blog_info=Blog(title=title,author=auther,email=email,types=types,signature=signature)
    blog_info.save()
    print("form submitted")
    return render(request,'jobs/index.html')
