import eyed3
import logging
import base64
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import FileResponse
from django.http import JsonResponse
from django.core.files import File
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from wsgiref.util import FileWrapper
from base.models import Song
from datetime import datetime
from sqlite3 import Date
from PIL import Image

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        song_file = request.data['file']
        default_image_name = "/thumb.jpg"
        image_file = open(default_image_name, 'rb')
        default_image = SimpleUploadedFile(default_image_name, image_file.read(), content_type="image/*")

        song = Song(data = song_file, image = default_image)
        song.save()

        song_data = eyed3.load(song.data.path)
        song_data.initTag()
        song_data.tag.genre = 12
        
        song_data.tag.save()
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
        
        song_data = eyed3.load(Song.objects.get(id=int(song_id)).data.path)
        
        response = JsonResponse({
            "title": song_data.tag.title if song_data.tag.title else Song.objects.get(id=int(song_id)).data.name,
            "artist": song_data.tag.artist if song_data.tag.artist else "Undefined Artist",
            "album": song_data.tag.album if song_data.tag.album else "Undefined Album",
            "genre": song_data.tag.genre.name if not isinstance(song_data.tag.genre, type(None)) else "Undefined Genre"
        })

        return response

class GetImageView(APIView):
    def get(self, request):
        song_id = request.GET.get('id', '')
        if not song_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        img = open(Song.objects.get(id=int(song_id)).image.path, 'rb')
        response = FileResponse(Song.objects.get(id=int(song_id)).image)

        return response

class SetMetadataView(APIView):
    def post(self, request):
        if not 'id' in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        song_id = request.data['id']
        song_title = request.data['title']
        song_album = request.data['album']
        song_artist = request.data['artist']
        song_genre = request.data['genre']
        song_image = ""
        if 'image' in request.data:
            song_image_b64 = request.data['image']
            song_image_b64 = song_image_b64.partition(",")[2]
            pad = len(song_image_b64)%4
            song_image_b64 += "="*pad
            song_image = base64.b64decode(song_image_b64)
        
        song = Song.objects.get(id=int(song_id))
        song_data = eyed3.load(song.data.path)
        if song_title:
            song_data.tag.title = song_title
        if song_album:
            song_data.tag.album = song_album
        if song_artist:
            song_data.tag.artist = song_artist
        if song_genre:
            song_data.tag.genre = song_genre
        if song_image:
            song.image = SimpleUploadedFile(song.image.name, song_image, content_type="image/*")

        song_data.tag.save()
        song.save()

        return Response(status=status.HTTP_200_OK)

class SearchView(APIView):
    def post(self, request):
        search_value = request.data['value']

        if not search_value:
            search_value = ""

        songs = [] 
        songs = Song.objects.filter()
        results = []

        for song in songs:
            song_data = eyed3.load(song.data.path)
            
            tags = str(song_data.tag.title) + " " + str(song_data.tag.album) + " " + str(song_data.tag.artist) + " "
            tags += str(song_data.tag.genre) + " " + str(song_data.tag.release_date)
            if search_value in tags:
                results.append(song.id)
        
        response = JsonResponse({
            "results": results
        })

        return response

class TestView(APIView):
    def get(self, request):
        songs = Song.objects.filter()
        response = JsonResponse({
            "results": songs[0].data.path
        })

        return response