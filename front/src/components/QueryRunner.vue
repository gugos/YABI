<script setup lang="ts">
import * as monaco from 'monaco-editor';
import { ref, onMounted } from 'vue'

// monaco.languages.register({ id: 'custom' })
const props = defineProps({
  filter: {
    type: Object
  }
});

const editor = ref()

if (props.filter) {
  monaco.typescript.javascriptDefaults.addExtraLib(`const filter = ${JSON.stringify(props.filter)};`);
}

onMounted(() => {
  monaco.editor.create(editor.value, {
    value:
`/*
const filter = ${JSON.stringify(props.filter)}
*/

const getQueryText = () => {
  return \`\`; // retrun query
};
`,
    language: 'javascript',
  });
})
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
      ></v-btn>
      <v-btn
        class="ms-2"
        icon="mdi-content-save-outline"
      ></v-btn>
    </v-sheet>

    <div class="pa-4">
      <div id="query-runner" ref="editor"></div>
    </div>
  </v-sheet>
</template>

<style scoped>
#query-runner {
  width: 100%;
  height: 500px;
}
</style>
