
<template>
  <div>
    <h1>File Upload</h1>
    <input type="file" accept="audio/*" @change="handleFileUpload( $event )"/>
    <br>
    <button v-on:click="setAudioData()">Upload File</button>
  </div>
</template>

<script>
export default {
  name: "upload",
  data() {
    return {
      audios: [],
    };
  },
  methods: {
    setAudioData(){
      let formData = new FormData();
      let audioFile = this.audios;
      formData.append("audio", audioFile);
      this.axios.post('', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    },

    handleFileUpload( event ){
      this.audios = event.target.files[0];
  }
}
};
</script>