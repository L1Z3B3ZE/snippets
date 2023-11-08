from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import SnippetViewSet, UserViewSet


snippet_list = SnippetViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
   'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
   'get': 'list'
})
user_detail = UserViewSet.as_view({
   'get': 'retrieve'
})



urlpatterns = [
   path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
   path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
   path('users/', views.UserList.as_view(), name='user-list'),
   path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
   path('auth/', include('rest_framework.urls')),
   path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
   path('', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)
