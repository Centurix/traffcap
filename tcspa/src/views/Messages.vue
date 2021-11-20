<template>
  <v-container>
    <v-row dense v-for="(message, i) in messages.slice().reverse()" v-bind:key="i">
      <v-col cols="12">
        <v-card dark :color="card_color(message)" elevation="24">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5"><v-chip>{{ scope(message).method }}</v-chip> <v-chip>{{ called_url(message) }}</v-chip></v-card-title>
              <v-card-subtitle>From: {{ scope(message).client.join(":") }}</v-card-subtitle>
              <v-card-text>
                <p>Received: {{ message.attributes.created }}</p>
                <p>HTTP Version: {{ scope(message).http_version }}</p>
                <p>Scheme: {{ scope(message).scheme }}</p>
                <p>Headers: {{ scope(message).headers }}</p>
                <p>Query Params: {{ scope(message).query_string }}</p>
                <p>Body: {{ message.attributes.body }}</p>
              </v-card-text>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Messages',
  components: {},
  data: () => ({
    card_colors: {
      "get": "#61affe",
      "post": "#49cc90",
      "put": "#fca130",
      "patch": "#50e3c2",
      "delete": "#f93e3e",
      "head": "#9012fe",
      "trace": "#000",
      "options": "#0d5aa7"
    },
    messages: []
  }),
  created() {
    setTimeout(this.refresh, 500)
  },
  methods: {
    card_color(message) {
      return this.card_colors[this.scope(message).method.toLowerCase()]
    },
    called_url(message) {
      let scope = this.scope(message)
      let server = scope.server.join(":")
      let query_string = (scope.query_string ? "?" + scope.query_string : "")

      return scope.scheme + "://" + server + scope.path + query_string
    },
    scope(message) {
      return JSON.parse(message.attributes.scope)
    },
    refresh() {
      console.log("Starting websocket connection")
      this.connection = new WebSocket("ws://localhost:8000/requests/MTYzNjI1OTM2MDQyMQ/ws")
      this.connection.onopen = () => {
        console.log("Connected to Traffcap, waiting for requests...")
        this.connection.onmessage = ({data}) => {
          this.messages = this.messages.concat(JSON.parse(data).data)
        }
      }
    },
    sendMessage() {
      console.log("Sending a message")
      this.connection.send('{"data": {"type": "messages", "id": "abcdefg"}}')
    }
  }
})
</script>
