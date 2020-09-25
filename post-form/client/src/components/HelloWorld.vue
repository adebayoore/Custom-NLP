<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1 class="display-2 font-weight-bold mb-3">
          New Job Request?<v-btn icon @click="dialog = true">
            <v-icon>mdi-help-circle-outline</v-icon>
          </v-btn>
        </h1>
        <v-form @submit="onSubmit">
        <v-textarea
          v-model="rawtext"
          label="Enter the details of your Job Request"
        ></v-textarea>
        <!-- <v-btn text outlined type="submit" @click="dialog3 = true">Post</v-btn> -->
        </v-form>
        <v-spacer></v-spacer>
      </v-col>
        <v-col
          cols="12"
          md="4"
        >
        <v-text-field
        prepend-icon="mdi-close"
          outlined
            v-model="openings"
            label="Target Openings"
            disabled
          ></v-text-field>
          <v-text-field outlined
                  prepend-icon="mdi-close"
          disabled
            v-model="date"
            label="Start Date"
          ></v-text-field>
          <v-text-field
          outlined
          disabled
          prepend-icon="mdi-close"
            v-model="loc"
            :rules="emailRules"
            label="Location"
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
        <v-text-field
        disabled
          outlined
          prepend-icon="mdi-close"
            v-model="title"
            label="Job Title"
          ></v-text-field>
          <v-text-field
          outlined
          prepend-icon="mdi-close"
          disabled
            v-model="duration"
            label="Duration"
          ></v-text-field>
          <v-text-field
          outlined
          disabled
          prepend-icon="mdi-close"
            v-model="rate"
            label="Rate"
          ></v-text-field>
        </v-col>
         <v-col
          cols="12"
          md="4"
        >
        <span>Skills</span>
        <v-spacer></v-spacer>
          <!-- <v-textarea
          disabled
          name="input-7-1"
          label="Skills"
          v-model="w"
        ></v-textarea> -->
           <v-chip
           v-if="chip1"
      class="ma-2"
      close
      color="error"
      outlined
      @click:close="chip1 = false"
    >
      Graphql
    </v-chip>
           <v-chip
           v-if="chip2"
      class="ma-2"
      close
      color="error"
      outlined
      @click:close="chip2 = false"
    >
      SQL
    </v-chip>
           <v-chip
           v-if="chip3"
      class="ma-2"
      close
      color="error"
      outlined
      @click:close="chip3 = false"
    >
      Java
    </v-chip>
           <v-chip
           v-if="chip4"
      class="ma-2"
      close
      color="error"
      outlined
      @click:close="chip4 = false"
    >
      C++
    </v-chip>
        </v-col>
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title class="headline grey lighten-2">
          How it Works
        </v-card-title>
        <v-card-text>
          Enter a Message with a description of the job request.
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
        </v-dialog>
        <v-row class="text-center">
            <v-btn large @click="dialog2 = true">POst</v-btn>
        </v-row>
    </v-row>
<v-dialog v-model="dialog2" max-width="374">
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <v-img
      height="200"
      src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
    ></v-img>

    <v-card-title>{{title}}</v-card-title>
    <v-spacer></v-spacer>
    <v-card-subtitle>{{openings}} Open Positions</v-card-subtitle>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
      <v-icon small>mdi-map-marker</v-icon>{{loc}}
      <!-- <div class="grey--text ml-4">{{loc}}</div> -->
      </v-row>

      <div class="my-4 subtitle-1">
        start and end
      </div>

      <div>$ {{rate}}</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Skills Required*</v-card-title>

    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>Graphql</v-chip>

        <v-chip>SQL</v-chip>

        <v-chip>Java</v-chip>

        <v-chip>C++</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Apply
      </v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data: () => ({
    chip3: true,
    chip2: true,
    chip1: true,
    chip4: true,
    dialog: false,
    dialog2: false,
    date: 'June 7th 2021',
    openings: '8',
    rate: '50',
    duration: '10 months',
    loc: 'Cayman Islands',
    title: 'Java Developer',
    rawtext: '8 Java developers needed for 10 months in the Cayman Islands. skilled in graphql sql java go c++, .net starting from june 7th with a pay of $50 an hour',
    ents: [],
    ecosystem: [
      {
        text: 'Medium Blog',
        href: 'https://medium.com/@adebayo.oremule',
      },
      {
        text: 'Github Portfolio',
        href: 'https://github.com/adebayoore',
      },
    ],
  }),
  methods: {
    entPull(payload) {
      const path = 'http://localhost:8080/process';
      axios.post(path, payload)
        .then(() => {
          this.getEnts();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getEnts();
        });
    },
  },
  initForm() {
    this.rawtext = '';
    this.ents = [];
  },
  onSubmit(evt) {
    evt.preventDefault();
    this.$refs.entPull.hide();
    let ents = false;
    if (this.rawtext[0]) ents = true;
    const payload = {
      rawtext: this.rawtext,
      ents,
    };
    this.entPull(payload);
    this.initForm();
  },
};
</script>
