from pynput.keyboard import Key, Listener
import simpleaudio
import os

PATH_TO_THIS_FILE = os.path.dirname(__file__)
type_sound = simpleaudio.WaveObject.from_wave_file(os.path.join(PATH_TO_THIS_FILE, 'sound.wav'))

def on_press(key):
    type_sound.play()
    

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()
    pass

if __name__ == '__main__':
    main()
    