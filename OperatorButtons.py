# Operator Buttons
add = Button(root, height=2, width=5, text='+', font=9, bg='DarkOrange', command=lambda: add_text('+', entry_strvar))
add.place(x=195, y=340)

subtract = Button(root, height=2, width=5, text='-', font=9, bg='DarkOrange', command=lambda: add_text('-', entry_strvar))
subtract.place(x=195, y=280)

multiply = Button(root, height=2, width=5, text='x', font=9, bg='DarkOrange', command=lambda: add_text('*', entry_strvar))
multiply.place(x=195, y=225)

divide = Button(root, height=2, width=5, text='/', bg='DarkOrange', font=9, command=lambda: add_text('/', entry_strvar))
divide.place(x=195, y=170)

decimal = Button(root, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar))
decimal.place(x=65, y=340)

bracket_open = Button(root, height=2, width=5, text='(', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar))
bracket_open.place(x=65, y=110)

bracket_close = Button(root, height=2, width=5, text=')', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar))
bracket_close.place(x=125, y=110)