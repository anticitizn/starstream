<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="store.increment()">
      From ABout: {{ store.count }}
    </button>
  </div>
</template>

<script>
import { store } from './store.js'

export default {
  data() {
    return {
      store
    }
  }
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
