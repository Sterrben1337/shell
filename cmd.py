import os
import shutil


class CMD:
    curr_dir: str

    def __init__(self,curr_dir):
        self.curr_dir = curr_dir

    def show_dir(self) -> None:
        count_1 = 0
        count_2 = 0
        print(f"Folder contents: {self.curr_dir}")
        for i in os.scandir(self.curr_dir):
            if i.is_dir():
                print(i)
                count_1 += 1
            if i.is_file():
                count_2 += 2
        print(f'Number of directories: {count_1}\nNumber of files: {count_2}')


    def change_dir(self, new_dir=None) -> None:
        if new_dir is None:
            if self.curr_dir != 'C:/':
                self.__change_dir()
            return
        try:
            if self.curr_dir[len(self.curr_dir) - 1] != '/':
                os.chdir(self.curr_dir + '/' + new_dir)
                self.curr_dir += '/'
            else:
                os.chdir(self.curr_dir + new_dir)

            self.curr_dir += new_dir
        except:
            print('there is no such directory')

    def __change_dir(self) -> None:
        index = -1
        for i in range(0, len(self.curr_dir)):
            if self.curr_dir[i] == '/':
                index = i

        if index != -1:
            os.chdir(self.curr_dir[:index])
            self.curr_dir = self.curr_dir[:index]

    def create_dir(self, name):
        try:
            os.mkdir(self.curr_dir + '/' + name)
        except:
            print(f"There is already a file with the same name {name}")

    def read_file(self, file_name):
        try:
            with open(self.curr_dir + '/' + file_name) as f:
                for i in f.readlines():
                    print(i, end='')
                print()
        except IOError:
            print('File not found!')

    def rename(self, name, new_name):
        try:
            os.rename(self.curr_dir + '/' + name, new_name)
        except:
            print('No such file or directory')

    def del_file(self, file_name):
        try:
            os.remove(self.curr_dir + '/' + file_name)
        except:
            print('No such file in this directory')

    def remove_dir(self, dir_name):
        try:
                if input('Delete it?\ny/n\n') == 'y':
                    shutil.rmtree(self.curr_dir + '/' + dir_name)
        except:
            print("No such directory")

    def __str__(self) -> str:
        return f'{self.curr_dir}>'

