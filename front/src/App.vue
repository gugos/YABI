<template>
  <div class="container">
    <div class="header">
      <h1>{{ appName }}</h1>
      <p>BI System MVP - Proof of Concept</p>
      <p>Version: {{ appVersion }}</p>
    </div>

    <div class="content">
      <div class="card">
        <h2>System Overview</h2>
        <p>This is a Minimum Viable Product (MVP) for a BI System with the following planned features:</p>
        <ul>
          <li>✅ Database connection management</li>
          <li>🔲 Faceted filters with drilling</li>
          <li>🔲 Custom queries for data visualization</li>
          <li>🔲 Data transformation scripts</li>
          <li>🔲 Dashboard sharing and saving</li>
        </ul>
        <p>Start by testing the backend connection using the panel on the right.</p>
      </div>

      <HealthCheck />
    </div>

    <div class="card">
      <h2>API Endpoints</h2>
      <div class="endpoint-card">
        <h3>Available Endpoints:</h3>
        <ul>
          <li><strong>GET</strong> /api/health - Service health check</li>
          <li><strong>GET</strong> /api/test - Test endpoint</li>
          <li><strong>GET</strong> /api/data - Sample data</li>
          <li><strong>GET</strong> /docs - Interactive API documentation</li>
          <li><strong>GET</strong> /redoc - Alternative API documentation</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import HealthCheck from './components/HealthCheck.vue';

const appName = import.meta.env.VITE_APP_NAME || 'BI System MVP';
const appVersion = import.meta.env.VITE_APP_VERSION || '0.1.0';
</script>