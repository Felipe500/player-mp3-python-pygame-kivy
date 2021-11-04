
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from arquivos.Player_Funcoes import Funcoes_Player
from sys import path
path.append("arquivos")

# Interação da interface grafica
class Tela_Principal(FloatLayout, Funcoes_Player):

    def posicao2(self):
        posicao_atual = self.ids.barra.value
        posicao_atual += 1
        # while tocando==True:
        self.ids.barra.value = posicao_atual

    def inicio(self):
        """
        Inicializar o player de musica
        1° procurar todos arquivos .mp3 no diretorio selecionado - alterar
        arquivos/classe_player.py - Na classe Player altere em atributos -
        self.pasta_linux = "/media/the_felipe/Arquivos2/musicas/"
        self.pasta_windows = "D:/musicas"
        2° Ira iniciar o mixer de audio
        """
        self.buscar_arquivos_mp3()
        self.iniciar()

        posicao_time = self.posicao()
        # self.id.tempo2.text = str(pos2)
        # self.ids.tempo.text = 'str(p)'
        # self.posicao2()
        print("contador: ", posicao_time)
        return posicao_time

    def play_musica(self):
        """
        Pausar e continuar a musica
        """
        nome = self.play_pause()
        print("situacao--", nome)
        self.ids.play_pause.text = nome['botao']
        self.ids.nmusica.text = nome['musica']

    def proximo(self):
        """
        avançar para a próxima musica
        """
        nome_musica = self.avancar_musica()
        self.ids.nmusica.text = nome_musica

    def voltar(self):
        """
        Voltar para a musica anterior
        """
        nome_musica = self.voltar_musica()
        self.ids.nmusica.text = nome_musica

    def confi_voll(sefl, x):
        print("novo voulume", x)
        sefl.config_volume(x)


class Player_mp3App(App, Tela_Principal):

    def build(self):
        self.inicio()


if __name__ == '__main__':
    Player_mp3App().run()
