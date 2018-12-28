from django.urls import path

from opencv_oprtns.contour.views import ContourDetection
from opencv_oprtns.horizontal_line.views import HorizontalLineDetection
from opencv_oprtns.vertical_line.views import VerticalLineDetection


urlpatterns = [
    path('contour/', ContourDetection.as_view(), name="opencv_oprtns"),
    path('vertical-line/', VerticalLineDetection.as_view(), name="opencv_oprtns"),
    path('horizontal-line/', HorizontalLineDetection.as_view(), name="opencv_oprtns"),
]