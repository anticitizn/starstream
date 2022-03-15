<template>
  <div class="about">
    <UploadComponent></UploadComponent>
  </div>
</template>

<script>
import UploadComponent from "../components/uploadComponent.vue";
export default {
  components: {UploadComponent}
}

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
