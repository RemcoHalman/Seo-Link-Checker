<template>
  <div class="flex flex-col mt-8">
    <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
      <div
        class="inline-block min-w-full shadow overflow-hidden sm:rounded-lg border-b border-gray-200"
        v-if="Object.keys(data).length"
      >
        <h2 class="text-2xl text-center py-2">Searching on: {{ data.link }}</h2>
        <table class="min-w-full">
          <tbody class="bg-white">
            <tr>
              <td
                class="w-2/3 px-6 py-4 whitespace-no-wrap border-b border-gray-200"
              >
                <div class="flex items-center">
                  <div class="ml-4">
                    <div class="text-sm leading-5 font-medium text-gray-900">
                      {{ data.link }}
                    </div>
                  </div>
                </div>
              </td>
              <td
                class="w-1/3 px-6 py-4 whitespace-no-wrap border-b border-gray-200"
              >
                <span
                  :class="data.status_code === 200 ? succes : failure"
                  class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full"
                >
                  <span v-if="data.status_code === 200">Active</span>
                  <span v-else>No link found</span>
                </span>
              </td>
            </tr>
          </tbody>
        </table>
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
      succes: "bg-green-800 text-green-200",
      failure: "bg-red-800 text-red-200",
    };
  },
};
</script>
