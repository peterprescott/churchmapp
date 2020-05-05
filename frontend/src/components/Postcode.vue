<template>
		<div class="container">
			<input v-model='postcode' 
				placeholder='Enter Postcode'
			  @keyup.enter='markPostcode'>
		<p>{{ coords }}</p>
		<button type="button" 
				class="btn btn-primary ml-3 mt-3 mr-3 mb-3" 
				@click="showLongText">
        Toggle long popup
      </button>
			<button type="button" 
        class="btn btn-primary ml-3 mt-3 mr-3 mb-3" 
				@click="showMap = !showMap">
        Toggle map
      </button>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'Postcode',
  props: {
    apiURL: String,
  },
  data() {
    return {
      pcode: 'L1 4BS',
      response: '',
    };
  },
  methods: {
	  getCoords() {
      const path = this.api + '/convert/' + this.postcode;
        axios.get(path)
          .then((response) => {
             this.coords = latLng(
       response.data.latitude, response.data.longitude
               );
									        })
				        .catch((error) => {
									          // eslint-disable-next-line
									          console.error(error);
									        });
				    },


    getMessage() {
			const path = 'https://churchmapp.pythonanywhere.com/convert/';
      axios.get(path+this.pcode)
        .then((res) => {
          this.response= [res.data['latitude'], res.data['longitude']];
        })
        .catch((error) => {
          // eslint-disable-next-line
          this.response = "Failed to connect with server.";
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
