from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ParagraphSerializer, StatSerializer
from .models import GlobalStats, Paragraph

@api_view(['GET'])
def get_paragrahs(request):
    result = Paragraph.objects.all()
    serialized_paragraphs = ParagraphSerializer(result, many=True)
    return Response(serialized_paragraphs.data)

@api_view(['POST'])
def add_paragraph(request):
    print(request)
    new_paragraph = ParagraphSerializer(data=request.data)
    if new_paragraph.is_valid():
        new_paragraph.save()
    return Response(new_paragraph.data)

@api_view(['DELETE'])
def delete_paragraph(request, id_to_delete):
    paragraph = Paragraph.objects.get(id = id_to_delete)
    operation = paragraph.delete()
    data = {}
    if operation:
        data["success"] = "Delete Successful"
    else:
        data["failure"] = "Delete Operation Failed"
    return Response(data=data)

@api_view(['POST'])
def update_paragraph(request, id_to_update):
    paragraph = Paragraph.objects.get(id = id_to_update)
    existing_paragraph = ParagraphSerializer(instance = paragraph, data = request.data)
    if existing_paragraph.is_valid():
        existing_paragraph.save()
    return Response(existing_paragraph.data)



@api_view(['POST'])
def add_stat(request):
    stats = StatSerializer(data = request.data)
    if stats.is_valid():
        stats.save()
    return Response(stats.data)

@api_view(['GET'])
def get_stats(request):
    stats = GlobalStats.objects.all()
    serialized_stats = StatSerializer(stats, many = True)
    return Response(serialized_stats.data)

def index(request):
    return HttpResponse("Welcome to Paragraphs' Rift! Visit getPara/ or addPara/ for your requests.")
