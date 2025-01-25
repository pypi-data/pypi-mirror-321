import json
import os
import shutil
import re

from osve.osve_subscriber import OsvePtrAbstract

def copy_with_full_permissions(src, dest):
    """
    Copies a file from `src` to `dest` and ensures that the copied file
    has full permissions (read, write, and execute for all users).
    """
    # Copy the file
    shutil.copy(src, dest)

    # Set full permissions for the copied file
    os.chmod(dest, 0o777)  # Full read, write, and execute permissions for all users


def create_structure(parent_path, metakernel_path='input_mk.tm', ptr_content='input_ptr.ptx', step=5, no_power=False,
                     sa_ck=False, mga_ck=False, quaternions=False):
    """
    Create the structure and contents for an OSVE session folder.

    Parameters
    ----------
    parent_path : str
        Path to the parent folder where the structure will be created.

    metakernel_path : str, optional
        Path to an existing and valid metakernel file (default is 'input_mk.tm').

    ptr_content : str, optional
        Content for the PTR file (default is 'input_ptr.ptx').

    step : int, optional
        Time step for the simulation configuration (default is 5).

    no_power : bool, optional
        If True, disables power-related configurations in the session file (default is False).

    sa_ck : bool, optional
        If True, enables Solar Array CK file output (default is False).

    mga_ck : bool, optional
        If True, enables MGA CK file output (default is False).

    quaternions : bool, optional
        If True, includes attitude quaternion data in the output (default is False).

    Returns
    -------
    str
        The absolute path to the generated session file.

    Note
    ----
    This function organizes files and creates necessary configurations for an OSVE session,
    including the kernel and input/output file structures. It also adjusts the session JSON
    based on the provided options.
    """
    crema_id = crema_identifier(metakernel_path)

    session_json_filepath = os.path.join(
        os.path.dirname(__file__), "config", "session_file.json"
    )

    agm_config_filepath = os.path.join(
        os.path.dirname(__file__), "config", "age", "cfg_agm_jui.xml"
    )

    fixed_definitions_filepath = os.path.join(
        os.path.dirname(__file__), "config", "age", "cfg_agm_jui_fixed_definitions.xml"
    )

    predefined_blocks_filepath = os.path.join(
        os.path.dirname(__file__), "config", "age", "cfg_agm_jui_predefined_block.xml"
    )

    event_definitions_filepath = os.path.join(
        os.path.dirname(__file__), "config", "age", "cfg_agm_jui_event_definitions.xml"
    )

    bit_rate_filepath = os.path.join(
        os.path.dirname(__file__), "config", "ise", "BRF_MAL_SGICD_2_1_300101_351005.brf"
    )

    eps_config_filepath = os.path.join(
        os.path.dirname(__file__), "config", "ise", "eps.cfg"
    )

    eps_events_filepath = os.path.join(
        os.path.dirname(__file__), "config", "ise", "events.juice.def"
    )

    sa_cells_count_filepath = os.path.join(
        os.path.dirname(__file__), "config", "ise", "phs_com_res_sa_cells_count.asc"
    )

    sa_cells_efficiency_filepath = os.path.join(
        os.path.dirname(__file__), "config", "ise", "RES_C50_SA_CELLS_EFFICIENCY_310101_351003.csv"
    )

    eps_units_filepath = os.path.join(
        os.path.dirname(__file__), "config", "ise", "units.def"
    )

    itl_downlink_filepath = os.path.join(
        os.path.dirname(__file__), "input", "itl", "downlink.itl"
    )

    itl_platform_filepath = os.path.join(
        os.path.dirname(__file__), "input", "itl", "platform.itl"
    )

    itl_tbd_filepath = os.path.join(
        os.path.dirname(__file__), "input", "itl", "TBD.itl"
    )

    itl_top_timelines_filepath = os.path.join(
        os.path.dirname(__file__), "input", "itl", "TOP_timelines.itl"
    )

    edf_spc_link_kab_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "EDF_JUI_SPC_LINK_KAB.edf"
    )

    edf_spc_link_xb_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "EDF_JUI_SPC_LINK_XB.edf"
    )

    edf_spacecraft_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "juice__spacecraft.edf"
    )

    edf_spacecraft_platform_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "juice__spacecraft_platform.edf"
    )

    edf_spacecraft_ssmm_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "juice__spacecraft_ssmm.edf"
    )

    edf_tbd_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "TBD.edf"
    )

    edf_top_experiments_filepath = os.path.join(
        os.path.dirname(__file__), "input", "edf", "TOP_experiments.edf"
    )

    evf_top_events_filepath = os.path.join(
        os.path.dirname(__file__), "input", f"TOP_{crema_id}_events.evf"
    )

    evf_downlink_filepath = os.path.join(
        os.path.dirname(__file__), "input", "downlink.evf"
    )

    evf_crema_filepath = os.path.join(
        os.path.dirname(__file__), "input", "evf", f"EVT_{crema_id.upper()}_GEOPIPELINE.EVF"
    )

    with open(session_json_filepath, "r") as session_json_file:
        session_json = json.load(session_json_file)

    # Paths for the execution
    config_dir = "pt_temp_config"
    input_dir = "pt_temp_input"
    kernel_dir = "pt_temp_kernels"
    output_dir = "pt_temp_outputs"

    age_config_path = os.path.join(parent_path, config_dir, "age")
    ise_config_path = os.path.join(parent_path, config_dir, "ise")
    os.makedirs(age_config_path, exist_ok=True)
    os.makedirs(ise_config_path, exist_ok=True)

    # age
    copy_with_full_permissions(agm_config_filepath, age_config_path)
    copy_with_full_permissions(fixed_definitions_filepath, age_config_path)
    copy_with_full_permissions(predefined_blocks_filepath, age_config_path)
    copy_with_full_permissions(event_definitions_filepath, age_config_path)
    # ise
    copy_with_full_permissions(bit_rate_filepath, ise_config_path)
    copy_with_full_permissions(eps_config_filepath, ise_config_path)
    copy_with_full_permissions(eps_events_filepath, ise_config_path)
    copy_with_full_permissions(sa_cells_count_filepath, ise_config_path)
    copy_with_full_permissions(sa_cells_efficiency_filepath, ise_config_path)
    copy_with_full_permissions(eps_units_filepath, ise_config_path)

    file_list = session_json["sessionConfiguration"]["attitudeSimulationConfiguration"][
        "kernelsList"
    ]["fileList"]

    file_list.append(
        {
            "fileRelPath": os.path.basename(metakernel_path),
            "description": f"{os.path.basename(metakernel_path)}",
        }
    )

    if not quaternions:
        del session_json['sessionConfiguration']['outputFiles']['txtAttitudeFilePath']
    if not sa_ck:
        del session_json['sessionConfiguration']['outputFiles']['ckSaFilePath']
        del session_json['sessionConfiguration']['outputFiles']['saDataFilePath']
    if not mga_ck:
        del session_json['sessionConfiguration']['outputFiles']['ckMgaFilePath']
        del session_json['sessionConfiguration']['outputFiles']['mgaDataFilePath']
    if no_power:
        del session_json['sessionConfiguration']['outputFiles']['powerFilePath']
        del session_json['sessionConfiguration']['outputFiles']['powerConfig']

    session_json['sessionConfiguration']['simulationConfiguration']['timeStep'] = step
    session_json['sessionConfiguration']['outputFiles']['ckConfig']['ckTimeStep'] = step
    session_json['sessionConfiguration']['inputFiles']['eventTimelineFilePath'] = f"TOP_{crema_id}_events.evf"

    kernel_path = os.path.join(parent_path, kernel_dir)
    os.makedirs(kernel_path, exist_ok=True)
    try:
        copy_with_full_permissions(metakernel_path, kernel_path)
    except (OSError, shutil.Error) as e:
        print(f'[ERROR]    {"<PTWR>":<27} An error occurred while copying the file: {e}')

    # Dump the ptr content
    ptr_folder_path = os.path.join(parent_path, input_dir)
    os.makedirs(ptr_folder_path, exist_ok=True)

    ptr_path = os.path.join(ptr_folder_path, "PTR_PT_V1.ptx")
    with open(ptr_path, encoding="utf-8", mode="w") as ptr_file:
        ptr_file.write(ptr_content)

    # Create the dummy ITL and EDF inputs
    itl_folder_path = os.path.join(parent_path, input_dir, "itl")
    os.makedirs(itl_folder_path, exist_ok=True)

    copy_with_full_permissions(itl_downlink_filepath, itl_folder_path)
    copy_with_full_permissions(itl_platform_filepath, itl_folder_path)
    copy_with_full_permissions(itl_tbd_filepath, itl_folder_path)
    copy_with_full_permissions(itl_top_timelines_filepath, itl_folder_path)

    edf_folder_path = os.path.join(parent_path, input_dir, "edf")
    os.makedirs(edf_folder_path, exist_ok=True)

    copy_with_full_permissions(edf_spc_link_kab_filepath, edf_folder_path)
    copy_with_full_permissions(edf_spc_link_xb_filepath, edf_folder_path)
    copy_with_full_permissions(edf_spacecraft_filepath, edf_folder_path)
    copy_with_full_permissions(edf_spacecraft_platform_filepath, edf_folder_path)
    copy_with_full_permissions(edf_spacecraft_ssmm_filepath, edf_folder_path)
    copy_with_full_permissions(edf_tbd_filepath, edf_folder_path)
    copy_with_full_permissions(edf_top_experiments_filepath, edf_folder_path)

    evf_folder_path = os.path.join(parent_path, input_dir, "evf")
    os.makedirs(evf_folder_path, exist_ok=True)

    copy_with_full_permissions(evf_top_events_filepath, ptr_folder_path)
    copy_with_full_permissions(evf_downlink_filepath, ptr_folder_path)
    copy_with_full_permissions(evf_crema_filepath, evf_folder_path)

    # Prepare the output folder
    output_path = os.path.join(parent_path, output_dir)
    os.makedirs(output_path, exist_ok=True)

    # Finally dump the session file
    session_file_path = os.path.abspath(os.path.join(parent_path, "session_file.json"))
    with open(session_file_path, "w") as session_json_file:
        json.dump(session_json, session_json_file, indent=2)

    return session_file_path


def get_base_path(rel_path, root_path):
    """
    Generate the absolute path of a relative path based on the provided root directory.

    Parameters
    ----------
    rel_path : str
        The relative path that needs to be converted into an absolute path.

    root_path : str
        The root directory from which the relative path should be resolved. If it's already
        an absolute path, `rel_path` is returned unchanged.

    Returns
    -------
    str
        The absolute path computed based on the relative path and root directory.

    """
    return rel_path if os.path.isabs(root_path) \
                    else os.path.abspath(os.path.join(root_path, rel_path))


def crema_identifier(metakernel_path):
    """
    Extract the JUICE Crema identifier from a metakernel file.

    This function scans the metakernel file for the pattern 'juice_events_*_vXX.tf' and
    extracts the portion between 'juice_events_' and '_v'. If multiple identifiers are
    found, a warning is printed, and the first one is used.

    Parameters
    ----------
    metakernel_path : str
        The path to the metakernel file from which the identifier will be extracted.

    Returns
    -------
    str
        The JUICE Crema identifier extracted from the file. If no identifier is found,
        an empty string is returned.
    """
    # Define the pattern with a capturing group around '.*'
    pattern = r'juice_events_(.*)_v\d{2}\.tf'  # The part between juice_events_ and _v is captured

    # Open the file and read its content
    with open(metakernel_path, 'r') as file:
        content = file.read()

    # Find all occurrences of the pattern and capture the part that matches '.*'
    matches = re.findall(pattern, content)

    if len(matches) > 1:
        print(f'[WARNING] {"<PTWR>":<27} More than one JUICE Crema reference found, {matches[0]} will be used')
    elif len(matches) == 0:
        print(f'[WARNING] {"<PTWR>":<27} No JUICE Crema reference found: eclipses not taken into account.')
        return ''
    return matches[0]


def dict_to_html_table(data_dict):
    """
    Generate an HTML table representation of a dictionary containing PTR debugging logs.

    This function takes a nested dictionary of PTR logs and transforms it into an HTML table format.
    The generated HTML includes error messages styled according to their severity (e.g., 'error',
    'warning', 'info') and is formatted for clarity using a clean and modern design.

    Parameters
    ----------
    data_dict : dict
        A dictionary structured with keys, each containing blocks
        of observations. Each block has the following fields: 'observation', 'start_time',
        'end_time', and a list of 'error_messages'. Each error message includes 'time', 'severity',
        and 'text' attributes.

    Returns
    -------
    str
        A string representing the HTML content with a structured table for PTR debugging logs.
    """

    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>PTR Debugging Log</title>
<style>
    body {
        font-family: 'Roboto', sans-serif; /* Change font to Roboto */
        background-color: #f0f0f5;
        color: #444;
        margin: 10;
        padding: 10;
    }
    h1 {
        text-align: left; /* Left alignment */
        color: #2c3e50;
        font-size: 24px;
        margin-top: 20px;
    }
    h2, h3 {
        color: #34495e;
        font-size: 18px;
        margin-top: 20px;
    }
    table {
        width: 90%;
        margin: 20px 0 20px 20px; /* Left-aligned margin */
        border-collapse: collapse;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        background-color: white;
        border-radius: 5px;
        overflow: hidden;
    }
    th {
        background-color: #2980b9;
        color: #fff;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-align: left; /* Ensure header text is also left-aligned */
    }
    td {
        border-bottom: 1px solid #ddd;
        text-align: left; /* Ensure text is aligned to the left */
    }
    tr:last-child td {
        border-bottom: none;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .error {
        color: #e74c3c;
    }
    .warning {
        color: #f39c12;
    }
    .info {
        color: #3498db;
    }
    table th, table td {
        border: none;
    }
    .table-header {
        background-color: #2980b9;
        color: white;
    }

    /* Adjustments for column widths */
    td:first-child {
        width: 200px; /* First column width */
        text-align: left !important; /* Force left alignment with !important */
    }
    td:nth-child(2) {
        width: 100px; /* Second column width */
        text-align: left !important; /* Force left alignment with !important */
    }
    td:nth-child(3) {
        width: auto; /* Third column takes the remaining space */
        text-align: left !important; /* Force left alignment with !important */
    }
</style>



</head>
    <body>
        <h1>PTR Debugging Log</h1>
    '''

    # Loop through SOC, then blocks
    for designer_key, designer_value in data_dict.items():
        html_content += f'<h2>{designer_key}</h2>'

        # Loop through blocks within SOC
        for block_key, block_value in designer_value.items():
            html_content += f'<h3>{block_key} - {block_value["observation"]} [{block_value["start_time"]} - {block_value["end_time"]}] </h3>'

            # Add error messages
            # html_content += '<tr><td>Error Messages</td><td><table>'
            html_content += '<table>'
            for error in block_value["error_messages"]:
                severity_class = error['severity'].lower()  # Use the severity for styling
                html_content += f'''
                <tr class="{severity_class}">
                    <td>{error["time"]}</td>
                    <td>{error["severity"]}</td>
                    <td>{error["text"]}</td>
                </tr>
                '''
            html_content += '</table></td></tr>'
            html_content += '</table><br>'

    # Close the HTML document
    html_content += '''
    </body>
    </html>
    '''

    return html_content


class OsvePtrLogger(OsvePtrAbstract):
    """
    A logger class that captures and logs PTR (Pointing Timeline Request) block data, extending
    from the OsvePtrAbstract class.

    Attributes
    ----------
    blocks_data : list
        A list that stores block data for each logged block in the PTR.
    """
    blocks_data = []

    def __init__(self):
        """
        Initializes the logger by invoking the parent class's constructor and setting
        the logger name to 'theOsvePtrLogger'.
        """
        super().__init__("theOsvePtrLogger")

    def onPtrBlockEnd(self, blockData) -> int:
        """
        Appends the block data to the logger's list when a block ends.

        Parameters
        ----------
        blockData : dict
            A dictionary containing the data for a completed PTR block.

        Returns
        -------
        int
            Always returns 0, indicating successful logging of the block.
        """
        self.blocks_data.append(blockData)
        return 0

    def log(self, verbose=False):
        """
        Processes and logs block data, focusing on blocks containing errors,
        and generates a log summary.
        """
        ptr_log = {}
        idx = 1

        for block_data in self.blocks_data:
            if self._has_errors(block_data):
                if block_data["block_type"] != "SLEW":
                    self._process_standard_block(block_data, ptr_log, idx, verbose)
                else:
                    self._process_slew_block(block_data, ptr_log, idx, verbose)
            idx += 1

        return ptr_log

    def _has_errors(self, block_data):
        """
        Checks if the block contains any error logs.
        """
        return any(log["severity"] == "ERROR" for log in block_data.get("block_logs", []))

    def _process_standard_block(self, block_data, ptr_log, idx, verbose):
        """
        Processes a standard (non-SLEW) block and updates the log.
        """
        designer, designer_obs = self._get_designer_and_obs(block_data)
        if verbose:
            self._print_block_summary(idx, designer, designer_obs, block_data["block_start"], block_data["block_end"])

        error_messages = self._extract_error_messages(block_data, verbose)

        if designer not in ptr_log:
            ptr_log[designer] = {}
        ptr_log[designer][f"Block ({idx})"] = {
            "observation": designer_obs,
            "start_time": str(block_data["block_start"]),
            "end_time": str(block_data["block_end"]),
            "error_messages": error_messages,
        }

    def _process_slew_block(self, block_data, ptr_log, idx, verbose):
        """
        Processes a SLEW block and updates the log.
        """
        prev_info = self._get_slew_context(idx - 2, default_designer="SOC")
        next_info = self._get_slew_context(idx, default_designer="SOC")

        if verbose:
            self._print_slew_summary(idx, prev_info, next_info)

        error_messages = self._extract_error_messages(block_data, verbose)

        if prev_info and isinstance(prev_info, dict) and "designer" in prev_info:
            self._update_slew_log(ptr_log, prev_info, next_info, idx, error_messages)
        else:
            print(f'[WARNING] {"<PTWR>":<27} The SLEW block {idx-1} cannot be logged.')


    def _get_designer_and_obs(self, block_data):
        """
        Extracts the designer and observation details from the block data.
        """
        if "observations" in block_data:
            designer = block_data["observations"]["designer"]
            observations = block_data["observations"]["observations"]
            for observation in observations:
                if observation["unit"] == designer:
                    return designer, observation["definition"]
        return "SOC", f'{block_data["block_type"]} {block_data["block_mode"]}'

    def _extract_error_messages(self, block_data, verbose):
        """
        Extracts error messages from the block logs.
        """
        error_messages = []
        for log_data in block_data.get("block_logs", []):
            if log_data["severity"] != "DEBUG" and log_data["module"] == "AGM":
                error_message = f"      {log_data['severity']} , {log_data['time']} , {log_data['text']}"
                if verbose:
                    print(error_message)
                error_messages.append({
                    "severity": log_data["severity"],
                    "time": log_data["time"],
                    "text": log_data["text"],
                })
        return error_messages

    def _get_slew_context(self, index, default_designer="SOC"):
        """
        Gets context (designer, observation, and time) for a SLEW block.
        """
        try:
            block = self.blocks_data[index]
            designer = block["observations"]["designer"]
            observations = block["observations"]["observations"]
            for observation in observations:
                if observation["unit"] == designer:
                    return {
                        "designer": designer,
                        "obs": observation["definition"],
                        "time": str(block["block_end"]) if index < len(self.blocks_data) - 1 else str(
                            block["block_start"]),
                    }
        except (IndexError, KeyError):
            return {
                "designer": default_designer,
                "obs": f'{self.blocks_data[index]["block_type"]} {self.blocks_data[index]["block_mode"]}',
                "time": str(self.blocks_data[index]["block_start"]),
            }

    def _update_slew_log(self, ptr_log, prev_info, next_info, idx, error_messages):
        """
        Updates the log for a SLEW block.
        """
        if prev_info["designer"] not in ptr_log:
            ptr_log[prev_info["designer"]] = {}
        ptr_log[prev_info["designer"]][f"Block ({idx - 1}) SLEW AFTER"] = {
            "observation": prev_info["obs"],
            "start_time": prev_info["time"],
            "end_time": next_info["time"],
            "error_messages": error_messages,
        }

        if next_info["designer"] not in ptr_log:
            ptr_log[next_info["designer"]] = {}
        ptr_log[next_info["designer"]][f"Block ({idx + 1}) SLEW BEFORE"] = {
            "observation": next_info["obs"],
            "start_time": prev_info["time"],
            "end_time": next_info["time"],
            "error_messages": error_messages,
        }

    def _print_block_summary(self, idx, designer, designer_obs, start_time, end_time):
        """
        Prints a summary of a standard block.
        """
        print(f"BLOCK {idx} | {designer} | {designer_obs} | {start_time} - {end_time}")

    def _print_slew_summary(self, idx, prev_info, next_info):
        """
        Prints a summary of a SLEW block.
        """
        print(
            f"BLOCK {idx} | {prev_info['designer']},{next_info['designer']} | SLEW | "
            f"{prev_info['time']} ({prev_info['obs']}) - {next_info['time']} ({next_info['obs']})"
        )
