from django.urls import path
from apps.chatapp import views

urlpatterns = [
    path('chat_room/', views.ChatRoomList.as_view()),
    path('chat_room/<uuid:pk>/', views.ChatRoomDetail.as_view()),
]
