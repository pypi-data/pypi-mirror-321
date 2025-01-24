from pygubu.utils.widget import iter_menu
from pygubu.plugins.tk.tkstdwidgets import TKMenu, TKMenuitem, TKMenuitemSubmenu


class TkMenuBOPreview(TKMenu):
    ...


class TkMenuitemSubmenuBOPreview(TKMenuitemSubmenu):
    def realize(self, parent, extra_init_args: dict = None):
        widget = super().realize(parent, extra_init_args)
        uid = self.wmeta.identifier
        if not hasattr(self.widget, "preview_data"):
            self.widget.preview_data = {}
        self.widget.preview_data[uid] = {
            "index": self._index,
            "master": self.get_child_master(),
            }
        return widget

    def configure(self):
        print("here submenu")
        uid = self.wmeta.identifier
        if hasattr(self.widget, "preview_data"):
            master: tk.Menu = self.widget.preview_data[uid]["master"]
            index = self.widget.preview_data[uid]["index"]
            print("My index is:", index)
            print("master:", master)
            print("index type:", master.type(index))
            offset = 1 if master.cget("tearoff") else 0
            print("index+offset type:", master.type(index+offset))
            print(f"{offset=}")
            menu_properties = dict(
                (k, v)
                for k, v in self.wmeta.properties.items()
                if k in TKMenu.properties or k == "specialmenu"
            )
            print("menu prop:", menu_properties)
            self._setup_item_properties(menu_properties)
    
            item_properties = dict(
                (k, v)
                for k, v in self.wmeta.properties.items()
                if k in TKMenuitem.properties
            )
            print("item prop:", item_properties)
            self._setup_item_properties(item_properties)
            
            self.widget.configure(**menu_properties)
            master.entryconfigure(index+offset, **item_properties)
