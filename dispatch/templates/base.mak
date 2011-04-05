<html> 
  <head> 
  	<link href="http://fonts.googleapis.com/css?family=Oswald:regular" rel="stylesheet" type="text/css" > 
  	<link rel='stylesheet' href="${request.static_url('dispatch:static/style.css')}" type='text/css' /> 
    <meta charset="utf-8"> 
    <title>Floating Post Developers | Victoria, BC</title> 
  	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.js"></script> 
  	<script type="text/javascript"> 
  		$(document).ready(function () {
  			$('#about.section-title').click(function () { 
				$('#about.submenu').slideToggle('medium');
  			});
  			$('#projects.section-title').click(function () { 
				$('#projects.submenu').slideToggle('medium');
  			});
  			$('#releases.section-title').click(function () { 
				$('#releases.submenu').slideToggle('medium');
  			});
  			$('#devs.section-title').click(function () { 
				$('#devs.submenu').slideToggle('medium');
  			});
  		});
  	</script> 
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
    	<li class="section-title" id="about">About</li> 
    	<ul class="submenu" id="about"></ul> 
    	<li class="section-title" id="projects">Projects</li> 
    	<ul class="submenu" id="projects"> 
    		<li><a href="./dispatch.html">Dispatch</a></li> 
    	</ul> 
    	<li class="section-title" id="releases">Releases</li> 
    	<ul class="submenu" id="releases"> 
    		<li>Coming Soon</li> 
    	</ul> 
    	<li class="section-title" id="devs">Developers</li> 
    	<ul class="submenu" id="devs"></ul> 
    	<li class="section-title">Contact</li> 
    </ul> 
    </ul> 
    </div> 
    </div>
    <!-- End Nav Body -->
    <!-- Begin Content Body -->
    <div id="content">
    
    </div>
    <!-- End Content Body -->
  </body> 
</html>