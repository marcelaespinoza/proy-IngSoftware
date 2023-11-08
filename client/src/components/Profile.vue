<script>
export default {
  name: "Profile",
  props: {
    "username": String,
    "lastname": String,
    "email": String,
    "role": String,
    "password": String
  },

  created() {
    
  }
}
</script>


<template>

<!-- por ahora asumimos que nos logueamos un usuario y este mismo ya autenticado desde Login -->
<section>
    <div class="box-info" id="user-box">
      <div id="img-user">
        <img src="http://" alt="User profile" width="300" />
      </div>
      <div id="section-user">
        <p>Nombre: {{ $props.username }}</p>
        <p>Correo: {{ $props.email }}  </p>
        <p>Rol: {{ $props.role }}</p>
      </div>
    </div>
</section>

</template>


<style scoped>

#user-box {
  display: flex;
  justify-content: space-around;
  height: 50%;
}

#user-box div {
  margin-bottom: 0;
}

</style>