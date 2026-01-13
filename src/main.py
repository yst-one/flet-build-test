import sys

import flet as ft

from my_modules.some_module import greeter
from my_modules.utils import cube_util, square_util


def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("Flet Build Test"),
        actions=[ft.Text(f"v{ft.__version__}")],
    )
    page.horizontal_alignment = page.vertical_alignment = "center"

    from android_notify import Notification

    # Simple notification
    Notification(
        title="Hello",
        message="This is a basic notification."
    ).send()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                [
                    ft.Text(greeter("world"), weight=ft.FontWeight.BOLD),

                ],
            )
        )
    )


ft.run(main)
