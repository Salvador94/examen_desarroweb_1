from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from libros.models import Libro
from .pagination import StandardResultPagination
from .serializers import LibroModelSerializer

class LibroCreateAPIView(generics.CreateAPIView):
    serializer_class = LibroModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LibroListAPIView(generics.ListAPIView):
    serializer_class = LibroModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self, *args, **kwargs):
        qs = Libro.objects.all().order_by("-created")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(Nombre__icontains=query) |
                            Q(Autor__icontains=query) |
                            Q(user__username__icontains=query)
                          )
        return qs
