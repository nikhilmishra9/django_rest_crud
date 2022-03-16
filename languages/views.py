from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Paradigm, Programmer
# from .models import Language as LanguageModel, Paradigm as ParadigmModel, Programmer as ProgrammerModel
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework import mixins
from rest_framework import generics

# class LanguageView(viewsets.ModelViewSet):
#     queryset = Language.objects.all()
#     serializer_class = LanguageSerializer
#     # permission_classes = (permissions.IsAuthenticated,)

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer