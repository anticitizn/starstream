import eyed3

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import FileResponse
from django.http import JsonResponse
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from wsgiref.util import FileWrapper

from base.models import Song

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        song_file = request.data['file']

        song = Song(data = song_file)
        song.save()

        return Response(status=status.HTTP_201_CREATED)

class FileDownloadView(APIView):
    def get(self, request):
        song_id = request.GET.get('id', '')
        if not song_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        song_file = Song.objects.get(id=int(song_id)).data
        response = FileResponse(song_file)
        return response;
        
class GetMetaDataView(APIView):
    def get(self, request):
        song_id = request.GET.get('id', '')
        if not song_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        song_loaded = eyed3.load(Song.objects.get(id=int(song_id)).data.path)
        response = JsonResponse({
            "title": song_loaded.tag.title,
            "album": song_loaded.tag.album,
            "artist": song_loaded.tag.album_artist,
            "genre": song_loaded.tag.genre.name,
            "release-date": song_loaded.tag.release_date
        })
        return response;
