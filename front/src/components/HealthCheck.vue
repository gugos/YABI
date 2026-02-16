<template>
  <div class="card">
    <h2>Backend Connection Test</h2>
    <div class="button-group">
      <button @click="checkHealth" :disabled="loading.health">
        {{ loading.health ? 'Checking...' : 'Check Health' }}
      </button>
      <button @click="testConnection" :disabled="loading.test">
        {{ loading.test ? 'Testing...' : 'Test API' }}
      </button>
      <button @click="fetchData" :disabled="loading.data">
        {{ loading.data ? 'Loading...' : 'Get Sample Data' }}
      </button>
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="loading.health || loading.test || loading.data" class="loading">
      Loading...
    </div>

    <div v-if="healthStatus" class="endpoint-card">
      <h3>Health Status</h3>
      <p><strong>Status:</strong> <span class="status-healthy">{{ healthStatus.status }}</span></p>
      <p><strong>Service:</strong> {{ healthStatus.database }}</p>
      <p><strong>Version:</strong> {{ healthStatus.tables }}</p>
      <p><strong>Message:</strong> {{ healthStatus.tables_count }}</p>
      <!-- <p><strong>Timestamp:</strong> {{ formatDate(healthStatus.timestamp) }}</p> -->
    </div>

    <div v-if="testResult" class="endpoint-card">
      <h3>Test Result</h3>
      <pre>{{ JSON.stringify(testResult, null, 2) }}</pre>
    </div>

    <div v-if="sampleData" class="endpoint-card">
      <h3>Sample Data</h3>
      <p><strong>Total Items:</strong> {{ sampleData.summary.total }}</p>
      <p><strong>Total Value:</strong> {{ sampleData.summary.total_value }}</p>
      <p><strong>Average Value:</strong> {{ sampleData.summary.avg_value }}</p>
      
      <h4>Data Items:</h4>
      <div v-for="item in sampleData.data" :key="item.id" class="data-item">
        <p><strong>{{ item.name }}</strong> ({{ item.category }}) - Value: {{ item.value }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { healthCheck, testApi, getSampleData } from '../services/api.js';

const loading = ref({
  health: false,
  test: false,
  data: false
});
const error = ref(null);
const healthStatus = ref(null);
const testResult = ref(null);
const sampleData = ref(null);

const checkHealth = async () => {
  loading.value.health = true;
  error.value = null;
  try {
    healthStatus.value = await healthCheck();
  } catch (err) {
    error.value = `Health check failed: ${err}`;
  } finally {
    loading.value.health = false;
  }
};

const testConnection = async () => {
  loading.value.test = true;
  error.value = null;
  try {
    testResult.value = await testApi();
  } catch (err) {
    error.value = `API test failed: ${err}`;
  } finally {
    loading.value.test = false;
  }
};

const fetchData = async () => {
  loading.value.data = true;
  error.value = null;
  try {
    sampleData.value = await getSampleData();
  } catch (err) {
    error.value = `Failed to fetch data: ${err}`;
  } finally {
    loading.value.data = false;
  }
};

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleString();
};
</script>