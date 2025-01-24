# Flashlight control for Flet

`Flashlight` control for Flet.

## Usage

Add `flet-flashlight` as dependency (`pyproject.toml` or `requirements.txt`) to your Flet project.

## Example

```py

import flet as ft

import flet_flashlight as ffl

def main(page: ft.Page):
    flashlight = ffl.Flashlight()
    page.overlay.append(flashlight)
    page.add(
        ft.TextButton("toggle", on_click=lambda _: flashlight.toggle())
    )

ft.app(main)
```