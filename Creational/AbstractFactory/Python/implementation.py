from abc import ABC, abstractmethod

class CheckBox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class WindowsCheckBox(CheckBox):
    def render(self) -> str:
        return "Rendering a Windows CheckBox"

class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering a Windows Button"

class MacOSCheckBox(CheckBox):
    def render(self) -> str:
        return "Rendering a MacOS CheckBox"

class MacOSButton(Button):
    def render(self) -> str:
        return "Rendering a MacOS Button"

class GUIFactory(ABC):
    @abstractmethod
    def create_check_box(self) -> CheckBox:
        pass

    @abstractmethod
    def create_button(self) -> Button:
        pass

class WindowsFactory(GUIFactory):
    def create_check_box(self) -> CheckBox:
        return WindowsCheckBox()

    def create_button(self) -> Button:
        return WindowsButton()

class MacOSFactory(GUIFactory):
    def create_check_box(self) -> CheckBox:
        return MacOSCheckBox()

    def create_button(self) -> Button:
        return MacOSButton()

def application(factory: GUIFactory) -> None:
    check_box = factory.create_check_box()
    button = factory.create_button()
    print(check_box.render())
    print(button.render())           

if __name__ == "__main__":
    os_type = "Windows"  # Change to "MacOS" to test MacOSFactory

    if os_type == "Windows":
        factory = WindowsFactory()
    else:
        factory = MacOSFactory()

    application(factory)