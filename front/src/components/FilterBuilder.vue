<script setup>
import { computed, ref } from 'vue';
import FieldSelector from './FieldSelector.vue';
import FilterEditor from './FilterEditor.vue';

const fields = ref(new Set([
  'field_1',
  'field_2',
  'field_3',
]));

const filters = ref({});

const fieldList = computed(() => {
  return Array.from(fields.value);
})

const handleFieldSelected = (field) => {
  fields.value.delete(field);
  filters.value[field] = {
    field: field,
    label: field,
    is_multiselect: true,
  };
};

const handleFilterRemoved = (field) => {
  delete filters.value[field];
  fields.value.add(field);
};

const handleFilterItemSave = (filter) => {
  filters.value[filter.field] = filter;
};

const handleReset = () => {
  fields.value = new Set([
    'field_1',
    'field_2',
    'field_3',
  ]);
  filters.value = {};
};
</script>

<template>
  <div class="d-flex ga-4 pa-12">
    <FieldSelector @on-selected="handleFieldSelected" :fields="fieldList" @on-reset="handleReset" />
    <FilterEditor @on-removed="handleFilterRemoved" :filters="filters" @on-save="handleFilterItemSave" />
  </div>
</template>