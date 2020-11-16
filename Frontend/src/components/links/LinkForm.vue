<template>
  <div class="flex w-full items-center border-b border-teal-500 py-2">
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
  <p v-if="isLoading">Loading ...</p>
  <div v-if="linkData" class="flex flex-wrap">
    <link-output
      v-for="link in linkData.links"
      :key="link"
      :name="link"
      status="200"
      styling="failure"
      class="flex w-full items-center border-b"
    ></link-output>
  </div>
</template>

<script>
import axios from "axios";
import LinkOutput from "./LinkOutput.vue";

export default {
  components: {
    LinkOutput
  },
  data() {
    return {
      url: "",
      linkData: null,
      isLoading: false
    };
  },
  methods: {
    submit() {
      this.isLoading = true;
      this.linkData = null;
      this.search = this.url.split(".");
      axios
        .get(
          `http://localhost:3201/api/v1/${this.search[1]}/${this.search[2]}`,
          {
            name: this.search[1]
          }
        )
        .then(res => {
          const result = res.data;
          console.log(result);
          this.linkData = result;
          // return result;
          this.isLoading = false;
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style></style>
