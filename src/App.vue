<script setup>
import Dashboard from './components/Dashboard.vue';
</script>

<template>
  <nav id="sup-navbar">
    <div id="logo-title">
      <div style="margin-right: 20px;">
        <img src="./icons/feelscan.svg" type="image/svg+xml"/>
      </div>
      <h1>FeelScan</h1>
    </div>
    
    <div>
      <div style="margin-right: 2em"> Username </div>
      <button></button>  <!--log in or log out-->
    </div>
  </nav>

  <nav id="lateral-navbar">
    <li>
      <ol><div>
         <img src="./icons/home.svg" type="image/svg+xml"/>
      </div></ol>
      
      <ol><div>
         <img src="./icons/user.svg" type="image/svg+xml"/>
      </div></ol>

      <ol></ol>
    </li>
  </nav>

  <Dashboard />
  
  <!--  -->
</template>

<style scoped>

</style>
