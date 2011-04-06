<html> 
  <head> 
  	<link href="http://fonts.googleapis.com/css?family=Oswald:regular" rel="stylesheet" type="text/css" > 
  	<link rel='stylesheet' href="${request.static_url('dispatch:static/style.css')}" type='text/css' /> 
    <meta charset="utf-8"> 
    <title>Floating Post Developers | Victoria, BC</title> 
  	<script src="http://yui.yahooapis.com/3.3.0/build/yui/yui-min.js" charset="utf-8"></script>
	<script type="text/javascript" src="${request.static_url('dispatch:static/menuanim.js')}"></script>
  </head> 
  <body>
  	<!-- Begin Nav Body -->
    <div id="menubg"></div> 
    <div id="menu"> 
    <div class="container"> 
      <a href="${request.application_url}"> 
	<img src="${request.static_url('dispatch:static/logo.png')}"> 
	<ul> 
	<img src="${request.static_url('dispatch:static/dotBar.png')}"> 
        <li class="site-title1">Floating</li> 
        <li class="site-title2">Post.Devs</li> 
        <img src="${request.static_url('dispatch:static/dotBar.png')}">
      </a> 
      <ul> 
        <li class="section-title" id="about">About</br>
	  <ul class="submenu">
	    <li>Mission</li>
	    <li>MV Scenic</li>
	  </ul>
        </li> 
        <li class="section-title" id="projects">Projects</br>
	  <ul class="submenu"> 
      	  <li><a href="${request.route_url('home')}">Dispatch</a></li> 
      	</ul>
        </li>
        <li class="section-title" id="releases">Releases</br> 
      	<ul class="submenu"> 
      	  <li>Coming Soon</li> 
      	</ul>
        </li>
        <li class="section-title" id="devs">Developers</br> 
      	<ul class="submenu"></ul>
        </li>
        <li class="section-title">Contact</li> 
      </ul> 
      </ul> 
    </div> 
    </div>
    <!-- End Nav Body -->
    <!-- Begin Content Body -->
    <div id="content">
      ${self.body()}
    </div>
    <!-- End Content Body -->
  </body> 
</html>