import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo'],
    odoo_addon={
        'external_dependencies_override': {
            'python': {
                'accept_language': 'parse-accept-language',
                'apispec': 'apispec>=4.0.0'
            },
        },
    }
)
