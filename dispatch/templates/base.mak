<html> 
  <head> 
  	<link href="http://fonts.googleapis.com/css?family=Oswald:regular" rel="stylesheet" type="text/css" > 
  	<link rel='stylesheet' href="${request.static_url('dispatch:static/style.css')}" type='text/css' /> 
    <meta charset="utf-8"> 
    <title>Floating Post Developers | Victoria, BC</title> 
  	<script src="http://ajax.googleapis.com/ajax/libs/dojo/1.6/dojo/dojo.xd.js"></script>
	<script type="text/javascript" src="${request.static_url('dispatch:static/ready.js')}"></script>
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
	<li class="section-title">Dispatch:</li>
      </a>
      <ul>
	<li class="section-title">Node Nav</br>
	  <ul class="submenu">
	    <li><a href="${request.route_url('home')}">All Nodes</a></li>
	    <li><a href="${request.route_url('home')}">View Node</a></li>
	  </ul>
        </li> 
        <li class="section-title">Project</br>
	  <ul class="submenu"> 
      	  <li><a href="https://github.com/djohn/Dispatch">GitHub</a></li>
      	</ul>
        </li>
        <li class="section-title">Developers</br> 
      	<ul class="submenu">
	  <li><a href="https://github.com/djohn">Doug Johnson</a></li>
	  <li><a href="https://github.com/mike-anderson">Mike Anderson</a></li>
	</ul>
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