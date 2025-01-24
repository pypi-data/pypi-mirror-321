from django.urls import path
from .endpoints import DomainListEndpoint, DomainItemEndpoint

urlpatterns = [
    path('domains', DomainListEndpoint.as_view()),
    path('domains/<pk>', DomainItemEndpoint.as_view()),
]
