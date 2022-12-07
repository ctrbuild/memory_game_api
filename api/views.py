from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from memorygame.models import Card, Score
from .serializers import CardSerializer, ScoreSerializer

@api_view(['GET'])
def getCard(request):
    card =Card.objects.all()
    serializer =CardSerializer(card, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCard(request):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getScores(request):
    score =Score.objects.all()
    serializer =ScoreSerializer(score, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addScores(request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)



