<script>
import { RouterView } from 'vue-router';
import Sidebar from './components/Sidebar.vue'
import Notification from './components/Notification.vue'

export default {
  name: "App",
  computed: {
    user_logged() {
        return this.$route.path !== '/login' && this.$route.path !== '/welcome';
    },

    // in_dashboard() {
    //   return this.$route.path === '/dashboard';
    // }
  },
  components: { Sidebar, Notification }
}

</script>

<template>
 

  <Sidebar v-if="user_logged"/>

  <router-view />

  <Notification v-if="in_dashboard" />
  <!--  -->

</template>

<style scoped>

</style>
