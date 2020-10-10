<template>
  <div>
    <div class="flex bg-gray-200">
      <div class="flex-1 flex flex-col overflow-hidden">
        <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200">
          <div class="container mx-auto px-6 py-8">
            <div class="flex flex-wrap">
              <div
                class="flex w-full items-center border-b border-teal-500 py-2"
              >
                <input
                  class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                  type="text"
                  id="url"
                  placeholder="https://www.example.com"
                  v-model="passURL"
                />
                <button
                  class="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                  type="button"
                  @click="getUrl(passURL)"
                >
                  Search page
                </button>
              </div>
            </div>
            <LinkStatus :url="this.url" />
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import LinkStatus from "./LinkStatus.vue";

export default {
  name: "LinkInput",
  components: {
    LinkStatus,
  },
  data() {
    return {
      passURL: "",
      url: "",
    };
  },
  methods: {
    getUrl(value) {
      this.url = value;
    },
  },
};
</script>
