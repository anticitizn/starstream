<template>
  <div class="container" style="margin-top: 5vh;">
    <div class="row">
      <div class="col-sm-2">
        <h1 style="writing-mode:vertical-rl; font-weight: bold; margin-top: 20px;">STARSTREAM</h1>
      </div>
      <div class="col-sm-6">
        <Search/>
      </div>
      <div class="col-sm-1" style="margin: 20px;">
        <Upload/>
      </div>
    </div>
  </div>
</template>

<script>
import Search from './search.vue';
import Upload from './upload.vue';
export default {
  name: 'Home',
  components: { Search, Upload }
}
</script>

<style scoped>

</style>