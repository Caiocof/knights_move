from knight.views import PossitionKinight
from knight.views import Prices

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('possition/<int:id_piece>/search/', PossitionKinight.as_view()),
    path('piece/', Prices.as_view())
]
