import sys

import flet as ft
import flet_ads  # noqa: F401
import flet_audio  # noqa: F401
import flet_audio_recorder  # noqa: F401
import flet_charts  # noqa: F401
import flet_datatable2  # noqa: F401
import flet_flashlight  # noqa: F401
import flet_geolocator  # noqa: F401
import flet_lottie  # noqa: F401
import flet_map  # noqa: F401
import flet_permission_handler  # noqa: F401
import flet_rive  # noqa: F401
import flet_video  # noqa: F401
import flet_webview  # noqa: F401

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
