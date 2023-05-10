import time

# from cts.cts.settings import LOGIN_REDIRECT_URL
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class OnlyAuthUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print("custom middleware before next middleware/view")
        response = self.get_response(request)
        print(request.user)
        return response

    # def process_view(self, request, view_func, *view_args, **view_kwargs):
    #     user = request.user
    #     if user.is_authenticated:
    #         return HttpResponse(status=200)
    #     else:
    #         # return HttpResponse('Unauthorised', status=401)
    #         return redirect("posts:index")


class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Время выполнения запроса: {time_taken}")
        response['X-Time-Taken'] = str(time_taken)

        return response
