<template>
    <div class="base">
        <table>
            <tr>
                <th>名前</th>
                <th>アクション</th>
            </tr>
            <template v-for='user of userdata' v-bind:key="user.name">
            <tr>
                <td>
                  <a>{{ user.name }}</a>
                </td>
                <td>
                  <a>未定</a>
                </td>
            </tr>
            </template>
        </table>
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
      userdata
    }
  }
}
</script>
