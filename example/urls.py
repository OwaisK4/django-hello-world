# example/urls.py
from django.urls import path
from example.views import index, cover, display_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", index, name="index"),
    # path("cover/", cover, name="cover"),
    path("", cover, name="cover"),
    path("image/<image_id>/", display_image, name="image"),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
