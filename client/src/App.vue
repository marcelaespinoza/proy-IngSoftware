<script>
import { RouterLink, RouterView } from 'vue-router';

export default {
  name: "App",
  data() {
    return { user_logged: false }
  },
  watch: {
    '$route'(to, _) {
      // this.$refs[`${this.$route.params.name}`].style.background = "white";
    }
  },
  
  computed: {
    user_logged() {
      return this.$route.path !== '/login' && this.$route.path !== '/welcome';
    },
  },
}

</script>

<template>
    
  <nav v-if="user_logged" id="sup-navbar">
    <div id="logo-title">
      <div style="margin-right: 20px;">
        <img src="./svg/feelscan.svg" type="image/svg+xml" width="50" loading="lazy"/>
      </div>
      <h1>FeelScan</h1>
    </div>
    
    <div>
      <div style="margin-right: 2em"> </div>
      <button></button>  <!--log in or log out-->
    </div>
  </nav>

  <nav v-if="user_logged" id="lateral-navbar">
    <li>
      <ol><div ref="dashboard">
         <router-link to="/dashboard"><img src="./svg/home.svg" type="image/svg+xml" loading="lazy"/></router-link>
      </div></ol>
      
      <ol><div ref="user">
        <router-link to="/profile"><img src="./svg/user.svg" type="image/svg+xml" loading="lazy"/></router-link>
      </div></ol>

      <ol><div ref="recommendation">
        <router-link to="/recommendation"><img src="./svg/recommendation.svg" type="image/svg+xml" loading="lazy"/></router-link>
      </div></ol>

      <!-- AQUI NO HAY ROUTER LINK, solo muestra la ventana flotante de notificaciones -->
      <ol><div ref="notification">
        <img src="./svg/notification.svg" type="image/svg+xml" loading="lazy"/>
      </div></ol>
    </li>
  </nav>

  <router-view />
  <!--  -->
</template>

<style scoped>

</style>
