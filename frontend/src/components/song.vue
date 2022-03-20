<template>
  <div class="song-box">
    <div class="song-box-inner">
        <div class="song-box-metadata">
            <p>{{ song.title }}</p>
            <p>{{ song.artist }}</p>
            <p>{{ song.album }}</p>
            <p>{{ song.genre }}</p>
        </div>
        <div class="song-box-buttons">
            <button>
                <img>
            </button>
            <button>
                <img>
            </button>
        </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Song',
    props: {
        song: {
            id: Number,
            title: String,
            artist: String,
            album: String,
            genre: String,
            required: true
        }
    },
    data () {
      return {

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