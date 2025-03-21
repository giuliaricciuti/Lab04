import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page
        self.__dd = None
        self.__txtOut = None
        self.__txtOut2 = None
        self.__frase = None
        self.__btn = None
        self.__lvResult = None


    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )


        # Add your stuff here
        self.__ddLan = ft.Dropdown(label="Lingua", options=[ft.dropdown.Option("italian"),
                                                          ft.dropdown.Option("english"),
                                                          ft.dropdown.Option("spanish")],
                                on_change=self.__controller.handleChangeLan)

        self.__txtOut = ft.Text("")

        row1 = ft.Row([self.__ddLan, self.__txtOut], alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row1)

        self.__ddSearch = ft.Dropdown(label="Tipo di ricerca", options=[ft.dropdown.Option("Default"),
                                                         ft.dropdown.Option("Linear"),
                                                         ft.dropdown.Option("Dichotomic")],
                                        on_change=self.__controller.handleChangeSearch)
        self.__txtOut2 = ft.Text("")
        self.__frase = ft.TextField(label = "inserisci qui la frase", label_style= ft.TextStyle(color = "grey"))
        self.__btn = ft.ElevatedButton(text="Vai", on_click=self.__controller.handleSpellCheck, bgcolor = "blue", color="white")
        row2 = ft.Row([self.__ddSearch, self.__txtOut2, self.__frase, self.__btn])
        self.page.add(row2)

        self.__lvResult = ft.ListView(expand=1,spacing=10,padding=20,auto_scroll=True)
        row3 = ft.Row([self.__lvResult])
        self.page.add(row3)

        self.page.update()

    def setTxtout(self, valore):
        self.__txtOut.value = valore

    def setTxtout2(self, valore):
        self.__txtOut2.value = valore

    def getFrase(self):
        return self.__frase.value

    def getLanguage(self):
        return self.__ddLan.value

    def getSearch(self):
        return self.__ddSearch.value

    def showWarning(self):
        warning = ft.Text("inserisci tutti i campi")
        self.page.add(warning)

    def showResult(self, txtIn, errate, time):
        self.__frase.value=""
        self.__lvResult.controls.append(ft.Text(f"""
        Frase cercata:
        {txtIn}
        Le parole sbagliate sono:
        {errate}
        Il tempo impiegato è
        {time}"""))
        self.page.add(self.__lvResult)


    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
