from django.urls import path
from .views import TaskViewSet,CategoryViewSet

urlpatterns = [
    path('categories/',CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('categories/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve','post':'update','delete':'destroy'})),
    path('task/',TaskViewSet.as_view({'get':'list','post':'create'})),
    path('task/<int:pk>/',TaskViewSet.as_view({'get':'retrieve','delete':'destroy'})),
]
