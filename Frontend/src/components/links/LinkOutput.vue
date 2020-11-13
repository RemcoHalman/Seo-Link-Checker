<template>
  <div class="flex w-full items-center border-b">
    <link-name>Link name</link-name>
    <link-status styling="failure">Test</link-status>
  </div>
</template>

<script>
import LinkStatus from "./LinkStatus.vue";
import LinkName from "./LinkName.vue";

export default {
  name: "LinkOutput",
  components: {
    LinkStatus,
    LinkName
  }
};
</script>

<style></style>
