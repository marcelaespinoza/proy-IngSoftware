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
        navData: [
          {
              routeLink: '/dashboard',
              icon: "./src/svg/home.svg",
              label: 'Dashboard'
          },
          {
              routeLink: '/profile',
              icon: './src/svg/user.svg',
              label: 'User'
          },
          {
              routeLink: '/recommendation',
              icon: './src/svg/recommendation.svg',
              label: 'Recommendation'
          },
          // {
          //     routeLink: '/mail',
          //     icon: '/svg/mail.png',
          //     label: 'mail'
          // },
          // {
          //     routeLink: '/settings',
          //     icon: '/svg/settings.png',
          //     label: 'settings'
          // },
        ],
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
    <!--
      <li>
        <ul><div ref="dashboard">
           <router-link to="/dashboard">
            <img src="./svg/home.svg" type="image/svg+xml" loading="lazy"/>
            <span class="sidenav-link-text" v-if="collapsed">Dashboard</span>
          </router-link>
        </div></ul>
        
        <ul><div ref="user">
          <router-link to="/profile">
            <img src="./svg/user.svg" type="image/svg+xml" loading="lazy"/>
            <span class="sidenav-link-text" v-if="collapsed">Profile</span>
          </router-link>
        </div></ul>
  
        <ul><div ref="recommendation">
          <router-link to="/recommendation">
            <img src="./svg/recommendation.svg" type="image/svg+xml" loading="lazy"/>
            <span class="sidenav-link-text" v-if="collapsed">Recommendation</span>
          </router-link>
        </div></ul>

        <ul><div ref="notification">
          <router-link to="/notification">
            <img src="./svg/notification.svg" type="image/svg+xml" loading="lazy"/>
            <span class="sidenav-link-text" v-if="collapsed">Recommendation</span>
          </router-link>
        </div></ul> -->
  
        <!-- <ol></ol>
      </li> -->
      <li class="sidenav-nav-item" v-for="data in navData" :key="data.routeLink">
        <router-link :to="data.routeLink" class="sidenav-nav-link" exact>
          <img :src="data.icon" type="image/svg+xml" loading="lazy" class="sidenav-link-icon" />
          <span class="sidenav-link-text" v-if="collapsed">{{ data.label }}</span>
        </router-link>
      </li>
      <li @click="viewNotifications" class="sidenav-nav-item">
          <img src="../svg/notification.svg" type="image/svg+xml" loading="lazy" class="sidenav-link-icon" />
          <span class="sidenav-link-text" v-if="collapsed">Notification</span>
       </li>
    </ul>
  </div>

  <Notification v-if="showNotifications" />
</template>


<style scoped>


</style>