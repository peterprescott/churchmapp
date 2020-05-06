<template>
  <div id="app">
		<LoginNav />
		<LeafletMap 
			apiURL="https://churchmapp.pythonanywhere.com"
		  />
  </div>
</template>

<script>
import LoginNav from './components/LoginNav.vue'
import LeafletMap from './components/LeafletMap.vue'

export default {
  name: 'App',
  components: {
		LoginNav,
    LeafletMap,
  }
}
</script>

<style>
#app {
	text-align: center;
}
</style>
