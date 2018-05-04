# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import logging

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from containers.models import Service

LOG = logging.getLogger(__name__)


# Create your views here.
@login_required
def containers(request):

    user = request.session.get('user')
    services = Service.objects.filter(user=user)

    resp = {
        'status': 'success',
        'services': [{'name': s.name, 'url': s.url} for s in services]
    }

    return HttpResponse(json.dumps(resp))


@login_required
def create(request):
    body = json.loads(request.body)

    name = body.get('name')
    url = 'https://www.baidu.com'
    user = request.session.get('user')

    Service.objects.create(name=name, url=url, user=user)

    service = {
        'name': name,
        'url': url
    }

    resp = {
        'status': 'success',
        'service': service
    }

    return HttpResponse(json.dumps(resp))
