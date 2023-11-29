<template>
  <div class="base">
  <div class="color-asist">
    <a class="red">学校外</a>
    <a>＜ー＞</a>
    <a class="blue">学内</a>
    <a>＜ー＞</a>
    <a class="green">研究室内</a>
  </div>
    <div class="container">
      <template v-for="user of users" v-bind:key="user.name">
        <div class="user_data"
          @touchstart="touchStart"
          @touchmove="touchMove(user.name,colordict[user.color])"
          @touchend="touchEnd"
          v-bind:style='{"background-color": user.color }'>
            {{ user.name }}
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
    const startX = ref([])
    const endX = ref([])
    const users = ref([])
    const changeuser = ref([])
    const colornum = ref([])
    const colordict = ref({
      red: 0,
      green: 1,
      royalblue: 2
    })
    const colorlist = [
      'red',
      'green',
      'royalblue'
    ]
    axios
      .get('/get_data')
      .then(function (res) {
        console.log(res.data)
        users.value = res.data
      })
    return {
      colordict,
      users,
      touchStart (event) {
        event.preventDefault()
        startX.value = event.touches[0].pageX
      },
      touchMove (user, num) {
        colornum.value = num
        changeuser.value = user
      },
      touchEnd (event) {
        event.preventDefault()
        endX.value = event.changedTouches[0].pageX
        if (startX.value - endX.value >= 0) {
          colornum.value = colornum.value + 1
        } else {
          colornum.value = colornum.value - 1
        }
        if (colornum.value === -1) {
          colornum.value = 2
        }
        if (colornum.value === 3) {
          colornum.value = 0
        }
        const user = changeuser.value
        const color = colorlist[colornum.value]
        axios
          .post('/change_color', {
            Name: user,
            Color: color
          })
          .then(function () {
            let idx = null
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
.color-asist{
  display: inline;
  justify-content: center;
  padding:10px;
}
.container{
  display: grid;
  padding-left: 10px;
  padding-right: 10px;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 10px;
}
.user_data{
  font-size: large;
  aspect-ratio: 8/3;
  display: flex;
  justify-content: center;
  align-items: center;
}
.name{
  margin: 0px;
  padding: 0px;
  text-align: center;
}
body{
  background-color:antiquewhite;
}
.red{
  background-color: red;
}
.green{
  background-color: green;
}
.blue{
  background-color:royalblue ;
}
</style>
