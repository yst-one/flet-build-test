import flet as ft
import random

def main(page: ft.Page):
    page.title = "Flet 瀑布流布局示例"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # 1. 设置列数
    COLUMN_COUNT = 3
    
    # 2. 创建列容器列表
    columns = [
        ft.Column(
            expand=1, 
            spacing=10, 
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        ) for _ in range(COLUMN_COUNT)
    ]

    # 3. 生成模拟数据并分发到各列
    items_data = [
        {"title": f"项目 {i}", "color": random.choice([ft.Colors.AMBER_200, ft.Colors.BLUE_200, ft.Colors.GREEN_200, ft.Colors.RED_200, ft.Colors.PURPLE_200]), "height": random.randint(100, 300)}
        for i in range(20)
    ]

    for index, data in enumerate(items_data):
        # 使用取模运算决定放入哪一列
        target_col = columns[index % COLUMN_COUNT]
        
        target_col.controls.append(
            ft.Container(
                content=ft.Text(data["title"], weight=ft.FontWeight.BOLD),
                height=data["height"],
                bgcolor=data["color"],
                border_radius=10,
                alignment=ft.Alignment.CENTER,
                shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.with_opacity(0.1, "black"))
            )
        )

    # 4. 将所有列放入一个 Row 中
    waterfall_layout = ft.Row(
        controls=columns,
        vertical_alignment=ft.CrossAxisAlignment.START, # 关键：顶部对齐
        spacing=10,
    )

    # 添加到页面（包裹在 Column 中以支持滚动）
    page.add(
        ft.Text("简单瀑布流布局", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        ft.Divider(),
        ft.Column([waterfall_layout], scroll=ft.ScrollMode.AUTO, expand=True)
    )
if __name__ == "__main__":
    ft.run(main)