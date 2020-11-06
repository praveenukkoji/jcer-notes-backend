from django.urls import path

from subject.controller.controller import CreateSubjectController, GetSubjectController, UpdateSubjectController, \
    DeleteSubjectController, GetByBranchIdSubjectController, GetBySemSubjectController

urlpatterns =[
    path('create/subjects/', CreateSubjectController.as_view()),
    path('get/subjects/', GetSubjectController.as_view()),
    path('update/subjects/', UpdateSubjectController.as_view()),
    path('delete/subjects/', DeleteSubjectController.as_view()),

    # extras

    # get by branch
    path('getBid/subjects/', GetByBranchIdSubjectController.as_view()),

    # get by branch and sem
    path('getSem/subjects/', GetBySemSubjectController.as_view())
]