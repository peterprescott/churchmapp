<template>
  <div id="app">
    <h1>churchmAPP</h1>
    <LeafletMap />
    <Postcode />
  </div>
</template>

<script>
import LeafletMap from './components/LeafletMap.vue'
import Postcode from './components/Postcode.vue'

export default {
  name: 'App',
  components: {
    LeafletMap,
    Postcode,
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
