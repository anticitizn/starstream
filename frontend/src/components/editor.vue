<template>
  <div class="song-container" id="song-container-editor">
      <div class="song-metadata">
        <div class="row">
          <div class="col-sm">
            <input class="input-title" v-model="this.song.title">
          </div>
          <div class="col-sm">
            <input class="input-artist" v-model="this.song.artist">
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
            <input class="input-album" v-model="this.song.album">
          </div>
          <div class="col-sm">
            <input class="input-genre" v-model="this.song.genre">
          </div>
        </div>
        <div class="row">
          <div class="col-sm">
            <div class="upload-button-container">
              <input id="upload" style="display: none;" type="file" accept="image/*" @change="onFilePicked"/>
              <label :class="{'upload-button': !hasUploaded, 'upload-button-success': hasUploaded}" for="upload">Upload</label>
            </div>
          </div>
        </div>
      </div>
      <div class="song-box-buttons row">
        <div class="col-sm">
          <button class="accept-button" v-on:click="accept">Accept</button>
        </div>
        <div class="col-sm">
          <button class="reject-button" v-on:click="reject">Reject</button>
        </div>
      </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Editor',
  props: {
    state: {
      state: String,
      id: Number
    }
  },
  data () {
    return {
      song: {
        title: String,
        artist: String,
        album: String,
        genre: String,
        image: String,
        required: true
      },
      hasUploaded: false
    }
  },
  created() {
    axios.get("http://localhost:8000/getmetadata/?id=" + this.state.id).then(response => {
      this.song = response.data
    })
  },
  methods: {
    accept() {
      let request = {
        id: this.state.id, 
        title: this.song.title, 
        artist: this.song.artist, 
        album: this.song.album, 
        genre: this.song.genre,
        image: this.song.image
      }

      axios.post("http://localhost:8000/setmetadata/", request)
      this.state.state = "Collapsed"
    },
    reject() {
      this.state.state = "Collapsed"
    },
    onFilePicked(event) {
      let imageFile = event.target.files[0]

      const reader = new FileReader()
        reader.onload = (e) => {
          this.song.image = e.target.result;
        };

        reader.readAsDataURL(imageFile)

      // set upload button color to green for 2 seconds
      this.hasUploaded = true
      setTimeout(()=>{
        this.hasUploaded = false
      },2000);
    }
  }
}
</script>

<style scoped>

  #song-container-editor {
    height: 220px;
  }

  input {
    width: 100%;
    padding: 3px;
    border: 1px solid gray;
    border-radius: 20px;
    background-color: #E5E5E5;
  }

  button {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
    background-color: #ffffff;
    width: 100%;
    height: 30px;
    border: 1px solid gray;
    border-radius: 20px;
    transition: background-color 0.5s;
  }

  button:hover {
    background-color: #FCA311;
  }

  .col-sm {
    margin: 10px;
  }

  .upload-button {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
    text-align: center;
    background-color: white;
    width: 100%;
    height: 30px;
    border: -2px solid;
    border-color: #E5E5E5;
    transition: background-color 0.5s;
    border: 1px solid gray;
    border-radius: 20px;
  }

  .upload-button:hover {
    background-color: #FCA311;
  }

  .upload-button-success {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
    text-align: center;
    background-color: #6db959;
    width: 100%;
    height: 30px;
    border: -2px solid;
    border-color: #E5E5E5;
    border-radius: 20px;
    transition: background-color 0.5s;
    border: 1px solid gray;
    border-radius: 20px;
  }

</style>