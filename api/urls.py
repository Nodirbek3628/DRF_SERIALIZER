from django.urls import path
from .views import TaskViewSet,CategoryViewSet,RegisterAPIView,LoginAPIView


urlpatterns = [
    path('register/',RegisterAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('category/',CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('category/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve','post':'update','delete':'destroy'})),
    path('task/',TaskViewSet.as_view({'get':'list','post':'create'})),
    path('task/<int:pk>/',TaskViewSet.as_view({'get':'retrieve','delete':'destroy'})),
]
