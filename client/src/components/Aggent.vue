<template>

  <div class="container" v-if="showWindow">
    <div id="container-modal">

      <h3>Agende una cita de {{ $props.username }} con nuestros especialistas</h3>
      <p>Send {{ $props.email }}</p>

      <div class="contact-form">
        <form ref="form" @submit.prevent="sendEmail">
          <div class="form-group">
            <input v-model="psicologo" class="form-control" type="text" placeholder="Psicólogo *" />
          </div>
          <div class="form-group">
            <input v-model="date" class="form-control" type="date" placeholder="Fecha de visita *" />
          </div>
          <div class="form-group">
            <textarea v-model="message" class="form-control" placeholder="Mensaje *" cols="45" rows="8"></textarea>
          </div>
          <div class="form-group">
            <button class="btn send-button" type="submit">Enviar</button>
          </div>
          <p v-if="!isFormValid" class="error-message">Por favor, llene todos los campos.</p>
          <div v-if="isEmailSent" class="success-message">
            <p>Correo enviado satisfactoriamente!</p>
            <button @click="closePopup" class="btn btn-secondary">Cerrar</button>
          </div>
        </form>
      <!-- <router-link to="/psicologos" class="btn psychologists-button">Lista de psicólogos</router-link> -->
      <button @click="viewWindow()" class="btn psychologists-button">Ir atrás</button>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    name: "Aggent",
    props: {
      "username": String,
      "email": String,
    },
    data() {
      return {
        psicologo: "",
        date: "",
        message: "",
        isFormValid: true,
        isEmailSent: false,
        showWindow: true
      };
    },
    methods: {
        sendEmail() {
        // Validar que todas las casillas del formulario estén llenas
        if (
          this.userData.name &&
          this.userData.email &&
          this.userData.date &&
          this.userData.message
        ) {
          // Lógica para enviar el correo
          this.isFormValid = true; // El formulario es válido, puede enviar el correo
          //implementar la lógica para enviar el correo
        } else {
          this.isFormValid = false; // El formulario no es válido
        }
      },
      closePopup() {
        this.isEmailSent = false;
      },
      viewWindow() {
        this.showWindow = false;
      }
    }
  }
</script>

<style scoped>

</style>