<template>
  <div>
		<p>{{ pcode }}</p>
		<p>{{ response }} </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Postcode',
  data() {
    return {
      pcode: 'L1 4BS',
      response: '',
    };
  },
  methods: {
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
