from pygame import mixer,mixer_music
from os.path import  join, basename
from os import curdir
from glob import glob
from arquivos.classe_player import Player
from sys import platform
import time


Player_Musica = Player()
class Funcoes_Player(object):

    def buscar_arquivos_mp3(self):
        if len(Player_Musica.playlist) > 0:
            # verificar se a lista já possui musicas
            # caso sim, a lista será limpada
            Player_Musica.playlist.clear()
            print('limpando lista')
        # verificando qual o sistema operacional está em uso
        if 'linux' in platform:
            print(Player_Musica.Linux)
            try:
                for musica in glob(join(curdir, "/media/the_felipe/Arquivos2/musicas", '*.mp3')):
                    # contar numero de musicas
                    Player_Musica.nmusicas = Player_Musica.nmusicas + 1
                    # nome da musica
                    print(Player_Musica.nmusicas, '°', basename(musica[:-4]).replace('_', ' '))
                    # adicionar a lista de reprodrução
                    Player_Musica.playlist.append(musica)


            except:
                print("Diretórios de músicas não encontrados!...");
        # verificando qual o sistema operacional está em uso
        if 'win' in platform:
            print(Player_Musica.windows)
            try:
                for musica in glob(join(curdir, "/media/the_felipe/Arquivos2/musicas", '*.mp3')):
                    # contar numero de musicas
                    Player_Musica.nmusicas = Player_Musica.nmusicas + 1
                    # nome da musica
                    print(Player_Musica.nmusicas, '°', basename(musica[:-4]).replace('_', ' '))
                    # adicionar a lista de reprodrução
                    Player_Musica.playlist.append(musica)

            except:

                print("Diretórios de músicas não encontrados!...")


        print("player mp3 inicializado...")


    def inicializar(self):
        mixer.init(frequency=Player_Musica.frequencia_som, size=-16, channels=2, buffer=5996)
        musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
        mp3 = mixer.Sound(Player_Musica.playlist[Player_Musica.rodando])
        mixer.music.set_volume(Player_Musica.volume)

    def iniciar(self):

        if mixer.get_init()==None:
            self.inicializar()
            mp3 = mixer.Sound(Player_Musica.playlist[Player_Musica.rodando])
            pos3 = time.strftime("%H:%M:%S", time.gmtime(mp3.get_length()))

            mixer_music.set_volume(Player_Musica.volume)
            mixer_music.play()
            mixer.music.pause()
        else:
            print("Mixer de audio ja inicializou...")

    def sair(self):
        mixer_music.stop()
        mixer.quit()
        print("Encerrando music_x player.....")



    def posicao(self):
        """
        Retorna
        :return:
        """
        global MUSIC_END
        print('evento: ', mixer_music.get_endevent())
        if mixer.music.get_busy():
            pos2 = time.strftime("%H:%M:%S", time.gmtime(mixer.music.get_pos() / 1000))
            return pos2
        else:
            pos2 = time.strftime("%H:%M:%S", time.gmtime(mixer.music.get_pos() / 1000))
            return pos2

    def play_pause(self):
        nome_musica = basename(Player_Musica.playlist[Player_Musica.rodando][:-4]).replace('_', ' ')
        situacao = {}
        tocando = mixer_music.get_busy()
        pos = self.posicao()
        if tocando == False:
            botao = 'Pause'
            situacao = nome_musica + ' - Tocando'
            mixer_music.unpause()
            print("Musica tocando")
            situacao = {'botao': botao, 'musica': situacao}
            print("posicao : ", pos)
            return situacao

        else:
            botao = 'Play'
            situacao = nome_musica + ' - Pause'
            mixer_music.pause()
            print("Musica em parad")
            situacao = {'botao': botao, 'musica': situacao}
            return situacao

    def reinicio(self):
        mixer_music.rewind()



    def config_volume(self,valor):

        valor
        mixer_music.set_volume(valor)
        print('volume: ', str(valor))

    def avancar_musica(self):
        if Player_Musica.rodando + 1 >= len(Player_Musica.playlist):
            mixer_music.stop
            Player_Musica.rodando = 0
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("if frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))
            nome_musica = basename(Player_Musica.playlist[Player_Musica.rodando][:-4]).replace('_', ' ')
            print("nome: ", nome_musica)
            return  nome_musica

        else:
            mixer_music.stop
            Player_Musica.rodando = Player_Musica.rodando + 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("else frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))
            nome_musica = basename(Player_Musica.playlist[Player_Musica.rodando][:-4]).replace('_', ' ')
            print("nome: ", nome_musica)
            return  nome_musica




    def voltar_musica(self):
        if Player_Musica.rodando <= 0:
            music_x = 0
            mixer_music.stop
            l = len(Player_Musica.playlist)
            Player_Musica.rodando = l - 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("frequênci atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', Player_Musica.playlist[Player_Musica.rodando])
            nome_musica = basename(Player_Musica.playlist[Player_Musica.rodando][:-4]).replace('_', ' ')

            print("nome: ", nome_musica)


        else:
            music_x = 0
            mixer_music.stop
            Player_Musica.rodando = Player_Musica.rodando - 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("frequênci atual:  ", Player_Musica.playlist)
            print(Player_Musica.rodando + 1, ' ', Player_Musica.playlist[Player_Musica.rodando])
            nome_musica = basename(Player_Musica.playlist[Player_Musica.rodando][:-4]).replace('_', ' ')
            print("nome: ", nome_musica)

        return nome_musica


    def tempo_segundos(self):
        temp = mixer_music.get_pos()
        print(temp)






