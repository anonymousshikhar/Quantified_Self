<template>
  <div
    class="container my-2 py-3"
    style="background-color: rgba(70, 42, 42, 0.9)"
  >
    <div class="row">
      <h2>'The Logit', Welcomes You!</h2>
      <p id="msg">
        The final step! <br />
        Register to the app.
      </p>
    </div>
    <div class="row">
      <div class="row-fluid">
        <input type="text" v-model="name" placeholder="Enter Your Full Name" />
      </div>
      <div class="row-fluid">
        <input type="text" v-model="email" placeholder="Enter Email address" />
      </div>
      <div class="row-fluid">
        <input
          type="password"
          v-model="password"
          placeholder="Create a Password"
        />
      </div>
      <div class="row-fluid">
        <input type="password" placeholder="Rewrite the Password" />
      </div>
      <div class="row-fluid">
        <button
          id="custom_btn"
          type="button"
          @click="register()"
          class="btn btn-dark"
        >
          Register
        </button>
      </div>
    </div>
    <div class="row-fluid">
      <p>
        Already have an account?
        <span><a href="#" @click="statusChange()">Login</a></span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupCard",
  data() {
    return {
      name: "",
      email: "",
      password: "",
      status: true,
    };
  },
  methods: {
    statusChange() {
      console.log("clicked");
      this.$emit("changes", this.status);
      console.log(this.status);
    },

    register() {
      fetch("http://127.0.0.1:5000/api/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: this.name,
          email: this.email,
          pass: this.password,
        }),
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            alert("User Registered");
            this.statusChange();
          } else {
            return res.text().then((text) => {
              throw new Error(text);
            });
          }
        })
        .catch((e) => {
          console.log(e);
          alert(e);
        });
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
