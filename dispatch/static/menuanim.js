YUI().use('anim', function(Y) {
    var module = Y.one('#about');
    var submenu = module.one('.submenu');
    // add fx plugin to module body
    var content = submenu.plug(Y.Plugin.NodeFX, {
        from: { height: submenu.all('li').size() * 28 + 'px' },
        to: { height: 0 },
        easing: Y.Easing.backIn,
        duration: 0.5
    });
    var onClick = function(e) {
        module.toggleClass('yui-closed');
        content.fx.set('reverse', !content.fx.get('reverse')); // toggle reverse
        content.fx.run();
    };
    module.on('click', onClick);
});
YUI().use('anim', function(Y) {
    var module = Y.one('#projects');
    var submenu = module.one('.submenu');
    // add fx plugin to module body
    var content = submenu.plug(Y.Plugin.NodeFX, {
        from: { height: submenu.all('li').size() * 28 + 'px' },
        to: { height: 0 },
        easing: Y.Easing.backIn,
        duration: 0.5
    });
    var onClick = function(e) {
        module.toggleClass('yui-closed');
        content.fx.set('reverse', !content.fx.get('reverse')); // toggle reverse
        content.fx.run();
    };
    module.on('click', onClick);
});
YUI().use('anim', function(Y) {
    var module = Y.one('#releases');
    var submenu = module.one('.submenu');
    // add fx plugin to module body
    var content = submenu.plug(Y.Plugin.NodeFX, {
        from: { height: submenu.all('li').size() * 28 + 'px' },
        to: { height: 0 },
        easing: Y.Easing.backIn,
        duration: 0.5
    });
    var onClick = function(e) {
        module.toggleClass('yui-closed');
        content.fx.set('reverse', !content.fx.get('reverse')); // toggle reverse
        content.fx.run();
    };
    module.on('click', onClick);
});
YUI().use('anim', function(Y) {
    var module = Y.one('#devs');
    var submenu = module.one('.submenu');
    // add fx plugin to module body
    var content = submenu.plug(Y.Plugin.NodeFX, {
        from: { height: submenu.all('li').size() * 28 + 'px' },
        to: { height: 0 },
        easing: Y.Easing.backIn,
        duration: 0.5
    });
 
    var onClick = function(e) {
        module.toggleClass('yui-closed');
        content.fx.set('reverse', !content.fx.get('reverse')); // toggle reverse
        content.fx.run();
    };
    module.on('click', onClick);
});