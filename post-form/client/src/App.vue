<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <span>Adebayo Oremule</span>
      </div>

      <v-spacer>
      </v-spacer>
      <v-tooltip left>
      <template v-slot:activator="{ on, attrs }">
      <v-btn icon href="https://github.com/adebayoore" target="blank"
      v-bind="attrs"
          v-on="on"><v-icon>mdi-github</v-icon></v-btn>
      </template>
      <span>Programming Portfolio</span>
      </v-tooltip>

      <v-tooltip right>
      <template v-slot:activator="{ on, attrs }">
      <v-btn text icon v-bind="attrs" v-on="on" href="https://medium.com/@adebayo.oremule" target="blank"><v-icon>mdi-post</v-icon></v-btn>
      </template>
      <span>Medium Blog</span>
      </v-tooltip>
      <v-spacer>
      </v-spacer>
    </v-app-bar>
    <v-main>
      <HelloWorld/>
    </v-main>
    <v-footer padless>
    <v-col
      class="text-left"
      cols="12"
    ><strong><span>&copy;Orem</span></strong>
    </v-col>
  </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
