import { createApp } from "vue";
import App from "./App.vue";
import titleMixin from "./mixins/titleMixin";

createApp(App)
  .mixin(titleMixin)
  .mount("#app");
