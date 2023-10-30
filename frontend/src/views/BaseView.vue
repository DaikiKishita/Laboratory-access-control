<template>
  <div class="base">
    <table class="user_table">
      <tr>
        <th>名前</th>
        <th>場所</th>
        <th>説明</th>
      </tr>
      <template v-for="user of users" v-bind:key="user.name">
        <tr><td v-bind:style='{"background-color": user.color }'>
          <a class="name">{{ user.name }}</a>
        </td>
        <td>
          <a-select
            ref="select"
            v-model:value="user.status"
            style="width: 120px"
            :options="statuses"
            @change=ChangeColor(user.name,user.status)
          >
          </a-select>
        </td>
          <template v-if="user.color == 'silver'">
            <td><input type="text"/></td>
          </template>
          <template v-else-if="user.color == 'red'">
            <td>家に帰宅済み</td>
          </template>
          <template v-else-if="user.color == 'green'">
            <td>説明不要っ！</td>
          </template>
          <template v-else-if="user.color == 'yellow'">
          <td>邪魔してOK！</td>
          </template>
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
    const users = ref([])
    const statuses = ref([
      {
        value: 'silver',
        label: '学校内'
      },
      {
        value: 'green',
        label: '研究室内'
      },
      {
        value: 'red',
        label: '学校外'
      },
      {
        value: 'yellow',
        label: '面談中'
      }
    ])
    axios
      .get('/get_data')
      .then(function (res) {
        users.value = res.data
      })
    return {
      users,
      statuses,
      ChangeColor: function (user, color) {
        axios
          .post('/change_color', {
            Name: user,
            Color: color
          })
          .then(function () {
            var idx = null
            users.value.forEach((userData, i) => {
              if (userData.name === user) {
                idx = i
              }
            })
            if (idx !== null) {
              const tmpUsers = users.value
              tmpUsers[idx].color = color
              users.value = tmpUsers
            }
          })
      }
    }
  }
}
</script>

<style>
.base{
  margin: auto;
  text-align: center;
}
.user_table{
  margin: auto;
  text-align: center;
}
.name{
  margin: 10px;
  text-align: center;
}
td{

}
</style>
