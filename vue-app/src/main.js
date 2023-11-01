import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

const app =createApp(App); // create our app instance


app.use(router); //tel our app to use our route


app.mount('#app');