from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from subject.implementation.implementation import SubjectImplementation


# create subjects
class CreateSubjectController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.create_subjects()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# get subjects
class GetSubjectController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.get_subjects()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# update subjects
class UpdateSubjectController(GenericAPIView):
    def post(self,requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.update_subjects()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# delete subjects
class DeleteSubjectController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            subject_implementation = SubjectImplementation(requests)
            payload, message = subject_implementation.delete_subjects()

            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = "Subject id required."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)