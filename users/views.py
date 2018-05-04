# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as user_logout
from django.contrib.auth import login as user_login
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    body = json.loads(request.body)
    username = body.get('username', '').strip()
    passwd = body.get('password', '').strip()

    user = authenticate(username=username, password=passwd)
    if user is not None:
        user_login(request, user)
        request.session['user'] = user.id
        resp = {'status': 'success'}
    else:
        resp = {'status': 'failed', 'msg': 'username or passward incorrect'}

    return HttpResponse(json.dumps(resp))


def register(request):
    body = json.loads(request.body)
    username = body.get('username', '').strip()
    passwd = body.get('password', '').strip()

    user = User.objects.create_user(username, '', passwd)
    user.save()

    user_login(request, user)
    request.session['user'] = user.id

    return HttpResponse(json.dumps({'status': 'success'}))


@login_required
def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    finally:
        user_logout(request)

    return HttpResponse(json.dumps({'status': 'success'}))


def unauthenticate(request):
    return HttpResponse(status=400)
