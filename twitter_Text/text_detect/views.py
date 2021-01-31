from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib.request # python 3
import json
import os

# Create your views here.

@csrf_exempt
def detect(request):
	
    
    #Put dummy data here

    data = {"success": False}


    
	# check to see if this is a post request
	if request.method == "POST":
            url = request.POST.get("url", None)
            if url is None:
                data["error"] = "No URL provided."
                return JsonResponse(data)
            else:
                data.update({"success": True})
	# return a JSON response
	return JsonResponse(data)
