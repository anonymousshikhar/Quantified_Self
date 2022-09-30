<template>
  <footer class="footer bg-dark text-center text-white" style="background-color: rgba(0,0,0,0.1)">
    <!-- Grid container -->
    <div class="container-fluid">
      <!-- Section: Form -->
      <section class="">
        <form action="">
          <!--Grid row-->
          <div class="row d-flex justify-content-center" style="padding:1rem">
            <!--Grid column-->
            <div class="col-auto d-flex align-items-center p-1">
              <p class="pt-2">
                <strong>Sign up for our newsletter</strong>
              </p>
            </div>
            <!--Grid column-->

            <!--Grid column-->
            <div class="col-auto d-flex align-items-center p-1">
              <!-- Email input -->
              <div class="form-outline form-white">
                <input type="email" id="form5Example29" class="form-control" />
              </div>
            </div>
            <!--Grid column-->

            <!--Grid column-->
            <div class="col-auto d-flex align-items-center p-1">
              <!-- Submit button -->
              <button type="submit" class="btn btn-outline-light" @click="logout()">
                Logout
              </button>
            </div>
            <!--Grid column-->
          </div>
          <!--Grid row-->
        </form>
      </section>
      <!-- Section: Form -->
    </div>
    <!-- Grid container -->

    <!-- Copyright -->
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0,0.5)">
      © 2020 Copyright:
      <a class="text-white" href="https://shikhar.com/">Shikhar's personal</a>
    </div>
    <!-- Copyright -->
  </footer>
</template>

<script>
export default {
  name: "Footer",
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push({ name: "Login" });
    },
  },
};
</script>


<style scoped>
.footer{
    position: relative;
    left: 0;
    bottom: 0;
    right: 0;
    color: #fff;
  
}
</style>