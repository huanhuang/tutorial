"""
created by 贝壳 on 2022/5/2
"""
__autor__ = 'shelly'
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import mixins,generics
from . import permission

class SnippetList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request,format = None):
        snippets = Snippet.objects.all()
        seriaizer = SnippetSerializer(snippets,many=True)
        return Response(seriaizer.data)

    def post(self,request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #覆盖perform_create方法，修改保存实例的时候增加owner字段
    def perform_create(self,serializer):
        serializer.save(owner = self.request.user)

class SnippetList2(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        print("===== get ++++")
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class SnippetDetail2(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permission.IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer