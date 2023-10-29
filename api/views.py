from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import  getQuestionAnswer, get_question,getAllQuestion, convert_audio_to_text
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/answers/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Returns answer to the question'
        },
         {
            'Endpoint': '/allquestion/',
            'method': 'GET',
            'body': None,
            'description': 'Returns all question answer'
        },
        {
            'Endpoint': '/question/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single question object'
        },
    ] 
    return Response(routes)

@api_view(['GET'])
def getQuestion(request, pk):
    if request.method == 'GET':
        return get_question(request, pk)
    
@api_view(['GET'])
def getAllQues(request):
    if request.method == 'GET':
        return getAllQuestion(request)


@api_view(['POST']) 
def getAnswer(request):
    if request.method == 'POST':
        return getQuestionAnswer(request)


@api_view(['POST']) 
def getNote(request):
    if request.method == 'POST':
        return convert_audio_to_text(request)
    


    
    
    
    

    