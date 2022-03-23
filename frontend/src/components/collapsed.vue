<template>
  <div class="song-container">
    <div class="row">
      <div class="song-metadata col-sm-10">
        <p class="primary-info" style="font-weight: bold;">{{ this.song.title }} - {{ this.song.artist }}</p>
        <p class="secondary-info">{{ this.song.album }} | {{ this.song.genre }}</p>
      </div>
      <div class="song-box-buttons col-sm-2">
        <button class="edit-button" v-on:click="edit">Edit</button>
      </div>
    </div>
    <div class="song-player">
      <audio :src="audioFile" controls></audio>
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
    axios.get("http://backend-starstream.localhost:8000/getmetadata/?id=" + this.state.id).then(response => {
      this.song = response.data
    })
    this.audioFile = "http://backend-starstream.localhost:8000/download/?id=" + this.state.id
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
      audioFile: ""
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
    height: 18vh;
    min-height: 170px;
    padding: 10px;
    border-radius: 20px;
    overflow: hidden;
    margin: 20px;
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