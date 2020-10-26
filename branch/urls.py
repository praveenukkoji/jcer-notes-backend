from django.urls import path

from branch.controller.controller import CreateBranchController, GetBranchController, DeleteBranchController,\
    UpdateBranchController

urlpatterns = [
    path('create/branches/', CreateBranchController.as_view()),
    path('get/branches/', GetBranchController.as_view()),
    path('delete/branches/', DeleteBranchController.as_view()),
    path('update/branches/', UpdateBranchController.as_view())
]