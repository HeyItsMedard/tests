from app import App
from ui import UI


def main():
    app = App()
    ui = UI(app)
    ui.start()
    app.save()
    # print(vars(app))


if __name__ == "__main__":
    main()
