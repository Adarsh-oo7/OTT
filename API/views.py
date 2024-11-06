from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm  
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from moves.models import movie
from moves.models import watch_history,watch_list
from .serializers import MovieSerializer,MovieHistorySerializer,WatchListSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@csrf_exempt  # Use with caution
@api_view(['POST'])
@permission_classes((AllowAny,))
def Register(request):
    form = CustomUserCreationForm(data=request.data)
    
    if form.is_valid():
        form.save()
        return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)
    
    # Get errors and return them in a structured format
    errors = form.errors.as_json()  # This converts the errors to JSON format
    return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get("email")  # Use "email" as per your authentication method
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'}, status=HTTP_400_BAD_REQUEST)
    
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)



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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def movie_history(request):
    history = watch_history.objects.filter(user=request.user)
    serializer = MovieHistorySerializer(history, many=True)
    return Response(serializer.data)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_watch_later(request):
    user = request.user  
    print("Request Data:", request.data)  
    movie_id = request.data.get("movie")
    if not movie_id:
        return Response({'error': "Movie ID is required."}, status=status.HTTP_400_BAD_REQUEST)
    if watch_list.objects.filter(user_id=user, movie_id=movie_id).exists(): 
        return Response({'error': "This movie is already in your watch list."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        movie_instance = movie.objects.get(id=movie_id)  
    except movie.DoesNotExist:
        return Response({'error': "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
    watch_later_instance = watch_list(user_id=user, movie_id=movie_instance) 
    watch_later_instance.save()  
    return Response({
        'message': "Movie added to watch later successfully.",
        'movie_id': movie_id 
    }, status=status.HTTP_201_CREATED) 




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_email(request):
    print(request.user.email)
    return Response({"email": request.user.email})