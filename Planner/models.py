from django.db import models
from django.db.models import CheckConstraint, Q, F

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 64, unique = True)
    password = models.CharField(max_length = 64)
    name = models.CharField(max_length = 256)

class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)
    description = models.CharField(max_length = 1024)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    def __str__(self):
        return (
            f"Event '{self.title}' for user '{self.user.username}' at '{self.location}' "
            f"from {self.start_date} {self.start_time.strftime('%H:%M')} "
            f"to {self.end_date} {self.end_time.strftime('%H:%M')}: {self.description}"
        )

    class Meta:
        constraints = [
            CheckConstraint(
                condition = Q(end_date__gt=F("start_date")) | (Q(end_date=F("start_date")) & Q(end_time__gt=F("start_time"))), # type: ignore
                name = "event_ends_after_start"
            ),
        ]
