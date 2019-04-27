import Vue from 'vue'
import Router from 'vue-router'
import VideoList from '@/components/VideoList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: VideoList
    },
    {
      path: '/tag',
      name: 'VideoList',
      component: VideoList
    }
  ]
})
