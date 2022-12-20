from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommetViewSet, CreateRatingAPIView,favourite


router = DefaultRouter()
router.register('comments', CommetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/', CreateRatingAPIView.as_view()),
    path('fav/', favourite)
]