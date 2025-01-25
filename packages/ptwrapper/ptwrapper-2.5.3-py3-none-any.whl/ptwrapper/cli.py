import os
import json
import sys
import glob
import shutil as sh
from argparse import ArgumentParser

from .utils import dict_to_html_table

from osve import osve

from .main import simulation

def cli(test=False):
    """
    CLI to resolve a PTR file and generate a SPICE CK kernel.

    Parameters
    ----------
    test : bool, optional
        If True, return the argument parser for testing (default is False).
    """
    parser = setup_parser()
    args = parser.parse_args()

    validate_arguments(args)

    with open(args.ptr, 'r') as p:
        ptr_content = p.read()

    session_file_path, root_scenario_path, ptr_log = process_simulation(
        args, ptr_content
    )

    if ptr_log == -1:
        print(f'[ERROR]   {"<PTWR>":<27} PTWrapper session ended with ERRORS. Check your input files.')
        if test:
            return parser
        sys.exit(-1)

    handle_output(args, ptr_log, root_scenario_path)

    if not args.no_cleanup:
        cleanup(root_scenario_path)

    print(f'[INFO]    {"<PTWR>":<27} PTWrapper session ended successfully')

    if test:
        return parser


def setup_parser():
    parser = ArgumentParser(
        description='Pointing Tool Wrapper (PTWrapper) simulates a PTR and generates the '
                    'corresponding resolved PTR, SPICE CK kernels, '
                    'and other attitude related files. PTWrapper uses OSVE to simulate the PTR.'
    )

    parser.add_argument("-m", "--meta-kernel", help="[MANDATORY] Path to the SPICE Meta-kernel (MK) file")
    parser.add_argument("-p", "--ptr", help="[MANDATORY] Path to the Pointing Timeline Request (PTR) file.")
    parser.add_argument("-w", "--working-dir", default=os.getcwd(),
                        help="Path to the working directory. Default is the current directory.")
    parser.add_argument("-o", "--output-dir", help="Path to the output directory. Default is the current directory.")
    parser.add_argument("-t", "--time-step", default=5, type=int,
                        help="Output CK file time step in seconds. Default is 5s.")
    parser.add_argument("-np", "--no-power", action="store_true",
                        help="Indicates not to calculate available power.")
    parser.add_argument("-sa", "--sa-ck", action="store_true", help="Generate the Solar Arrays SPICE CK.")
    parser.add_argument("-mga", "--mga-ck", action="store_true", help="Generate the Medium Gain Antenna SPICE CK.")
    parser.add_argument("-q", "--quaternions", action="store_true", help="Calculate the quaternions.")
    parser.add_argument("-f", "--fixed-definitions", action="store_true",
                        help="Print the AGM Fixed Definitions in use for PTR design.")
    parser.add_argument("-nc", "--no-cleanup", action="store_true",
                        help="Indicates not to cleanup the output directory.")
    parser.add_argument("-v", "--version", action="store_true",
                        help="Print OSVE, AGM, and EPS libraries version.")

    return parser


def validate_arguments(args):
    if args.version:
        display_versions()
        sys.exit(1)

    if args.fixed_definitions:
        display_fixed_definitions()
        sys.exit(1)

    if not args.meta_kernel or not os.path.exists(args.meta_kernel):
        raise ValueError(f'[ERROR]    {"<PTWR>":<27} Meta-kernel not provided or does not exist.')

    if not args.ptr:
        raise ValueError(f'[ERROR]    {"<PTWR>":<27} PTR/PTX file not provided.')

    _, ext = os.path.splitext(args.ptr)
    if ext.lower() not in ['.xml', '.ptx', '.ptr']:
        raise ValueError(f'[ERROR]    {"<PTWR>":<27} Invalid PTR file extension.')


def display_versions():
    the_osve = osve.osve()
    print("\nOSVE LIB VERSION:       ", the_osve.get_app_version())
    print("OSVE AGM VERSION:       ", the_osve.get_agm_version())
    print("OSVE EPS VERSION:       ", the_osve.get_eps_version(), "\n")


def display_fixed_definitions():
    fixed_definitions_path = os.path.join(
        os.path.dirname(__file__), "config/age", "cfg_agm_jui_fixed_definitions.xml"
    )
    try:
        with open(fixed_definitions_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'[ERROR]    {"<PTWR>":<27} Fixed definitions file not found.')
    except Exception as e:
        print(f'[ERROR]    {"<PTWR>":<27} An error occurred: {e}')


def process_simulation(args, ptr_content):
    return simulation(
        args.meta_kernel, ptr_content,
        working_dir=args.working_dir,
        time_step=args.time_step,
        no_power=args.no_power,
        sa_ck=args.sa_ck,
        mga_ck=args.mga_ck,
        quaternions=args.quaternions
    )


def handle_output(args, ptr_log, root_scenario_path):
    output_dir = os.path.abspath(args.output_dir) if args.output_dir else os.getcwd()
    ptr_file_name = os.path.splitext(os.path.basename(args.ptr))[0]

    if ptr_log:
        create_logs(output_dir, ptr_file_name, ptr_log)

    rename_output_files(args, root_scenario_path, output_dir, ptr_file_name)


def create_logs(output_dir, file_name, ptr_log):
    html_path = os.path.join(output_dir, f'{file_name}_ptr_log.html')
    json_path = os.path.join(output_dir, f'{file_name}_ptr_log.json')

    with open(html_path, 'w') as html_file:
        html_file.write(dict_to_html_table(ptr_log))

    with open(json_path, 'w') as json_file:
        json.dump(ptr_log, json_file)


def rename_output_files(args, root_path, output_dir, file_name):
    file_mapping = {
        'quaternions.csv': f'{file_name}_quaternions.csv',
        'juice_sa_ptr.bc': f'juice_sa_{file_name}.bc',
        'juice_mga_ptr.bc': f'juice_mga_{file_name}.bc',
        'power.csv': f'{file_name}_power.csv',
        'ptr_resolved.ptx': f'{file_name}_resolved.ptx',
        'juice_sc_ptr.bc': f'juice_sc_{file_name.lower()}_v01.bc',
        'log.json': f'{file_name}_osve_log.json'
    }

    for src, dest in file_mapping.items():
        src_path = os.path.join(root_path, 'output', src)
        if os.path.exists(src_path):
            dest_path = os.path.join(output_dir, dest)
            sh.move(src_path, dest_path)


def cleanup(root_path):
    paths_to_remove = [
        os.path.join(root_path, 'pt_temp_input'),
        os.path.join(root_path, 'pt_temp_outputs'),
        os.path.join(root_path, 'pt_temp_config'),
        os.path.join(root_path, 'pt_temp_kernels'),
        os.path.join(root_path, 'session_file.json')
    ]

    delete_files_and_directories(paths_to_remove)


def delete_files_and_directories(paths_to_remove):
    """
    Deletes files and directories matching the specified paths.

    Parameters:
    -----------
    paths_to_remove : list of str
        List of file patterns or paths to be deleted.
    """
    for path in paths_to_remove:
        for item in glob.glob(path):
            try:
                if os.path.isfile(item):
                    os.remove(item)  # Delete file
                elif os.path.isdir(item):
                    sh.rmtree(item)  # Delete directory
                else:
                    print(f'[ERROR]    {"<PTWR>":<27} Skipping unknown item: {item}')
            except PermissionError as e:
                print(f'[ERROR]    {"<PTWR>":<27} PermissionError: Unable to delete {item}. {e}')
            except Exception as e:
                print(f'[ERROR]    {"<PTWR>":<27} Unable to delete {item}. {e}')