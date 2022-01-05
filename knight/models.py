from datetime import datetime

from django.db import models


# Create your models here.

class KnightAudits(models.Model):
    user_name = models.CharField(max_length=70)
    type_piece = models.CharField(max_length=20)
    posisiton = models.CharField(max_length=2)
    possibilities = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(default=datetime.today())

    class Meta:
        verbose_name = 'KnightAudit'


class Pieces(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name = 'Piece'
