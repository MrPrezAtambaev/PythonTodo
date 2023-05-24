from django.contrib import admin
# from rest_framework import routers
from django.urls import path
from todos.views import TodoItemViewSet, AuthViewSet, LoginViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# router = routers.DefaultRouter()
# router.register(r'todos', TodoItemViewSet, basename='todoItem')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API Documentation for Todo App",
        contact=openapi.Contact(email="akyl182003@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos',
         TodoItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/todos/<int:pk>/', TodoItemViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/auth/signup', AuthViewSet.as_view({'post': 'create'})),
    path('api/auth/login', LoginViewSet.as_view({'post': 'create'})),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
