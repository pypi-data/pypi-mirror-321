from selenium import webdriver
import argparse
import json
import os
import time

def get_local_storage_item(driver, key):
    return driver.execute_script(f"return window.localStorage.getItem('{key}');")

def set_local_storage_item(driver, key, value):
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

def load_file_to_planner(driver, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    data = data.replace('\n', '').replace('\r', '').replace(' ', '')
    set_local_storage_item(driver, 'planner', data)
    driver.get('https://satisfactory-planner.vercel.app/')

def save_planner_to_file(driver, filename):
    planner_dir = os.path.join(os.path.expanduser('~'), '.planner')
    os.makedirs(planner_dir, exist_ok=True)
    
    save_path = os.path.join(planner_dir, filename)
    value = get_local_storage_item(driver, 'planner')
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(value)
    print(f"Saved to {save_path}")

def list_json_files():
    planner_dir = os.path.join(os.path.expanduser('~'), '.planner')
    os.makedirs(planner_dir, exist_ok=True)
    
    json_files = [f for f in os.listdir(planner_dir) if f.endswith('.json')]
    if not json_files:
        print(f"No .json files found in {planner_dir}")
        return None
    
    print("\nAvailable files:")
    for i, file in enumerate(json_files, 1):
        print(f"{i}. {file}")
    
    while True:
        try:
            choice = int(input("\nChoose a file number to load (or 0 to cancel): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(json_files):
                return os.path.join(planner_dir, json_files[choice - 1])
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_config():
    config_path = os.path.join(os.path.expanduser('~'), '.planner', 'config.json')
    defaults = {
        'user_data_dir': f'{os.getenv("LOCALAPPDATA")}\\Google\\Chrome\\User Data',
        'profile_directory': 'Default'
    }
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return {**defaults, **json.load(f)}
    return defaults

def save_config(user_data_dir=None, profile_directory=None):
    config_path = os.path.join(os.path.expanduser('~'), '.planner', 'config.json')
    config = get_config()
    
    if user_data_dir:
        config['user_data_dir'] = user_data_dir
    if profile_directory:
        config['profile_directory'] = profile_directory
        
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

def get_driver():
    config = get_config()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument(f'--user-data-dir={config["user_data_dir"]}')
    options.add_argument(f'--profile-directory={config["profile_directory"]}')
    driver = webdriver.Chrome(options=options)
    driver.get('https://satisfactory-planner.vercel.app/')    
    return driver

def main():
    parser = argparse.ArgumentParser(description='Load or save Satisfactory Planner data')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--load', action='store_true', help='Load a file from .planner directory (interactive)')
    group.add_argument('--load_file', help='Load a specific file from given path')
    group.add_argument('--save', action='store_true', help='Save current planner to .planner directory')
    group.add_argument('--save_file', help='Save current planner to specified path')
    parser.add_argument('--clear', action='store_true', help='Clear planner data')
    parser.add_argument('--user-data-dir', help='Set Chrome user data directory')
    parser.add_argument('--profile-directory', help='Set Chrome profile directory')
    args = parser.parse_args()

    if args.user_data_dir or args.profile_directory:
        save_config(args.user_data_dir, args.profile_directory)
        print("Configuration updated")
        return

    driver = None
    if not args.load and not args.load_file and not args.save and not args.save_file and not args.clear:
        parser.error('At least one of --load, --load_file, --save, --save_file, or --clear is required')

    if args.clear:
        driver = get_driver()
        set_local_storage_item(driver, 'planner', '')
        driver.get('https://satisfactory-planner.vercel.app/')
    
    if args.load:
        filename = list_json_files()
        if filename:
            driver = get_driver()
            load_file_to_planner(driver, filename)
    
    if args.load_file:
        driver = get_driver()
        load_file_to_planner(driver, args.load_file)
    
    if args.save:
        filename = input("Enter filename to save (without .json extension): ") + '.json'
        driver = get_driver()
        save_planner_to_file(driver, filename)

    if args.save_file:
        driver = get_driver() if not driver else driver
        # Wait for page to load
        time.sleep(2)
        data = get_local_storage_item(driver, 'planner')
        if data:
            os.makedirs(os.path.dirname(args.save_file), exist_ok=True)
            with open(args.save_file, 'w') as f:
                f.write(data)
            print(f"Saved planner data to {args.save_file}")
        else:
            print("No planner data found")

    if driver is not None:
        driver.quit()

if __name__ == '__main__':
    main()
