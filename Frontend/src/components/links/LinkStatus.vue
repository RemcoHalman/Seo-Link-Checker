<template>
  <span
    id="status"
    class="w-1/12 px-6 py-1 px-1 text-xs whitespace-no-wrap border-b border-gray-200 font-semibold rounded-full text-center"
    :class="styling"
  >
    <slot></slot>
  </span>
</template>

<script>
export default {
  props: ["styling"],
  data() {
    return {};
  }
};
</script>

<style scoped>
.succes {
  background-color: green;
  color: rgb(196, 250, 196);
}
.warning {
  background-color: orange;
  color: rgb(88, 25, 0);
}
.failure {
  background-color: red;
  color: rgb(0, 0, 0);
}
</style>
