<template>
  <div class="container">
    <div class="setting_header">
      <h1>Tracker Setting</h1>
      <p>{{ tid }}</p>
      <hr />
      <div class="details">
        <p><b>TRACKER NAME:</b> {{ $store.state.tracker_name }}</p>
        <p><b>TRACKER DESCRIPTION:</b> {{ $store.state.tracker_desc }}</p>
        <p>
          <b>TRACKER PRIMARY QUESTION:</b> {{ $store.state.tracker_pri_question }}
          <button
            id="change_ques_btn"
            class="btn btn-secondary"
            data-bs-toggle="modal"
            data-bs-target="#updateTrackerQues"
          >
            Change
          </button>
        </p>
      </div>
    </div>

    <!-- Modal for changing tracker question-->
    <div
      class="modal fade"
      id="updateTrackerQues"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Update Tracker Primary Question
            </h5>
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
                  id="TrackerQuestion"
                  placeholder="Enter Primary question for tracker"
                  v-model="tracker_question"
                />
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
              @click="update_ques()"
              style="font-size: 0.8rem"
            >
              Update
            </button>
          </div>
        </div>
      </div>
    </div>

    <button
      class="btn btn-danger"
      data-bs-toggle="modal"
      data-bs-target="#delModal"
      @click="setModalShow()"
    >
      Delete Tracker
    </button>

    <!-- Modal HTML -->
    <div id="delModal" class="modal fade">
      <div class="modal-dialog modal-confirm">
        <div class="modal-content">
          <div class="modal-header flex-column">
            <div class="icon-box">
              <p>X</p>
            </div>
            <h4 class="modal-title w-100">Are you sure?</h4>
            <button
              type="button"
              class="close"
              data-bs-dismiss="modal"
              aria-hidden="true"
            >
              <font-awesome-icon icon="fa-solid fa-circle-xmark" />
            </button>
          </div>
          <div class="modal-body">
            <p>
              Do you really want to delete this tracker? This process cannot be
              undone.
            </p>
          </div>
          <div class="modal-footer justify-content-center">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Cancel
            </button>
            <button type="button" class="btn btn-danger" @click="del_tracker()">
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "TrackerSetting",
  components: ["TrackerSetting"],
  props: ["tid"],
  data() {
    return {
      count: 0,
      question: [],
      questions_list: [],
      isEmpty: false,
      time: "",
      tracker_question:''
  }
  },
  methods: {

    update_ques(){
      console.log("CLICKED")
      fetch(`http://127.0.0.1:5000/api/tracker_data?id=${this.tid}`,{
      method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          tid: this.tid,
          tques: this.tracker_question
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Data Updated Successfully");
          }

    })
    },
    del_tracker(){
      console.log("DELETE CLICKED")
      fetch("http://127.0.0.1:5000/api/tracker_update?id="+ String(this.tid),{
        method:"DELETE"
      })
      .then((res) => {
        if (res.status == 200){
          alert("Tracker Deleted Successfully")
          window.location.reload()
        }
        return res.text();
      })
      .then((text) => {
        throw new Error(text);
      })
      .catch((e)=>{
        alert(e)
      });
      
      },

    add_questions() {
      console.log(this.question);
      if (!this.checkEmpty()) {
        console.log("Before:", this.questions_list, this.question);

        this.questions_list.push(this.question[this.question.length - 1]);
        this.count++;
        console.log("After:", this.questions_list);
      }
    },

    commit_questions() {
      this.questions_list.push(this.question[this.question.length - 1]);
      fetch("http://127.0.0.1:5000/api/tracker_update", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          tid: this.tid,
          questions: this.questions_list,
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Question Added Successfully");
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

    checkEmpty() {
      if (this.question.length === this.questions_list.length) {
        return true;
      }
    },

    set_time() {
      console.log(this.time);
      fetch("http://127.0.0.1:5000/api/daily_report", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          time: this.time,
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("Timer Added Successfully");
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
      this.time = "";
    },
  },
};
</script>

<style scoped>
* {
  font-size: 0.9rem;
}
h1 {
  font-family: Cinzel;
  font-size: 1.5rem;

}

#change_ques_btn{
  margin-left: .6rem;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}

.container {
  display: flex;
  height: auto;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
}

form {
  min-width: 100%;
}
.form-group {
  display: flex;
  gap: 1rem;
  width: auto;
}
.timer {
  display: flex;
  gap: 1rem;
}

/* MODAL CSS */

.modal-confirm {
  color: #636363;
  width: 400px;
}
.modal-confirm .modal-content {
  padding: 20px;
  border-radius: 5px;
  border: none;
  text-align: center;
  font-size: 14px;
}
.modal-confirm .modal-header {
  border-bottom: none;
  position: relative;
}
.modal-confirm h4 {
  text-align: center;
  font-size: 26px;
  margin: 30px 0 -10px;
}
.modal-confirm .close {
  position: absolute;
  top: -5px;
  right: -2px;
  border: 0;
  background: transparent;
}
.modal-confirm .modal-body {
  color: #999;
}
.modal-confirm .modal-footer {
  border: none;
  text-align: center;
  border-radius: 5px;
  font-size: 13px;
  padding: 10px 15px 25px;
}
.modal-confirm .modal-footer a {
  color: #999;
}
.modal-confirm .icon-box {
  width: 80px;
  height: 80px;
  margin: 0 auto;
  border-radius: 50%;
  z-index: 9;
  text-align: center;
  border: 3px solid #f15e5e;
}
.modal-confirm .icon-box p {
  color: #f15e5e;
  font-size: 46px;
  font: bold;
  display: inline-block;
}
.modal-confirm .btn,
.modal-confirm .btn:active {
  color: #fff;
  border-radius: 4px;
  background: #60c7c1;
  text-decoration: none;
  transition: all 0.4s;
  line-height: normal;
  min-width: 120px;
  border: none;
  min-height: 40px;
  border-radius: 3px;
  margin: 0 5px;
}
.modal-confirm .btn-secondary {
  background: #c1c1c1;
}
.modal-confirm .btn-secondary:hover,
.modal-confirm .btn-secondary:focus {
  background: #a8a8a8;
}
.modal-confirm .btn-danger {
  background: #f15e5e;
}
.modal-confirm .btn-danger:hover,
.modal-confirm .btn-danger:focus {
  background: #ee3535;
}
</style>
