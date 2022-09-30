import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store/index"
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faTrash, faPen, faGear, faUser, faCircleXmark } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faTrash, faPen, faGear, faUser, faCircleXmark)


global.jQuery = require('jquery');
var $ = global.jQuery;
window.$ = $;

createApp(App)
.use(router).use(store)
.component('font-awesome-icon', FontAwesomeIcon)
.mount("#app");
