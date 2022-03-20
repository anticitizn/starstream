import { createRouter, createWebHistory } from "vue-router";
import homeComponent from "../components/homeComponent.vue";

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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../components/aboutComponent.vue"),
    },
    {
      path: "/upload",
      name: "upload",
      component: () => import("../components/uploadComponent.vue"),
    },
    {
      path: "/metaData",
      name: "metaData",
      component: () => import("../components/metaDataComponent.vue"),
    },
    {
      path: "/streaming",
      name: "streaming",
      component: () => import("../components/streamingComponent.vue")
    }
  ],
});

export default router;
