import VNetworkGraph from "v-network-graph"
import "v-network-graph/lib/style.css"
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
const app = createApp(App)

app.use(VNetworkGraph)
app.mount("#app")
