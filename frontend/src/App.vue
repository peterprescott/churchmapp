<template>
  <div id="app">
    <h1>App</h1>
    <LeafletMap />
    <Ping />
    <DemoComponent />
  </div>
</template>

<script>
import LeafletMap from './components/LeafletMap.vue'
import Ping from './components/Ping.vue'
import DemoComponent from './components/DemoComponent.vue'

export default {
  name: 'App',
  components: {
    LeafletMap,
    Ping,
    DemoComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
