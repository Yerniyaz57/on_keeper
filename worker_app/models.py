from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.

class UserProfile(AbstractUser):
    STATUS_ADMIN = 0
    STATUS_WORKER = 1
    STATUS_USER = 2

    STATUS_CHOICES = (
        (STATUS_ADMIN, _('admin')),
        (STATUS_WORKER, _('worker')),
        (STATUS_USER, _('user')),
    )

    WAGE_HOUR = 0
    WAGE_DAY = 1
    WAGE_MONTH = 2

    WAGE_CHOICES = (
        (WAGE_HOUR, _('hour')),
        (WAGE_DAY, _('day')),
        (WAGE_MONTH, _('month')),
    )

    DUTY_1 = 0
    DUTY_2 = 1
    DUTY_3 = 2
    DUTY_4 = 3
    DUTY_5 = 4

    DUTY_CHOICES = (
        (DUTY_1, _('security')),
        (DUTY_2, _('Chef')),
        (DUTY_3, _('cashier')),
        (DUTY_4, _('manager')),
        (DUTY_5, _('waitress')),
    )  

    mobile = models.IntegerField(_('phone number'), null=True)
    avatar = models.ImageField(upload_to='image/avatar/worker' ,default='image/avatar/worker/default.png', null=True)
    status = models.SmallIntegerField(_("Status"),choices=STATUS_CHOICES, null=True)
    wage = models.IntegerField(_("Wage"), null=True)
    wage_type = models.SmallIntegerField(_("Wage type"), choices=WAGE_CHOICES, null=True)
    duty = models.SmallIntegerField(_("Duty"), choices=DUTY_CHOICES, null=True)

    def __str__(self):
        return self.username