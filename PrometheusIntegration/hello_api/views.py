from django.shortcuts import render

# Create your views here.
# hello_api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disable CSRF protection for simplicity in this example
def hello_world(request):
    if request.method == 'POST':
        # Process any type of data here; the logic can be extended as needed
        return JsonResponse({"message": "Hello World"})
    return JsonResponse({"error": "Method not allowed"}, status=405)
