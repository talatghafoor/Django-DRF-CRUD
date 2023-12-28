from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('task-list', views.tasklist, name="task-list"),
    path('task-detail/<str:pk>', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskcreate, name="task-create"),
    path('task-update/<str:pk>', views.taskupdate, name="task-update"),
    path('task-delete/<str:pk>', views.taskDelete, name="task-delete"),

]