import { createApp } from 'vue'
import App from "./App.vue";
import router from "./routes/index.js";
import './assets/content.css'
import './assets/dashboard.css'

const app = createApp(App);

const window = document.getElementById('ventanaCita');
const iconoCampana = document.getElementById('icono-campana');
const closewindowButton = document.getElementById('closewindow');
const miembrosPendientes = document.getElementById('miembrosPendientes');

function abrirVentana(citasPendientes) {
  miembrosPendientes.innerHTML = '';
  citasPendientes.forEach((cita) => {
    const li = document.createElement('li');
    li.textContent = cita;
    miembrosPendientes.appendChild(li);
  });

  window.style.display = 'block';
}

function cerrarwindow() {
    window.style.display = 'none';
}

iconoCampana.addEventListener('click', abrirVentana);
closewindowButton.addEventListener('click', cerrarwindow);

const citasPendientes = ["Margiory", "Marcela", "Milloshy", "Fabiola", "Adrian"]; //aqui se reemplazaría con la data que tengamos
abrirVentana(citasPendientes);


app.use(router);
app.mount("#app")