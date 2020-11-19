import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    if request.COOKIES.get('last_visit_connection'):
        last_visit_connection = request.COOKIES['last_visit_connection']
        last_connection_time = datetime.datetime.fromisoformat(last_visit_connection)
    else:
        last_connection_time = None
    t = loader.get_template('base.html')
    c = {
        'last_connection_time': last_connection_time,
    }
    res = HttpResponse(t.render(c, request))
    res.set_cookie('last_visit_connection', datetime.datetime.now().isoformat())
    return res


