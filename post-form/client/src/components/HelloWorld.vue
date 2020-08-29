<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1 class="display-2 font-weight-bold mb-3">
          Custom Entity Recognition <v-btn icon @click="dialog = true">
            <v-icon>mdi-help-circle-outline</v-icon>
          </v-btn>
        </h1>
        <v-textarea
          clearable
          clear-icon="mdi-close"
          label="Enter Job Request"
        ></v-textarea>
        <v-btn text outlined>Post</v-btn>
        <v-spacer></v-spacer>
      </v-col>
        <v-col
          cols="12"
          md="4"
        >
        <v-text-field
          outlined
            v-model="firstname"
            label="Target Openings"
            disabled
          ></v-text-field>
          <v-text-field outlined
          disabled
            v-model="lastname"
            label="Start Date"
          ></v-text-field>
          <v-text-field
          outlined
          disabled
            v-model="email"
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
            v-model="lastname"
            label="Job Title"
          ></v-text-field>
          <v-text-field
          outlined
          disabled
            v-model="email"
            label="Duration"
          ></v-text-field>
          <v-text-field
          outlined
          disabled
            v-model="lastname"
            label="Rate"
          ></v-text-field>
        </v-col>
         <v-col
          cols="12"
          md="4"
        >
          <v-textarea
          disabled
          name="input-7-1"
          label="Skills"
          v-model="w"
        ></v-textarea>
        </v-col>
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title class="headline grey lighten-2">
          How it Works
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit
          pariatur. Excepteur sint occaecat cupidatat non proident,
          sunt in culpa qui officia deserunt mollit anim id est laborum.
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
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',

  data: () => ({
    dialog: false,
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
};
</script>
