<template>
  <div class="about">
    <UploadComponent></UploadComponent>
    <StreamingComponent></StreamingComponent>
  </div>
</template>

<script>
import UploadComponent from "../components/uploadComponent.vue";
import StreamingComponent from "../components/streamingComponent.vue";
export default {
  components: {StreamingComponent, UploadComponent}
}

</script>