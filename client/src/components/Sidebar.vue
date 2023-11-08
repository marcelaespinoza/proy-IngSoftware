<script>
import { RouterLink } from 'vue-router';
import Notification from './Notification.vue';

export default {
    name: "Sidebar",
    data() {
      return {
        collapsed: false,
        showNotifications: false,
        screenWidth: window.innerWidth,

        userNane: "Usuario",
      };
    },
    methods: {
        toggleCollapse() {
            this.collapsed = !this.collapsed;
        },
        closeSidenav() {
            this.collapsed = false;
        },
        onResize(event) {
            this.screenWidth = window.innerWidth;
            if (this.screenWidth > 768) {
                this.collapsed = false; // Oculta el sidenav en dispositivos no móviles
            }
        },
        viewNotifications() {
          this.showNotifications = !this.showNotifications;
      }
    },

    mounted() {
        window.addEventListener("resize", this.onResize);
    },
    destroyed() {
        window.removeEventListener("resize", this.onResize);
    },
    components: { Notification }
}
</script>


<template>
  <div :class="['sidenav', collapsed ? 'sidenav-collapsed' : '']">
    <div class="logo-container">
      <button class="logo" @click="toggleCollapse()"><img src="../svg/feelscan.svg" loading="lazy"></button>
      <div class="logo-text" v-if="collapsed">FeelScan</div>
      <button class="btn-close" v-if="collapsed && screenWidth <= 768" @click="closeSidenav()">
        <i class="fal fa-times close-icon"></i>
      </button>
    </div>

    <ul class="sidenav-nav">
      
      <li class="sidenav-nav-item">
        <router-link class="sidenav-nav-link" to="/profile" exact>
          <img src="../svg/user.svg" type="image/svg+xml" loading="lazy" class="sidenav-link-icon" />
          <span class="sidenav-link-text" v-if="collapsed">Profile</span>
        </router-link>
      </li>

        <li class="sidenav-nav-item">
           <router-link class="sidenav-nav-link" to="/dashboard" exact>
            <img src="../svg/home.svg" type="image/svg+xml" loading="lazy" class="sidenav-link-icon" />
            <span class="sidenav-link-text" v-if="collapsed">Dashboard</span>
          </router-link>
        </li>
  
        <li class="sidenav-nav-item">
          <router-link class="sidenav-nav-link" to="/recommendation" exact>
            <img src="../svg/recommendation.svg" type="image/svg+xml" loading="lazy" class="sidenav-link-icon" />
            <span class="sidenav-link-text" v-if="collapsed">Recommendation</span>
          </router-link>
        </li>

        <li @click="viewNotifications" class="sidenav-nav-item"><div class="sidenav-nav-link">
            <img src="../svg/notification.svg" type="image/svg+xml" loading="lazy" class="sidenav-link-icon" />
            <span class="sidenav-link-text" v-if="collapsed">Notification</span></div>
        </li>
    </ul>
  </div>

  <Notification v-if="showNotifications" />
</template>


<style scoped>


</style>