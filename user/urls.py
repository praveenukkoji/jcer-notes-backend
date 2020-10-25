from django.urls import path

from user.controllers.controllers import CreateStudentController, GetStudentController, DeleteStudentController, \
    UpdateStudentController, LoginStudentController

urlpatterns = [
    path('create/students/', CreateStudentController.as_view()),
    path('get/students/', GetStudentController.as_view()),
    path('update/students/', UpdateStudentController.as_view()),
    path('delete/students/', DeleteStudentController.as_view()),
    path('login/student/', LoginStudentController.as_view())
]
