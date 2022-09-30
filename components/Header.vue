<template>
  <header class="nav">
    <div class="logo">
      <img src="@/assets/nav_logo.png" alt="" />

    </div>
    <div class="howdy">
      <span style="font-family:Homemade Apple; color: rgba(208, 218,127, 0.8)">Howdy, </span>
      <span style="font-family:Cinzel">{{user_name}}!</span>
    </div>
    <div class="links">
      <ul class="link_items">
        <a><li>Trackers</li></a>
        <a @click="signout()"><li>Signout</li></a>
        <a><li><font-awesome-icon icon="fa-solid fa-user" /></li></a>
      </ul>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
  props: ["user_name"],

  methods: {
    signout() {
      localStorage.clear();
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

<style scoped>
header {
  background: rgb(101,121,155);
background: linear-gradient(90deg, rgba(101,121,155,1) 0%, rgba(94,37,99,0.7959558823529411) 100%);
  box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.2);
  /* background: transparent; */
  /* margin: 0.2rem 0.2rem; */
}
.nav {
  display: flex;

  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 2rem;
  /* border-radius: 1rem; */
}

.howdy{
  font-size: 1.5rem;
}
.logo {
  max-width: 100%;
  max-height: 100%;
  display: block;
}

.links {
  display: flex;
  justify-content: space-evenly;
}
.link_items {
  display: flex;
  list-style: none;
  gap: 1em 1em;
  justify-items: space-between;
  flex-direction: row;
  align-items: center;
}
li {
  color: antiquewhite;
  padding: 0 1rem;
  font-size: 1rem;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
}
li:hover {
  background: rgb(2, 0, 36);
  background: linear-gradient(
    90deg,
    rgba(2, 0, 36, 1) 0%,
    rgba(9, 9, 121, 1) 35%,
    rgba(0, 212, 255, 1) 100%
  );
  cursor: pointer;
  border-radius: 2rem;
}
img {
  width: 8rem;
}
</style>
