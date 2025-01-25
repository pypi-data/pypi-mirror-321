from argparse import ArgumentParser, Namespace
from sys import exit

class Args():
    def __init__(self) -> None:
        self.parser: ArgumentParser = ArgumentParser(
                                        prog='vertexdata',
                                        description='for feeding data of .obj files to a vertex buffer'
        )
        self.parser.add_argument(
            'obj_file', help='the file name of the .obj file'
        )
        self.parser.add_argument(
            'target_file', 
            help='[optional] enter the target file name', 
            default='',
            nargs='?'
        )
        self.parser.add_argument(
            '-nvn', '--no-vn',
            help='no normal data in output file',
            action='store_true',
            dest='no_normal_data'
        )
        self.parser.add_argument(
            '-nvt', '--no-vt',
            help='no vertex texture in output file',
            action='store_true',
            dest='no_texture_data'
        )
        self.args: Namespace = self.parser.parse_args()

        if not self.args.obj_file.endswith(".obj"):
            print(f"Expected .obj file, got: {self.args.obj_file}")
            exit()
        elif self.args.target_file and not self.args.target_file.endswith(".obj"):
            print(f"Expected .obj file, got: {self.args.target_file}")
            exit()