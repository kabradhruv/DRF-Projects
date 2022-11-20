from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework.parsers import MultiPartParser

def home(request):
    return render(request,'home.html')

def download(request,uid):
    return render(request,'download.html',context={'uid':uid})

# Create your views here.
class HandleFileUpload(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    "message":"Files Uploaded Successfully",
                    'data':serializer.data
                })
            return Response({
                'status':400,
                "message":"Unsuccessfull",
                'data':serializer.errors
            })

        except Exception as e:
            return Response({
                'status':400,
                "message":f"Unsuccessfull because of = {e}",
                'data':serializer.errors
            })