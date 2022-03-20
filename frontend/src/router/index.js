import { createRouter, createWebHistory } from "vue-router";
import homeComponent from "../components/home.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: homeComponent,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../components/about.vue"),
    },
    {
      path: "/upload",
      name: "upload",
      component: () => import("../components/upload.vue"),
    },
    {
      path: "/metaData",
      name: "metaData",
      component: () => import("../components/metadata.vue"),
    },
    {
      path: "/streaming",
      name: "streaming",
      component: () => import("../components/streaming.vue")
    }
  ],
});

export default router;
