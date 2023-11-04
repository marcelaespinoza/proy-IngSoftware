<script>
import axios from 'axios'

import Aggent from './Aggent.vue'
import puntajes from '../utils/puntajes.json'

export default {
  name: "Dashboard",
  data() {
    return {
      // featureEmotions: JSON.parse(JSON.stringify(puntajes)),
      featureEmotions: axios.get('http://127.0.0.1:5000/api/Nmembers').then(res => res.data),
      
      showAgent: false,
      unDoneCheck: [],
      meanWhileCheck: [],
      DoneCheck: [],

      dominantEmotion: "",
      imageDomEmotion: "",
      
      userToCitar: "",
      emailToCitar: ""
    }
  },
  created() {
      // this.dominantEmotion = "Enojo"
      // this.dominantEmotion = axios.get('http://127.0.0.1:5000/emocion/predominante').then(res => res.data)
      
      axios.get('http://127.0.0.1:5000/emocion/predominante')
      .then(res => {
        this.dominantEmotion = res.data;
        // Aquí puedes realizar cualquier otra operación que necesites con this.dominantEmotion
      })
      .catch(error => {
        console.error('Error al obtener el dato:', error);
      });
      
      console.log(this.dominantEmotion)
      // carga los estados checks de cada miembro por defecto
      for (let i = 0; i < this.featureEmotions.length; i++) {
        this.unDoneCheck[i] = false
        this.meanWhileCheck[i] = this.DoneCheck[i] = false;
      }
  },
  methods: {
    viewAgenda() {
      this.showAgent = !this.showAgent;
    },

    getUserRow(index) {
      const infoUser = this.featureEmotions[index-1]
      this.userToCitar = infoUser.nombre
      this.emailToCitar = infoUser.correo
    },

    tounDoneCheck(index) {
        if (this.unDoneCheck[index]) {
          this.meanWhileCheck[index] = false;
          this.DoneCheck[index] = false;
        }
        const codeuser = this.featureEmotions[index-1].codigo
        // axios.post(`http://127.0.0.1:5000/api/Member/State/${codeuser}/1`) //
      },
      
    toNeanwhileCheck(index) {
      if (this.meanWhileCheck[index]) {
        this.unDoneCheck[index] = false;
        this.DoneCheck[index] = false;
      }
      const codeuser = this.featureEmotions[index-1].codigo
      // axios.post(`http://127.0.0.1:5000/api/Member/State/${codeuser}/2`) //
    },

    toDoneCheck(index) {
      if (this.DoneCheck[index]) {
        this.unDoneCheck[index] = false;
        this.meanWhileCheck[index] = false;
      }
      const codeuser = this.featureEmotions[index-1].codigo
      // axios.post(`http://127.0.0.1:5000/api/Member/State/${codeuser}/3`) //
    },
  },

  mounted() {

  },
  components: { Aggent }
}
</script>

<template>
<section>
  
  <div id="select-emotion-b" class="box-info">

    <div id="pet-select-em"><h4>Selecciona la emoción: </h4></div>
    <div id="form-select-em">
      <form action="#">
        <label for="select-emotion">
          <select name="emotion-active" id="lang">
            <option value="felicidad">Felicidad</option>
            <option value="tristeza">Tristeza</option>
            <option value="estres">Estres</option>
            <option value="enojo">Enojo</option>
            <option value="ansiedad">Ansiedad</option>
            <option value="aburrimiento">Aburrimiento</option>
            <option value="alivio">Alivio</option>
          </select>
        </label>
      </form>
    </div>

  </div>
  

  <div id="section-emotion">

    <div id="dominant-emotion-b" class="box-info">
      <div><h1>Emocion dominante</h1></div>
      <div id="get-dom-image">
          <!-- <h2>{{ dominantEmotion }}</h2> -->
          <img :src="`./public/images/` + dominantEmotion + '.jpg'" :alt="dominantEmotion" width="100">
      </div>  
    </div>
    

    <div id="circular-graph-b">
      
    </div>
    
  </div>
  

  <div id="chart-emotion-area-b">
    
  </div>
  
  <div id="feature-emotion-trend-b" class="box-info">

    <div id="scroll-block">
      <div id="table-box">
        <table id="miembros-table">
        <thead>
            <tr>
              <th>Código</th>
              <th>Nombre</th><th>Área</th>
              <th>Edad</th><th>Puntaje</th>
              <th>Asistencia</th>
            </tr>
        </thead>
        <tbody>
          <!-- Los datos se cargan EN VUE -->
          <tr :id="`row-${index++}`" v-for="(row, index) in featureEmotions" :key="index">
            <td v-for="cell in row">{{ cell }} </td>
            <td id="state-cell">
              <div id="state-check">
                <input type="checkbox" :class="`check-style n-undone`" v-model="unDoneCheck[index]" @change="tounDoneCheck(index)">
                <input type="checkbox" :class="`check-style n-meanwhile`" v-model="meanWhileCheck[index]" @change="toNeanwhileCheck(index)">
                <input type="checkbox" :class="`check-style n-done`" v-model="DoneCheck[index]" @change="toDoneCheck(index)">
              </div>
            </td>
          </tr>
            
          </tbody>
        </table>
      </div>
    
      <div id="agent-button">
        <h5>Citar</h5>
        <ul>
          <li :id="`li-${index-1}`" v-for="index in featureEmotions.length" :key="index">
            <div id="plus-env" @click="{getUserRow(index); viewAgenda()}"><h1>+</h1></div>
          </li>
        </ul>
      </div>

    </div>

  </div>
</section>

<Aggent v-if="showAgent" :username="userToCitar" :email="emailToCitar"/>

</template>

<style scoped>

#get-dom-image {
  width: 100px;
  height: 70px;
  /* border: 1px solid black; */
}

#state-check {
  margin: 20px 23px 0 0;
}

#state-cell {
  display: flex;
  /* align-items: center; */
  width: 80%;
}

.check-style {
    margin-left: 5px;
    cursor: pointer;
}

.n-undone:checked { 
  accent-color: red;
} 

.n-meanwhile:checked { 
    accent-color: yellow; 
} 

.n-done:checked { 
    accent-color: green; 
} 

</style>
