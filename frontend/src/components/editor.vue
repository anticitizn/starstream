<template>
  <div class="song-container">
      <div class="song-metadata">
          <input class="input-title" v-model="this.song.title">
          <input class="input-artist" v-model="this.song.artist">
          <input class="input-album" v-model="this.song.album">
          <input class="input-genre" v-model="this.song.genre">
      </div>
      <div class="song-box-buttons">
          <button class="accept-button" v-on:click="accept">Accept</button>
          <button class="reject-button" v-on:click="reject">Reject</button>
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
        required: true
    }
  }
},
  created() {
    axios.get("http://backend-starstream.localhost:8000/getmetadata/?id=" + this.state.id).then(response => {
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
        genre: this.song.genre
        }

      axios.post("http://backend-starstream.localhost:8000/setmetadata/", request)
      this.state.state = "Collapsed"
    },
    reject() {
      this.state.state = "Collapsed"
    }
  }
}
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>