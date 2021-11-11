<template>
  <v-container>
    <v-card>
      <v-row dense>
        <v-col cols="12">
          <v-card-title class="text-h5">
            <v-img :src="require('../assets/traffcap_logo_615x112.png')"></v-img>
          </v-card-title>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Messages',
  components: {},
  data: () => ({
  }),
})
</script>
