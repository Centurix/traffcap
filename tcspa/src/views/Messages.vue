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

interface Message {
  id: string,
  type: string,
  attributes: {
    code: string,
    created: string,
    id: string,
    modified: string,
    scope: string,
    body: string
  }
}

interface Scope {
  method: string,
  client: Array<string>,
  http_version: string,
  scheme: string
  headers: Array<string>,
  query_string: string,
  message: string,
  path: string,
  server: Array<string>
}


export default Vue.extend({
  name: 'Messages',
  components: {},
  data: () => ({
    connection: new WebSocket("ws://localhost:8000/requests/MTYzNjI1OTM2MDQyMQ/ws"),
    card_colors: new Map([
      ["get", "#61affe"],
      ["post", "#49cc90"],
      ["put", "#fca130"],
      ["patch", "#50e3c2"],
      ["delete", "#f93e3e"],
      ["head", "#9012fe"],
      ["trace", "#000"],
      ["options", "#0d5aa7"]
    ]),
    messages: []
  }),
  created() {
    setTimeout(this.refresh, 500)
  },
  methods: {
    card_color(message: Message): string {
      return this.card_colors.get(this.scope(message).method.toLowerCase()) ?? ""
    },
    called_url(message: Message): string {
      let scope = this.scope(message)
      let server = scope.server.join(":")
      let query_string = (scope.query_string ? "?" + scope.query_string : "")

      return scope.scheme + "://" + server + scope.path + query_string
    },
    scope(message: Message): Scope {
      return JSON.parse(message.attributes.scope)
    },
    refresh() {
      this.connection = new WebSocket("ws://localhost:8000/requests/MTYzNjI1OTM2MDQyMQ/ws")
      this.connection.onopen = () => {
        this.connection.onmessage = ({data}) => {
          this.messages = this.messages.concat(JSON.parse(data).data)
        }
      }
    }
  }
})
</script>
