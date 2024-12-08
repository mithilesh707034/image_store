from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image as PILImage
from .models import WebsiteFrontImage, WebsiteBlogImage, CatalogueLogo, CatalogueImage
from .serializers import WebsiteFrontImageSerializers, WebsiteBlogImageSerializers, CatalogueLogoSerializers, CatalogueImageSerializers
import os
from django.conf import settings

class AddImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        image_type = request.data.get('image_type')  # Get image type from request data
        model, serializer_class = self.get_model_and_serializer_by_type(image_type)

        if not model:
            return Response({
                "error": "Invalid image_type provided. Must be one of ['website_front', 'website_blog', 'catalogue_logo', 'catalogue_image']."
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(data=request.data)
        
        if serializer.is_valid():
            image_instance = serializer.save()

            # Compress the image after saving
            original_path = image_instance.image.path
            compressed_path = original_path  # Optionally, you could save it to a new location
            self.compress_image(original_path, compressed_path)

            image_url = request.build_absolute_uri(image_instance.image.url)
            return Response({
                "message": "Image uploaded and compressed successfully.",
                "image_url": image_url
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_model_and_serializer_by_type(self, image_type):
        """
        Map the image_type to the corresponding model and serializer.
        """
        model_map = {
            'website_front': (WebsiteFrontImage, WebsiteFrontImageSerializers),
            'website_blog': (WebsiteBlogImage, WebsiteBlogImageSerializers),
            'catalogue_logo': (CatalogueLogo, CatalogueLogoSerializers),
            'catalogue_image': (CatalogueImage, CatalogueImageSerializers),
        }
        return model_map.get(image_type, (None, None))

    def compress_image(self, original_path, compressed_path):
        """
        Compress the image and save it to the given path.
        """
        try:
            with PILImage.open(original_path) as img:
                # Optimize the image and reduce quality
                img.save(compressed_path, format=img.format, optimize=True, quality=70)
        except Exception as e:
            print(f"Error compressing image: {e}")
