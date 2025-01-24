

def show(filename):
    import importlib.resources as pkg_resources
    from IPython.display import display, Image
    package = "varr_0.theory"
    filename += '.png'
    try:
        with pkg_resources.path(package, filename) as file_path:
            img = Image(filename=str(file_path))
            display(img)
    except Exception as e:
        print(f'Неправильное имя файла: {e}')
    return filename



def show_pdf(filename):
    import importlib.resources as pkg_resources
    from IPython.display import display, IFrame
    package = "varr_0.theory"
    filename += '.pdf'
    try:
        with pkg_resources.path(package, filename) as file_path:
            # Создаем IFrame для отображения PDF
            pdf_iframe = IFrame(src=str(file_path), width=1000, height=800)
            display(pdf_iframe)
    except Exception as e:
        print(f'Неправильное имя файла: {e}')
    return filename

def v():
    show('1')
    show('2')
    show('3')
    show('4')

