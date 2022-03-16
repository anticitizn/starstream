from django.shortcuts import render
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Song

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty file")

        f = request.data['file']

        Song.data.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)
