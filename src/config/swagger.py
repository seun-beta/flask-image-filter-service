# Swagger template and configuration setup

template = {
    "swagger": "2.0",
    "info": {
        "title": "Image Filter App Backend",
        "description": "Image Filter App Backend",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "adegokeseunfunmi1999@gmail.com",
            "url": "https://image-filter-backend.herokuapp.com/",
        },
        "termsOfService": "https://image-filter-backend.com/terms",
        "version": "1.0",
    },
    "basePath": "/api/v1",  # base path for blueprint registration
    "schemes": ["http", "https"],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/",
}
