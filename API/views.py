from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm  
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from moves.models import movie
from .serializers import MovieSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404




@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def Register(request):
    # Corrected spelling for the form instantiation
    form = CustomUserCreationForm(data=request.data)
    if form.is_valid():
        form.save()
        return Response("Account created successfully")
    return Response(form.errors, status=400)




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)



@api_view(["GET"])
@permission_classes((AllowAny,))
def movie_listing(request):
    data=movie.objects.all()
    for da in data:
        print(da.title)
    Sdata=MovieSerializer(data, many=True)
    return Response(Sdata.data)


@api_view(["GET"])
@permission_classes((AllowAny,))
def movie_detail(request, id):
    Movie = get_object_or_404(movie, id=id)
    Sdata = MovieSerializer(Movie)
    return Response(Sdata.data, status=status.HTTP_200_OK)