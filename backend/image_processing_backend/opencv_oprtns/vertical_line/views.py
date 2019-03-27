import json
import cv2

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import FileSerializer


class VerticalLineDetection(APIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (MultiPartParser, FileUploadParser)

    def post(self, request):
        request_data = request.data.dict()
        # request_data['contour'] = json.loads(request.data['contour']) if 'contour' in request_data else {}
        contour_serializer = ContourSerializer(data=request_data)
        if contour_serializer.is_valid():
            file_data = {'name': contour_serializer.validated_data['name'],
                         'file': contour_serializer.validated_data['file']}
            file_serializer = FileSerializer(data=file_data)
            file_serializer.is_valid()
            file_serializer.save()

            serialized_data = contour_serializer.data
            serialized_data['file'] = file_serializer.data['file']

            img = settings.BASE_DIR + str(file_serializer.data['file'])

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150, apertureSize=3)

            crop_cord_list = list()

            lines = cv2.HoughLines(edges, 1, np.pi, int(0.85 * (img.shape[0])))

            if lines is not None and lines.any():
                for line in lines:
                    for rho, theta in line:
                        a = np.cos(theta)
                        b = np.sin(theta)

                        x0 = a * rho
                        y0 = b * rho

                        line_length = img.shape[0]

                        x1 = int(x0 + line_length * (-b))
                        y1 = int(y0 + line_length * (a)) if y0 != 0.0 else 0
                        x2 = int(x0 - line_length * (-b))
                        y2 = int(y0 - line_length * (a)) if y0 != 0.0 else img.shape[0]

                        if (0.10 * (img.shape[1])) < x1 < (0.90 * (img.shape[1])):
                            crop_cord_list.append([x1, y1, x2, y2])

            else:
                raise ImageProcessingError('Vertically dividing was not possible')
            if not crop_cord_list:
                raise ImageProcessingError('Vertically dividing was not possible')

            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            return Response(contour_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        dictionery_value = {'test': 1, 'value': 4}
        serialized_data = json.dumps(dictionery_value)
        print(serialized_data)

        return Response('errors', status=status.HTTP_400_BAD_REQUEST)
