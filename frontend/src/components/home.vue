<script>
import songlist from './songlist.vue';
import search from './search.vue';
export default {
  name: 'Home',
  components: {
    search,
    songlist
  }
}
</script>

<template>
  <header>
  </header>
  <body>
    <search/>
    <songlist/>
  </body>
</template>
