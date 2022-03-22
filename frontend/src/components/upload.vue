
<template>
  <div>
    <h1>File Upload</h1>
    <input type="file" accept="audio/*" @change="onFilePicked"/>
  </div>

</template>

<script>
export default {
  name: "Upload",
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
    }
  }
};
</script>