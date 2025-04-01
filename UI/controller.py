import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailerScelto = None
        self._brand = ""
        self.data = 0

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def riempiDDAnno(self):
        self._view._ddAnno.options.append(ft.dropdown.Option(key="Nessun filtro"))
        date = []
        for anno in self._model.getAnni():
            self._view._ddAnno.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def riempiDDBrand(self):
        self._view._ddBrand.options.append(ft.dropdown.Option(key="Nessun filtro"))
        for brand in self._model.getBrand():
            self._view._ddBrand.options.append(ft.dropdown.Option(brand))
        self._view.update_page()

    def riempiDDRetailer(self):
        self._view._ddRetailer.options.append(ft.dropdown.Option(key="Nessun filtro"))
        retailers = self._model.getRetailer()
        for key in retailers:
            retailer = retailers[key]
            self._view._ddRetailer.options.append(ft.dropdown.Option(key=retailer.code,
                                                                    text=retailer.name,
                                                                    data=retailer,
                                                                    on_click=self.handleRetailer))
        self._view.update_page()

    def handleRetailer(self, e):
        self._retailerScelto = e.control.data.code

    def handleTopVendite(self, e):
        self._view._lv.controls.clear()
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._retailerScelto
        print(anno, brand, retailer)

        for vendita in self._model.getVendite(anno, brand, retailer):
            print(vendita)
            self._view._lv.controls.append(ft.Text(vendita))
        self._view.update_page()

    def handleAnalizza(self, e):
        self._view._lv.controls.clear()
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer = self._retailerScelto
        print(anno, brand, retailer)
        d = self._model.getVenditeAnalizza(anno, brand, retailer)
        print(d)
        s = (f"Statistiche Vendite\nGiro d'affari: {d['ricavi']}\nNumero Vendite: {d['numero']}\n"
             f"Numero Retails coinvolti {len(d['retailers'])}\nNumero Prodotti Coinvolti: {len(d['prodotti'])}")
        self._view._lv.controls.append(ft.Text(s))
        self._view.update_page()


