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
	# initialize the data dictionary to be returned by the request
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
