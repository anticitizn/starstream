<template>
  <div class="song-container">
    <div class="row" style="height: 100%;">
      <div class="col-sm-2 song-img-container">
        <img class="song-img" :src="this.songImage">
      </div>
      <div class="row col-sm-10 song-metadata">
        <div class="col-sm-10">
          <p class="primary-info" style="font-weight: bold;">{{ this.song.title }} - {{ this.song.artist }}</p>
          <p class="secondary-info">{{ this.song.album }} | {{ this.song.genre }}</p>
        </div>
        <div class="song-box-buttons col-sm-2">
          <button class="edit-button" v-on:click="edit">Edit</button>
        </div>
        <div class="song-player">
          <audio :src="audioFile" controls></audio>
        </div>
      </div>
      
    </div>
  </div>
  
</template>

<script>
import axios from "axios";

export default {
  name: 'Collapsed',
  props: {
    state: {
      state: String,
      id: Number
    }
  },
  created() {
    axios.get("http://localhost:8000/getmetadata/?id=" + this.state.id).then(response => {
      this.song = response.data
    })
    this.audioFile = "http://localhost:8000/download/?id=" + this.state.id
    this.songImage = "http://localhost:8000/getimage/?id=" + this.state.id
  },
  data () {
    return {
        song: {
          title: String,
          artist: String,
          album: String,
          genre: String,
          required: true
      },
      audioFile: "",
      songImage: ""
    }
  },
  methods: {
    play() {
      this.state.state = "Player"
    },
    edit() {
      this.state.state = "Editor"
    }
  }
}
</script>

<style>
  .song-metadata {
    margin-top: 10px;
  }

  .edit-button {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
    background-color: #ffffff;
    width: 100%;
    height: 5vh;
    min-height: 40px;
    padding: 10px;
    border-color: #E5E5E5;
    border-radius: 20px;
    transition: background-color 0.5s;
  }

  .edit-button:hover {
    background-color: #FCA311;
  }

  .song-container {
    background: #ffffff;
    width: 100%;
    height: 170px;
    border-radius: 20px;
    overflow: hidden;
    margin: 20px;
  }

  .song-img {
    border-radius: 20px;
    flex-shrink: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;

  }

  audio {
    width: 100%;
    padding: 5px;
    border-radius: 5px;
    margin: 5px;
  }

  audio::-webkit-media-controls-panel {
    border-radius: 20px; 
  }

</style>