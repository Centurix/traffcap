<template>
  <v-container>
    <v-navigation-drawer v-model="drawer" app >
      <v-sheet class="pa-4" >
        <v-img :src="require('../assets/traffcap_logo_615x112.png')"></v-img>
      </v-sheet>
      <v-divider></v-divider>
      <v-list>
        <v-list-item>
          <v-list-item-content>
            <v-btn text :to="{ name: 'messages' }">Messages</v-btn>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-btn text :to="{ name: 'about' }">About</v-btn>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-btn text :to="{ name: 'api_docs' }">API Documentation</v-btn>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-switch
            v-model="$vuetify.theme.dark"
            inset
            label="Dark Mode"
            persistent-hint
          ></v-switch>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'Navigation',

    data: () => ({
      drawer: null
    }),
  })
</script>
