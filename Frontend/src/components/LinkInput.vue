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
                <form @submit.prevent="submit">
                  <input
                    class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                    type="text"
                    id="url"
                    placeholder="https://www.example.com"
                    v-model="url"
                  />
                  <button
                    class="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                    type="submit"
                  >
                    Search page
                  </button>
                </form>
              </div>
            </div>
            <LinkStatus :data="this.data" />
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import LinkStatus from "./LinkStatus.vue";
import axios from "axios";

export default {
  name: "LinkInput",
  components: {
    LinkStatus,
  },
  data() {
    return {
      passURL: "",
      url: "",
      data: {},
    };
  },
  methods: {
    submit() {
      this.search = this.url.split(".");
      axios
        .get(
          `http://localhost:3201/api/v1/${this.search[1]}/${this.search[2]}`,
          {
            name: this.search[1],
          }
        )
        .then((res) => {
          this.data = res.data;
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
