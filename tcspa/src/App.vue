<template>
  <v-app id="inspire">
    <Navigation />
    <v-container>
      <v-main>
        <router-view></router-view>
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import Navigation from '@/components/Navigation.vue'

export default {
  data: () => ({}),
  components: {
    Navigation
  }
}
</script>