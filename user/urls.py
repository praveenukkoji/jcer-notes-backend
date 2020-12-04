from django.urls import path

from user.controllers.controllers import CreateFacultyController, GetFacultyController, \
    UpdateFacultyController, DeleteFacultyController, LoginFacultyController

urlpatterns = [
    # faculty
    path('create/faculties/', CreateFacultyController.as_view()),
    path('get/faculties/', GetFacultyController.as_view()),
    path('update/faculties/', UpdateFacultyController.as_view()),
    path('delete/faculties/', DeleteFacultyController.as_view()),
    path('login/faculties/', LoginFacultyController.as_view())
]
