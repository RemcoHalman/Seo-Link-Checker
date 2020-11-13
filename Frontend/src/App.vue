<template>
  <the-header>Search and display</the-header>
  <the-input></the-input>
  <the-footer></the-footer>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import TheFooter from "./components/layout/TheFooter.vue";
import TheInput from "./components/links/TheInput.vue";

export default {
  name: "App",
  title: "Link Status Checker",
  components: {
    TheHeader,
    TheFooter,
    TheInput
  }
};
</script>

<style></style>
