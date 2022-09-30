<template>
  <div class="container-fluid g-0">
    <div class="main_section">
      <div
        class="row no-gutters d-flex justify-content-between"
        style="position: relative"
      >
        <div class="custom col">
          <div class="row g-0 justify-content-center">
            <img class="logo" src="../assets/infinity.png" alt="Logo Here" />
          </div>
          <div class="row justify-content-center">
            <div class="app_name">
              <h1>The <span id="logit">Logit.</span></h1>
            </div>
            <div class="desc" style="margin: 1rem; padding: 2rem">
              <h2 style="color: #501b1d; text-shadow: 2px 2px 2px#64485c">
                A Quantified Self App
              </h2>
              <p class="lineUp">
                This is a tracking application to keep a record of all the
                activities of an individual.<br />
                It helps you keep yourself forward without missing any deadline.
              </p>
            </div>

            <h2
              style="font-family: Cinzel; color: #501b1d; padding-bottom: 1rem"
            >
              You Need It. We Keep It.
            </h2>
          </div>
        </div>
        <div class="col d-flex align-items-center">
          <div class="login_form">
            <LoginCard @change="updateStatus" v-if="status" />
            <SignupCard @changes="updateStatus" v-if="!status" />
          </div>
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer"
import LoginCard from "@/components/LoginCard";
import SignupCard from "@/components/SignupCard";

export default {
  name: "Login",
  components: {
    Footer,
    LoginCard,
    SignupCard
  },
  data() {
    return {
      email: "",
      password: "",
      status:true,
    };
  },
  methods: {
    updateStatus(value){
      console.log(value)
      this.status = value;
      console.log(this.status)
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
.app_name {
  position: relative;
  width: 20rem;
  border-radius: 3rem;
  background-color: rgba(0, 0, 0, 1);
}
#logit {
  padding: 0.2rem 0.3rem;
  background-color: #dddfd4;
  color: black;
  font-family: rock salt;
}

.main_section {
  background: url("@/assets/bg.jpg") no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;

  overflow-y: scroll;
  scrollbar-width: none;
  -ms-overflow-style: none;

  min-height: 70vh;
  min-height: -webkit-calc(100vh - 10.5rem);
  min-height: -moz-calc(100vh - 10.5rem);
  min-height: calc(100vh - 10.5rem);
}

.main_section::-webkit-scrollbar {
  width: 0;
  height: 0;
}

h1 {
  font-family: "Cinzel";
  font-size: bold;
  color: rgba(165, 42, 42, 0.8);
}
.lineUp {
  animation: 3s anim-lineUp ease-out;
  color: #34421e;
  padding: 0.5rem 1rem;
  font-family: monospace;
}
@keyframes anim-lineUp {
  0% {
    opacity: 0;
    transform: translateY(80%);
  }
  20% {
    opacity: 0;
  }
  50% {
    opacity: 1;
    transform: translateY(0%);
  }
  100% {
    opacity: 1;
    transform: translateY(0%);
  }
}

h2,
p {
  font-family: "Monteserrat";
  font: 700;
}
.logo {
  max-width: 100%;
  max-height: 100%;
  display: block;
  width: 15rem;
}

.login_form {
  /* background: rgba(165, 42, 42, 0.8); */
  margin: 2rem 5rem;
  /* border-radius: 10rem; */
}

.custom {
  background: rgba(165, 42, 42, 0.17);
}
</style>
