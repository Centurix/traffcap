<template>
  <v-container>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#61affe">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5">GET http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#fca130">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >PUT http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#49cc90">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >POST http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#f93e3e">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >DELETE http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#0d5aa7">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >OPTIONS http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#9012fe">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >HEAD http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#50e3c2">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >PATCH http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions></v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="12">
        <v-card dark color="#000">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h5" >TRACE http://localhost:8080/r/MTYzNjE4NDk4NTU5NQ</v-card-title>
              <v-card-subtitle></v-card-subtitle>
              <v-card-actions>
                <v-btn @click="sendMessage()" small color="primary">Click Me!</v-btn>
              </v-card-actions>
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
  }),
  created: function() {
    console.log("Starting websocket connection")
    this.connection = new WebSocket("ws://localhost:8000/requests/abcdefg/ws")
    this.connection.onmessage = function (event) {
      console.log("On message")
      console.log(event)
    }
    this.connection.onopen = function (event) {
      console.log("On open")
      console.log(event)
    }
  },
  methods: {
    sendMessage: function() {
      console.log("Sending a message")
      this.connection.send('{"data": {"type": "messages", "id": "abcdefg"}}')
    }
  }
})
</script>
