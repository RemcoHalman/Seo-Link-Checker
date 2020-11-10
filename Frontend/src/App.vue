<template>
  <div>
    <TheHeader />
    <LinkInput />
    <TheFooter />
  </div>
</template>

<script>
import TheHeader from "./components/layout/TheHeader.vue";
import TheFooter from "./components/layout/TheFooter.vue";
import LinkInput from "./components/LinkInput.vue";

export default {
  name: "App",
  title: "Link Status Checker",
  components: {
    TheHeader,
    TheFooter,
    LinkInput,
  },
};
</script>

<style></style>
