<template>
  <div id="app">
		<LeafletMap 
			apiURL="https://churchmapp.pythonanywhere.com"
		  />
  </div>
</template>

<script>
import LeafletMap from './components/LeafletMap.vue'

export default {
  name: 'App',
  components: {
    LeafletMap,
  }
}
</script>

<style>
#app {
	text-align: center;
}
</style>
