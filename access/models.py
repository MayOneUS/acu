from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.ForeignKey(User)
    code = models.CharField(max_length=5, min_length=5)
    added = models.DateTimeField(auto_now_add=True)
    # Record when this token was used, to determine whether it is valid.
    # TODO: replace with valid/invalid boolean?
    used = models.DateTimeField(null=True, blank=True)

    @property
    def is_valid(self):
        return self.used is None
