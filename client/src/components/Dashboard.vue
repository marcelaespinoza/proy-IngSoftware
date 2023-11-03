<script>
import Aggent from './Aggent.vue'

import loadEmotions from '../utils/emotions'
import members from '../utils/members.json'
import regEmotions from '../utils/regEmotions.json'

export default {
  name: "Dashboard",
  data() {
    return {
      // url: 'https://syy8260zh3.execute-api.us-east-1.amazonaws.com/UTEC/miembros',
      members: JSON.parse(JSON.stringify(members)),
      // member: {}
      regEmotions: JSON.parse(JSON.stringify(regEmotions)),

      sort_codigos: [],
      featureEmotions: [],
      
      showAgent: false,
      unDoneCheck: [],
      meanWhileCheck: [],
      DoneCheck: [],

      userToCitar: "",
      emailToCitar: ""
    }
  },
  created() {

      // members = axios.get(this.url).then(res => res.data.body)
    this.sort_codigos = loadEmotions(this.regEmotions);
    
    this.sort_codigos.forEach((reg) => {
        const val = this.members.find(member => member.id.toString() === reg[0])
        if (val) {
          let resultado = {
            "codigo": reg[0],
            "nombre": val.nombre,
            "area": val.area,
            "edad": val.edad,
            "puntaje": reg[1],
          }
          this.featureEmotions.push(resultado);
        }
      })

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
      const infoUser = this.sort_codigos[index-1]
      const UserData = this.members.find(member => member.id.toString() === infoUser[0])
      this.userToCitar = UserData.nombre
      this.emailToCitar = UserData.correo
      console.log(this.userToCitar, this.emailToCitar)
    },

    tounDoneCheck(index) {
        if (this.unDoneCheck[index]) {
          this.meanWhileCheck[index] = false;
          this.DoneCheck[index] = false;
        }
      },
    toNeanwhileCheck(index) {
      if (this.meanWhileCheck[index]) {
        this.unDoneCheck[index] = false;
        this.DoneCheck[index] = false;
      }
    },
    toDoneCheck(index) {
      if (this.DoneCheck[index]) {
        this.unDoneCheck[index] = false;
        this.meanWhileCheck[index] = false;
      }
    }
  },
  mounted() {

  },
  components: { Aggent }
}
</script>

<template>
<section>
  
  <div id="select-emotion-b">

  </div>
  
  <div id="section-emotion">
    <div id="dominant-emotion-b">
      
    </div>
    
    <div id="circular-graph-b">
      
    </div>
    
  </div>
  
  <div id="chart-emotion-area-b">
    
  </div>
  
  <div id="feature-emotion-trend-b">
    <div id="scroll-block">
      <div id="table-box">
        <table id="miembros-table">
        <thead>
            <tr>
              <th>Código</th>
              <th>Nombre</th><th>Área</th>
              <th>Edad</th><th>Puntaje</th>
              <th>Estado</th>
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

#state-check {
  margin-top: 20px;
  margin-bottom: 14px;
}

#state-cell {
  display: flex;
  align-items: center;
  width: 60%;
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
