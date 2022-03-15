<template>
  <div class="about">
    <h1>This is the streaming page</h1>
    <audio id="audio-preview" controls loop v-show="file != ''" />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
