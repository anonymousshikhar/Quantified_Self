<template>
  <div class="container">
    <img class="logo" src="../assets/icon.png" alt="Logo Here" />
    <h1>Regiter Yourself</h1>
    <div class="register">
      <input type="text" v-model="name" placeholder="Enter Name" />
      <input
        type="email"
        v-model="email"
        placeholder="Enter Email address"
        required
      />
      <input
        type="password"
        v-model="password"
        placeholder="Create a password"
        required
      />
      <input type="password" placeholder="Confirm the password" required />
      <button @click="login()">Register</button>
      <p><router-link to="/"> Login </router-link></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  data: function () {
    return {
      name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    login() {
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
            this.$router.push({ name: "Login" });
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
    if (user) {
      this.$router.push({ name: "Dashboard" });
    }
  },
};
</script>

<style scoped>
.logo {
  width: 150px;
  border-radius: 10%;
}

.register input {
  width: 20rem;
  height: 2rem;
  padding: 0.5rem;
  display: block;
  margin: 1rem auto;
}

.register button {
  width: 21rem;
  height: 2rem;
  background-color: gainsboro;
  padding: 0.5rem 0.5rem;
  color: black;
  border-color: red;
  border-width: thin;
  border-radius: 2rem;
}
.register button:hover {
  cursor: pointer;
}
</style>
