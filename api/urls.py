from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, PostGeneric, PostGenericDetail
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/generics/', PostGeneric.as_view()),
    path('posts/generics/<int:pk>/', PostGenericDetail.as_view()),
    path('docs/', include_docs_urls(title='Blog')),
]
