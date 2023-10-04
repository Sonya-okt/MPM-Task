# Creating the functions
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')


def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')