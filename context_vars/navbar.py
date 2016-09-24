def get_navbar():
    return {
        "main_navigation" : [
            {
                "name"      : "Valencia Food tours",
                "link"      : "known.html",
				"id"        : "known",
                "rel"       : "Go to...",
                "submenu"   : [
                    {
                        "name" : "Tapas, wine & History Tour",
                        "link" : "known.html",
						"id"   : "tapas"
                    },
                    {
                        "name" : "Cabanyal Foodtour",
                        "link" : "history.html",
                        "id"   : "foodtour"
                    },
                    {
                        "name" : "Private tour",
                        "link" : "history.html",
                        "id"   : "history"
                    }
                ]
            },
            {
                "name"  : "Valencia Food Blog",
                "id"    : "blog",
                "link"  : "supermarket.html"
            },
            {
                "name"  : "About",
                "id"    : "about",
                "link"  : "supermarket.html",
				"rel"       : "Go to...",
                "submenu"   : [
                    {
                        "name" : "About me",
                        "link" : "known.html",
						"id"   : "aboutme"
                    },
                    {
                        "name" : "FAQ",
                        "link" : "history.html",
                        "id"   : "foodtour"
                    },
                    {
                        "name" : "Culinary map",
                        "link" : "history.html",
                        "id"   : "culinary"
                    },
                    {
                        "name" : "Jobs",
                        "link" : "history.html",
                        "id"   : "jobs"
                    }
                ]
            },
            {
                "name"  : "Gift cards",
                "id"    : "giftcards",
                "link"  : "supermarket.html"
            },
            {
                "name"  : "Contact",
                "id"    : "contact ",
                "link"  : "supermarket.html"
            }

        ]

    }
