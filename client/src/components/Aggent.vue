<template>
  
    <div class="container">
    <h1 class="text-center">Agenda tu visita</h1>
    <h3>Reserve una consulta con nuestros especialistas en salud mental para fortalecer su bienestar emocional y mental.</h3>
  
      <div class="contact-form">
        <form ref="form" @submit.prevent="sendEmail">
          <div class="form-group">
            <input v-model="userData.name" class="form-control" type="text" placeholder="Nombre *" />
          </div>
          <div class="form-group">
            <input v-model="userData.email" class="form-control" type="email" placeholder="Correo *" />
          </div>
          <div class="form-group">
            <input v-model="userData.date" class="form-control" type="date" placeholder="Fecha de visita *" />
          </div>
          <div class="form-group">
            <textarea v-model="userData.message" class="form-control" placeholder="Mensaje *" cols="45" rows="8"></textarea>
          </div>
          <div class="form-group">
            <button class="btn send-button" type="submit">Enviar</button>
          </div>
          <p v-if="!isFormValid" class="error-message">Por favor, llene todos los campos.</p>
          <div v-if="isEmailSent" class="success-message popup">
            <p>Correo enviado satisfactoriamente!</p>
            <button @click="closePopup" class="btn btn-secondary">Cerrar</button>
          </div>
        </form>
        <!-- <router-link to="/psicologos" class="btn psychologists-button">Lista de psicólogos</router-link> -->
        <router-link to="/dashboard" class="btn psychologists-button">Ir atrás</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Aggent",
    data() {
      return {
        userData: {
          name: "",
          email: "",
          date: "",
          message: ""
        },
        isFormValid: true,
        isEmailSent: false
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
    }
    }
  }
  </script>
  
  <style scoped>
  .container {
    text-align: center;
  }
  
  .contact-form {
    width: 100%;
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff;
  }
  
  .form-group {
    margin-bottom: 15px;
    margin-right: 20px;
  }
  
  .form-control {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .btn {
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .send-button {
    width: 150px;
    height: 50px;
    background-color: #365627;
    color: white;
    font-size: 22px;
    font-weight: 700;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .btn-secondary {
    background-color: #6c757d;
    color: #fff;
  }
  
  .error-message {
    color: #ff0000;
  }
  
  .popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    text-align: center;
  }
  
  .popup button {
    margin-top: 10px;
    cursor: pointer;
  }

  .psychologists-button {
  margin-top: 20px;
  display: inline-block;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.psychologists-button:hover {
  background-color: #0056b3;
}
  </style>