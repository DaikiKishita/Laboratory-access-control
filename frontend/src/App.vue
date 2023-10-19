<template>
  <div class="head">
    <a-menu mode="horizontal" :selected-keys="selectedKeys" :items="items" @click="handleMenuClick"/>
  </div>
  <div class="views">
    <router-view></router-view>
  </div>
</template>

<script>
import { Menu } from 'ant-design-vue'
import { ref } from 'vue'

const items = ref([
  {
    key: '',
    label: '入退情報',
    title: 'base'
  },
  {
    key: 'new_user',
    label: '新規追加',
    title: 'new_user'
  }
])
export default {
  name: 'App',
  components: { 'a-menu': Menu },
  data () {
    return {
      selectedKeys: [''], // デフォルトで選択されるメニューキー
      items
    }
  },
  methods: {
    handleMenuClick ({ key }) {
      this.selectedKeys = [key]
      this.$router.push({ path: '/' + key })
    }
  }
}
</script>

<style>
.head{
  padding-bottom: 10px;
}
body{
  margin: auto;
  text-align: center;
  background-color: silver;
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>
