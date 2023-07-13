from posts.models import Post
from rest_framework import serializers
from ckeditor.fields import RichTextField


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('perfil', 'titulo', 'head_image', 'post')

# class PostSerializers(serializers.Serializer):
#     perfil = serializers.CharField()
#     titulo = serializers.CharField()
#     head_image = serializers.ImageField()
#     post = serializers.CharField()