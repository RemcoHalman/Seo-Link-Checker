<template>
  <div class="flex w-full items-center border-b">
    <link-name>{{ name }}</link-name>
    <link-status :styling="styling">{{ status }}</link-status>
  </div>
</template>

<script>
import LinkStatus from "./LinkStatus.vue";
import LinkName from "./LinkName.vue";

export default {
  props: ["name", "status", "styling"],
  name: "LinkOutput",
  components: {
    LinkStatus,
    LinkName
  }
};
</script>

<style></style>
