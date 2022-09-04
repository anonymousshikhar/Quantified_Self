<template>
  <div
    class="container my-2 py-3"
    style="background-color: rgba(70, 42, 42, 0.9)"
  >
    <div class="row">
      <h2>'The Logit', Welcomes You!</h2>
      <p id="msg">Signin to the app.</p>
    </div>
    <div class="row">
      <div class="row-fluid">
        <input type="text" placeholder="Enter Email address" v-model="email" />
      </div>
      <div class="row-fluid">
        <input type="password" placeholder="Enter Password" v-model="password"/>
      </div>
      <div class="row-fluid">
        <button id="custom_btn" type="button" class="btn btn-dark" @click='login()'>
          Login
        </button>
      </div>
    </div>
    <div class="row-fluid">
      <p>
        Does not have an account?
        <span><a href="#" @click="changeStatus()">Register now</a></span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginCard",
  data() {
    return {
      email: '',
      password: '',
      status: false,
    };
  },
  methods: {
    changeStatus() {
      const values = this.status;
      this.$emit("change", values);
    },
    login() {
      fetch("http://127.0.0.1:5000/api/login_validation", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: this.email, pass: this.password }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            return res.json();
          } else if (res.status == 300) {
            return res.text().then((text) => {
              throw new Error(text);
            });
          } else if (res.status == 301) {
            return res.text().then((text) => {
              throw new Error(text);
            });
          }
        })
        .then((jsonobj) => {
          localStorage.setItem("user-info", JSON.stringify(jsonobj));
          this.$router.push({ name: "Dashboard" });
        })
        .catch((e) => alert(e));
    },
  },
};
</script>

<style scoped>
h2 {
  font-family: Cinzel;
  color: antiquewhite;
}
#msg {
  font-family: Montserrat;
  font: 700;
  font-size: 1.5rem;
}
input {
  background-color: transparent;
  margin: 1rem;
  padding: 0.6rem 0.5rem;
  border: 0.1rem solid white;
  border-radius: 1rem;
  color: aliceblue;
}

#custom_btn {
  background: transparent;
  border: 0.1rem solid white;
  margin: 1rem;
}

#custom_btn:hover {
  background: rgba(0, 0, 0, 0.7);
  font-size: bold;
}
</style>
