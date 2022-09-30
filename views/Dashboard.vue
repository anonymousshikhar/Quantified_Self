<template>
  <div class="main-container">
    <div class="header">
      <Header :user_name="user_name" />
    </div>

    <div v-if="!$store.state.isDetailsOpened" class="main_section">
      <Welcome />
    </div>

    <div v-if="!$store.state.isSettingOpened && $store.state.isDetailsOpened" class="main_section">
      <div class="log_area">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Tracker ID</th>
              <th scope="col">Timestamp</th>
              <th scope="col">Tracker value</th>
              <th scope="col">Note</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in tracker_details" :key="row.id">
              <td>{{ row.tid }}</td>
              <td>{{ row.timestamp }}</td>
              <td>{{ row.value }}</td>
              <td>{{ row.remark }}</td>
              <td>
                <button
                  class="btn btn-thin"
                  @click="edit(row.vid)"
                  data-bs-toggle="modal"
                  data-bs-target="#trackerLog"
                >
                  <font-awesome-icon icon="fa-solid fa-pen" />
                </button>
              </td>
              <td>
                <button class="btn btn-thin" @click="del(row.vid)">
                  <font-awesome-icon icon="fa-solid fa-trash" />
                </button>
              </td>
            </tr>
            <tr>
              <!-- Button trigger modal for logging data -->
              <td colspan="3">
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-toggle="modal"
                  data-bs-target="#trackerLog"
                  @click="updateData = false"
                >
                  Log new records
                </button>
              </td>
              <td>
                <button
                  type="button"
                  class="btn btn-secondary"
                  @click="export_excel()"
                >
                  Export CSV
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Button trigger modal for logging data -->
        <!-- <button
          type="button"
          class="btn btn-primary"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal"
        >
          Add Tracker +
        </button> -->

        <!-- Modal for logging data -->
        <div
          class="modal fade"
          id="trackerLog"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div
            class="modal-dialog modal-dialog-centered modal-dialog-scrollable"
          >
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Log Details</h5>
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <!-- Numerical modal body starts -->
              <div class="modal-body" v-if="this.ttype == 'Numerical'">
                <form>
                  <div class="form-group py-2">
                    <input
                      type="text"
                      class="form-control"
                      id="TrackerValue"
                      placeholder="Enter the value to log"
                      v-model="log_value"
                    />
                  </div>
                  <div class="form-group py-2">
                    <textarea
                      type="text"
                      class="form-control"
                      id="TrackerNote"
                      placeholder="Enter some note"
                      v-model="log_note"
                    />
                  </div>
                </form>
              </div>
              <!-- Numerical modal body ends -->

              <!-- Boolean modal body starts -->
              <div class="modal-body" v-else-if="this.ttype == 'Boolean'">
                <form>
                  <div class="form-group py-2">
                    <blockquote>
                      Primary Question: {{ $store.state.tracker_pri_question }}
                    </blockquote>
                    <hr />
                    <br />
                    <input
                      type="radio"
                      name="booleanyes"
                      value="1"
                      v-model="log_value"
                      style="padding: 1rem 2rem"
                    />

                    <label for="booleanyes" style="padding: 0 0.5rem"
                      >Yes</label
                    >
                    <input
                      type="radio"
                      name="booleanno"
                      value="0"
                      v-model="log_value"
                      style="padding: 1rem 2rem"
                    />
                    <label for="booleanno" style="padding: 0 0.5rem">No</label>
                  </div>
                  <div class="form-group py-2">
                    <textarea
                      type="text"
                      class="form-control"
                      id="TrackerNote"
                      placeholder="Enter some note"
                      v-model="log_note"
                    />
                  </div>
                </form>
              </div>
              <!-- Boolean modal body ends -->


              <!-- Time Duration modal starts -->
              <div class="modal-body" v-else-if="this.ttype == 'Time Duration'">
                <form>
                  <div class="form-group py-2">
                    <blockquote>
                      Primary Question: {{ $store.state.tracker_pri_question }}
                    </blockquote>
                    <hr />
                    <br />
                    <input
                      type="datetime-local"
                      name="datetime"
                      v-model="log_value"
                      style="padding: 1rem 2rem"
                    />
                  </div>
                  <div class="form-group py-2">
                    <textarea
                      type="text"
                      class="form-control"
                      id="TrackerNote"
                      placeholder="Enter some note"
                      v-model="log_note"
                    />
                  </div>
                </form>
              </div>
              <!-- Time Duration modal ends -->

              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-danger"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button
                  v-if="!updateData"
                  type="button"
                  class="btn btn-primary"
                  @click="logit()"
                >
                  Logit.
                </button>

                <button
                  v-if="updateData"
                  type="button"
                  class="btn btn-primary"
                  @click="update()"
                >
                  Update.
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="chart_area">
        <div class="chart1">
          <TrendLine
            v-if="chartStatus"
            :cdata="chartData"
            :options="{ responsive: true }"
            :chartStatus="chartStatus"
          />
        </div>
        <!-- 
        <div class="chart3">
          Chart 3 Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Ipsum, repellendus.
        </div> -->
      </div>
    </div>

    <div
      v-if="$store.state.isSettingOpened"
      class="main_section"
      id="tracker_setting"
    >
      <TrackerSetting :tid="$store.state.trackerId" />
    </div>

    <div class="tracker_list">
      <div v-for="tracker in tracker_list" :key="tracker.tracker_id">
        <TrackerCard
          :tracker_name="tracker.tracker_name"
          :tracker_desc="tracker.tracker_desc"
          :tracker_id="tracker.tracker_id"
          :tracker_pri_question="tracker.tracker_pri_question"
          @tracker_logs="tracker_log_details($event)"
        />
      </div>

      <!-- Button trigger modal for adding tracker -->
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#addTracker"
      >
        Add Tracker +
      </button>

      <!-- Modal for adding tracker-->
      <div
        class="modal fade"
        id="addTracker"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Add Tracker</h5>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group py-2">
                  <input
                    type="text"
                    class="form-control"
                    id="TrackerName"
                    placeholder="Tracker Name"
                    v-model="tracker_name"
                  />
                </div>
                <div class="form-group py-2">
                  <input
                    type="text"
                    class="form-control"
                    id="TrackerDescription"
                    placeholder="Tracker Description"
                    v-model="tracker_desc"
                  />
                </div>
                <div class="form-group py-2">
                  <input
                    type="text"
                    class="form-control"
                    id="TrackerPrimaryQuestion"
                    placeholder="Enter Tracker Primary Question"
                    v-model="tracker_question"
                  />
                </div>
                <div class="form-group py-2">
                  <select
                    id="inputType"
                    class="form-control"
                    v-model="tracker_type"
                  >
                    <option disabled value="">Choose Tracker Type</option>
                    <option>Numerical</option>
                    <option>Multiple Choice</option>
                    <option>Time Duration</option>
                    <option>Boolean</option>
                  </select>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-danger"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button
                type="button"
                class="btn btn-primary"
                @click="addTracker()"
                style="font-size: 0.8rem"
              >
                Add Tracker
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <Footer />
    </div>
  </div>
</template>

<script>
import exportFromJSON from "export-from-json";

import Footer from "@/components/Footer";
import Header from "@/components/Header";
import TrackerCard from "@/components/TrackerCard";
import TrendLine from "@/components/TrendLine";
import TrackerSetting from "@/components/TrackerSetting";
import Welcome from "@/components/Welcome"
export default {
  name: "Dashboard",
  components: {
    Footer,
    Header,
    TrackerCard,
    TrendLine,
    TrackerSetting,
    Welcome
  },
  data() {
    return {
      editId: "",
      chartData: {},
      updateData: false,
      chartStatus: false,
      chartlabels: [],
      tracker_name: "",
      tracker_desc: "",
      tracker_type: "",
      tracker_list: [],
      tracker_details: "",
      tracker_value_list: [],
      tracker_question: "",
      log_value: "",
      log_note: "",
      ttype: "",
      user_id: "",
      user_name: "",
    };
  },
  methods: {
    export_excel() {
      const data = this.tracker_details;
      const fileName = "details";
      const exportType = exportFromJSON.types.csv;

      if (data) exportFromJSON({ data, fileName, exportType });
    },

    edit(id) {
      console.log(id);
      this.editId = id;
      fetch(`http://127.0.0.1:5000/api/tracker_data_by_id?id=${id}`)
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          this.log_value = data.log_value;
          this.log_note = data.log_note;
          this.updateData = true;
        });
    },

    del(id) {
      alert("Are you sure?");
      fetch(`http://127.0.0.1:5000/api/tracker_data_by_id?id=${id}`, {
        method: "DELETE",
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Data Deleted Successfully");
          }
          return res.text();
        })
        .then((text) => {
          throw new Error(text);
        })
        .catch((e) => {
          console.log(e);
          alert(e);
        });
    },

    update() {
      console.log(this.log_value, this.log_note, this.editId);
      fetch(`http://127.0.0.1:5000/api/tracker_data_by_id?id=${this.editId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          log_id: this.editId,
          log_value: this.log_value,
          log_note: this.log_note,
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Data Updated Successfully");
          }
          return res.text();
        })
        .then((text) => {
          throw new Error(text);
        })
        .catch((e) => {
          console.log(e);
          alert(e);
        });
    },

    logit() {
      this.updateData = false;
      console.log(this.tracker_details[0]);
      fetch("http://127.0.0.1:5000/api/tracker_data", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          tracker_id: this.tracker_details[0].tid,
          log_value: this.log_value,
          log_note: this.log_note,
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Data Logged Successfully");
          }
          return res.text();
        })
        .then((text) => {
          throw new Error(text);
        })
        .catch((e) => {
          console.log(e);
          alert(e);
        });
    },

    tracker_log_details(log_array) {
      console.log(this.tracker_details);
      this.tracker_details = "";
      this.tracker_value_list = [];
      this.chartlabels = [];
      this.tracker_details = log_array;
      console.log(this.tracker_details);
      this.ttype = this.tracker_details[0].ttype;
      for (let i = 0; i < this.tracker_details.length; i++) {
        this.tracker_value_list.push(parseFloat(this.tracker_details[i].value));
        this.chartlabels.push(
          new Date(this.tracker_details[i].timestamp).toLocaleDateString()
        );
      }
      // this.tracker_value_list = {'data' : this.tracker_value_list} ;
      this.chartStatus = true;
      (this.chartData["cdata"] = this.tracker_value_list),
        (this.chartData["labels"] = this.chartlabels);
      console.log(this.chartData);
    },

    async get_trackerlist(id) {
      await fetch("http://127.0.0.1:5000/api/trackerlist?uid=" + String(id))
        .then((res) => res.json())
        .then((data) => (this.tracker_list = data));
    },

    addTracker() {
      fetch("http://127.0.0.1:5000/api/trackerlist", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_info: JSON.parse(localStorage.getItem("user-info")),
          tracker_name: this.tracker_name,
          tracker_desc: this.tracker_desc,
          tracker_pri_question: this.tracker_question,
          tracker_type: this.tracker_type,
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Tracker Added Successfully");
          }
          return res.text();
        })
        .then((text) => {
          throw new Error(text);
        })
        .catch((e) => {
          console.log(e);
          alert(e);
        });
    },
  },
  mounted() {
    let user = localStorage.getItem("user-info");
    if (!user) {
      this.$router.push({ name: "Login" });
    } else {
      this.user_id = JSON.parse(localStorage.getItem("user-info")).user_id;
      this.user_name = JSON.parse(localStorage.getItem("user-info")).user_name;
      this.get_trackerlist(this.user_id);
    }
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  color: black;
  font-size: 0.8rem;
}
/* .main-container > :nth-child(odd){
  background:#ddd;
} */

.main-container {
  height: auto;
  display: grid;
  grid-gap: 0.4em;
  grid-template-columns: repeat(4, 1fr);
  /* grid-template-rows: 1fr 3fr 3fr 2fr; */
  grid-auto-rows: auto;
  background-image: url("@/assets/dashboard_bg.jpg");
  grid-template-areas:
    "header header header header"
    "tracker_list main_section main_section main_section"
    "tracker_list main_section main_section main_section"
    "footer footer footer footer";
}

.header {
  grid-area: header;
  display: flex;
}

.main_section {
  background: rgba(0, 0, 111, 0.2);
  grid-area: main_section;
  /* grid-auto-rows: auto; */
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-areas:
    "a a a"
    "b b b";
  border-radius: 0.8rem;
  box-shadow: 1px 2px 2px rgba(0, 0, 111, 0.2);
  margin-right: 1.5rem;
}
.log_area {
  grid-area: a;
  padding: 1rem 1.2rem;
}
.chart_area {
  grid-area: b;
  display: flex;
  flex-direction: row;
  padding: 1rem 1.2rem;
}

.tracker_list {
  padding: 1rem;
  grid-area: tracker_list;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 1rem;
}

.tracker_info {
  background: red;
}

#tracker_setting {
  display: flex;
  height: auto;
  width: auto;
  justify-content: center;
  align-items: center;
}

.footer {
  grid-area: footer;
}
</style>
