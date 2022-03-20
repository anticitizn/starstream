<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:dblclick="getMetaData(searchingName)">
      <input type="text" v-model="searchingName" />
    </form>
  </div>
  <div class="container">
    <form>
      <label>Name:</label><br>
      <input v-model="name" /><br>

      <label>Album:</label><br>
      <input v-model="album"><br>

      <label>Artist:</label><br>
      <input v-model="artist"><br>

      <label>Genre:</label><br>
      <input v-model="genre">

    </form>
    <button type="button" v-on:click="setMetaData(id)">Submit</button>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      searchingName: '',
      audios: [],
      id: 0,
      name: "",
      album: "",
      artist: "",
      genre: ""
    };
  },
  methods: {
    async getMetaData(name) {
      try {
        const res = await axios.get(`http://backend-starstream.localhost:8000/getmetadata/`);
        // ????????
        // this only returns the metadata for one song, why iterate over it like an array?
        this.audios = res.data
        for(let i = 0; i < this.audios.length; i++){
          if(this.audios[i].name.includes(name)){
            this.id = this.audios[i].id
            this.name = this.audios[i].name
            this.album = this.audios[i].album
            this.artist = this.audios[i].artist
            this.genre = this.audios[i].genre
          }
        }
      } catch (error) {
        console.log(error);
      }
    },
    async setMetaData(id) {
      try{
        // PUT, not PATCH
        // ID should be passed inside json, not as URL parameter
        const res = await this.axios.patch(`http://backend-starstream.localhost:8000/editmetadata/${id}`, {
          name: this.name,
          album: this.album,
          artist: this.artist,
          genre: this.genre
        });
        res.data.json;
      } catch (error){
        console.log(error);
      }

    }
}};
</script>