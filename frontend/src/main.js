import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueAxios from "vue-axios";
import mitt from 'mitt';

const app = createApp(App);
app.use(VueAxios, axios)
app.use(router);

const emitter = mitt();
app.config.globalProperties.emitter = emitter;
app.mount("#app");
