from __future__ import absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Contact(models.Model):
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Detial Contact"
        verbose_name_plural = "Contacts"
        ordering = ["-created"]
