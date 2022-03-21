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
from datetime import datetime
from sqlite3 import Date

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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        song_file = Song.objects.get(id=int(song_id)).data
        response = FileResponse(song_file)

        return response
        
class GetMetadataView(APIView):
    def get(self, request):
        song_id = request.GET.get('id', '')
        if not song_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        song_loaded = eyed3.load(Song.objects.get(id=int(song_id)).data.path)
        song_date = None
        if not isinstance(song_loaded.tag.release_date, NoneType):
            song_date = datetime(song_loaded.tag.release_date.year, song_loaded.tag.release_date.month, song_loaded.tag.release_date.day).strftime("%Y-%m-%d")
        
        
        response = JsonResponse({
            "title": song_loaded.tag.title,
            "album": song_loaded.tag.album,
            "artist": song_loaded.tag.album_artist,
            "genre": song_loaded.tag.genre.name,
            "release-date": song_date
        })

        return response

class SetMetadataView(APIView):
    def put(self, request):
        song_id = request.GET.get('id', '')
        song_title = request.GET.get('title', '')
        song_album = request.GET.get('album', '')
        song_artist = request.GET.get('artist', '')
        song_genre = request.GET.get('genre', '')
        song_release_date = request.GET.get('release-date')

        if not song_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        song_loaded = eyed3.load(Song.objects.get(id=int(song_id)).data.path)
        song_loaded.tag.title = song_title
        song_loaded.tag.album = song_album
        song_loaded.tag.album_artist = song_artist 
        song_loaded.tag.genre.name = song_genre
        song_loaded.tag.release_date = song_release_date
        song_loaded.tag.save()

        return Response(status=status.HTTP_200_OK)

class SearchView(APIView):
    def post(self, request):
        if 'value' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        search_value = request.data['value']           

        songs = [] 
        songs = Song.objects.filter()
        results = []

        for song in songs:
            song_data = eyed3.load(song.data.path)
            print(song.data.path)
            tags = str(song_data.tag.title) + " " + str(song_data.tag.album) + " " + str(song_data.tag.album_artist) + " "
            tags += str(song_data.tag.genre) + " " + str(song_data.tag.release_date)
            if search_value in tags:
                results.append(song.id)
        
        response = JsonResponse({
            "results": results
        })

        return response