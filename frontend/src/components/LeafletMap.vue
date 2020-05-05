<template>

	<div id="mapframe" class="container-md">
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
			<l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 80%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker :lat-lng="withPopup">
        <l-popup>
          <div @click="innerClick">
            I am a popup
                      </div>
        </l-popup>
      </l-marker>
      <l-marker :lat-lng="withTooltip">
        <l-tooltip :options="{ permanent: true, interactive: true }">
          <div @click="innerClick">
            I am a tooltip
            <p v-show="showParagraph">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
              sed pretium nisl, ut sagittis sapien. Sed vel sollicitudin nisi.
              Donec finibus semper metus id malesuada.
            </p>
          </div>
        </l-tooltip>
      </l-marker>
		</l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from "vue2-leaflet";
import axios from 'axios';


export default {
  name: "LeafletMap",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip
  },
	props: {
		apiURL: String,
	},
  data() {
    return {
			api: this.apiURL,
			postcode: 'L1 4BS',
			coords: '',
      zoom: 15,
      center: latLng(53.376282, -2.920921),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OSM</a>',
      withPopup: latLng(47.41322, -1.219482),
      withTooltip: latLng(47.41422, -1.250482),
      currentZoom: 11.5,
      currentCenter: latLng(47.41322, -1.219482),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true
    };
  },
  methods: {
		getCoords() {
			const path = this.api + '/convert/' + this.postcode;
      axios.get(path)
        .then((response) => {
          this.coords = latLng(response.data.latitude, response.data.longitude);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

		markPostcode(){
			console.log(this.postcode);
			this.getCoords()
		},
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    innerClick() {
      alert("Click!");
    } }
};
</script>

<style scoped>

#mapframe {
	height: 50vh;
	width: 100%;
}

</style>
