# ViewSets
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Cafe.models import Cafe, Review
from Cafe.serializers import CafeListSerializer, CafeSerializer, ReviewSerializer


class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CafeListSerializer
        return CafeSerializer

    def list(self, request):
        queryset = self.get_queryset()

        # Search functionality
        search = request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)

        # Sorting by rating
        sort_by = request.query_params.get('sort', None)
        if sort_by == 'rating_desc':
            queryset = sorted(queryset, key=lambda x: x.average_rating, reverse=True)
        elif sort_by == 'rating_asc':
            queryset = sorted(queryset, key=lambda x: x.average_rating)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        cafe = self.get_object()
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(cafe=cafe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        cafe_id = self.request.query_params.get('cafe_id', None)
        if cafe_id:
            queryset = queryset.filter(cafe_id=cafe_id)
        return queryset