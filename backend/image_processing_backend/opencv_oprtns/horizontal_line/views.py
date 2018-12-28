import json
import cv2

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from opencv_oprtns.contour.image_operations import find_contours_in_image, draw_cordinates
from .serializers import ContourSerializer, FileSerializer


class HorizontalLineDetection(APIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (MultiPartParser, FileUploadParser)

    def post(self, request):
        request_data = request.data.dict()
        request_data['contour'] = json.loads(request.data['contour']) if 'contour' in request_data else {}
        contour_serializer = ContourSerializer(data=request_data)
        if contour_serializer.is_valid():
            file_data = {'name': contour_serializer.validated_data['name'],
                         'file': contour_serializer.validated_data['file']}
            file_serializer = FileSerializer(data=file_data)
            file_serializer.is_valid()
            file_serializer.save()
            serialized_data = contour_serializer.data
            serialized_data['file'] = file_serializer.data['file']

            image_save_file = settings.BASE_DIR + str(file_serializer.data['file'])

            image, cnts, hirerchy = find_contours_in_image(image_save_file,
                                                           join_lines=serialized_data['join_lines'],
                                                           kernal=serialized_data['kernal'],
                                                           thresholding=serialized_data['thresholding'],
                                                           retrievelmode=serialized_data['retrievelmode'],
                                                           approximation_method=serialized_data['approximation_method'])
            try:
                contour_image = draw_cordinates(image_save_file, cnts,
                                                colors=(contour_serializer.data['contour']['color']['red'],
                                                        contour_serializer.data['contour']['color']['blue'],
                                                        contour_serializer.data['contour']['color']['green']),
                                                index=contour_serializer.data['contour']['index'],
                                                thickness=contour_serializer.data['contour']['thickness'],
                                                contour_sorting=contour_serializer.data['contour']['sort_reverse']
                                                )
            except Exception as e:
                return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

            image_path = '{}_contour.{}'.format(str(file_serializer.data['file']).split('.')[0],
                                                str(file_serializer.data['file']).split('.')[1])
            save_file_path = '{}{}'.format(settings.BASE_DIR, image_path)

            cv2.imwrite(save_file_path, contour_image)

            serialized_data['output_image'] = image_path
            serialized_data['no_contours'] = len(cnts)

            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            return Response(contour_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        dictionery_value = {'test': 1, 'value': 4}
        serialized_data = json.dumps(dictionery_value)
        print(serialized_data)

        return Response('errors', status=status.HTTP_400_BAD_REQUEST)
