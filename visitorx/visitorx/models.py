from django.db import models
from django.contrib.sessions.models import Session
from django.utils.translation import gettext as _


class Visit(models.Model):
    """Visit - class for visit content"""

    visits_count = models.PositiveIntegerField(_('Count Visits'), default=0)
    http_user_agent = models.CharField(_('http user agent'), max_length=255)
    remote_addr = models.CharField(_('remote addr'), max_length=255)
    last_visit = models.DateTimeField(_('last visit'))

    ordering = ['-id', ]

    def __repr__(self):
        return _("<Visit #%s> ") % (self.id, )

    def __str__(self):
        return _("<Visit #%s> ") % (self.id, )

