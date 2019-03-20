import os
import shutil
from pathlib import Path
from string import ascii_uppercase


class DirUtil:

    def __init__(self):
        pass

    def get_immediate_subdirectories(self, a_dir):
        """
        Method for listing all immediate subdirectories

        Arguments:
            a_dir {str} -- directory name

        Returns:
            [list] -- List of all immediate subdirectories
        """

        return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

    def get_all_files_count(self, a_dir):
        """
            Number of files in a directory
        Arguments:
            a_dir {str} -- directory name

        Returns:
            [int] -- count of files
        """

        files = [name for name in os.listdir(a_dir)]
        return len(files)

    def get_files_in_directory(self, directory, absolute_path=False):
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(directory) if isfile("{}/{}".format(directory, f))]

        if not absolute_path:
            return onlyfiles

        else:
            return ["{}/{}".format(directory, file_) for file_ in onlyfiles]

    def create_directory(self, directory_path):
        import os
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    def copy_file(self, source_file, destination_dir):
        shutil.copy2(source_file, destination_dir)

    def copy_file_to_another_file(self, source_file, target_file):
        shutil.copyfile(source_file, target_file)

    def get_files_in_directories_recursively(self, directory):
        files_list = list()

        for path, subdirs, files in os.walk(directory):
            for file_name in files:
                file_path = "{}/{}".format(path, file_name)
                files_list.append(file_path)

        return files_list

    def get_folders_in_directories_recursively(self, directory, index=0):
        folder_list = list()
        parent_directory = directory

        for path, subdirs, _ in os.walk(directory):
            if not index:
                for sdirs in subdirs:
                    folder_path = "{}/{}".format(path, sdirs)
                    folder_list.append(folder_path)
            elif path[len(parent_directory):].count('/') + 1 == index:
                for sdirs in subdirs:
                    folder_path = "{}/{}".format(path, sdirs)
                    folder_list.append(folder_path)

        return folder_list

    def create_directory_with_timestamp(self, directory_path):
        import time, os
        folder_name = str(int(time.time() * 1000000))

        output_folder_path = os.path.join(directory_path, folder_name)
        self.create_directory(output_folder_path)

        return output_folder_path

    def remove_files_in_folder(self, folder):
        try:
            files = DirUtil().get_files_in_directories_recursively(folder)
            for file in files:
                os.remove(file)
            return True, 'Success'
        except Exception as e:
            return False, str(e)

    def remove_subfolders_in_folder(self, folder, index=1):
        try:
            folders = DirUtil().get_folders_in_directories_recursively(folder, index=index)
            for folder in folders:
                shutil.rmtree(folder)
            return True, 'Success'
        except Exception as e:
            return False, str(e)

    def remove_directory(self, directory):
        if os.path.isdir(directory):
            shutil.rmtree(directory)


    def create_data_set_folders(self, directory):
        # create number directories
        for number in range(0,10):
            folder_name = "{}/{}".format(directory, number)
            self.create_directory(folder_name)


        # create uppercase alphabet directories
        for character in ascii_uppercase:
            folder_name = "{}/{}".format(directory, character)
            self.create_directory(folder_name)


    @staticmethod
    def get_file_extension(file_path):
        return Path(file_path).suffix

    @staticmethod
    def get_file_name_with_extension(file_path):
        return Path(file_path).name

    @staticmethod
    def get_file_name_without_ext(file_path):
        return Path(file_path).name.split('.')[0]

    @staticmethod
    def check_file_exists(file_path):
        return Path(file_path).is_file()
