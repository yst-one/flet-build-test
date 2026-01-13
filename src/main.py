import flet as ft


def main(page: ft.Page):


    page.drawer = ft.NavigationDrawer(

    controls=[
        ft.Container(height=12),
        ft.NavigationDrawerDestination(
            label="Item 1",
            icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
            selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
        ),
        ft.Divider(thickness=2),
        ft.NavigationDrawerDestination(
            icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
            label="Item 2",
            selected_icon=ft.Icons.MAIL,
        ),
        ft.NavigationDrawerDestination(
            icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
            label="Item 3",
            selected_icon=ft.Icons.PHONE,
        ),
    ],
    )
    async def handle_show_drawer():
        await page.show_drawer()


    page.appbar = ft.AppBar(
    leading=ft.IconButton(ft.Icons.MENU, on_click=handle_show_drawer),
    leading_width=40,
    #title=ft.Text("AppBar Example"),
    center_title=False,
    bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.BLUE),
    actions_padding=10,
    actions=[
        ft.CircleAvatar(
            content=ft.Text("AB"),
            bgcolor=ft.Colors.PRIMARY,
            color=ft.Colors.ON_PRIMARY,
            max_radius=15
        )
    ],
    )
    page.add(
        
    )


if __name__ == "__main__":
    ft.run(main)