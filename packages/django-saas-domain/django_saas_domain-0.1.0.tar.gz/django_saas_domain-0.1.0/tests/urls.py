from django.urls import path, include

urlpatterns = [
    path('m/', include('saas_domain.management_api.urls')),
]
