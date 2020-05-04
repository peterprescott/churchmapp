<template>
  <div id="app">
		<div class="jumbotron">
			<h1>churchmAPP</h1>
			<p class="lead">Where is your Local Church?</p>
		</div>
    <Postcode />
		<LeafletMap />
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
  margin-top: 60px;
	text-align: center;
}
</style>
