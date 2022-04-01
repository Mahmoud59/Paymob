from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from analytics.views import index, similar, upload_file_data

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += format_suffix_patterns([
    path('upload/', upload_file_data, name='analytics-upload'),
    path('index/', index, name='analytics-index'),
    path('similar/', similar, name='analytics-similar'),
])
