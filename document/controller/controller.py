import uuid

from django.core.files.storage import FileSystemStorage
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json

from document.implementation.implementation import DocumentImplementation


class CreateDocumentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            document_implementation = DocumentImplementation(requests)
            payload, message = document_implementation.create_document()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class GetDocumentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            document_implementation = DocumentImplementation(requests)
            payload, message = document_implementation.get_document()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class DeleteDocumentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            document_implementation = DocumentImplementation(requests)
            payload, message = document_implementation.delete_document()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class UpdateDocumentController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            document_implementation = DocumentImplementation(requests)
            payload, message = document_implementation.update_document()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class UploadDocumentController(GenericAPIView):
    def post(self, request):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            file = request.data.get('document', None)
            filename = request.data.get('document_name', None)
            if file:
                fs = FileSystemStorage()
                fs.save(filename, file)
                response["message"] = "Document uploaded successfully."
            else:
                response["message"] = "Document is missing."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
