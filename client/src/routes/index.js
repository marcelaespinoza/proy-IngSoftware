import { createRouter, createWebHistory } from "vue-router";

// function isAuthenticated() {
//   const userEmail = localStorage.getItem("email");
//   return userEmail !== null && userEmail !== undefined;
// }

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ {
      path: "/",
      name: "/",
      component: () => import("../components/Landing.vue"),
      // meta: {
      //   requiresAuth: true
      // }
    },{
      path: "/welcome",
      name: "welcome",
      component: () => import("../components/Landing.vue"),
      // meta: {
      //   requiresAuth: false
      // }
    },{
      path: "/dashboard",
      name: "dashboard",
      component: () => import("../components/DashBoard.vue"),
      // meta: {
      //   requiresAuth: true
      // }
    },{
      path: "/login",
      name: "login",
      component: () => import("../components/Login.vue"),
    }, {
      path: "/recommendation",
      name: "recommendation",
      component: () => import("../components/Recommendation.vue"),
      // meta: {
      //   requiresAuth: false
      // }
    }, {
      path: "/profile",
      name: "profile",
      component: () => import("../components/Profile.vue"),
      // meta: {
      //   requiresAuth: true
      // }
    },
    // {
    //   path: "/notification",
    //   name: "notification",
    //   component: () => import("../components/Notification.vue")
    // }, 
    // {
    //   path: "/settings",
    //   name: "settings",
    //   component: () => import("../components/Settings.vue"),
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: "/mail",
    //   name: "mail",
    //   component: () => import("../components/Mail.vue"),
    //   meta: {
    //     requiresAuth: true
    //   }
    // }, 
    {
      path: "/sidebar",
      name: "sidebar",
      component: () => import("../components/Sidebar.vue"),
      // meta: {
      //   requiresAuth: true
      // }
    }
  ],
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // La ruta requiere autenticación
    if (isAuthenticated()) {
      // El usuario está autenticado, permitir el acceso
      next();
    } else {
      // El usuario no está autenticado, redirigir a la página de inicio de sesión
      next("/login");
    }
  } else {
    // La ruta no requiere autenticación, permitir el acceso sin verificar
    next();
  }
});

export default router;