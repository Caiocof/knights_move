from .models import KnightAudits
from .models import Pieces

from rest_framework import serializers


class KnightSerialize(serializers.ModelSerializer):
    class Meta:
        model = KnightAudits
        fields = ['position']


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieces
        fields = ['id']
