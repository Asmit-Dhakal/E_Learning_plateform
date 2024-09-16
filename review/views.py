from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import get_recommendations_for_user

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class RecommendationView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        num_recommendations = int(request.query_params.get('num_recommendations', 5))
        recommended_course_ids = get_recommendations_for_user(user_id, num_recommendations=num_recommendations)
        return Response({'recommended_courses': recommended_course_ids}, status=status.HTTP_200_OK)
