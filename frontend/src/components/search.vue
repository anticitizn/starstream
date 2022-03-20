<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:submit.prevent="searchForFileName()">
      <input type="text" placeholder="Start searching!" v-model="searchValue"/>
    </form>
  </div>
  <SongCard v-for="(item, index) in songs" :song="item.value" :key="item.id"/>
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
        const testsong = ref(data)
        let songs = [testsong, testsong]
        return {
           songs,
           searchValue: ""
        }
    },
    methods: {
        searchForFileName() {
            let request = { value: this.searchValue}
            axios.post("http://backend-starstream.localhost:8000/search/", request).then(response => (songs = response.data))
            // this needs to be a POST request
            // the body must be a JSON with a single key-value pair - { "value": "britney spears" }
            // the response to the request is a JSON containing a list with all matching song IDs
            // then you can get the metadata for every one of them separately
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

