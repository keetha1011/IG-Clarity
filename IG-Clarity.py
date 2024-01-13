import flet as ft
import modules.logic as logic


def main(page: ft.Page):
    page.title = "IG-Clarity"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    img = ft.Image(src=f"icons/ig.png", width=400, height=400)
    txt_box_1 = ft.TextField(label="Path for the zip file", width=500)
    # lv = ft.ListView(expand=False, spacing=10, height=300, width=400)


    def btn_click(e):
        if not txt_box_1.value:
            page_alternate_layout_1()
            txt_box_1.error_text = '''Please input the path\nI won't search your computer for that file 🙂'''
            ft.Row([txt_box_1], alignment=ft.MainAxisAlignment.START)
            page.update()
        else:
            # page_alternate_layout_1()
            logic_process()

    def logic_process():
        path = txt_box_1.value
        # for i in (logic.logic(path)):
        #     lv.controls.append(ft.Text(i))
        # page.add(lv)
        for i in logic.logic(path):
            page.add(ft.Column([ft.Row([ft.Text(i)], alignment=ft.MainAxisAlignment.CENTER)]))
        page.scroll = "always"
        page.update()

    # def progress_bar():
    #     page.add(ft.Text("Indeterminate progress bar", style="headlineSmall"))
    #     page.add(ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"))

    def page_alternate_layout_1():
        page.clean()
        page.add(ft.Row([txt_box_1], alignment=ft.MainAxisAlignment.START))
        page.add(ft.Row([ft.ElevatedButton("Start Checking", height=50, width=500, on_click=btn_click)],
                        alignment=ft.MainAxisAlignment.START))

    page.add(
        ft.Column(
            [ft.Row([img], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt_box_1], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("Start Checking", height=50, width=500, on_click=btn_click)],
               alignment=ft.MainAxisAlignment.CENTER)]
        )
    )


ft.app(target=main)
