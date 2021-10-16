from django.urls import path, include
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .api import *
from .views import *

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

schema_view = get_swagger_view(title='HRMIS API')

urlpatterns = [
	path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
	path('user_list/', UsersList, name="users_list"),
	path('autocomplete/', AutoComplete.as_view(), name="auto_completes"),
	path('', include(router.urls)),

]