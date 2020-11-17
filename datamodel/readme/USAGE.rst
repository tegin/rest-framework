This module is intended to use only by developers using something like

.. code-block:: python

    model = self.env.datamodels[DATAMODEL_NAME](partial=True)
    model.field1 = 'FIELD 1'
    model.field2 = 'FIELD 2'

    model.dump() -> {'field1': 'FIELD 1', 'field2': 'FIELD 2'}

For example, when used on rest api, if your return the object without dumping it will
be processed properly.
