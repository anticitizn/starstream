<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:submit.prevent="searchForFileName()">
      <input type="text" v-model="searchingName" />
    </form>
  </div>
</template>

<script>
  export default {

    name: 'search',
    data () {
      return {
        searchingName: ''
      }
    },
    methods: {
      searchForFileName () {
          this.axios.get("").then(response => (this.searchingName=response.data));
        }
    }
  }
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>