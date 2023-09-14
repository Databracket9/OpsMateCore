import os
import yaml

class base_setup:

    def __init__(self):
        pass

    def project_def(self, project_name):
        base_directory = os.getcwd()

        if not os.path.exists(project_name):
            os.mkdir(project_name)

        file_path = os.path.join(base_directory, project_name, 'config.yaml')
        data = {
                "name": "Jay", 
                "projectName": project_name,
                "email":"databracket9@gmail.com"
                }
        with open(file=file_path, mode="w") as file:
            yaml.dump(data, file, default_flow_style=False)
            # file.write(
            #     '{"name": "Jay", "email":"databracket9@gmail.com"}'
            # )
        


        