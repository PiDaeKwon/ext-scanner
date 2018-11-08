

import argparse
import scan

__VERSION = "1.0"


def title():

    title = r"""
        ███████╗██╗  ██╗████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
        ██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
        █████╗   ╚███╔╝    ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
        ██╔══╝   ██╔██╗    ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
        ███████╗██╔╝ ██╗   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
        ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ by.daekp"""
    print(title)

def get_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version",
                        action="store_true",
                        help="Show current version of ext scanner.")
    parser.add_argument("-q", "--quiet",
                        action="store_true")
    parser.add_argument("-d", "--directory", required=True,
                        help="Enter the path to search.")

    return parser.parse_args()

def main():
    args = get_args()
    if args.version:
        print("Version:" + __VERSION)
        exit()
    if not args.quiet:
        title()
    if args.directory:
        input_dir = args.directory

    else:
        print("    Usage: ext_scanner.py -h")

    print("\n")

    return input_dir


if __name__ == '__main__':

    try:
        dir = main()
        file_count, wrongfile_count, wrongfile_list, notsupport_count, notsupport_ext = scan.scan(dir)

        print("\t- Total {} files scanned.\n".format(file_count))
        print("\t- The extensions of the \"{}\" files were confirmed to be modulated.".format(wrongfile_count))
        print("\t- The number of files that can not be verified because the extension is not supported is \"{}\".\n".format(notsupport_count))
        print("\t== Bad Extension File List == \n")
        for i in range(len(wrongfile_list)):
            print("\t" + wrongfile_list[i])
        print("\n\t== Unsupported extension  == \n")
        for i in range(len(notsupport_ext)):
            print("\t" + notsupport_ext[i])

 
    except KeyboardInterrupt:
        print("Interrupt received! Exiting cleanly...")
