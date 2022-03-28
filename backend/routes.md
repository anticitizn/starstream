# Get audio file of song with id 1

GET /download/?id=1

RESPONSE 200
{
  "file": ""
}

# Get text metadata of song with id 1

GET /getmetadata/?id=1

RESPONSE 200
{
  "title": "",
  "album": "",
  "artist": "",
  "genre": ""
}

# Get the thumbnail image of song with id 1

GET /getimage/?id=1

RESPONSE 200
{
    "file": ""
}

# Get a list of song IDs whose tags match given string

POST /search/
{
  "value": ""
}

RESPONSE 200
{
  "results": ["1", "2", "3"]
}

# Upload song

POST /upload/
{
  "file": ""
}

RESPONSE 204

# Set the text metadata of song

POST /setmetadata/
{
  "id": "",
  "title": "",
  "album": "",
  "artist": "",
  "genre": "",
  "image": ""
}

RESPONSE 200