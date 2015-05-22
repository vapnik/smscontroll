__author__ = 'vapnik'


class BaseLogger():
    list = []

    def log(self, text):
        self.list.append(text)

    def get_last(self):
        return self.list.pop()

    def get_list(self):
        return self.list

    def show_last(self):
        print(self.get_last())

    def show_all(self):
        for index in range(len(self.list)):
            print(self.list[index])
            self.list.clear()