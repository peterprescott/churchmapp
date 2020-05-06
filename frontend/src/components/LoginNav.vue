<template>
<header class="mb-5" >
    <div class="inner container ">
        <nav>
							<p class="title">churchmAPP</p>
            <input type="checkbox" id="nav" class="nav-login"/><label for="nav"></label>
						<ul class="list-inline">
							<li class="list-inline-item">
								<input id="email" type="email" placeholder="name@email.com" class="nav-login">
							</li>
                <li class="list-inline-item">
								<input id="password" type="password" placeholder="password" class="nav-login">
                </li class="list-inline-item">
								<li class="list-inline-item"><a href="#"><button class="btn btn-primary nav-login">LOGIN/REGISTER</button></a></li>
            </ul>
        </nav>
    </div>
	</header>

</template>

<script>
/* import ; */

/* const x = y; */

export default {
  name: 'LoginNav',

	data() {
	  return {
		  show: true,
	  };
	
	},

	methods: {
	}
}
</script>

<style >
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
</style>

<docs>

</docs>
