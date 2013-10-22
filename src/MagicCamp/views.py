# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django import http
from django.shortcuts import render_to_response

import datetime

def index(request):
    r = http.HttpResponse('<h1>Django examples</h1><ul>')
    r.write('<li><a href="hello/html/">Hello world (HTML)</a></li>')
    r.write('<li><a href="hello/text/">Hello world (text)</a></li>')
    r.write('<li><a href="hello/write/">HttpResponse objects are file-like objects</a></li>')
    r.write('<li><a href="hello/metadata/">Displaying request metadata</a></li>')
    r.write('<li><a href="hello/getdata/">Displaying GET data</a></li>')
    r.write('<li><a href="hello/postdata/">Displaying POST data</a></li>')
    r.write('</ul>')
    return r

def hello(request):
    return HttpResponse("Hello world!")

def cur_dt(request):
    now = datetime.datetime.now()
    return render_to_response('cur_dt.html',locals())
    