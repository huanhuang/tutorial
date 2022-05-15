"""
created by 贝壳 on 2022/4/27
"""
from django.urls import include,path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views,class_views,specific_column_views

from rest_framework.routers import DefaultRouter
__autor__ = 'shelly'
# urlpatterns = [
#     path("snippets/",views.snippet_list),
#     path("snippets/<int:pk>",views.snippet_detail)
# ]
urlpatterns = [
    path("snippets/",class_views.SnippetList2.as_view(),name = "snippet-list"),
    path("snippets/<int:pk>",class_views.SnippetDetail2.as_view(),name = 'snippet-detail'),
    # path("users",class_views.UserList.as_view(),name = 'user-list'),
    # path("users/<int:pk>",class_views.UserDetail.as_view(),name = 'user-detail'),
    # path("",views.api_root,name = 'root'),
    # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),name = 'snippet-highlight'),
   # path(r'my_users',specific_column_views.MyUserViewSet.as_view(),name = 'my_user'),
]

router = DefaultRouter()
router.register(r'my_users',specific_column_views.MyUserViewSet,basename='my_users')
urlpatterns += router.urls

#urlpatterns = format_suffix_patterns(urlpatterns)
