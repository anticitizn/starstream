<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:submit.prevent="searchForFileName()">
      <input type="text" placeholder="Start searching!" v-model="searchValue"/>
    </form>
  </div>
  <SongCard v-for="item in songs" :song="item" :key="item.id"/>
</template>

<script>
import { ref } from 'vue'
import data from '../assets/testsong.js'
import SongCard from "./songcard.vue";
import axios from "axios";

  export default {
    name: "Search",
    components: { SongCard },
    data() {
        let songs = []
        return {
           songs
        }
    },
    methods: {
        searchForFileName() {
            this.songs.length = 0 // clear the array while making sure that reference isn't lost
            let searchRequest = { value: this.searchValue}
            axios.post("http://backend-starstream.localhost:8000/search/", searchRequest).then(response => {
              response.data.results.forEach(songId => {
                axios.get("http://backend-starstream.localhost:8000/getmetadata/?id=" + songId).then(response => (this.songs.push(response.data)))
              })
            })
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

