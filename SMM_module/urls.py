from django.urls import path
from .views import MunicipalityListCreate, MunicipalityRetrieveUpdateDestroy

urlpatterns = [
    path('municipios/', MunicipalityListCreate.as_view(), name='municipios-list-create'),
    path('municipios/<int:pk>/', MunicipalityRetrieveUpdateDestroy.as_view(), name='municipios-detail'),
]
