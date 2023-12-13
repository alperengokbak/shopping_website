# products/urls.py
from django.urls import path
from .views import home, search_results, product_detail, search_input
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_results, name='search_results'),
    path('search_input/', search_input, name='search_input'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)