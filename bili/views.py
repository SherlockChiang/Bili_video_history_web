from django.http import HttpResponse
from django.shortcuts import render
from .bili import login_qrcode, bzlogin

def my_view(request):

    # Generate image using bili.py
    image = login_qrcode()

    # Return image response
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response