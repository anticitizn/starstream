<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:dblclick="getMetaData(searchingName)">
      <input type="text" v-model="searchingName" />
    </form>
    <div class="about">
      <h1>This is the streaming page</h1>
      <audio id="audio-preview" controls />
    </div>
  </div>

</template>

<script>
import axios from "axios";

const res = await axios.get(`http://backend-starstream.localhost:8000/download/`);
// need to pass song ID as url parameter, like this: http://backend-starstream.localhost:8000/download/?id=3
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
