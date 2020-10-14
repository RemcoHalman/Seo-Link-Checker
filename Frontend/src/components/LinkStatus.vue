<template>
  <div class="flex flex-col mt-8">
    <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
      <div
        class="inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200"
      >
        <h2 class="text-2xl text-center py-2" v-if="url">
          Searching on: {{ url }}
        </h2>
        <table class="min-w-full">
          <tbody class="bg-white">
            <tr v-for="url in urls" :key="url">
              <td
                class="w-2/3 px-6 py-4 whitespace-no-wrap border-b border-gray-200"
              >
                <div class="flex items-center">
                  <div class="ml-4">
                    <div class="text-sm leading-5 font-medium text-gray-900">
                      {{ url.url }}
                    </div>
                  </div>
                </div>
              </td>
              <td
                class="w-1/3 px-6 py-4 whitespace-no-wrap border-b border-gray-200"
              >
                <span
                  :class="url.ok ? succes : failure"
                  class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full"
                >
                  <span v-if="url.ok">Active</span>
                  <span v-else>Not active</span>
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LinkStatus",
  props: ["url"],
  data() {
    return {
      succes: "bg-green-800 text-green-200",
      failure: "bg-red-800 text-red-200",
      data: {},
      urls: [""],
      mountains: [],
    };
  },
  async mounted() {
    const requests = [];
    this.urls.forEach((url) =>
      requests.push(fetch(`http://localhost:5000/api/v1/${url}`))
    );
    const data = await Promise.all(requests);
    this.urls = await Promise.all(data.map((url) => url));
  },
};

// .then((url) => {
//   console.log(url);
// })
</script>
