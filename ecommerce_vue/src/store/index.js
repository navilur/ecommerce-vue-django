import { createStore } from "vuex";

export default createStore({
  state: {
    cart: {
      item: [],
    },
    isAuthentication: false,
    token: "",
    isLoading: false,
  },
  mutations: {},
  actions: {},
  modules: {},
});
