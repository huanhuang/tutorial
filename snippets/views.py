from django.shortcuts import render

# Create your views here.

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse,JsonResponse
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from  rest_framework import generics

#from . import factories

@csrf_exempt
@api_view(http_method_names=['GET','POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serilizers = SnippetSerializer(snippets,many=True)
        print(serilizers.data)
        #return JsonResponse(data=serilizers.data,safe=False)
        return Response(serilizers.data)

    elif request.method == 'POST':
       # data = JSONParser.parse(request) #使用restframework后，可直接使用reqeust.data
        data = request.data
        serilizer = SnippetSerializer(data = data)
        if serilizer.is_valid():
            serilizer.save()
            #return JsonResponse(data=serilizer.data,status=201)
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        #return JsonResponse(data = serilizer.errors,status=400)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST','PUT'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        data = request.data
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


@api_view(['GET'])
def api_root(request,format = None):
    return Response({
        'users':reverse('user-list',request = request,format = format),
        'snippets':reverse('snippet-list',request = request,format=format)
    })

if __name__ == "__main__":
    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()

    snippet = Snippet(code='print("hello, world")\n')
    snippet.save()

    #factories.test()