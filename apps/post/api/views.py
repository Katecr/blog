from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from apps.post.api.permissions import IsAdminOrReadOnly
from apps.post.api.serializers import PostSerializer


class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = PostSerializer.Meta.model.objects.all()

    # def get_queryset(self,pk=None):
    #     if pk is None:
    #         return self.get_serializer().Meta.model.objects.all()
    #     else:
    #         return self.get_serializer().Meta.model.objects.filter(id = pk).first()

    # def list(self, request):
    #     '''Listar elementos'''
    #     post_serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(status=status.HTTP_200_OK, data=post_serializer.data)

    # def create(self, request):
    #     '''Crear elemento'''
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'Post created successfully!'},status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     '''Datos de un solo elemento'''
    #     post_serializer = self.get_serializer(self.get_queryset(pk), many=True)
    #     return Response(status=status.HTTP_200_OK, data=post_serializer.data)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass