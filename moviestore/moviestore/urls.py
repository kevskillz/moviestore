from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),  # Homepage and app views
    path('movies/', include('movies.urls')),  # Movies app views
    path('accounts/', include('accounts.urls')),  # Account-related views
    path('cart/', include('cart.urls')),  # Shopping cart views
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
