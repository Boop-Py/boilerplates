
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, resolve
from django.contrib import messages


def index(request):
    return render(request, "webapp/index.html") 