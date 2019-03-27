from rest_framework import serializers
from .models import Filesave
import cv2

approximation_choices = (
    (1, cv2.CHAIN_APPROX_NONE),
    (2, cv2.CHAIN_APPROX_SIMPLE)
)

retrievelmode_choices = (
    (0, cv2.RETR_EXTERNAL),
    (1, cv2.RETR_LIST),
    (2, cv2.RETR_CCOMP),
    (3, cv2.RETR_TREE),
    (4, cv2.RETR_FLOODFILL),
)

thresholding_choices = (
    (0, cv2.THRESH_BINARY),
    (1, cv2.THRESH_BINARY_INV),
    (2, cv2.THRESH_TRUNC),
    (3, cv2.THRESH_TOZERO),
    (4, cv2.THRESH_TOZERO_INV),

    (5, cv2.THRESH_TOZERO),
    (6, cv2.THRESH_TOZERO),

    (7, cv2.THRESH_MASK),
    (8, cv2.THRESH_OTSU),

    (9, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
)


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filesave
        fields = '__all__'


# class ColorSerializer(serializers.DictField):
#     child = serializers.IntegerField(min_value=0, max_value=255, allow_null=False)
#
#
# class DrawContours(serializers.Serializer):
#     index = serializers.IntegerField(allow_null=False, max_value=1000)
#     thickness = serializers.IntegerField(min_value=1, max_value=100, allow_null=False)
#     sort_reverse = serializers.BooleanField(allow_null=False, default=True)
#     color = ColorSerializer(required=True)
#
#
# class ContourSerializer(FileSerializer):
#     contour = DrawContours(required=True)
#     join_lines = serializers.BooleanField(allow_null=False)
#     kernal = serializers.IntegerField(min_value=1, max_value=5)
#     thresholding = serializers.ChoiceField(choices=thresholding_choices)
#     approximation_method = serializers.ChoiceField(choices=approximation_choices)
#     retrievelmode = serializers.ChoiceField(choices=retrievelmode_choices)
