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
  },
  {
    key: 'delete_user',
    label: "ユーザー削除",
    title: 'delete_user'
  }
])
export default {
  name: 'App',
  components: { 'a-menu': Menu },
  computed: {
    selectedKeys () {
      return this.$store.state.selectedKeys
    }
  },
  data () {
    return {
      items
    }
  },

  methods: {
    handleMenuClick ({ key }) {
      this.$store.commit('changeSelectedKeys', key)
      this.$router.push({ path: '/' + key })
    }
  }
}
</script>

<style>
#boby{
  background-color: aquamarine;
}
</style>
