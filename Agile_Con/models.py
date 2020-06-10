from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Presenter(models.Model):
    presenter_id = models.CharField(primary_key=True, max_length=50, blank=False, null=False, default=' ')
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='presenters',
                             default='')

    def __str__(self):
        return str(self.presenter_id)


class Attendee(models.Model):
    USERNAME_FIELD = 'attendee_id'
    attendee_id = models.CharField(primary_key=True, max_length=50, blank=False, null=False, default=' ')
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='attendees')
    def __str__(self):
        return self.attendee_id


class Presentation(models.Model):
    presentation_id = models.CharField(primary_key=True, max_length=50, blank=False, null=False, default=' ')
    presenter_id = models.ForeignKey(Presenter, on_delete=models.CASCADE, related_name='presentations')
    timeslot = models.CharField(max_length=50, blank=False, null=False, default=' ')
    cost = models.DecimalField(max_digits=10, blank=False, null=False, decimal_places=2)
    number_of_slots = models.DecimalField(max_digits=10, blank=False, null=False, default=50, decimal_places=0)
    number_of_slots_remaining = models.DecimalField(max_digits=10, blank=False, null=False, default=50,
                                                    decimal_places=0)
    location = models.CharField(max_length=50, blank=False, null=False, default=' ')
    description = models.CharField(max_length=200, blank=False, null=False, default=' ')

    def __str__(self):
        return self.presentation_id

class CustomerOrder(models.Model):
    attendee = models.ForeignKey(
        Attendee,
        on_delete=models.PROTECT,
        related_name='customer_orders'
    )
    presentation = models.ForeignKey(
        Presentation,
        on_delete=models.PROTECT,
        related_name='customer_orders'
    )

