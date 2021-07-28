from rest_framework import status, generics
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models.models import Cocktails
from .serializer import CocktailSerializer


class CocktailListAPiView(generics.GenericAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [AllowAny]
    queryset = Cocktails.objects.all()
    
    def get(self, request):
        serilizer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class CocktailretriveAPiView(generics.GenericAPIView):
    serializer_class = CocktailSerializer
    permission_classes =  [IsAuthenticated]
    queryset = Cocktails.objects.all()
    
    def get(self, request):
        queryset = self.get_queryset().filter(user_id=request.user.id)
        serilizer = self.serializer_class(queryset, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class CocktailCreateApiView(generics.GenericAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cocktails.objects.all()

    def post(self, request):
        
        cocktail_data = request.data
        cocktail_data['user_id'] = request.user.id
        print(cocktail_data)
        print("====" * 300)
        print(request.user.id)
        if len(self.get_queryset().filter(name=cocktail_data.get('name'))) == 0:
            serilizer = self.serializer_class(data=cocktail_data)
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(data=serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("cocktail alread exist try adding a different one",status= status.HTTP_409_CONFLICT)
       
