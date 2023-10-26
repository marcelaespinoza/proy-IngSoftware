import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ {
      path: "/",
      name: "welcome",
      component: () => import("../components/Landing.vue"),
    },{
      path: "/welcome",
      name: "welcome",
      component: () => import("../components/Landing.vue"),
    },{
      path: "/dashboard",
      name: "dashboard",
      component: () => import("../components/DashBoard.vue"),
    },{
      path: "/login",
      name: "login",
      component: () => import("../components/Login.vue"),
    }, {
      path: "/recommendation",
      name: "recommendation",
      component: () => import("../components/Recommendation.vue")
    }, {
      path: "/profile",
      name: "profile",
      component: () => import("../components/Profile.vue")
    }
  ],
});

export default router;