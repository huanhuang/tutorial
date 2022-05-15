"""
created by 贝壳 on 2022/5/14
"""
__autor__ = 'shelly'
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from snippets.models import MyUser,Organization
from .serializers import MyUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import pandas

class MyUserViewSet(ModelViewSet):
    serializer_class = MyUserSerializer
    def get_queryset(self,*columns):
        return MyUser.objects.select_related('organization').\
            values(*columns)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset("id","username","data","sex","org__name","org__type")
        page = self.paginate_queryset(queryset)
        if page:
            serializers = MyUserSerializer(page,many=True)
            return self.get_paginated_response(serializers.data)

        seri = MyUserSerializer(queryset,many=True)
        return self.get_paginated_response(seri.data)

    @action(methods=['GET'],url_path='export_exls_file',detail=False)
    def export_exls_file(self,request):
        queryset = self.get_queryset("username","data","sex","org__name","org__type")
        serilizers = MyUserSerializer(queryset,many=True)
        pdf = pandas.DataFrame(data=serilizers.data)
        pdf.to_excel('user_info.xlsx')
        return Response("ok")

