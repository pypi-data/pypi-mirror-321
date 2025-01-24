# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class interactive_graph(Component):
    """An interactive_graph component.
This parent component measures its own container size
then passes numeric width & height to the child graph.

Keyword arguments:

- id (string; required)

- chartType (a value equal to: 'categorical', 'continuous'; optional)

- data (list of dicts; optional)

    `data` is a list of dicts with keys:

    - x (string | number; required)

    - y (number; required)

- smoothingFactor (number; default 0.1)

- smoothingType (string; default 'bellcurve')

- style (dict; optional)

- xLabel (string; default 'X Label')

- yLabel (string; default 'Y Label')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'i2dgraph'
    _type = 'interactive_graph'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, chartType=Component.UNDEFINED, data=Component.UNDEFINED, xLabel=Component.UNDEFINED, yLabel=Component.UNDEFINED, smoothingType=Component.UNDEFINED, smoothingFactor=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'chartType', 'data', 'smoothingFactor', 'smoothingType', 'style', 'xLabel', 'yLabel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'chartType', 'data', 'smoothingFactor', 'smoothingType', 'style', 'xLabel', 'yLabel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(interactive_graph, self).__init__(**args)
