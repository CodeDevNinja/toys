import Vue from 'vue'
import App from './App.vue'
import VueTouch from 'vue-touch'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Router from 'vue-router'
import FlipScore from './components/FlipScore.vue'
import ba from 'vue-ba'

Vue.config.productionTip = false
Vue.use(VueTouch, {name: 'v-touch'})
Vue.use(ElementUI)
// import './components/FlipScore'
const routes = [
  { path: '/scoreboard', component: FlipScore }
]
// 3. 创建 router 实例，然后传 `routes` 配置
// 你还可以传别的配置参数, 不过先这么简单着吧。
const router = new Router({
  routes // （缩写）相当于 routes: routes
})
Vue.use(ba, {
  siteId: '878ffd1ef97678dcbc41d089b3d428b6'
});
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
