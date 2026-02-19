<script setup>
import { ref } from 'vue'

const props = defineProps(['filters'])
const emit = defineEmits(['on-removed', 'on-save'])

const dialog = ref(false)
const field = ref('');
const label = ref('');
const isMultiselect = ref(false);

const handleFilterClose = (filter) => {
  emit('on-removed', filter);
};

const handleFilterClick = (filter) => {
  dialog.value = true;
  field.value = filter.field;
  label.value = filter.label;
  isMultiselect.value = filter.is_multiselect;
};

const handleSaveClick = () => {
  emit('on-save', {
    field: field.value,
    label: label.value,
    is_multiselect: isMultiselect.value,
  });
  dialog.value = false;
};
</script>

<template>
  <v-sheet
    class="mx-auto"
    elevation="10"
    width="100%"
    rounded="lg"
  >
    <v-sheet
      class="pa-3 bg-primary text-right"
      rounded="t-lg"
    >
      <v-btn icon="mdi-content-save-outline"></v-btn>
    </v-sheet>

    <div class="pa-4" v-if="!Object.keys(props.filters).length">
      <v-empty-state icon="$info" class="text-center">
        <template v-slot:media>
          <v-icon color="surface-variant"></v-icon>
        </template>

        <template v-slot:headline>
          <div class="text-h4">
            No filters selected
          </div>
        </template>
      </v-empty-state>
    </div>

    <div class="pa-4 d-flex ga-2">
      <v-chip
        closable
        v-for="filter in props.filters"
        :key="filter.field"
        @click:close="handleFilterClose(filter.field)"
        @click="handleFilterClick(filter)"
      >
        {{ filter.label }}
      </v-chip>
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
      <v-form class="pa-4" validate-on="submit lazy" @submit.prevent="handleSaveClick">
        <v-text-field
          disabled
          v-model="field"
          label="Field"
        ></v-text-field>
        <v-text-field
          v-model="label"
          label="Label"
        ></v-text-field>
        <v-checkbox
          v-model="isMultiselect"
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