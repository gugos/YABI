<script setup>
import { ref } from 'vue';
import FilterBuilder from './components/FilterBuilder.vue';
import QueryRunner from './components/QueryRunner.vue';
// import ConsoleOutput from './components/ConsoleOutput.vue';

// const appName = import.meta.env.VITE_APP_NAME || 'BI System MVP';
// const appVersion = import.meta.env.VITE_APP_VERSION || '0.1.0';
const newFilter = ref(null);

const handleFilterSave = (filter) => {
  newFilter.value = filter;
};
</script>

<template>
  <FilterBuilder @on-save="handleFilterSave" />
  <QueryRunner v-if="newFilter !== null" :filter="newFilter" />
  <!-- <ConsoleOutput /> -->
</template>