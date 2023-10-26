import { createApp } from 'vue'
import App from "./App.vue";
import router from "./routes/index.js";
import './assets/content.css'
import './assets/dashboard.css'

const app = createApp(App);
// const cantidadPendientes = 10;
// document.getElementById('contador-pendientes').textContent = cantidadPendientes;

app.use(router);
app.mount("#app")