<html> 
  <head> 
  	<link href="http://fonts.googleapis.com/css?family=Oswald:regular" rel="stylesheet" type="text/css" > 
  	<link rel='stylesheet' href="${request.static_url('dispatch:static/style.css')}" type='text/css' />
	<link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/dojo/1.6/dijit/themes/claro/claro.css"/>
    <meta charset="utf-8"> 
    <title>Floating Post Developers | Victoria, BC</title> 
  	<script src="http://ajax.googleapis.com/ajax/libs/dojo/1.6/dojo/dojo.xd.js"></script>
	<script type="text/javascript">
	    dojo.require("dojo.fx");
	    dojo.require("dojo.window");
	    dojo.require("dijit.layout.BorderContainer");
	    dojo.require("dijit.layout.TabContainer");
	    dojo.require("dijit.layout.AccordionContainer");
	    dojo.require("dijit.layout.ContentPane");

	    dojo.ready(function(){
	        var sections = dojo.query(".section-title");
    
		sections.connect("onclick", function(evt){
		    var sub = dojo.query('.submenu', evt.target)[0],
		    dest = '';
	      
		    if (dojo.hasClass(evt.target, "dojo-open")) {
		        dest = 0;
		    } else {
		        dest = dojo.query('li', sub).length * 28;
		    }
	      
		    dojo.animateProperty({
		        node: sub,
		        properties: { height: dest }
		        }).play();
		    dojo.toggleClass(evt.target, "dojo-open");
		});
		var index = new dijit.layout.BorderContainer({style: "height: 100%; width: 26%;"});
		var cpIndex = new dijit.layout.ContentPane({
		    region: "center",
		    style: "height: 100%; width: 100%;",
		    content: "hello world index"
		});
		index.addChild(cpIndex)
		
		var main = new dijit.layout.BorderContainer({style: "height: 100%; width: 75%;"});
		var cpMain = new dijit.layout.ContentPane({
		    region: "center",
		    style: "height: 100%",
		    content: "hello world message"
		});
		main.addChild(cpMain)

	        // put the top level widget into the document, and then call startup()
	        dojo.byId('uiContainer').appendChild(index.domNode);
		dojo.byId('uiContainer').appendChild(main.domNode);
	        index.startup();
		main.startup();
		
		dojo.connect(window, "onresize", function(evt) {
		    if (dojo.window.getBox().w < 800) {
		    }
		    })
	    })
	</script>
  </head> 
  <body class="claro">
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

<div id="uiContainer" class="claro">
</div>

    </div>
    <!-- End Content Body -->
  </body> 
</html>