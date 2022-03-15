<template>
  <div>
    <input v-model="keyword" placeholder="search" />
    <div v-for="(f, index) of filterAudios" :key="index">
      <img :src="f.thumbnail" />
      <p>{{ f.description }}</p>
    </div>
  </div>
</template>

<script>
//Filter und Search-Funktion anpassen
const audios = [
  {
    url: "https://www.youtube.com/watch?v=glN0W8WogK8",
    thumbnail: "https://i.ytimg.com/vi/lkpSG4VGoVk/mqdefault.jpg",
    description: "lego death yoda",
  },
  {
    url: "https://images.dog.ceo/breeds/akita/Akita_Inu_dog.jpg",
    description: "akita",
  },
  {
    url: "https://images.dog.ceo/breeds/retriever-golden/n02099601_7771.jpg",
    description: "golden retriever",
  }
];
export default {
  name: "App",
  data() {
    return { keyword: "", audios };
  },
  computed: {
    filterAudios() {
      const { audios, keyword } = this;
      return audios.filter(({ description }) => description.includes(keyword));
    },
  },
};
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>