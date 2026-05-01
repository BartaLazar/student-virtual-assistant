import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
//import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
//import 'bootstrap-vue/dist/bootstrap-vue.css';

import { library } from "@fortawesome/fontawesome-svg-core";
import { faCalendarDays } from '@fortawesome/free-solid-svg-icons';
import { faListCheck} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { ModelListSelect } from 'vue-search-select';
import RadialProgressBar from "vue3-radial-progress";



library.add(faCalendarDays,faListCheck);

import Select2 from 'vue3-select2-component';


createApp(App).component("font-awesome-icon", FontAwesomeIcon).use(RadialProgressBar).use(store).component('Select2', Select2).use(router).mount('#app')
