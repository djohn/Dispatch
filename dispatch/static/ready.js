dojo.require("dojo.fx");

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
    })
})