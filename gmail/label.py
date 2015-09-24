from mailbox import Mailbox

class Label(Mailbox):
    """
    Child of Mailbox class
    """
    @property
    def label_tree(self):
        if "label_tree" not in vars(self):
            vars(self)["label_tree"] = encode_utf7(self.name).split('/')
        return vars(self)["label_tree"]

    @label_tree.setter
    def label_tree(self, tree):
        if "label_tree" in vars(self):
            del vars(self)["label_tree"]
        self.name = decode__utf7(tree.join('/'))