<template>
  <Header />
  <LinkInput />
  <Footer />
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import LinkInput from "./components/LinkInput.vue";

export default {
  name: "App",
  title: "Link Status Checker",
  components: {
    Header,
    Footer,
    LinkInput,
  },
};
</script>

<style></style>
