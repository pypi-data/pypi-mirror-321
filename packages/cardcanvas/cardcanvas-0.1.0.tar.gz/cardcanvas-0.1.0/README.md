![logo.svg](static/logo.svg)

![](static/animation.gif)

CardCanvas is a library to create runtime-configurable dashboards using
plotly dash. With a few class definitions, you can let your users build their
dashboards and also analyze and present the data the way they want.

CardCanvas is built using [plotly Dash](https://dash.plotly.com/). The UI is built using
[dash-mantine-components](https://www.dash-mantine-components.com/).
The drag and drop is built using [dash-snap-grid](https://github.com/idling-mind/dash_snap_grid).


Here's a simple example code.

```python
from cardcanvas import CardCanvas, Card
import dash_mantine_components as dmc

settings = {
    "title": "CardCanvas Demo",
    "subtitle": "A Demo application showing the capabilities of CardCanvas",
    "start_config": {},
    "logo": "https://img.icons8.com/?size=80&id=cjlQopC5NR3D&format=png",
    "grid_compact_type": "vertical",
    "grid_row_height": 100,
}


class TextCard(Card):
    title = "White text with a background color"
    description = "Testing out CardCanvas"
    icon = "mdi:file-document-edit"

    def render(self):
        return dmc.Card(
            dmc.Title(
                self.settings.get("text", "Hello CardCanvas"),
                c="white",
            ),
            bg=self.settings.get("color", "blue"),
            style={"height": "100%", "width": "100%"},
        )

    def render_settings(self):
        return dmc.Stack(
            [
                dmc.TextInput(
                    id={"type": "card-settings", "id": self.id, "setting": "text"},
                    value=self.settings.get("text", "Hello CardCanvas"),
                ),
                dmc.ColorPicker(
                    id={"type": "card-settings", "id": self.id, "setting": "color"},
                    value=self.settings.get("color", "grey"),
                ),
            ]
        )


canvas = CardCanvas(settings)
canvas.card_manager.register_card_class(TextCard)

canvas.app.run_server(debug=True)
```

## Explanation

The `CardCanvas` class is a container class for a dash app. You can access the
dash app instance using `canvas.app`. When initalizing the CardCanvas object, you
can pass in a dictionary of settings. The various items you can configure is not documented
yet, but look into the examples to get an idea. The plan is to add more configurable
parts in the future.

A card manager manages the different `Card`
classes. Each `Card` class is a blue print of how a configurable card looks like.

It should atleast have on method called `render` which will tell the app how to
render that card. Optionally, you could add a `render_settings` method to set
the configurable settings of the card. In the above example, you can set
the `text` of the card and also the background color of the card. You have to be
mindful of the `id` of the settings controls. They should follow the template 
`{"type": "card-setting", "id": self.id, "setting": "<your unique setting name>"}`

A limitation of the setting controls as of now is, they only support controls
that sets the attribute `value` as the control's value. So for eg: you cannot use
`dmc.Checkbox` which has it's value in the `checked` attribute. But you could use
a `CheckboxGroup` instead.

It is upto you as a developer to decide which settings you want to expose for
the user and use these settings in the render method. When the render method is
called, you can access these settings using `self.setting`.

`self.setting` is a dictionary with the setting name as the key and value of the
setting as the attribute. When the user updates the setting, the render method
will be called and it can pick up the new values of the settings.

Have a look at `usage.py` or the folder `examples` to see more examples.

The animation shown above can be found in examples/charts.py