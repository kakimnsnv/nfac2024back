from django.urls import path

from api.views import PaletteDetail, PalettesList



urlpatterns = [
    path('palettes/', PalettesList.as_view(), name='palettes'),
    path('palettes/<int:id>', PaletteDetail.as_view(), name='palettes-detail')
]