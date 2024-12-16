from django.urls import path
from jobs.api.views import JobOfferListCreateAPIView

urlpatterns = [
        path('jobs/', JobOfferListCreateAPIView.as_view(), name= 'job-list'),
]
