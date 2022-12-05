/*
	Dopetrope 2.0 by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

window._skel_config = {
	preset: 'standard',
	prefix: window.SITEURL + '/theme/css/style',
	resetCSS: true,
	breakpoints: {
		'desktop': {
			grid: {
				gutters: 50
			}
		}
	}
};

window._skel_panels_config = {
    panels: {
        navPanel: {
            breakpoints: "mobile",
            position: "left",
            style: "push",
            size: "40%",
            html: '<h2 id="sideMenu">Menu</h2>'
                // This "navList" action will copiy the content of #nav into the lateral navPanel:
                + '<div data-action="navList" data-args="nav"></div>'
        }
    },
    overlays: {
        titleBar: {
            breakpoints: "mobile",
            position: "top-left",
            width: "100%",
            height: 44,
            html: '<span class="toggle" data-action="togglePanel" data-args="navPanel"></span>'
        }
    }
};
