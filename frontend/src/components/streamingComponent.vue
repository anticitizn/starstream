<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:dblclick="getMetaData(searchingName)">
      <input type="text" v-model="searchingName" />
    </form>
  </div>
  <div class="about">
    <h1>This is the streaming page</h1>
    <audio id="audio-preview" controls />
  </div>
</template>

<script>
import axios from "axios";

const res = await axios.get(`http://localhost:3000/audios`);
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
