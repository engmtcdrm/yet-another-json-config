"""
Reading json files as a configuration file, supports nested json values
"""
import json
import os

class Config():
    """
    Configuration File class
    """

    def __init__(self, config_file_path: str):
        self.__settings = {}

        if os.path.exists(config_file_path) and os.path.isfile(config_file_path):
            self.__config_file_path = config_file_path

            self.__load()
        else:
            raise FileNotFoundError(f'Config File {config_file_path} does not exist.')

    def __load(self):
        """
        Loads the configuration file.
        """

        if os.path.exists(self.__config_file_path):
            # Open Config File, read the json information and close the file
            with open(self.__config_file_path, 'r', encoding = 'utf-8') as f:

                settings = json.loads(f.read())

            self.__settings = settings
        else:
            raise FileNotFoundError(f'Config File {self.__config_file_path} does not exist.')

    def save(self, indent = 4):
        """
        Saves the configuration file.
        """

        if self.__config_file_path is not None and os.path.isfile(self.__config_file_path):
            with open(self.__config_file_path, "w", encoding='utf-8') as out_file:
                json.dump(self.__settings, out_file, indent = indent)
        else:
            raise MissingConfigFileException('Config File must be set to save file.')

    def get(self, *keys: str):
        """
        Returns the specified setting.
        """

        if keys == ():
            raise KeyError('No key specified to get.')

        # convert based on being a tuple or not
        if type(keys[0]) == tuple:
            keys_list = list(*keys)
        else:
            keys_list = list(keys)

        if len(keys_list) == 0:
            raise KeyError('No key specified to get.')

        data = self.__settings

        last_key = keys_list[-1]

        if last_key == []:
            raise KeyError('No key specified to get.')

        # when assigning drill down to *second* last key
        for k in keys_list[:-1]:
            if k in data:
                data = data[k]
            else:
                raise KeyError(f'Setting {k} does not exist.')

        return data[last_key]

    def set(self, *keys: str, value):
        """
        Sets the specified setting.
        """

        if keys == ():
            raise KeyError('No key specified to set.')

        # convert based on being a tuple or not
        if type(keys[0]) == tuple:
            keys_list = list(*keys)
        else:
            keys_list = list(keys)

        if len(keys_list) == 0:
            raise KeyError('No key specified to set.')

        data = self.__settings

        last_key = keys_list[-1]

        if last_key == []:
            raise KeyError('No key specified to set.')

        # when assigning drill down to *second* last key
        for k in keys_list[:-1]:
            if k in data:
                data = data[k]
            else:
                raise KeyError(f'Setting {k} does not exist.')

        data[last_key] = value

    def delete(self, *keys: str):
        """
        Deletes the specified setting from the configuration if it exists.
        """

        if keys == ():
            raise KeyError('No key specified for delete.')

        # convert based on being a tuple or not
        if type(keys[0]) == tuple:
            keys_list = list(*keys)
        else:
            keys_list = list(keys)

        if len(keys_list) == 0:
            raise KeyError('No key specified for delete.')

        data = self.__settings

        last_key = keys_list[-1]

        if last_key == []:
            raise KeyError('No key specified for delete.')

        # when assigning drill down to *second* last key
        for k in keys_list[:-1]:
            if k in data:
                data = data[k]
            else:
                raise KeyError(f'Setting {k} does not exist.')

        if last_key in data:
            del data[last_key]
        else:
            raise KeyError(f'Setting {last_key} does not exist and cannot be deleted.')

        print(self.__settings)

    def settings(self):
        """
        Returns the current configuration settings.
        """
        return self.__settings

    def __str__(self):
        return str(self.__settings)

    def __repr__(self):
        return str(self.__settings)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, item, value):
        self.set(item, value=value)

    def __delitem__(self, item):
        self.delete(item)

    def __len__(self):
        return len(self.__settings)

    def __contains__(self, item):
        if item in self.__settings:
            return True
        else:
            return False

class Settings():

    def __init__(self, settings: str= {}):
        self.__settings = settings

    def get(self, *keys: str):
        """
        Returns the specified setting.
        """

        if keys == ():
            raise KeyError('No key specified to get.')

        # convert based on being a tuple or not
        if type(keys[0]) == tuple:
            keys_list = list(*keys)
        else:
            keys_list = list(keys)

        if len(keys_list) == 0:
            raise KeyError('No key specified to get.')

        data = self.__settings

        last_key = keys_list[-1]

        if last_key == []:
            raise KeyError('No key specified to get.')

        # when assigning drill down to *second* last key
        for k in keys_list[:-1]:
            if k in data:
                data = data[k]
            else:
                raise KeyError(f'Setting {k} does not exist.')

        return data[last_key]

    def set(self, *keys: str, value):
        """
        Sets the specified setting.
        """

        if keys == ():
            raise KeyError('No key specified to set.')

        # convert based on being a tuple or not
        if type(keys[0]) == tuple:
            keys_list = list(*keys)
        else:
            keys_list = list(keys)

        if len(keys_list) == 0:
            raise KeyError('No key specified to set.')

        data = self.__settings

        last_key = keys_list[-1]

        if last_key == []:
            raise KeyError('No key specified to set.')

        # when assigning drill down to *second* last key
        for k in keys_list[:-1]:
            if k in data:
                data = data[k]
            else:
                raise KeyError(f'Setting {k} does not exist.')

        data[last_key] = value

    def delete(self, *keys: str):
        """
        Deletes the specified setting from the configuration if it exists.
        """

        if keys == ():
            raise KeyError('No key specified for delete.')

        # convert based on being a tuple or not
        if type(keys[0]) == tuple:
            keys_list = list(*keys)
        else:
            keys_list = list(keys)

        if len(keys_list) == 0:
            raise KeyError('No key specified for delete.')

        data = self.__settings

        last_key = keys_list[-1]

        if last_key == []:
            raise KeyError('No key specified for delete.')

        # when assigning drill down to *second* last key
        for k in keys_list[:-1]:
            if k in data:
                data = data[k]
            else:
                raise KeyError(f'Setting {k} does not exist.')

        if last_key in data:
            del data[last_key]
        else:
            raise KeyError(f'Setting {last_key} does not exist and cannot be deleted.')

        print(self.__settings)

    def settings(self):
        """
        Returns the current configuration settings.
        """
        return self.__settings

    def __str__(self):
        return str(self.__settings)

    def __repr__(self):
        return str(self.__settings)

    def __getattr__(self, item):
        return self.get(item)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, item, value):
        self.set(item, value=value)

    def __delitem__(self, item):
        self.delete(item)

    def __len__(self):
        return len(self.__settings)

    def __contains__(self, item):
        if item in self.__settings:
            return True
        else:
            return False

class MissingConfigFileException(Exception):
    """
    Raises an exception when Config file is missing
    """
    pass