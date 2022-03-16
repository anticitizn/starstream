
<script>
export default {
  file: '',
  arr: [],

  methods: {
    add: function (e) {
      this.arr.push({first: this.file});
      console.log(1);
    },
    saveFile: function () {
      const data = JSON.stringify(this.arr)
      window.localStorage.setItem('arr', data);
      console.log(JSON.parse(window.localStorage.getItem('arr')))
    }
  } }

</script>