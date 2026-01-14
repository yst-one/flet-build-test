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

    page.end_drawer = ft.NavigationDrawer(
        # on_dismiss=handle_dismissal,
        # on_change=handle_change,
        bgcolor=ft.Colors.BLUE_GREY_50,
        controls=[
                ft.Container(height=50,content=ft.Row(alignment=ft.MainAxisAlignment.END,
                                                    controls=[ft.IconButton(ft.Icons.ABC,ft.Text("扫一扫")),
                                                                ft.IconButton(ft.Icons.SETTINGS,ft.Text("设置"))
                                                        ]
                                                    ),
                            ),
                ft.Stack(height=page.height-80,controls=[

                        ft.ListView(scroll=ft.ScrollMode.AUTO,
                                    controls=[
                                        ft.Container(expand=True,bgcolor=ft.Colors.WHITE,margin=ft.Margin.all(10),border_radius=ft.BorderRadius.all(10),padding=ft.Padding.all(10),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Row(alignment=ft.MainAxisAlignment.START,
                                                                controls=[ft.CircleAvatar(content=ft.Text("AB"),radius=30),
                                                                        ft.Column(expand=True,controls=[ft.Text("用户名"),ft.Text("用户签名")]),
                                                                        ft.IconButton(ft.Icons.EDIT)
                                                                        ]
                                                            ),
                                                            ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                controls=[ft.Container(alignment=ft.Alignment.CENTER,bgcolor=ft.Colors.BLUE_50,
                                                                                content=ft.Column(alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=1,
                                                                                                    controls=[ft.Text("47",text_align=ft.TextAlign.CENTER),ft.Text("收藏",text_align=ft.TextAlign.CENTER)]),
                                                                                        ) for _ in range(4) 

                                                                            ],
                                                                            )
                                                            ]
                                                        )

                                        ) for _ in range(5)
                        ]),
                         ft.TransparentPointer(content=
                            ft.Container(alignment=ft.Alignment.BOTTOM_CENTER,padding=ft.Padding.only(bottom=20),
                            content=ft.Button("退出登录",))
                        ),

                    ])
        ],
    )
    async def handle_show_end_drawer():
        await page.show_end_drawer()



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
            ft.GestureDetector(
                content=ft.CircleAvatar(
                    content=ft.Text("AB"),
                    bgcolor=ft.Colors.PRIMARY,
                    color=ft.Colors.ON_PRIMARY,
                    max_radius=15,
                
                )
                ,on_tap=handle_show_end_drawer
                )
        ],
    )



    page.appbar = appbar
    def on_scroll(e: ft.OnScrollEvent):
        print(e)
        log.value=f"scrolled{e.pixels,e.max_scroll_extent,e.min_scroll_extent,e.overscroll}"
        log.update
    log = ft.Text("scrolled")
    page.add(
        ft.ListView(
            expand=True,
            controls=[
                log,
                ft.Row(
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