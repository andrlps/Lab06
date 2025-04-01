import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after
        # the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddAnno = None
        self._ddBrand = None
        self._ddRetailer = None
        self._btnTopVendite = None
        self._btnAnalizza = None
        self._lv = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)
        self._ddAnno = ft.Dropdown(label="Anno", hint_text="Seleziona un filtro anno", width= 250)
        self._controller.riempiDDAnno()
        self._ddBrand = ft.Dropdown(label="Brand", hint_text="Seleziona un filtro brand",
                                    width= 250)
        self._controller.riempiDDBrand()
        self._ddRetailer = ft.Dropdown(label="Retailer",
                                       hint_text="Seleziona un filtro retailer",
                                       width= 250)
        self._controller.riempiDDRetailer()
        row1 = ft.Row([self._ddAnno, self._ddBrand, self._ddRetailer],
                      alignment=MainAxisAlignment.CENTER)
        self._btnTopVendite = ft.ElevatedButton(text="Top vendite",
                                                on_click=self._controller.
                                                handleTopVendite)
        self._btnAnalizza = ft.ElevatedButton(text="Analizza vendite",
                                              on_click=self._controller.
                                              handleAnalizza)
        row2 = ft.Row([self._btnTopVendite, self._btnAnalizza],
                      alignment=MainAxisAlignment.CENTER)
        self._lv = ft.ListView(expand=True)
        self._page.add(row1, row2, self._lv)
        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
