import os
from cmd import CMD

def init():
    test = CMD(r'C:/')
    os.chdir(test.curr_dir)
    while True:
        print(test, end = " ")
        com = input().strip().split()
        try:
            match com[0]:
                case 'dir':
                    test.show_dir()
                case 'cd':
                    if com[1] == '..':
                        test.change_dir()
                    else:
                        test.change_dir(com[1])
                case 'rm':
                    test.remove_dir(com[1])
                case 'del':
                    test.del_file(com[1])
                case 'ren':
                    test.rename(com[1], com[2])
                case 'read':
                    test.read_file(com[0])
                case 'crdir':
                    test.create_dir(com[1])
                case _:
                    print('Invalid command!')
        except IndexError:
            print('Incorrect command')
            pass



if __name__ == '__main__':
    init()