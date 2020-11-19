import datetime
from django.shortcuts import render
from django.db import models
from .models import Visit


def home(request):
    if request.COOKIES.get('last_visit_connection'):
        last_visit_connection = request.COOKIES['last_visit_connection']
        last_connection_time = datetime.datetime.fromisoformat(last_visit_connection)
        visit = Visit.objects.get_or_create(last_visit=last_connection_time)[0]
    else:
        last_connection_time = datetime.datetime.now()
        visit = Visit()
    try:
        visit.http_user_agent = request.META['HTTP_USER_AGENT']
    except KeyError:
        visit.http_user_agent = 'no HTTP_USER_AGENT'
    visit.remote_addr = request.META['REMOTE_ADDR']
    last_visit_connection = datetime.datetime.now()
    visit.last_visit = last_visit_connection
    visit.visits_count += 1
    visit.save()

    visits = Visit.objects.all()
    remote_addr = visits.aggregate(remote_addr=models.Count('remote_addr'))
    http_user_agent = visits.aggregate(http_user_agent=models.Count('http_user_agent'))
    visits_count = visit.visits_count
    res = render(request, 'base.html',
                 {
                     'last_connection_time': last_connection_time,
                     'remote_addr': remote_addr['remote_addr'],
                     'http_user_agent': http_user_agent['http_user_agent'],
                     'visits_count': visits_count,
                 }
                 )
    res.set_cookie('last_visit_connection', last_visit_connection.isoformat())
    return res


