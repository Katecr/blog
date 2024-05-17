from rest_framework.serializers import ModelSerializer

from apps.post.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_at']

    #asignar los items que se desean
    # def to_representation(self,instance):
    #     return {
    #         'id': instance['id'],
    #         'username': instance['username'],
    #         'password': instance['password'],
    #         'email': instance['email']
    #     }