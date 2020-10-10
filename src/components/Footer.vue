<template>
  <div>
    <h1 class="pt-10 pb-2 text-center text-gray-600">
      Created by: Remco Halman
    </h1>
    <hr />
    <h2 class="text-center pt-2">
      Want to contribute to this project?
    </h2>
    <a
      class="text-gray-700"
      href="https://github.com/RemcoHalman/Seo-Link-Checker"
      target="_blank"
    >
      <img :src="GithubIcon" class="mx-auto mt-1" alt="" />
    </a>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      GithubIcon: require("../assets/GitHub-Mark-32px.png"),
    };
  },
};
</script>
