<template>
  <div class="flex flex-col mt-8">
    <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
      <div
        class="inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200"
        v-if="Object.keys(data).length"
      >
        <h2 class="text-2xl text-center py-2">Searching on: {{ data.link }}</h2>
        <div
          id="links"
          v-for="link in data.links"
          :key="link.ID"
          class="bg-white"
        >
          <div id="link" class="flex">
            <span
              class=" w-2/3 px-6 py-4 whitespace-no-wrap border-b border-gray-200"
              >{{ link }}</span
            >
            <span
              id="status"
              class="w-1/3 px-6 py-4 whitespace-no-wrap border-b border-gray-200"
            >
              <span
                v-if="link.includes('http') && link.status_code === 200"
                :class="succes"
                >Active</span
              >
              <span v-else-if="link.includes('#')" :class="succes"
                >Internal Link</span
              >
              <span
                v-else-if="link.includes('http') && link.status_code != 200"
                :class="warning"
                >Link found but no status</span
              >
              <span v-else :class="failure">This is not a link</span>
            </span>
          </div>
        </div>

        <p
          class="w-full px-6 py-4 whitespace-no-wrap border-b border-gray-200 text-center"
        >
          This are all the links found
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LinkStatus",
  props: ["data"],
  data() {
    return {
      succes:
        "bg-green-800 text-green-200 px-2 inline-flex text-xs leading-5 font-semibold rounded-full",
      warning:
        "bg-yellow-800 text-yellow-200 px-2 inline-flex text-xs leading-5 font-semibold rounded-full",
      failure:
        "bg-red-800 text-red-200 px-2 inline-flex text-xs leading-5 font-semibold rounded-full",
    };
  },
};
</script>
