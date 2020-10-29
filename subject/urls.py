from django.urls import path

from subject.controller.controller import CreateSubjectController, GetSubjectController, UpdateSubjectController, \
    DeleteSubjectController

urlpatterns =[
    path('create/subjects/', CreateSubjectController.as_view()),
    path('get/subjects/', GetSubjectController.as_view()),
    path('update/subjects/', UpdateSubjectController.as_view()),
    path('delete/subjects/', DeleteSubjectController.as_view()),
]