<script setup>
import { Console, DataAPI } from 'vue-console-feed'
import 'vue-console-feed/style.css'

const c = new DataAPI(false, 1) // if you use API set option to true, argument 2 offset deep location

c.log({
  key1: [1,2,3],
  key2: 'value_2',
})
</script>

<template>
  <Console :data="c.value" />
</template>