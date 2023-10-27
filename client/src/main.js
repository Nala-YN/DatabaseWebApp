import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import ElementPlus from "element-plus"
import 'element-plus/dist/index.css'
import VTooltip from 'v-tooltip'
import service from './axios'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.config.globalProperties.$http = service;
app.use(ElementPlus).use(store).use(VTooltip).use(router).mount('#app')
