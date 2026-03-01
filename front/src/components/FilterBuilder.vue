<script setup>
import { ref, reactive } from 'vue'

const emit = defineEmits(['on-save']);

const fields = ref([
  { label: 'field_1', value: 'field_1', is_multiselect: true, },
  { label: 'field_2', value: 'field_2', is_multiselect: true, },
  { label: 'field_3', value: 'field_3', is_multiselect: true, },
  { label: 'field_4', value: 'field_4', is_multiselect: true, },
])

const selectedFields = ref([])

const dialog = ref(false)
const filterItem = reactive({
  value: '',
  label: '',
  is_multiselect: false,
});

const handleChipClick = (item) => {
  Object.assign(filterItem, item);
  dialog.value = true;
};

const handleSaveItemClick = () => {
  Object.assign(
    fields.value.find(item => item.value === filterItem.value),
    filterItem,
  );
  dialog.value = false;
};

const handleResetClick = () => {
  selectedFields.value = [];

  fields.value = fields.value.map(item => {
    return {
      value: item.value,
      label: item.value,
      is_multiselect: true,
    }
  })
};

const handleSaveFilterClick = () => {
  const filter = {};
  for (const item of selectedFields.value) {
    filter[item.value] = [];
  }

  emit('on-save', filter);
};
</script>

<template>
  <v-sheet
    class="mx-auto"
    elevation="10"
    width="60%"
    rounded="lg"
  >
    <v-sheet
      class="pa-3 bg-primary text-right"
      rounded="t-lg"
    >
      <v-btn
        icon="mdi-refresh"
        @click="handleResetClick"
      ></v-btn>
      <v-btn
        class="ms-2"
        icon="mdi-content-save-outline"
        @click="handleSaveFilterClick"
      ></v-btn>
    </v-sheet>

    <div class="pa-4">
      <v-combobox
        v-model="selectedFields"
        :items="fields"
        label="Select"
        chips
        closable-chips
        multiple
      >
        <template v-slot:chip="{ props, item }">
          <v-chip v-bind="props" :text="item.raw.label" @click="handleChipClick(item.raw)"></v-chip>
        </template>

        <template v-slot:item="{ props, item }">
          <v-list-item
            v-bind="props"
            :title="item.raw.label"
          ></v-list-item>
        </template>
      </v-combobox>
    </div>
  </v-sheet>

  <v-dialog
    v-model="dialog"
    max-width="600"
  >
    <v-card
      prepend-icon="mdi-filter"
      title="Filter item"
    >
      <v-form class="pa-4" validate-on="submit lazy" @submit.prevent="handleSaveItemClick">
        <v-text-field
          disabled
          v-model="filterItem.value"
          label="Field"
        ></v-text-field>
        <v-text-field
          v-model="filterItem.label"
          label="Label"
        ></v-text-field>
        <v-checkbox
          v-model="filterItem.is_multiselect"
          label="Multiselect"
        ></v-checkbox>

        <div class="text-end">
          <v-btn
            text="Save"
            type="submit"
          ></v-btn>
        </div>
      </v-form>
    </v-card>
  </v-dialog>
</template>