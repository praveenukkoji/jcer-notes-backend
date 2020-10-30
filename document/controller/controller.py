import uuid
from datetime import datetime
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
import os

from document.implementation.implementation import DocumentImplementation

BASE_DIR = Path(__file__).resolve().parent.parent


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
            if file:
                fs = FileSystemStorage()
                extension = file.name.split(".")[-1]
                filename = str(uuid.uuid4())+"."+extension
                fs.save(filename, file)
                response["payload"] = {"document_url": "/media/"+filename}
                response["message"] = "Document uploaded successfully."
            else:
                response["message"] = "Document is missing."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
