<script>
import { ref } from 'vue'
import data from '../assets/testsong.js'
import Song from "./song.vue";
export default {
    name: "Songlist",
    components: { Song },
    setup() {
        const testsong = ref(data)
        return {testsong}
    }
}
</script>

<template>
    <div class="song-list">
        <Song :song="testsong"/>
    </div>
</template>
