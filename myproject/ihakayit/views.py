from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import IHASerializer
from .models import IHA
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class IHARegistrationView(APIView):
    serializer_class = IHASerializer
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IHADeleteView(DestroyAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class IHAUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = IHA.objects.all()
    serializer_class = IHASerializer

    def perform_update(self, serializer):
        serializer.save()


class IHAListView(APIView):
    serializer_class = IHASerializer
    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        ihas = IHA.objects.all()
        serializer = self.serializer_class(ihas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IHAFilterView(ListAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['brand', 'model', 'weight', 'category']
    search_fields = ['brand', 'model', 'category']
