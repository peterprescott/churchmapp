<template>
	<div>
<header class="mb-5" >
		<div>

    <div class="inner container ">
        <nav >
							<p class="title">churchmAPP</p>
							<form v-if="!connected" class="form-signin" @submit.prevent="auth">
            <input type="checkbox" id="nav" class="nav-login"/><label for="nav"></label>
						<ul class="list-inline">
							<li class="list-inline-item">
								<input v-model="email" id="inputEmail" type="email" placeholder="name@email.com" class="nav-login">
							</li>
                <li class="list-inline-item">
								<input v-model="password" id="inputPassword" type="password" placeholder="password" class="nav-login">
                </li class="list-inline-item">
								<li class="list-inline-item"><a href="#"><button class="btn btn-dark">LOGIN/REGISTER</button></a></li>
            </ul>
					</form>
        </nav>
				<p v-if="connected">Signed in as {{ email }}. <br> 
					<a @click="signOut"><strong>[Click here to Sign Out]</strong></a></p>
			</div>
    </div>
	</header>

	<div id="mapframe" class="container-md">
			<l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
			:max-bounds="bounds"
      :options="mapOptions"
      style="height: 80%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    > <l-tile-layer
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
        <l-popup :content="marker.name" />
        <l-tooltip :content="marker.name" />
		</l-marker>
			</l-map>

	
			<div class="col-auto">
			<div class="col">
			<textarea 
				v-model='multiplePostcodes'
				class="mb-2 mr-2 mt-2 form-control"
				placeholder='Postcodes should be spaced, capitalized, and separated by a line break. Login to save locations and labels.'
	
				@keypress="checkLength"
				@keyup.enter='markPostcodes'
				rows="2" cols="50"
			>
			</textarea>
				</div><div class="col">
	     <button
        name="button"
				type="button"
				class="btn btn-info mb-2"
        @click="markPostcodes"
      >
        Mark Postcodes
    </button>
</div>
	</div>

	<div id="marker-table">
      <table class="table table-hover" v-if="markers.length">
				<thead>
        <tr>
					<!--					<th>[ @ ]</th> -->
          <th scope="col">[ X ]</th>
          <th scope="col">Name</th>
          <th scope="col">Postcode</th>
          <th scope="col" v-if="connected">[ SAVE ]</th>
        </tr>
			</thead>
			<tbody>
        <tr
          v-for="(item, index) in markers"
          :key="index"
        >
	        <td style="text-align: center">
            <input v-if="!item.saved"
              type="button"
              value="X"
							class="btn btn-dark"
              @click="removeMarker(index)"
            >
            <input v-if="item.saved"
              type="button"
              value="X"
							class="btn btn-danger"
              @click="unSave(index)"
            >
          </td>
 				<!-- <td><button @click="centerUpdate(
							item.latitude, 
							item.longitude)">@</button></td> -->
          <td>
            <input v-if="!item.saved"
              v-model.text="item.name"
              type="text"
            >
              <span v-if="item.saved">{{ item.name }}</span>
          </td>
          <td>
						{{ item.postcode }}
          </td>
					<td v-if="connected" 
						style="text-align: center">
            <input v-if="!item.saved"
              type="button"
						  class="btn btn-info"
              value="SAVE"
              @click="savePlace(index)"
            >
                        <span v-if="item.saved">(SAVED)</span>
          </td>
       </tr>
			</tbody>
      </table>
     	</div>

  </div>

</div>
</template>

<script>
import { latLng, latLngBounds } from "leaflet";
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
			email:'',
			password:'',
			connected: false,
			token: '',
			longPostcode: false,

			api: this.apiURL,
			postcode: '',
			multiplePostcodes: '',
			coords: '',
			markers: [],
      zoom: 15,
      center: latLng(53.376282, -2.920921),
			bounds: latLngBounds(
        { lat: 49.0, lng: 2.75 },
        { lat: 60.7, lng: -7.81 }
      ),
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
		

		checkLength() {
			if (this.postcode.length > 7) {
				this.longPostcode = true;
			}
			/* if (this.multiplePostcodes.length < 8) { */
			/* 	this.longPostcode = false; */
			/* } */
		},

		auth() {
			console.log('Authenticating...')
			axios.post(this.api+'/auth',
			 { email: this.email, password: this.password } 
			).then((response) => this.authSuccess(response))
				.catch(() => this.authFail() )
		},

		authSuccess(response) {
			if (!response.data.JWT) { this.authFail(); return }
			this.token = response.data.JWT;
			this.connected = true;
            this.password = '';
			console.log('Connected!');
            this.getPlaces()

		},
		authFail() {
			this.token='';
			this.connected = false;
			console.log('Failed.')
		},
       
       signOut() {
           this.token='';
           this.connected=false;
           this.markers = [];
           this.email='';
           console.log('Signed Out.')
       },
      
       getPlaces() {
           console.log('Getting Places')
          axios.get(this.api+'/places',
            {headers:{'JWT':this.token}}
            )
          .then((response) => this.addPlaces(response.data)
)
				.catch(() => console.log() )
       },
      
      addPlaces(data) {
          console.log('adding places');
          console.log(data.places);
             for (let i = 0; i < data.places.length; i++){
                 data.places[i].saved = true;
                 data.places[i].coords = {
                     lat: data.places[i].latitude,
                     lng: data.places[i].longitude
                 };
                data.places[i].position = data.places[i].coords; 
                 data.places[i].visible = true;
   this.markers.push(data.places[i]) ;
            }         
      },
      
      savePlace(index) {
          let place = this.markers[index];
          
          axios.post(this.api+'/places',
           {
                         'postcode': place.postcode,
                         'latitude': place.latitude,
                         'longitude': place.longitude,
                         'name': place.name,
                },
          {headers:{'JWT':this.token}},
          ).then(function(response) {place.saved=true; place.id=response.data.id})
				.catch(() => console.log() )
          
      },
      

      unSave(index) {
          let place = this.markers[index];
          axios.delete(this.api+'/places/'+place.id,
                     {headers:{'JWT':this.token}},
          ).then(function(response){ place.saved=false;})
				.catch(() => console.log() )
          
      },

		getCoords(postcode) {
          let path = this.api + '/convert/' + postcode;
      axios.get(path)
        .then((response) => {
					this.coords = {
						lat: response.data.latitude, 
						lng: response.data.longitude
					},
					this.addMarker(this.coords, postcode);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
      
		addMarker(position, postcode) {
      const newMarker = {
				position: position,
				postcode: postcode,
				latitude: position.lat,
				longitude: position.lng,
              saved:false,
      };
      this.markers.push(newMarker);
			this.center=this.coords;
    },

		removeMarker: function(index) {
      this.markers.splice(index, 1);
    },
		saveMarker(index) {
			console.log(this.markers[index])

		},

		markPostcode(){
			this.getCoords(this.postcode)
		},
		markPostcodes(){
			let postcodeList = this.multiplePostcodes.split('\n')
			for (let i=0;i<postcodeList.length;i++){
				this.postcode = postcodeList[i];
				this.markPostcode();

			}
			/* this.getCoords() */
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

.title {
	font-size: larger;
	text-align: left;
	width: 100%;
}

input {
	text-align: center;
}

.nav-login {
  border-radius: 10px;
	margin-left: 10px;
	margin-right: 10px;
}

header {
    background: #fff;
		height: 100px;
    padding-top: 40px;
}

ul {
	list-style-type: none;
}

nav > ul {
    float: center;
}
nav > ul > li {
    text-align: center;
    line-height: 40px;
    margin-left: 70px;
}
nav > ul li ul li {
    width: 100%;
    text-align: left;
}
nav ul li:hover {
    cursor: pointer;
    position: relative;
}
nav ul li:hover > ul {
    display: block;
}

nav > ul > li > a {
    cursor: pointer;
    display: block;
    outline: none;
    width: 100%;
    text-decoration: none;
}
nav > ul > li {
    float: center;
}
nav a {
	color: grey;
}
nav > ul li ul {
    display: none;
    position: absolute;
    top: 100%;
    width: 100%;
    z-index: 2000;
}
nav > ul li ul li > a {
    text-decoration: none;
}
[type="checkbox"],
label {
	display: none;
}
@media screen and (max-width: 768px) {
    nav ul {
        display: none;
    }
    label {
        display: block;
				background: #fff;
        width: 40px;
        height: 40px;
        cursor: pointer;
        position: absolute;
        right: 20px;
        top: 0px;
    }
    label:after {
        content: '';
        display: block;
        width: 30px;
        height: 5px;
        background: #333;
        margin: 7px 7px;
        box-shadow: 0px 10px 0px #333, 0px 20px 0px #333
    }
    [type="checkbox"]:checked ~ ul {
        display: block;
        z-index: 9999;
        position: absolute;
        right: 30px;
        left: 30px;
    }
   nav ul li {
        display: block;
        float: none;
        width: 100%;
        background: #fff;
        text-align: center;
    }
    nav > ul > li {
        margin-left: 0px;
    }
    nav > ul li ul li {
        display: block;
        float: none;
    }
    nav > ul li ul {
        display: block;
        position: relative;
        width: 100%;
        z-index: 9999;
        float: none;
    }
}
#mapframe {
	height: 50vh;
	width: 100%;
}

</style>
