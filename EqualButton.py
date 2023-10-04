# Equal, C and AC buttons
equal = Button(root, height=2, width=5, text='=', font=9, bg='Blue', command=lambda: submit(eqn_entry, entry_strvar))
equal.place(x=125, y=340)

clear = Button(root, height=2, width=5, text='C', font=9, bg='OrangeRed', command=lambda: entry_strvar.set(entry_strvar.get()[:-1]))
clear.place(x=195, y=110)

AC_btn = Button(root, height=2, width=5, text='AC', font=9, bg='Red', command=lambda: entry_strvar.set(''))
AC_btn.place(x=5, y=110)