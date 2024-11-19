from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file']

class CustomImageField(serializers.ImageField):
    default_error_messages = {
        'invalid_image': 'Only "jpg", "jpeg", "png", "webp", "gif", "bmp", "ico", "tiff" image files are allowed.'
    }

class ImageUploadSerializer(serializers.Serializer):
    file = CustomImageField()

class PdfUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        valid_extensions = ['pdf']
        if value.name.split('.')[-1].lower() not in valid_extensions:
            raise serializers.ValidationError("Only PDF files are allowed.")
        return value
    

class DocxUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        valid_extensions = ['doc', 'docx']
        if value.name.split('.')[-1].lower() not in valid_extensions:
            raise serializers.ValidationError("Only .doc, .docx files are allowed.")
        return value
class VideoUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        valid_extensions = ['mp4', 'mov', 'mkv', 'wmv', 'flv']
        if value.name.split('.')[-1].lower() not in valid_extensions:
            raise serializers.ValidationError("Only MP4, MOV, MKV, WMV, FLV files are allowed.")
        return value