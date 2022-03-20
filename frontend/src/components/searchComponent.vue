<template>
  <div class="search">
    <h1>Search for Song-Name</h1>
    <form v-on:submit.prevent="searchForFileName()">
      <input type="text" v-model="searchValue" @change="searching( $event )"/>
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
          this.axios.get('http://backend-starstream.localhost:8000/download/').then(response => (this.searchingName=response.data));
          // this needs to be a POST request
          // the body must be a JSON with a single key-value pair - { "value": "britney spears" }
          // the response to the request is a JSON containing a list with all matching song IDs
          // then you can get the metadata for every one of them separately
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