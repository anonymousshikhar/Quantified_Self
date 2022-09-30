import { createStore } from "vuex";

export default createStore({
  state:{
    isSettingOpened: false,
    isDetailsOpened: false,
    trackerId: '',
    tracker_name: '',
    tracker_desc: '',
    tracker_pri_question: ''
  },
  mutations: {
    setIsSettingOpened(state, value){
      state.isSettingOpened = value
    },
    setIsDetailsOpened(state, value){
      state.isDetailsOpened = value
    },
    getTrackerdetails(state, value){
      state.trackerId = value.tid
      state.tracker_name = value.tname
      state.tracker_desc = value.tdesc
      state.tracker_pri_question = value.tques
    },
    getTrackerQues(state, value){
      state.tracker_pri_question = value
    }
  }
})