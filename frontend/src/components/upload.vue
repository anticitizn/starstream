
<template>
  <div>
    <h1>File Upload</h1>
    <input type="file" accept="audio/*" @change="setAudioData()"/>
    <br>
    <button v-on:click="setAudioData()">Upload File</button>
  </div>
</template>

<script>
export default {
  name: "Upload",
  data() {
    return {
      file: [],
    };
  },
  methods: {
    setAudioData() {
      let formData = new FormData();
      let audioFile = this.file;
      formData.append("file", audioFile);
      this.axios.post('http://backend-starstream.localhost:8000/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    },

    handleFileUpload(event) {
      this.file = event.target.files[0];
  }
}
};
</script>