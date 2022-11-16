from api.views import Train, Predict
from django.urls import path, re_path

app_name = 'api'


urlpatterns = [
    re_path(r'^train/', Train.as_view(), name='train'),
    re_path(r'^predict/', Predict.as_view(), name='predict')
    # path('train/', Train.as_view(), name="train"),
    # path('predict/', Predict.as_view(), name="predict"),
]