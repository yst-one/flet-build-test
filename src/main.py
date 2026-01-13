import flet as ft


def main(page: ft.Page):


    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=50,),
            ft.Container(content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[ft.Text("提问历史"),ft.TextButton("删除")],),alignment=ft.Alignment.CENTER),
            ft.Divider(),
            ft.Container(content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,controls=[ft.Text("提问历史"),ft.TextButton("删除")],),alignment=ft.Alignment.CENTER),
            
        ]

    )
    async def handle_show_drawer():
        await page.show_drawer()

    appbar=ft.AppBar(
        title=ft.Text("AppBar Example"),
        leading=ft.IconButton(ft.Icons.MENU, on_click=handle_show_drawer),
        leading_width=40,
        #title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.Colors.with_opacity(0.0, ft.Colors.BLUE),
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



    page.appbar = appbar
    def on_scroll(e: ft.OnScrollEvent):
        print(e)
        page.show_dialog(ft.SnackBar(ft.Text(f"scrolled{e.pixels,e.max_scroll_extent,e.min_scroll_extent}")))
        appbar.title=f"scrolled{e.pixels,e.max_scroll_extent,e.min_scroll_extent}",
        appbar.update()

    page.add(
        ft.ListView(
            expand=True,
            controls=[ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[ft.Column(expand=True,alignment=ft.MainAxisAlignment.START,controls=[ft.Container(height=30,bgcolor=ft.Colors.AMBER_200) for _ in range(100)]),
                        ft.Column(expand=True,alignment=ft.MainAxisAlignment.START,controls=[ft.Container(height=60,bgcolor=ft.Colors.AMBER_200) for _ in range(55)]),
                        ],
            )],
            on_scroll=on_scroll
        )
        
    )


if __name__ == "__main__":
    ft.run(main)