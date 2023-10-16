import { createStore } from 'vuex'

export default createStore({
  namespace:true,
  //loginData拥有参数：
  //username:string;userid:int
  state: {
    userInfo: localStorage.getItem('loginData') && JSON.parse(localStorage.getItem('loginData'))
  },
  getters: {
    //第一个参数必须是state
    status(state){
      return state.userInfo;
    }
  },
  mutations: {
    //
    setStatus(state,userInfo){
      state.userInfo=userInfo;
    },
  },
  actions: {
  },
  modules: {
  }
})
