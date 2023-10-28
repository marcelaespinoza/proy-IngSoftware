import { createApp } from 'vue'
import App from "./App.vue";
import router from "./routes/index.js";
import './assets/content.css'
import './assets/dashboard.css'
import './assets/sidebar.css'

const app = createApp(App);

app.use(router);
app.mount("#app")