from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class BlackjackApp(App):
    def build(self):
        return BlackjackUI()

class BlackjackUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Button(text='Commencer', on_press=self.start_game))
        # Ajoutez d'autres widgets ici selon vos besoins.

    def start_game(self, instance):
        print("Le jeu commence !")
        # Ajoutez votre logique de démarrage de jeu ici.

if __name__ == '__main__':
    BlackjackApp().run()
    
class CardWidget(Image):
    def __init__(self, card_image, **kwargs):
        super().__init__(**kwargs)
        self.source = card_image  # le chemin de l'image de la carte

