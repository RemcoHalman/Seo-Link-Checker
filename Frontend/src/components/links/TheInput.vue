<template>
  <main>
    <div class="flex bg-gray-200">
      <div class="flex-1 flex flex-col overflow-hidden">
        <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200">
          <div class="container mx-auto px-6 py-8">
            <div class="flex flex-wrap">
              <link-form></link-form>
            </div>
          </div>
        </main>
      </div>
    </div>
  </main>
</template>

<script>
import LinkForm from "./LinkForm.vue";

export default {
  name: "Link Display",
  components: {
    LinkForm
  },
  props: ["data"]
};
</script>
