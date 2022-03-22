<template>
  <div class="song-container">
      <div class="song-metadata">
          <input class="input-title" v-model="state.song.title">
          <input class="input-artist" v-model="state.song.artist">
          <input class="input-album" v-model="state.song.album">
          <input class="input-genre" v-model="state.song.genre">
      </div>
      <div class="song-box-buttons">
          <button class="accept-button" v-on:click="accept"></button>
          <button class="reject-button" v-on:click="reject"></button>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'Editor',
    props: {
      state: {
        state: String,
        song: {
            id: Number,
            title: String,
            artist: String,
            album: String,
            genre: String,
            required: true
        }
      }
    },
    data () {
      return {

      }
    },
    methods: {
      accept() {
        axios.put("http://backend-starstream.localhost:8000/setmetadata/", this.state.song)
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