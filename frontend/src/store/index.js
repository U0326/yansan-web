import 'babel-polyfill'
import Vue from 'vue'
import Vuex from 'vuex'

import videoList from '@/store/videoList.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    videoList
  }
})
