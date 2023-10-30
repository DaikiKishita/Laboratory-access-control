<template>
    <div class="format">
        <a class="name">名前</a>
        <div class="Input_name">
            <a-input v-model:value="Name" placeholder="Enter your name" >
            <template #prefix>
                <user-outlined />
            </template>
            <template #suffix>
                <a-tooltip title="Extra information">
                    <info-circle-outlined style="color: rgba(0, 0, 0, 0.45)" />
                </a-tooltip>
            </template>
            </a-input>
            <a-button type="button" @click="posting">送信</a-button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  methods: {
    posting: function () {
      const Names = this.Name
      axios
        .post('/add_user', {
          name: Names
        })
        .catch((err) => {
          console.log(err)
        })
      this.$router.push({ path: '/' })
      this.$store.commit('changeSelectedKeys', '')
    }
  },
  data: function () {
    return {
      Name: '' // 初期値を空文字列に設定
    }
  }
}
</script>

<style>
.format{
    margin: auto;
    text-align: center;
    background-color: silver;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-left: 30px;
    margin-right: 30px;
}
.Input_name{
    margin: auto;
    width: 30%;
    margin-bottom: 10px;
}
.name{
    size: 120%;
}
</style>
