export default {
  namespaced: true,
  state: {
    listTitle: null,
    allVideoList: []
  },
  getters: {
    listTitle (state) {
      return state.listTitle
    },
    allVideoList (state) {
      return state.allVideoList
    }
  },
  mutations: {
    mutationListTitle (state, newValue) {
      state.listTitle = newValue
    },
    mutationAllVideoList (state, newValue) {
      state.allVideoList = newValue
    }
  }
}
