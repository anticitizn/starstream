
<template>
  <div>
    <h1>My Weather App</h1>
    <button v-on:click="setTest()">Get Weather Data</button>
    <input type="file" accept="audio/*" @change="handleFileUpload( $event )"/>
    <div v-for="audio in audios" :key="audio.id" class="audio-data">
      {{audios}}
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "upload",
  data() {
    return {
      audios: [],
      audioName: "Franz",
    };
  },
  methods: {
    getAudioData() {
      axios
          .get("audio.json")
          .then(response => (this.audios = response.data));
    },

    setAudioData(){
      let formData = new FormData();
      let audioFile = this.audios;
      formData.append("audio", audioFile);
      this.axios.post('upload_file', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    },

    async getTest(){
      try {
        const res = await axios.get(`http://localhost:3000/audio.json`);
        this.audios = res.data;
      } catch (error) {
        console.log(error);
      }
    },

    async setTest(){
      const res = await axios.post(`http://localhost:3000/audio.json`, {
        name: this.audioName,
      });
      this.audios = [...this.audios, res.data];
      this.audioName = '';
    },

    handleFileUpload( event ){
      this.audios = event.target.files[0];
  }
}
};
</script>