<template>
  <div class="container">
		<p> {{ variableName }} </p>
	</div>
</template>

<script>
/* import ; */

/* const x = y; */

export default {
  name: 'MyComponent',
	components: {
	  ,
	},

	props: {
	/**
	  * Doc for property
	*/
    aProperty: {
  		},
	},

	data() {
	  return: {
		  variableName: 'value',
	  };
	
	},

	computed: {
    computedVariable: function() {
		  return this.variableName.reverse() // or whatever
			}

	},

	beforeDestroy() {
	  console.log('Do something *beforeDestroy*');
	},

	mounted() {
	  console.log('Do something when mounted.');
	},

	methods: {
    someFunction() {
		  alert('Do something when called');
		},
	}
}
</script>

<style scoped>

</style>

<docs>

</docs>
