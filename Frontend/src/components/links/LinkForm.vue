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
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      url: "",
      linkData: {
        link: "https://www.example.com",
        status_code: "200",
        links: ""
      }
    };
  },
  methods: {
    submit() {
      this.search = this.url.split(".");
      axios
        .get(
          `http://localhost:3201/api/v1/${this.search[1]}/${this.search[2]}`,
          {
            name: this.search[1]
          }
        )
        .then(res => {
          this.linkData = res.data;
          console.log(this.linkData.links);
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  provide() {
    return {
      dataUrl: this.linkData.url,
      dataStatus: this.linkData.status_code,
      dataLinks: this.linkData.links
    };
  }
};
</script>

<style></style>
