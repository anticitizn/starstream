<template>
  <div class="song-container">
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
        required: true
    }
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
        genre: this.song.genre
        }

      axios.post("http://localhost:8000/setmetadata/", request)
      this.state.state = "Collapsed"
    },
    reject() {
      this.state.state = "Collapsed"
    }
  }
}
</script>

<style scoped>

  input {
    width: 100%;
    padding: 3px;
    border-color: #E5E5E5;
    border-radius: 20px;
  }

  button {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
    background-color: #ffffff;
    width: 100%;
    height: 30px;
    border-color: #E5E5E5;
    border-radius: 20px;
    transition: background-color 0.5s;
  }

  button:hover {
    background-color: #FCA311;
  }

  .col-sm {
    margin: 10px;
  }
</style>