<script>
import loadEmotions from '../utils/emotions'

import members from '../utils/members.json'
import regEmotions from '../utils/regEmotions.json'

export default {
  name: "Dashboard",
  data() {
    return {
      // url: 'https://syy8260zh3.execute-api.us-east-1.amazonaws.com/UTEC/miembros',
      featureEmotions: [],
      members: JSON.parse(JSON.stringify(members)),
      regEmotions: JSON.parse(JSON.stringify(regEmotions)),

      showAgent: false
    }
  },
  created() {

    const sort_codigos = loadEmotions(this.regEmotions);
    
    // const members = axios.get(this.url).then(res => res.data.body)
    sort_codigos.forEach((reg) => {
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
  },
  methods: {
    viewAgenda() {
      this.showAgent = !this.showAgent;
    }
  },
  mounted() {

  }
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
              <th>Anotación</th><th>Código</th>
              <th>Nombre</th><th>Área</th>
              <th>Edad</th><th>Puntaje</th>
              <th>Estado</th>
            </tr>
        </thead>
        <tbody>
          <!-- Los datos se cargan EN VUE -->
          <tr v-for="(row, index) in featureEmotions" :key="index">
            <td> <!-- La anotacion de checks --> </td>
            <td v-for="cell in row">{{ cell }} </td>
            <td>
              <div id="state-check">
                <div class="circulo rojo" @click=""></div>
                <div class="circulo amarillo" @click=""></div>
                <div class="circulo verde" @click=""></div>
              </div>
            </td>
          </tr>
            
          </tbody>
        </table>
      </div>
    
      <div id="agent-button">
        <ul>
          <li v-for="index in featureEmotions.length" :key="index">
            <div id="plus-env" @click="viewAgenda"><h1>+</h1></div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>
</template>

<style scoped>

#state-check {
  margin-top: 30px;
  margin-bottom: 0;
}

 .circulo {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    display: inline-block;
    margin-left: 5px;
    cursor: pointer;
}

.rojo {
    background-color: red;
}

.amarillo {
    background-color: gray;
}

.verde {
    background-color: gray;
}

</style>
