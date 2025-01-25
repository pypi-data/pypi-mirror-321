from json import load, dump
from os import path, getcwd

from .json_attributdict import AttributDict

class setup():



    def __init__(self, paths: dict[str: str], encode: str = 'utf-8', newline: str = ''):
        """
        Init datas
        :param paths:> ``key`` : str, ``value`` : path of the file.
        :param encode: File encoding for write and read. Default 'utf-8'
        :param newline: The new line in the file. Default ''
        """

        self.__proprietes_dynamiques = {}
        self.paths = paths
        self.encode = encode
        self.newline = newline

        for i in paths.keys():
            self.__load_json(i, paths[i])


    def add_file(self, name: str, path: str) -> None:
        """
        Add files append to init paths files
        :param name: the name to find the file (attribute) in the setup class
        :param path: the path (absolute or not)
        :return: None
        """
        self.__load_json(name, path)


    def delete_files(self, *names: str) -> None:
        """
        Delete all charged file in the class
        :param names: names given to files in the init or with add_file function
        :return: None
        """
        for name in names:
            self.__unload_json(name)



    def __read_file(self, file_path):
        with open(file_path, 'r', encoding=self.encode, newline=self.newline, errors='ignore') as f:
            file = load(f)
            return file

    def __load_json(self, name: str, path_: str):
        """
        Load json file in the class
        :param name: the name associated to the file
        :param path_: the json file path
        :return:
        """
        if not path.isabs(path_):
            # Conserver le chemin relatif à l'utilisateur
            file_path = path.join(getcwd(), path_)
        else:
            # Utiliser directement le chemin absolu
            file_path = path_

        file = self.__read_file(file_path=file_path)

        self.__proprietes_dynamiques[name] = AttributDict(file)


    def __unload_json(self, name: str) -> None:
        """
        Unload json file in the class
        :param name: the name associated to the file
        :return: None
        """
        if name not in self.__proprietes_dynamiques.keys():
            raise NameError(f"'{name}' file not found !")

        del self.__proprietes_dynamiques[name]


    def __getattr__(self, key):

        # Cette méthode est appelée uniquement si l'attribut n'est pas trouvé normalement
        if key in self.__proprietes_dynamiques:
            return self.__proprietes_dynamiques[key]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")


    def __delattr__(self, item):
        if item in self.__proprietes_dynamiques:
            del self.__proprietes_dynamiques[item]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{item}'")

    def __get_path(self, _path: str)->str:
        """
        Renvoie le chemin complet
        :param _path: un chemin d'accès
        :return:
        """
        if not path.isabs(_path):
            # Conserver le chemin relatif à l'utilisateur
            return path.join(getcwd(), _path)

        return _path

    def write(self)->None:
        """
        Write all files if a modification is detected.
        :return: None
        """
        for i in self.paths.keys():

            file_path = self.__get_path(self.paths[i])

            if self.__read_file(file_path) == self.__proprietes_dynamiques[i]:
                pass

            else:
                with open(file_path, 'w', encoding=self.encode, newline=self.newline, errors='ignore') as f:
                    dump(self.__proprietes_dynamiques[i], f, indent=2)


