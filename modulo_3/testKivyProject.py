from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage

class MainApp ( App ):
    # def build ( self ):
    #     label = Label ( text = 'Fala galera!',
    #         size_hint = ( .5, .5 ),
    #         pos_hint = { 'center_x': .5, 'center_y': .5 })
        
    #     return label
    
    def build ( self ):
        img = AsyncImage ( source = 'https://supermariorun.com/assets/img/stage/mario03.png' ,
        # img = AsyncImage ( source = 'https://icon2.cleanpng.com/lnd/20250316/iq/c119a72deeaa4766f05807551ddc6e.webp' ,
        # img = AsyncImage ( source = 'https://i.pinimg.com/736x/10/51/7f/10517f8dbcbf03227ada14a72e8f502c.jpg' ,
            size_hint = ( 1 , .5 ),
            pos_hint = { 'center_x': .5 , 'center_y': .5 })
        return img

if __name__ == '__main__' :
    app = MainApp()
    app.run()