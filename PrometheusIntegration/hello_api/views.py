# hello_api/views.py
from prometheus_client import Counter
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Define a counter metric to count requests
REQUEST_COUNTER = Counter('hello_world_requests', 'Number of requests to the hello world endpoint')

@csrf_exempt  # Disable CSRF protection for simplicity in this example
def hello_world(request):
    if request.method == 'POST':
        # Process any type of data here; the logic can be extended as needed
        return JsonResponse({"message": "Hello World"})
    return JsonResponse({"error": "Method not allowed"}, status=405)
