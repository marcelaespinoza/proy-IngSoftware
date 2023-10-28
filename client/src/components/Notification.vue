<script>
export default {
  name: "Notification",
  data() {
    return {
        showCitas: true,
        citasPendientes: ["Margiory", "Marcela", "Milloshy", "Fabiola", "Adrian"],
    }
  },
  computed: {
    viewNotifications() {
        this.showCitas = !this.showCitas;
    }
  }
}
</script>


<template>
<div v-if="showCitas" id="ventanaCita" class="window">
  <div class="window-content">
    <button @click="viewNotifications" class="close" id="closewindow">&times;</button>
    <h2>Tienes citas pendientes!!</h2>
    <ul id="miembrosPendientes">
      <!-- Aquí se agregaría la data a usar sobre las citas de FeelScan? -->
      <li v-for="(integer, index) in citasPendientes" :key="index">
        {{ integer }}
      </li>
    </ul>
  </div>
</div>
</template>


<style scoped>

</style>