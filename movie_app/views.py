from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import *
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)