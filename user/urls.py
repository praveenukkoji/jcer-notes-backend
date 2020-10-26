from django.urls import path

from user.controllers.controllers import CreateStudentController, GetStudentController, DeleteStudentController, \
    UpdateStudentController, LoginStudentController, CreateFacultyController, GetFacultyController, \
    UpdateFacultyController, DeleteFacultyController, LoginFacultyController

urlpatterns = [
    # student
    path('create/students/', CreateStudentController.as_view()),
    path('get/students/', GetStudentController.as_view()),
    path('update/students/', UpdateStudentController.as_view()),
    path('delete/students/', DeleteStudentController.as_view()),
    path('login/student/', LoginStudentController.as_view()),

    # faculty
    path('create/faculties/', CreateFacultyController.as_view()),
    path('get/faculties/', GetFacultyController.as_view()),
    path('update/faculties/', UpdateFacultyController.as_view()),
    path('delete/faculties/', DeleteFacultyController.as_view()),
    path('login/faculties/', LoginFacultyController.as_view())
]
