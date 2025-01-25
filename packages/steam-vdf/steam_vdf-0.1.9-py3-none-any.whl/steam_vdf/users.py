#!/usr/bin/env python

import datetime
import json
import logging
import os
import platform

import vdf

from steam_vdf import utils

logger = logging.getLogger("cli")


def add_shortcut(args, selected_library):
    """
    Add a shortcut to the shortcuts.vdf file.
    """
    shortcuts_vdf = os.path.join(selected_library, "userdata")

    if not os.path.exists(shortcuts_vdf):
        logger.error("No userdata directory found at %s", shortcuts_vdf)
        print("No Steam user data found.")
        exit(1)

    user_dirs = [
        d
        for d in os.listdir(shortcuts_vdf)
        if os.path.isdir(os.path.join(shortcuts_vdf, d))
    ]

    if not user_dirs:
        logger.error("No Steam users found in userdata directory")
        print("No Steam users found.")
        exit(1)

    if len(user_dirs) > 1:
        user_names = get_steam_user_names(args, selected_library)
        print("\nMultiple Steam users found. Please choose one:")
        for idx, user_dir in enumerate(user_dirs, 1):
            user_info = user_names.get(
                user_dir,
                {
                    "PersonaName": "Unknown Account",
                    "AccountName": "Unknown Account",
                },
            )
            persona_name = user_info["PersonaName"]
            account_name = user_info["AccountName"]

            if account_name != "Unknown Account":
                print(f"{idx}. {user_dir} - {persona_name} ({account_name})")
            else:
                print(f"{idx}. {user_dir} - {persona_name}")

        while True:
            try:
                choice = int(input("\nEnter user number: ")) - 1
                if 0 <= choice < len(user_dirs):
                    user_dir = user_dirs[choice]
                    break
                else:
                    logger.info(
                        "Please enter a number between 1 and %s",
                        len(user_dirs),
                    )
            except ValueError:
                logger.info("Please enter a valid number")
    else:
        user_dir = user_dirs[0]
        user_names = get_steam_user_names(args, selected_library)
        account_name = user_names.get(user_dir, "Unknown Account")
        logger.info(f"Using only available user: {user_dir} ({account_name})")

    shortcuts_vdf = os.path.join(
        shortcuts_vdf, user_dir, "config", "shortcuts.vdf"
    )

    try:
        if os.path.exists(shortcuts_vdf):
            with open(shortcuts_vdf, "r", encoding="utf-8"):
                shortcuts = load_shortcuts_file(args, shortcuts_vdf)
                new_entry = add_shortcut_entry()
                if new_entry:
                    shortcuts = add_shortcut_to_shortcuts(shortcuts, new_entry)
                    if save_shortcuts(shortcuts_vdf, shortcuts):
                        logger.info("Shortcut added successfully")
                    else:
                        logger.error("Failed to save shortcuts")
    except Exception as e:
        logger.error("Error loading shortcuts.vdf: %s", e)
        exit(1)


def dump_vdf_to_json(args, vdf_data, vdf_path):
    """
    Dump VDF data to JSON file in /tmp directory
    The JSON filename will include the source directory (steamapps or config)
    """

    if not args.dump_vdfs:
        return

    if not args.dump_vdfs:
        return

    # Get the base filename and parent directory
    base_name = os.path.basename(vdf_path)
    parent_dir = os.path.basename(os.path.dirname(vdf_path))

    # If it's libraryfolders.vdf, use parent directory in name
    if base_name == "libraryfolders.vdf":
        json_filename = f"steam-{parent_dir}-vdf.json"
    else:
        # For other files (like loginusers.vdf), use the base name without .vdf
        json_filename = f"steam-{os.path.splitext(base_name)[0]}.json"

    json_path = os.path.join("/tmp", json_filename)

    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(vdf_data, f, indent=4)
        logger.info("VDF data ({base_name}) dumped to JSON at: %s", json_path)
        return True
    except Exception as e:
        logger.error("Error dumping VDF to JSON: %s", e)
        return False


def delete_shortcut(args, library_path):
    """
    Delete an existing shortcut after selecting user and shortcut
    """
    userdata_path = os.path.join(library_path, "userdata")
    if not os.path.exists(userdata_path):
        logger.error("No userdata directory found at: %s", userdata_path)
        return False

    user_dirs = [
        d
        for d in os.listdir(userdata_path)
        if os.path.isdir(os.path.join(userdata_path, d))
    ]

    if not user_dirs:
        logger.error("No Steam users found in userdata directory")
        return False

    user_names = get_steam_user_names(args, library_path)

    # Present user selection
    print("\nAvailable Steam users:")
    for idx, user_dir in enumerate(user_dirs, 1):
        user_info = user_names.get(
            user_dir,
            {
                "PersonaName": "Unknown Account",
                "AccountName": "Unknown Account",
            },
        )
        persona_name = user_info["PersonaName"]
        account_name = user_info["AccountName"]

        if account_name != "Unknown Account":
            print(f"{idx}. {persona_name} ({account_name})")
        else:
            print(f"{idx}. {persona_name}")

    # Get user selection
    while True:
        try:
            choice = input("\nEnter user number: ").strip()
            if not choice:
                logger.error("No user selected")
                return False

            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(user_dirs):
                selected_user = user_dirs[choice_idx]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            logger.info("\nOperation cancelled by user")
            return False

    shortcuts_vdf = os.path.join(
        userdata_path, selected_user, "config", "shortcuts.vdf"
    )

    if not os.path.exists(shortcuts_vdf):
        logger.error("No shortcuts.vdf file found")
        return False

    try:
        with open(shortcuts_vdf, "rb") as f:
            shortcuts = vdf.binary_load(f)

        if not shortcuts or "shortcuts" not in shortcuts:
            logger.error("No shortcuts found")
            return False

        # Show available shortcuts
        print("\nAvailable shortcuts:")
        print("-" * 50)

        shortcut_list = []
        for idx, shortcut in shortcuts["shortcuts"].items():
            shortcut_list.append((idx, shortcut))
            exe_path = shortcut.get("Exe", "Unknown").strip('"')
            start_dir = shortcut.get("StartDir", "Unknown").strip('"')
            print()
            print(
                f"{len(shortcut_list)}. {shortcut.get('AppName', 'Unknown')}:"
            )
            print(f"    Executable: {exe_path}")
            print(f"    Start Dir: {start_dir}")

        print("\n" + "-" * 50)

        # Get shortcut selection
        while True:
            try:
                choice = input(
                    "\nEnter number of shortcut to delete (or 'q' to quit): "
                ).strip()
                if choice.lower() == "q":
                    logger.info("Delete operation cancelled by user")
                    return False

                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(shortcut_list):
                    shortcut_id = shortcut_list[choice_idx][0]
                    shortcut_name = shortcuts["shortcuts"][shortcut_id].get(
                        "AppName", "Unknown"
                    )

                    # Confirm deletion
                    confirm = (
                        input(
                            f"\nAre you sure you want to "
                            f"delete '{shortcut_name}'? (y/N): "
                        )
                        .strip()
                        .lower()
                    )
                    if confirm != "y":
                        logger.info("Delete operation cancelled by user")
                        return False

                    # Delete the shortcut
                    del shortcuts["shortcuts"][shortcut_id]

                    # Save the modified shortcuts back to file
                    with open(shortcuts_vdf, "wb") as f:
                        vdf.binary_dump(shortcuts, f)

                    logger.info(
                        "Successfully deleted shortcut: %s", shortcut_name
                    )
                    print(f"\nSuccessfully deleted shortcut: {shortcut_name}")

                    # Dump updated shortcuts to JSON
                    json_path = os.path.join(
                        "/tmp", f"steam-shortcuts-{selected_user}.json"
                    )
                    with open(json_path, "w", encoding="utf-8") as f:
                        json.dump(shortcuts, f, indent=4)
                    logger.info(
                        "Updated shortcuts dumped to JSON at: %s", json_path
                    )

                    return True
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            except (KeyboardInterrupt, EOFError):
                logger.info("\nOperation cancelled by user")
                return False
            except Exception as e:
                logger.error("Error deleting shortcut: %s", e)
                return False

    except Exception as e:
        logger.error("Error reading shortcuts file: %s", e)
        return False


def list_shortcuts(args, library_path):
    """List existing non-Steam game shortcuts"""
    userdata_path = os.path.join(library_path, "userdata")
    if not os.path.exists(userdata_path):
        logger.error("No userdata directory found at: %s", userdata_path)
        return False

    user_dirs = [
        d
        for d in os.listdir(userdata_path)
        if os.path.isdir(os.path.join(userdata_path, d))
    ]

    if not user_dirs:
        logger.error("No Steam users found in userdata directory")
        return False

    user_names = get_steam_user_names(args, library_path)

    for user_dir in user_dirs:
        shortcuts_vdf = os.path.join(
            userdata_path, user_dir, "config", "shortcuts.vdf"
        )

        # Get user info
        user_info = user_names.get(
            user_dir,
            {
                "PersonaName": "Unknown Account",
                "AccountName": "Unknown Account",
            },
        )
        persona_name = user_info["PersonaName"]
        account_name = user_info["AccountName"]

        # Print user header
        if account_name != "Unknown Account":
            print(f"\nShortcuts for user: {persona_name} ({account_name})")
        else:
            print(f"\nShortcuts for user: {persona_name}")

        if not os.path.exists(shortcuts_vdf):
            print("  No shortcuts.vdf file found")
            continue

        print(f"Loading shortcuts from: {shortcuts_vdf}")
        try:
            with open(shortcuts_vdf, "rb") as f:
                shortcuts = vdf.binary_load(f)

            if not shortcuts or "shortcuts" not in shortcuts:
                print("  No shortcuts found")
                continue

            print("\n  Found shortcuts:")
            print("  " + "-" * 50)

            for idx, shortcut in shortcuts["shortcuts"].items():
                exe_path = shortcut.get("Exe", "Unknown").strip('"')
                app_name = shortcut.get("AppName", "Unknown")
                start_dir = shortcut.get("StartDir", "Unknown").strip('"')
                app_id = shortcut.get("appid", "Unknown")

                print(f"\n  Shortcut #{idx}")
                print("  " + "-" * 20)
                print(f"    Name: {app_name}")
                print(f"    Executable: {exe_path}")
                print(f"    Start Dir: {start_dir}")
                print(f"    App ID: {app_id}")

                # Only print these if they exist
                if launch_opts := shortcut.get("LaunchOptions"):
                    print(f"    Launch Options: {launch_opts}")
                if shortcut.get("IsHidden", 0) == 1:
                    print("    [Hidden]")
                if icon := shortcut.get("icon"):
                    print(f"    Icon: {icon}")
                if tags := shortcut.get("tags"):
                    print("    Tags:", ", ".join(tags.values()))
                print("  " + "-" * 20)

            print()  # Extra newline for spacing between users

        except Exception as e:
            logger.error(
                "Error reading shortcuts for user %s: %s", persona_name, e
            )

    return True


def _process_loginusers_data(login_data, user_names):
    """Process user data from loginusers.vdf"""
    if "users" not in login_data:
        return

    for steam64_id, user_data in login_data["users"].items():
        # Convert Steam64 ID to Steam32 ID
        steam32_id = utils.steam64_to_steam32(steam64_id)
        if steam32_id:
            user_names[steam32_id] = {
                "PersonaName": user_data.get("PersonaName", "Unknown Account"),
                "AccountName": user_data.get("AccountName", "Unknown Account"),
                "Steam64ID": steam64_id,
            }
            logger.debug(
                "Found user in loginusers.vdf: " "Steam64: %s -> Steam32: %s",
                steam64_id,
                steam32_id,
            )

        # Also store under Steam64 ID
        user_names[steam64_id] = {
            "PersonaName": user_data.get("PersonaName", "Unknown Account"),
            "AccountName": user_data.get("AccountName", "Unknown Account"),
            "Steam32ID": steam32_id,
        }


def _process_config_data(config_data, user_names):
    """Process user data from config.vdf"""
    try:
        steam_config = (
            config_data.get("InstallConfigStore", {})
            .get("Software", {})
            .get("Valve", {})
            .get("Steam", {})
        )

        if "Accounts" not in steam_config:
            return

        for user_id, account_data in steam_config["Accounts"].items():
            # Try both Steam32 and Steam64 IDs
            steam64_id = utils.steam32_to_steam64(user_id)
            if steam64_id in user_names:
                # We already have this user from loginusers.vdf
                continue

            # If we don't have this user yet, add them
            user_names[user_id] = {
                "PersonaName": account_data.get(
                    "PersonaName", "Unknown Account"
                ),
                "AccountName": account_data.get(
                    "AccountName", "Unknown Account"
                ),
                "Steam64ID": steam64_id,
            }
    except Exception as e:
        logger.error("Error processing config data: %s", e)


def get_steam_user_names(args, steam_path):
    """
    Get Steam account names from both loginusers.vdf and config.vdf
    Returns a dictionary mapping user IDs to account names
    """
    logger.debug("Attempting to read Steam user names")
    user_names = {}

    # Process loginusers.vdf
    login_file = os.path.join(steam_path, "config", "loginusers.vdf")
    try:
        if os.path.exists(login_file):
            with open(login_file, "r", encoding="utf-8") as f:
                login_data = vdf.load(f)
                dump_vdf_to_json(args, login_data, login_file)
                _process_loginusers_data(login_data, user_names)
    except Exception as e:
        logger.error("Error reading loginusers.vdf: %s", e)

    # Process config.vdf
    config_file = os.path.join(steam_path, "config", "config.vdf")
    try:
        if os.path.exists(config_file):
            with open(config_file, "r", encoding="utf-8") as f:
                config_data = vdf.load(f)
                dump_vdf_to_json(args, config_data, config_file)
                _process_config_data(config_data, user_names)
    except Exception as e:
        logger.error("Error reading config.vdf: %s", e)

    return user_names


def _get_steam_config_from_localconfig(config):
    """Extract Steam config from localconfig data structure"""
    return config.get("Software", {}).get("Valve", {}).get("Steam", {})


def _create_game_entry(app_id, app_data):
    """Create a game entry from app data"""
    return {
        "app_id": app_id,
        "last_played": datetime.datetime.fromtimestamp(
            int(app_data["LastPlayed"])
        ),
    }


def get_recent_games(userdata_path, user_id):
    """
    Get the last 5 played games for a user
    """
    config_path = os.path.join(
        userdata_path, user_id, "config", "localconfig.vdf"
    )
    recent_games = []

    if not os.path.exists(config_path):
        return recent_games

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = vdf.load(f)
            steam_config = _get_steam_config_from_localconfig(config)

            if "apps" not in steam_config:
                return recent_games

            # Process each app's data
            for app_id, app_data in steam_config["apps"].items():
                if "LastPlayed" in app_data:
                    game_entry = _create_game_entry(app_id, app_data)
                    recent_games.append(game_entry)

    except Exception as e:
        logger.error("Error reading localconfig.vdf: %s", e)

    # Sort by last played time and return top 5
    return sorted(recent_games, key=lambda x: x["last_played"], reverse=True)[
        :5
    ]


def _format_user_display(user_dir, user_info):
    """Format the user display string"""
    if not user_info:
        return f"\t- {user_dir} - Unknown Account"

    persona_name = user_info["PersonaName"]
    account_name = user_info["AccountName"]

    if account_name != "Unknown Account":
        return f"\t- {user_dir} - {persona_name} ({account_name})"

    return f"\t- {user_dir} - {persona_name}"


def _display_recent_games(games):
    """Display recent games for a user"""
    if not games:
        return

    print("\n  Recent Games:")
    for game in games:
        print(
            f"\t- App ID {game['app_id']}, "
            f"Last played: {game['last_played']}"
        )


def _get_user_info_from_names(user_dir, user_names):
    """Get user info from user_names dict, trying both Steam32 and Steam64 IDs"""
    user_info = user_names.get(user_dir)
    if not user_info:
        steam64_id = utils.steam32_to_steam64(user_dir)
        if steam64_id:
            user_info = user_names.get(steam64_id)
    return user_info


def get_user_info(args, selected_library):
    """Display user account information"""
    userdata_path = os.path.join(selected_library, "userdata")

    if not os.path.exists(userdata_path):
        print("\nNo Steam userdata directory found")
        return

    user_dirs = [
        d
        for d in os.listdir(userdata_path)
        if os.path.isdir(os.path.join(userdata_path, d))
    ]

    if not user_dirs:
        print("\nNo Steam accounts found")
        print()
        return

    user_names = get_steam_user_names(args, selected_library)
    print("\nSteam Accounts:")

    for user_dir in user_dirs:
        # Get and display user info
        user_info = _get_user_info_from_names(user_dir, user_names)
        print(_format_user_display(user_dir, user_info))

        # Display recent games
        recent_games = get_recent_games(userdata_path, user_dir)
        _display_recent_games(recent_games)

    print()


def add_shortcut_entry():
    """
    Add a new shortcut entry
    """
    # Get the application name
    app_name = input("Enter application name: ").strip()
    if not app_name:
        # Assume we are done
        logger.info("Exiting entry process, blank name entered")
        return None

    # Get the executable path
    exe_path = utils.prompt_path("Enter path to executable: ", is_file=True)
    if not exe_path:
        return None

    # Get the start directory (default to executable's directory)
    exe_dir = os.path.dirname(exe_path)
    start_dir = utils.prompt_path(
        "Enter start directory (press Enter for executable's directory): ",
        is_file=False,
        default_path=exe_dir,
    )
    if start_dir is None:  # User cancelled
        return None

    # Get launch options (optional)
    launch_options = input("Enter launch options (optional): ").strip()

    # Create the shortcut entry
    entry = {
        "appname": app_name,
        "exe": f'"{exe_path}"',
        "StartDir": f'"{start_dir}"',
        "icon": "",
        "ShortcutPath": "",
        "LaunchOptions": launch_options,
        "IsHidden": 0,
        "AllowDesktopConfig": 1,
        "AllowOverlay": 1,
        "OpenVR": 0,
        "Devkit": 0,
        "DevkitGameID": "",
        "LastPlayTime": 0,
        "tags": {},
    }

    return entry


def add_shortcut_to_shortcuts(shortcuts, new_entry):
    """
    Add a new shortcut entry to the shortcuts structure
    """
    # Initialize shortcuts list if it doesn't exist
    if "shortcuts" not in shortcuts:
        shortcuts["shortcuts"] = {}

    # Find the next available index
    next_index = 0
    while str(next_index) in shortcuts["shortcuts"]:
        next_index += 1

    # Add the new entry
    shortcuts["shortcuts"][str(next_index)] = new_entry
    logger.info(
        f"Added new shortcut '{new_entry['appname']}' at index {next_index}"
    )
    return shortcuts


def load_shortcuts_file(args, shortcuts_vdf):
    """
    Load shortcuts.vdf file using binary mode
    """
    try:
        if os.path.exists(shortcuts_vdf):
            with open(shortcuts_vdf, "rb") as f:  # Use binary mode
                shortcuts = vdf.binary_load(
                    f
                )  # Use vdf.binary_load instead of vdf.load
                dump_vdf_to_json(args, shortcuts, shortcuts_vdf)
                return shortcuts
        else:
            logger.debug("No shortcuts.vdf found at: %s", shortcuts_vdf)
            return {"shortcuts": []}
    except Exception as e:
        logger.error("Error loading shortcuts.vdf: %s", e)
        return {"shortcuts": []}


def save_shortcuts(shortcuts_vdf, shortcuts):
    """
    Save the shortcuts back to the VDF file
    """
    try:
        with open(shortcuts_vdf, "wb") as f:
            vdf.binary_dump(shortcuts, f)
        logger.info("Successfully saved shortcuts to: %s", shortcuts_vdf)
        return True
    except Exception as e:
        logger.error("Error saving shortcuts: %s", e)
        return False


def find_steam_library(args):
    """
    Find the Steam library location based on the operating system.
    Returns the path to the Steam library or None if not found.
    """
    system = platform.system().lower()
    home = os.path.expanduser("~")
    logger.info("Searching for Steam library on %s system", system)

    if system == "windows":
        # Check common Windows locations
        possible_paths = [
            "C:\\Program Files (x86)\\Steam",
            "C:\\Program Files\\Steam",
            os.path.join(os.getenv("ProgramFiles(x86)", ""), "Steam"),
            os.path.join(os.getenv("ProgramFiles", ""), "Steam"),
        ]

    elif system == "darwin":  # macOS
        possible_paths = [
            os.path.join(home, "Library/Application Support/Steam"),
            "/Applications/Steam.app/Contents/MacOS",
        ]

    elif system == "linux":
        possible_paths = [
            os.path.join(home, ".local/share/Steam"),
            os.path.join(home, ".steam/steam"),
            os.path.join(home, ".steam"),
            "/usr/share/steam",
        ]
    else:
        logger.error("Unsupported operating system: %s", system)
        return None

    logger.debug("Checking possible paths: %s", possible_paths)
    # Check each possible path
    for path in possible_paths:
        if os.path.exists(path):
            logger.info("Found Steam library at: %s", path)
            return path

    logger.warning("No Steam library found in common locations")
    exit(1)


def find_steam_library_folders(args):
    """
    Find all Steam library folders including additional library folders.
    Returns a list of paths to all found Steam libraries.
    """
    libraries = []
    main_library = find_steam_library(args)

    if not main_library:
        logger.warning("No main Steam library found")
        return libraries

    libraries.append(main_library)

    # Check for additional library folders in libraryfolders.vdf
    vdf_paths = [
        os.path.join(main_library, "steamapps/libraryfolders.vdf"),
        os.path.join(main_library, "config/libraryfolders.vdf"),
    ]

    logger.debug("Checking VDF paths: %s", vdf_paths)
    for vdf_path in vdf_paths:
        if os.path.exists(vdf_path):
            try:
                logger.debug("Reading VDF file: %s", vdf_path)
                with open(vdf_path, "r", encoding="utf-8") as f:
                    content = vdf.load(f)
                    dump_vdf_to_json(args, content, vdf_path)

                    # Process library folders
                    if isinstance(content, dict):
                        for key, value in content.items():
                            if isinstance(value, dict) and "path" in value:
                                path = value["path"]
                                if (
                                    os.path.exists(path)
                                    and path not in libraries
                                ):
                                    logger.info(
                                        "Found additional library at: %s", path
                                    )
                                    libraries.append(path)
            except Exception as e:
                raise Exception("Error reading VDF file %s: %s", vdf_path, e)

    return libraries


def choose_library(libraries):
    """
    Prompt user to choose a Steam library from the available options.
    Returns the chosen library path or None if no valid selection is made.
    """
    if not libraries:
        logger.warning("No Steam libraries found")
        logger.error("No Steam libraries found.")
        return None

    if len(libraries) == 1:
        logger.info("Using only available Steam library: %s", libraries[0])
        return libraries[0]

    logger.info("Available Steam libraries:")
    for idx, library in enumerate(libraries, 1):
        logger.info("%s. %s", idx, library)

    while True:
        try:
            choice = input("\nChoose a Steam library (enter number): ")
            index = int(choice) - 1
            if 0 <= index < len(libraries):
                selected = libraries[index]
                logger.info("User selected library: %s", selected)
                return selected
            else:
                logger.warning("Invalid selection: %s", choice)
                logger.info(
                    "Please enter a number between 1 and %s", len(libraries)
                )
        except ValueError:
            logger.warning("Invalid input: %s", choice)
            logger.info("Please enter a valid number")
        except KeyboardInterrupt:
            logger.info("Operation cancelled by user")
            logger.info("\nOperation cancelled")
            return None
