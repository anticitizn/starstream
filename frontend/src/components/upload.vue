
<template>
  <div>
    <input id="upload" style="display: none;" type="file" accept="audio/*" @change="onFilePicked"/>
    <div class="upload-button-container">
      <button :class="{'upload-button': !hasUploaded, 'upload-button-success': hasUploaded}" for="upload">Upload</button>
    </div>
  </div>

</template>

<script>
export default {
  name: "Upload",
  data() {
    return {
      hasUploaded: false
    }
  },
  methods: {
    onFilePicked(event) {
      let audioFile = event.target.files[0]

      let formData = new FormData();
      formData.append("file", audioFile);

      this.axios.post('http://backend-starstream.localhost:8000/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })

      this.hasUploaded = true
      setTimeout(()=>{
        this.hasUploaded = false
      },2000);
    }
  }
};
</script>

<style scoped>
.upload-button {
  cursor: pointer;
  color: #000000;
  font-weight: bold;
  background-color: #ffffff;
  width: 100%;
  height: 5vh;
  min-height: 50px;
  padding: 10px;
  border: -2px solid;
  border-color: #E5E5E5;
  border-radius: 20px;
  transition: background-color 0.5s;
}

.upload-button:hover {
  background-color: #FCA311;
}

.upload-button-success {
  cursor: pointer;
  color: #000000;
  font-weight: bold;
  background-color: #6db959;
  width: 100%;
  height: 5vh;
  min-height: 50px;
  padding: 10px;
  border: -2px solid;
  border-color: #E5E5E5;
  border-radius: 20px;
  transition: background-color 0.5s;
  
}

</style>