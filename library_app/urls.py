# library_app/urls.py

from django.urls import path
from .views import UserListCreateView, BookListCreateView, OrderListCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain token (login)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]
