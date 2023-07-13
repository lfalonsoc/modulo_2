from rest_framework import viewsets
from posts.models import Post
from .serializers import PostSerializers
from rest_framework import generics

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostGeneric(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_queryset(self):
        queryset = super(PostGeneric, self).get_queryset()
        user = self.request.user
        if not self.request.user.is_superuser:
            queryset.objects.filter(estado=True)
        return queryset


    def get(self, request, *args, **kwargs):
        """Prueba de documentación

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        print("Hola entre al get")
        return super(PostGeneric, self).get(request, *args, **kwargs)


class PostGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def retrieve(self, request, *args, **kwargs):
        print("Soy retrieve")
        return super(PostGenericDetail, self).retrieve(request, *args, **kwargs)
