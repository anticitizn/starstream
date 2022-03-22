<template>
  <div class="song-container">
      <div class="song-metadata">
          <p class="primary-info">{{ this.song.title }} - {{ this.song.artist }}</p>
          <p class="secondary-info">{{ this.song.album }} - {{ this.song.genre }}</p>
      </div>
      <div class="song-box-buttons">
          <button class="play-button" v-on:click="play"></button>
          <button class="edit-button" v-on:click="edit"></button>
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

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>