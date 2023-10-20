import { createStore } from 'vuex'

export default createStore({
  state: {
    selectedKeys: ['']
  },
  getters: {
  },
  mutations: {
    changeSelectedKeys (state, key) {
      state.selectedKeys = [key]
    }
  },
  actions: {
  },
  modules: {
  }
})
