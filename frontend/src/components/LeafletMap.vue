<template>

	<div id="mapframe" class="container-md">
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
			<l-marker
        v-for="marker in markers"
        :key="marker.id"
        :visible="marker.visible"
        :draggable="marker.draggable"
        :lat-lng.sync="marker.position"
        :icon="marker.icon"
        @click="alert(marker)"
      >
        <l-popup :content="marker.tooltip" />
        <l-tooltip :content="marker.tooltip" />
		</l-marker>
			</l-map>

	
			<div class="col-auto">
			<div class="col">
			<input v-model='postcode' 
				class ="mb-2 mr-2 form-control"
				placeholder='Enter Postcode'
			  @keyup.enter='markPostcode'>
				</div><div class="col">
     <button
        name="button"
				type="button"
				class="btn btn-primary mb-2"
        @click="markPostcode"
      >
        Mark Postcode
    </button>
	</div>
	</div>

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
			postcode: 'L18 8DB',
			coords: '',
			markers: [],
      zoom: 15,
      center: latLng(53.376282, -2.920921),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OSM</a>',
      currentZoom: 11.5,
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
					this.coords = {
						lat: response.data.latitude, 
						lng: response.data.longitude
					},
					this.addMarker(this.coords);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
		addMarker(position) {
      const newMarker = {
				position: position,
        draggable: true,
        visible: true,
      };
      this.markers.push(newMarker);
			this.center=this.coords;
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
    
    }
};
</script>

<style scoped>

#mapframe {
	height: 50vh;
	width: 100%;
}

</style>
