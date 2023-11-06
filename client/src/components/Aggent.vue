<template>

  <div class="container" v-if="showWindow">
    <div id="container-modal">

      <div id="text-aggent">
        <h3>Agende una cita de {{ $props.username }} con nuestros especialistas</h3>
        <p>Send email: {{ $props.email }}</p>
      </div>
      

      <div class="contact-form">
        <form ref="form" @submit.prevent="sendEmail">
          <div class="form-group-table">
            <table>
              <thead>
                <tr>
                  <th>Horario</th>
                  <th>Lunes</th><th>Martes</th>
                  <th>Miercoles</th><th>Jueves</th>
                  <th>Viernes</th>
                </tr>
            </thead>
            <tbody>
              <tr v-for="(horarios, code) in horariosPsico" :key="code">
                <td > {{ horarios.nombre }}</td>
                <td > {{ horarios["Lunes"]  }}</td>
                <td > {{ horarios["Martes"]  }}</td>
                <td > {{ horarios["Miercoles"]  }}</td>
                <td > {{ horarios["Jueves"]  }}</td>
                <td > {{ horarios["Viernes"]  }}</td>
              </tr>
            </tbody>
          </table>
            
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
import horariosPsico from '../utils/horariosPsico.json'

  export default {
    name: "Aggent",
    props: {
      "username": String,
      "email": String,
    },
    data() {
      return {
        // psicologos: [],
        horariosPsico: JSON.parse(JSON.stringify(horariosPsico)),
        date: "",
        message: "",
        isFormValid: true,
        isEmailSent: false,
        showWindow: true
      };
    },
    // created() {
    //   this.horariosPsico = fetch('')
    // },

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