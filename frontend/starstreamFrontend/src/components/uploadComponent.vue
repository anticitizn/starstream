<template>
  <div class="container">
    <div>
      <input type="file" accept="audio/*" @change="handleFileUpload( $event )"/>
      <br>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
  <audio id="audio-preview" controls v-show="file != ''"/>
</template>

<script setup>
function previewAudio(){
  let audio = document.getElementById('audio-preview');
  let reader = new FileReader();

  reader.readAsDataURL( this.file );
  reader.addEventListener('load', function(){
    audio.src = reader.result;
  })
}

function handleFileUpload( event ){
  this.file = event.target.files[0];
  this.previewAudio();
}
</script>

<style scoped>

</style>