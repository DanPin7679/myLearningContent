from .models import Category, Subject, Content
from .serializer import CategorySerializer, SubjectSerializer, ContentSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectCategoryList(APIView):
    def get(self, request, pk, format=None):
        subjects = Subject.objects.filter(category=pk)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class ContentList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentSubjectList(APIView):
    def get(self, request, pk, format=None):
        contents = Content.objects.filter(subject=pk)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

