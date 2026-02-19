<script setup>
const props = defineProps(['fields'])
const emit = defineEmits(['on-selected', 'on-reset'])

const handleFieldClick = (field) => {
  emit('on-selected', field);
};

const handleResetClick = () => {
  emit('on-reset');
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
      <v-btn
        class="ms-2"
        icon="mdi-refresh"
        @click="handleResetClick"
      ></v-btn>
    </v-sheet>

    <div class="pa-4" v-if="!props.fields.length">
      <v-empty-state icon="$success" class="text-center">
        <template v-slot:media>
          <v-icon color="surface-variant"></v-icon>
        </template>

        <template v-slot:headline>
          <div class="text-h4">
            All fields are used!
          </div>
        </template>
      </v-empty-state>
    </div>

    <div class="pa-4 d-flex ga-2">
      <v-chip
        v-for="field in props.fields"
        :key="field"
        @click="handleFieldClick(field)"
      >
        {{ field }}
      </v-chip>
    </div>
  </v-sheet>
</template>