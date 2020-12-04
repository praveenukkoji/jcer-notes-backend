from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from user.implementation.implementation import UserImplementation


# create faculty
class CreateFacultyController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.create_faculties()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# get faculty
class GetFacultyController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.get_faculties()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# update faculty
class UpdateFacultyController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.update_faculties()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# delete faculty
class DeleteFacultyController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.delete_faculties()

            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = "Faculty id required."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# login faculty
class LoginFacultyController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implementation = UserImplementation(requests)
            payload, message = user_implementation.login_faculty()

            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = "Invalid Credentials."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
