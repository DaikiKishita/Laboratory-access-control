<template>
    <div class="base">
      <div class="container">
        <template v-for='user of userdata' v-bind:key="user.name">
          <div class="user_data">
            <button v-on:click="buttonclick(user.name)">{{ user.name }}</button>
          </div>
        </template>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup () {
    const userdata = ref([])
    axios
      .get('/get_data')
      .then(function (res) {
        userdata.value = res.data
      })
    return {
      userdata,
      buttonclick (params) {
        const user = params
        axios
          .post('/delete', {
            Name: user
          })
        this.$router.push({ path: '/' })
        this.$store.commit('changeSelectedKeys', '')
      }
    }
  }
}
</script>
