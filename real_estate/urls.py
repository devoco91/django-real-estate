from django.contrib import admin
from django.urls import path

from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from listings.views import (
    listing_list,
    listing_retrieve,
    listing_create,
    listing_update,
    listing_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<pk>/', listing_retrieve),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete),
    path('add-listing/', listing_create),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
