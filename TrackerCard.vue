<template>
  <div class="card text-white bg-primary mb-3" style="width: 18rem; box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, 0.2)">
    <div class="card-header">
      <h5>Tracker Id: {{ tracker_id }}</h5>
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ tracker_name }}</h5>
      <p class="card-text">{{ tracker_desc }}</p>
    </div>
    <div class="custom card-footer">
      <button class="btn btn-thin " @click="get_tracker_details()" style="font-size:0.8rem">
        Details
      </button>

      <button class="btn btn-thin" @click="get_tracker_setting()">

        <font-awesome-icon icon="fa-solid fa-gear" />
      </button>
    </div>
  </div>
</template>

<script>

export default {
  name: "TrackerCard",
  props: ["tracker_name", "tracker_desc", "tracker_id", "tracker_pri_question"],
  data() {
    return {
      tracker_logs: [],
    };
  },
  methods: {
    get_tracker_details() {
      this.$store.commit('setIsSettingOpened', false)
      console.log(this.tracker_id);
      fetch(
        "http://127.0.0.1:5000/api/tracker_data?tid=" + String(this.tracker_id)
      )
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          this.tracker_logs = data;
          console.log(this.tracker_logs);
          this.$store.commit('getTrackerdetails', this.tracker_pri_question)

          this.$emit("tracker_logs", this.tracker_logs);
        });
    },

    get_tracker_setting() {
      console.log("inside get_tracker_setting");
      console.log(this.$store.state.isSettingOpened, this.tracker_id);
      this.$store.commit('setIsSettingOpened', true)
      this.$store.commit('getTrackerdetails', {'tid':this.tracker_id, 'tname':this.tracker_name, 'tdesc': this.tracker_desc, 'tques': this.tracker_pri_question})
      console.log(this.$store.state.isSettingOpened, this.tracker_id);

    },
  },
};
</script>

<style scoped>
*{
  font: 0.8rem;
}
.bg-primary{
  background: rgb(101,121,155);
background: linear-gradient(90deg, rgba(101,121,155,1) 0%, rgba(94,37,99,1) 100%);
}
.custom {
  display: flex;
  justify-content: space-between;
}
h5{
  font-size: 0.8rem;
}
</style>
