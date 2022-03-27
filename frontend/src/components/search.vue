<template>
  <div class="search-box">
    <form v-on:submit.prevent="searchForFileName()">
      <input class="search-bar" type="text" placeholder="Start searching!" v-model="searchValue"/>
    </form>
  </div>
  <component :is="item.state" v-for="item in songContainers" :state="item" :key="item.id"/>
</template>

<script>
import Collapsed from "./collapsed.vue";
import Editor from "./editor.vue";
import axios from "axios";

export default {
  name: "Search",
  components: { Collapsed, Editor },
  data() {
      let songContainers = []
      let searchValue = ""
      return {
          songContainers,
          searchValue
      }
  },
  created() {
    let searchRequest = { value: ""}
    axios.post("http://localhost:8000/search/", searchRequest).then(response => {
      response.data.results.forEach(songId => {
        this.songContainers.push({ state: "Collapsed", id: songId })
      })
    })
  },
  methods: {
      searchForFileName() {
          this.songContainers.length = 0 // clear the array while making sure that reference isn't lost
          let searchRequest = { value: this.searchValue}
          axios.post("http://localhost:8000/search/", searchRequest).then(response => {
            response.data.results.forEach(songId => {
              this.songContainers.push({ state: "Collapsed", id: songId })
            })
          })
      }
  }
}
</script>

<style scoped>
.search-bar {
  width: 100%;
  height: 5vh;
  min-height: 50px;
  padding: 10px;
  border: 1px solid gray;
  border-radius: 20px;
  overflow: hidden;
  margin: 20px;
}
</style>

