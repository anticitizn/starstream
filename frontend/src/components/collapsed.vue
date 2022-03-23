<template>
  <div class="song-container">
      <div class="song-metadata">
          <p class="primary-info">{{ this.song.title }} - {{ this.song.artist }}</p>
          <p class="secondary-info">{{ this.song.album }} - {{ this.song.genre }}</p>
      </div>
      <div class="song-box-buttons">
          <button class="edit-button" v-on:click="edit">Edit</button>
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
  .song-container {
    background: #e5e5e5;
    width: 100%;
    height: 15vh;
    min-height: 150px;
    padding: 10px;
    border-radius: 20px;
    overflow: hidden;
    margin: 20px;
  }
</style>