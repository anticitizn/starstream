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
      path: "/upload",
      name: "upload",
      component: () => import("../components/upload.vue"),
    }
  ]
});

export default router;
