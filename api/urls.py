from django.urls import path, include
from .views import custom_users, custom_user_detail, project, project_detail, task, task_detail

urlpatterns = [
    path('custom_users', custom_users),
    path('custom_user/<int:pk>/', custom_user_detail),
    path('project/', project),
    path('project/<int:pk>/', project_detail),
    path('task/', task),
    path('task/<int:pk>/', task_detail),

    path('auth/', include('dj_rest_auth.urls'))
]

