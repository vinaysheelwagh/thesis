from os import walk, path, makedirs
from shutil import copy2 as cp


def get_files(base_dir):
    # Minmizing (halfing) list to just pre image files
    base_dir = path.join(base_dir, "images")
    files = [f for f in next(walk(base_dir))[2] if "pre" in f]

    return files


def move_files(files, base_dir, output_dir):
    for filename in files:
        disaster = filename.split("_")[0]

        # If the output directory and disater name do not exist make the directory
        if not path.isdir(path.join(output_dir, disaster)):
            makedirs(path.join(output_dir, disaster))

        # Check if the images directory exists
        if not path.isdir(path.join(output_dir, disaster, "images")):
            # If not create it
            makedirs(path.join(output_dir, disaster, "images"))

        # Move the pre and post image to the images directory under the disaster name
        cp(
            path.join(base_dir, "images", filename),
            path.join(output_dir, disaster, "images", filename),
        )
        post_file = filename.replace("_pre_", "_post_")
        cp(
            path.join(base_dir, "images", post_file),
            path.join(output_dir, disaster, "images", post_file),
        )

        # Check if the label directory exists
        if not path.isdir(path.join(output_dir, disaster, "labels")):
            # If not create it
            makedirs(path.join(output_dir, disaster, "labels"))

        pre_label_file = filename.replace("png", "json")
        # Move the pre and post label files to the labels directory under the disaster name
        cp(
            path.join(base_dir, "labels", pre_label_file),
            path.join(output_dir, disaster, "labels", pre_label_file),
        )
        post_label_file = pre_label_file.replace("_pre_", "_post_")
        cp(
            path.join(base_dir, "labels", post_label_file),
            path.join(output_dir, disaster, "labels", post_label_file),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="split_into_disasters.py: Splits files under a single directory (with images/ and labels/ into directory of disasters/images|labels for the base submission pipeline (copies files)"
    )
    parser.add_argument(
        "--input",
        required=True,
        metavar="/path/to/dataset/train",
        help="Full path to the train (or any other directory) with /images and /labels",
    )
    parser.add_argument(
        "--output",
        required=True,
        metavar="/path/to/output/xBD",
        help="Full path to the output root dataset directory, will create disaster/images|labels under this directory",
    )

    args = parser.parse_args()

    files = get_files(args.input)
    move_files(files, args.input, args.output)
