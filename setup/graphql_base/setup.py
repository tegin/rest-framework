import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo'],
    odoo_addon={
        "external_dependencies_override": {
            "python": {
                "graphql_server": "graphql-server-core",
                "graphene": "graphene<3",
            }
        }
    },
)
