from django.contrib import admin
from .models import Pieces
from .models import KnightAudits


# Register your models here.

class Piece(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    list_display_links = ('id',)
    search_fields = ('name',)


admin.site.register(Pieces, Piece)


class Knitgh(admin.ModelAdmin):
    list_display = ('id','user_name', 'posisiton', 'possibilities')
    list_display_links = ('id',)
    search_fields = ('user_name',)


admin.site.register(KnightAudits, Knitgh)
