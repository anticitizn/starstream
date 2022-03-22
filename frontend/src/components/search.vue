<template>
  <Upload/>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:submit.prevent="searchForFileName()">
      <input type="text" placeholder="Start searching!" v-model="searchValue"/>
    </form>
  </div>
  <component :is="item.state" v-for="item in songContainers" :state="item" :key="item.id"/>
</template>

<script>
import Collapsed from "./collapsed.vue";
import Upload from "./upload.vue";
import axios from "axios";

export default {
  name: "Search",
  components: { Collapsed, Upload},
  data() {
      let songs = []
      let songContainers = []
      return {
          songs,
          songContainers
      }
  },
  methods: {
      searchForFileName() {
          this.songs.length = 0 // clear the array while making sure that reference isn't lost
          let searchRequest = { value: this.searchValue}
          axios.post("http://backend-starstream.localhost:8000/search/", searchRequest).then(response => {
            response.data.results.forEach(songId => {
              this.songContainers.push({ state: "Collapsed", id: songId })
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

