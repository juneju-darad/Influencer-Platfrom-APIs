from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import response
from googleapiclient.discovery import build
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from django.http import HttpResponse
from django.template import loader, Context
from django.template.response import TemplateResponse
# Create your views here.



def ythome(request):
    return render(request, 'ythome.html', {'name':'ada'})

def ytresult(request):
    api_key = 'AIzaSyAu0II3vr64fZdqYHzQHFIHn1avRFPk-zA'

    yt = build('youtube', 'v3', developerKey=api_key)
    link = request.GET['url']
    username = link[26:]
    id = link[32:]

    request = yt.channels().list(
        part='statistics',
        # forUsername=username,
        id=id
    )

    response1 = request.execute()
    a = response1['items'][0]['statistics']['subscriberCount']
    b = response1['items'][0]['statistics']['videoCount']
    c = response1['items'][0]['statistics']['viewCount']

    #print(a)

    #return render(request, 'ytresult.html', {'response':a})

    # return TemplateResponse(request, 'ytresult.html' , {'response':a})

    # return render_to_response('ytresult.html', {'response':a})

    return HttpResponse({a})
