import PySimpleGUI as psg

label_a = psg.Text('Select Files to Compress: ')
input_a = psg.Input()
choose_btn_a = psg.FileBrowse('Choose')

label_b = psg.Text('Select Destination Folder: ')
input_b = psg.Input()
choose_btn_b = psg.FolderBrowse('Choose')


compress_btn = psg.Button('Compress')


window = psg.Window('File Compressor',
                    layout=[[label_a, input_a, choose_btn_a],
                            [label_b, input_b, choose_btn_b],
                            [compress_btn]])

window.read()
window.close()
