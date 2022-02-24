link = StringVar()

Label (root, text = "Paste your link here: ", font = "arial 10 bold", bg = "gray").place(x=160, y=60)

link_enter = Entry(root, width = 70, textvariable = link).place(x=32, y=90)

def progress_bar():
    for i in range(5):
        root.update_idletasks()
        pb_1['value'] += 20
        time.sleep(0.1)
        txt['text'] = pb_1['value'], '%'

#function to download
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = "arial 10", bg="gray").place(x=180, y=210)
    progress_bar()

#progress bar
pb_1 = Progressbar(root, orient = HORIZONTAL, length=200, mode="determinate")
pb_1.place(x=170, y=250)

#text beside progress bar showing progress in percentage
txt = Label(root,text = '0%',bg = '#345',fg = '#fff')
txt.place(x=150 ,y=250 )

Button(root, text='DOWNLOAD', font = "arial 15 bold", bg = "yellow" , padx=2, pady=2, command=Downloader).place(x=180, y=150)

root.mainloop()
