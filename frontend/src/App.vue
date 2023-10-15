<template>
  <div id="app">
    <a-menu mode="horizontal">
      <a-menu-item><router-link to="/">home</router-link></a-menu-item>
      <a-menu-item><router-link to="/about">about</router-link></a-menu-item>
    </a-menu>
  </div>
</template>

<script>
import { Menu, MenuItem } from 'ant-design-vue'
export default {
  components: {
    'a-menu': Menu,
    'a-menu-item': MenuItem
  }
}
</script>
