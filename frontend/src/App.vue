<template>
  <div id="app">
		<div class="jumbotron">
			<h1>churchmAPP</h1>
			<p class="lead">Where is your Local Church?</p>
		</div>
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
  margin-top: 60px;
	text-align: center;
}
</style>
