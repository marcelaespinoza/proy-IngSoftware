<script>
import { RouterLink, RouterView } from 'vue-router';

export default {
  name: "App",
  // data() {
  //   return { active_section: "dashboard" }
  // },
  watch: {
    '$route'(to, _) {
      // this.$refs[`${this.$route.params.name}`].style.background = "white";
    }
  },
}

</script>

<template>
  <nav id="sup-navbar">
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

  <nav id="lateral-navbar">
    <li>
      <ol><div ref="dashboard">
         <img src="./svg/home.svg" type="image/svg+xml" loading="lazy"/>
      </div></ol>
      
      <ol><div ref="user">
         <img src="./svg/user.svg" type="image/svg+xml" loading="lazy"/>
      </div></ol>

      <ol><div ref="recommendation">
        <img src="./svg/activity.svg" type="image/svg+xml" loading="lazy"/>
      </div></ol>
    </li>
  </nav>

  <router-view />
  <!--  -->
</template>

<style scoped>

</style>
