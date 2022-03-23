<template>
  <div class="song-container">
      <div class="song-metadata">
          <p class="primary-info">{{ this.song.title }} - {{ this.song.artist }}</p>
          <p class="secondary-info">{{ this.song.album }} - {{ this.song.genre }}</p>
      </div>
      <div class="song-box-buttons">
          <button class="back-button" v-on:click="back">Stop</button>
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
  name: 'Player',
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
    back() {
      this.state.state = "Collapsed"
    },
    edit() {
      this.state.state = "Editor"
    }
  }
}
</script>

<style scoped>

</style>