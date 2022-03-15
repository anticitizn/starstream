<script setup>
  import {onMounted, reactive} from "vue";
  import firebase from 'firebase';

  const audioFiles = reactive([]);
  onMounted(async () => {
    try {
      const audioSnap = await firebase
          .firestore()
          .collection("audios")
          .get();
      audioSnap.forEach((doc) => {
        audioFiles.push(doc.data());
      });
    } catch (e) {
      console.log("Error Loading Products");
    }
    return { audioFiles };
  });

</script>