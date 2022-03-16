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
        query: '',
        results: ''
      }
    },
    methods: {
      getResults (q) {
        q = q.replace(/ /g, '%20')
        console.log(q)
        this.$http.get('https://images-api.nasa.gov/search?q=' + q + '&media_type=image').then(response => {
          this.results = response.body.collection.items
        }, response => {
          console.log('Error: ', response)
        })
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