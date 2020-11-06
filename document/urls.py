from django.urls import path

from document.controller.controller import CreateDocumentController, GetDocumentController, UpdateDocumentController, \
    DeleteDocumentController, UploadDocumentController, GetSubjectIdDocumentController

urlpatterns =[
    path('create/document/', CreateDocumentController.as_view()),
    path('get/document/', GetDocumentController.as_view()),
    path('update/document/', UpdateDocumentController.as_view()),
    path('delete/document/', DeleteDocumentController.as_view()),

    # extras

    # upload document
    path('upload/document/', UploadDocumentController.as_view()),

    # get by subject_id
    path('getSid/document/', GetSubjectIdDocumentController.as_view())
]
