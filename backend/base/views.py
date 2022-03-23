import eyed3
import logging

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
        eyed3.log.setLevel("ERROR") # really stupid placing but idk where else to put it
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

class SetMetadataView(APIView):
    def post(self, request):
        song_id = request.data['id']
        song_title = request.data['title']
        song_album = request.data['album']
        song_artist = request.data['artist']
        song_genre = request.data['genre']

        if not song_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        song_data = eyed3.load(Song.objects.get(id=int(song_id)).data.path)
        if song_title:
            song_data.tag.title = song_title 
        if song_album:
            song_data.tag.album = song_album 
        if song_artist:
            song_data.tag.artist = song_artist 
        if song_genre:
            song_data.tag.genre = song_genre

        song_data.tag.save()

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