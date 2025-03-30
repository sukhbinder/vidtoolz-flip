import vidtoolz
import subprocess
import os


def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)

    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_flip.mp4")


def flip_video(input_file, output_file, fliptype):
    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        # Define the FFmpeg command
        command = [
            "ffmpeg",
            "-i",
            input_file,
            "-vf",
            fliptype,
            "-c:a",
            "copy",
            output_file,
        ]

        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors during FFmpeg execution
        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg error: {result.stderr}")

        print(f"Video trimmed successfully! Output saved to '{output_file}'.")

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return output_file


def create_parser(subparser):
    parser = subparser.add_parser(
        "flip", description="Flip a vedio vertically or horizontally"
    )
    # Add subprser arguments here.
    parser.add_argument("input", type=str, help="Single file name")
    parser.add_argument(
        "-f",
        "--fliptype",
        type=str,
        default="vflip",
        choices=["vflip", "hflip"],
        help="Flip type vertical or horizontal (default: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file (default: %(default)s)",
        default=None,
    )
    return parser


class ViztoolzPlugin:
    """Flip a vedio vertically or horizontally"""

    __name__ = "flip"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        output = determine_output_path(args.input, args.output)
        outputfile = flip_video(args.input, output, args.fliptype)
        print("{} created.".format(outputfile))

    def hello(self, args):
        # this routine will be called when "vidtoolz "flip is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


flip_plugin = ViztoolzPlugin()
