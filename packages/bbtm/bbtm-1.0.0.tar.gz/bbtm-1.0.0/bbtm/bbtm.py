import json
import subprocess
import shutil
import curses
import os

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def check_prerequisite(prerequisite):
    """Check if a prerequisite is installed."""
    return shutil.which(prerequisite) is not None

def install_prerequisite(prerequisite):
    """Install a prerequisite."""
    if prerequisite == "pip3":
        subprocess.run(["sudo", "apt-get", "install", "-y", "python3-pip"], check=True)
    elif prerequisite == "go":
        subprocess.run(["sudo", "apt-get", "install", "-y", "golang-go"], check=True)
    elif prerequisite == "gem":
        subprocess.run(["sudo", "apt-get", "install", "-y", "ruby-full"], check=True)
    # Add more prerequisites as needed

def safe_addstr(stdscr, y, x, text):
    """Safely add a string to the screen, avoiding out-of-bounds errors."""
    try:
        stdscr.addstr(y, x, text)
    except curses.error:
        pass  # Ignore out-of-bounds errors

def execute_commands(stdscr, selected_items, data, is_wordlist=False):
    """Execute installation commands for selected items."""
    for category, items_list in data.items():
        for item in items_list:
            if item['name'] in selected_items:
                if is_wordlist:
                    target_dir = os.path.expanduser("~/Wordlists")
                    os.makedirs(target_dir, exist_ok=True)
                
                # Check for prerequisite
                prerequisite = item.get('prerequisite')
                if prerequisite and not check_prerequisite(prerequisite):
                    stdscr.clear()
                    safe_addstr(stdscr, 0, 0, f"Installing prerequisite: {prerequisite}...")
                    stdscr.refresh()
                    try:
                        install_prerequisite(prerequisite)
                        safe_addstr(stdscr, 1, 0, f"Successfully installed prerequisite: {prerequisite}!")
                        stdscr.refresh()
                        curses.napms(1000)
                    except subprocess.CalledProcessError as e:
                        safe_addstr(stdscr, 1, 0, f"Failed to install prerequisite: {prerequisite}. Error: {e}")
                        stdscr.refresh()
                        curses.napms(2000)
                        continue  # Skip this tool if prerequisite installation fails

                # Proceed with tool installation
                command = item['command']
                stdscr.clear()
                safe_addstr(stdscr, 0, 0, f"Downloading {item['name']}...")
                stdscr.refresh()
                process = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                y = 1
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        safe_addstr(stdscr, y, 0, output.strip())
                        y += 1
                        stdscr.refresh()
                return_code = process.poll()
                if return_code == 0:
                    safe_addstr(stdscr, y, 0, f"Successfully downloaded {item['name']}!")
                else:
                    safe_addstr(stdscr, y, 0, f"Failed to download {item['name']}. Error code: {return_code}")
                stdscr.refresh()
                curses.napms(1000)


def draw_box(stdscr, y, x, height, width):
    """Draw a box with borders."""
    safe_addstr(stdscr, y, x, "╭" + "─" * (width - 2) + "╮")
    for i in range(1, height - 1):
        safe_addstr(stdscr, y + i, x, "│" + " " * (width - 2) + "│")
    safe_addstr(stdscr, y + height - 1, x, "╰" + "─" * (width - 2) + "╯")

def draw_menu(stdscr, selected_row_idx, modules, current_module, tools, wordlists, presets, selected_items, selected_presets, selected_wordlists, selected_categories):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    min_height = 24
    min_width = 80

    if h < min_height or w < min_width:
        safe_addstr(stdscr, 0, 0, "Terminal too small! Please resize to at least {}x{}.".format(min_width, min_height))
        stdscr.refresh()
        return

    draw_box(stdscr, 0, 0, 3, w)

    total_modules = len(modules)
    available_width = w - 2
    spacing = available_width // total_modules

    y = 1
    for idx, module in enumerate(modules):
        x = idx * spacing + (spacing - len(module)) // 2 + 1
        if idx == current_module:
            stdscr.attron(curses.A_REVERSE)
            safe_addstr(stdscr, y, x, module)
            stdscr.attroff(curses.A_REVERSE)
        else:
            safe_addstr(stdscr, y, x, module)

    if current_module == 0:  # Tools
        draw_box(stdscr, 3, 0, h - 5, w)
        y_offset = 4
        x_offset = 2
        available_height = h - 6
        rows_per_column = available_height - 1
        items = []
        for category, tools_list in tools.items():
            items.append((category, "category"))
            for tool in tools_list:
                items.append((tool, "tool"))
        cols_needed = (len(items) + rows_per_column - 1) // rows_per_column
        columns = [items[i:i+rows_per_column] for i in range(0, len(items), rows_per_column)]
        column_width = (w - 4) // cols_needed
        for col in range(cols_needed):
            x = x_offset + col * column_width
            col_start_idx = col * rows_per_column
            for row_in_col in range(rows_per_column):
                y = y_offset + row_in_col
                if y >= h - 2:
                    break
                item_index = col_start_idx + row_in_col
                if item_index < len(items):
                    item, item_type = items[item_index]
                    if item_type == "category":
                        checkbox = "[x]" if item in selected_categories else "[ ]"
                        if selected_row_idx == item_index:
                            stdscr.attron(curses.A_REVERSE)
                            safe_addstr(stdscr, y, x, f"{checkbox} {item}:")
                            stdscr.attroff(curses.A_REVERSE)
                        else:
                            safe_addstr(stdscr, y, x, f"{checkbox} {item}:")
                    else:
                        tool_name = item['name']
                        checkbox = "[x]" if tool_name in selected_items else "[ ]"
                        if selected_row_idx == item_index:
                            stdscr.attron(curses.A_REVERSE)
                            safe_addstr(stdscr, y, x + 4, f"{checkbox} {tool_name}")
                            stdscr.attroff(curses.A_REVERSE)
                        else:
                            safe_addstr(stdscr, y, x + 4, f"{checkbox} {tool_name}")
    elif current_module == 1:  # Presets
        draw_box(stdscr, 3, 0, h - 5, w)
        y_offset = 4
        x_offset = 2
        available_height = h - 6
        rows_per_column = available_height - 1
        items = list(presets.keys())
        cols_needed = (len(items) + rows_per_column - 1) // rows_per_column
        columns = [items[i:i+rows_per_column] for i in range(0, len(items), rows_per_column)]
        column_width = (w - 4) // cols_needed
        for col in range(cols_needed):
            x = x_offset + col * column_width
            col_start_idx = col * rows_per_column
            for row_in_col in range(rows_per_column):
                y = y_offset + row_in_col
                if y >= h - 2:
                    break
                item_index = col_start_idx + row_in_col
                if item_index < len(items):
                    preset_name = items[item_index]
                    checkbox = "[x]" if preset_name in selected_presets else "[ ]"
                    if selected_row_idx == item_index:
                        stdscr.attron(curses.A_REVERSE)
                        safe_addstr(stdscr, y, x, f"{checkbox} {preset_name}")
                        stdscr.attroff(curses.A_REVERSE)
                    else:
                        safe_addstr(stdscr, y, x, f"{checkbox} {preset_name}")
    elif current_module == 2:  # Wordlists
        draw_box(stdscr, 3, 0, h - 5, w)
        y_offset = 4
        x_offset = 2
        available_height = h - 6
        rows_per_column = available_height - 1
        items = []
        for category, wordlists_list in wordlists.items():
            items.append((category, "category"))
            for wordlist in wordlists_list:
                items.append((wordlist, "wordlist"))
        cols_needed = (len(items) + rows_per_column - 1) // rows_per_column
        columns = [items[i:i+rows_per_column] for i in range(0, len(items), rows_per_column)]
        column_width = (w - 4) // cols_needed
        for col in range(cols_needed):
            x = x_offset + col * column_width
            col_start_idx = col * rows_per_column
            for row_in_col in range(rows_per_column):
                y = y_offset + row_in_col
                if y >= h - 2:
                    break
                item_index = col_start_idx + row_in_col
                if item_index < len(items):
                    item, item_type = items[item_index]
                    if item_type == "category":
                        checkbox = "[x]" if item in selected_categories else "[ ]"
                        if selected_row_idx == item_index:
                            stdscr.attron(curses.A_REVERSE)
                            safe_addstr(stdscr, y, x, f"{checkbox} {item}:")
                            stdscr.attroff(curses.A_REVERSE)
                        else:
                            safe_addstr(stdscr, y, x, f"{checkbox} {item}:")
                    else:
                        wordlist_name = item['name']
                        checkbox = "[x]" if wordlist_name in selected_wordlists else "[ ]"
                        if selected_row_idx == item_index:
                            stdscr.attron(curses.A_REVERSE)
                            safe_addstr(stdscr, y, x + 4, f"{checkbox} {wordlist_name}")
                            stdscr.attroff(curses.A_REVERSE)
                        else:
                            safe_addstr(stdscr, y, x + 4, f"{checkbox} {wordlist_name}")
    elif current_module == 3:  # Help
        draw_box(stdscr, 3, 0, h - 5, w)
        y = 4
        x = 2
        help_text = [
            "Help and Usage:",
            "----------------",
            "",
            "1. Navigation:",
            "   - Use the UP and DOWN arrow keys to navigate.",
            "   - Use the LEFT and RIGHT arrow keys to switch modules.",
            "   - Press 't' to return to the Tools module.",
            "",
            "2. Selection:",
            "   - Press SPACE to select/deselect an item.",
            "   - Selecting a category selects all items in that category.",
            "   - Deselecting an item in a selected category deselects the category.",
            "",
            "3. Installation:",
            "   - Press 'i' to install selected tools, presets, or wordlists.",
            "",
            "4. Quit:",
            "   - Press 'q' to switch to the Quit module.",
            "   - Press 'y' to confirm quit or 'n' to cancel.",
            "",
            "5. Help:",
            "   - Press 'h' to display this help message.",
            ""
        ]
        for line in help_text:
            safe_addstr(stdscr, y, x, line)
            y += 1
    elif current_module == 4:  # Quit
        draw_box(stdscr, h // 2 - 1, w // 2 - 20, 3, 40)
        y = h // 2
        x = w // 2 - len("Are you sure you want to quit? (y/n)") // 2
        if selected_row_idx == 0:
            stdscr.attron(curses.A_REVERSE)
            safe_addstr(stdscr, y, x, "Are you sure you want to quit? (y/n)")
            stdscr.attroff(curses.A_REVERSE)
        else:
            safe_addstr(stdscr, y, x, "Are you sure you want to quit? (y/n)")

    safe_addstr(stdscr, h - 2, 0, "─" * w)
    hints = {
        0: "Press 'i' to install selected tools or categories",
        1: "Press 'i' to install selected presets",
        2: "Press 'i' to download selected wordlists",
        3: "Press 't' to return to Tools module",
        4: "Press 'y' to confirm quit, 'n' to cancel"
    }

    hint_text = hints.get(current_module, "")
    bbtm_text = "bbtm - github.com/padsalatushal/bbtm"
    hint_x = 0
    bbtm_x = w - len(bbtm_text) - 1  # Right-aligned
    # Write hint text and "bbtm" text
    safe_addstr(stdscr, h - 1, hint_x, hint_text)
    safe_addstr(stdscr, h - 1, bbtm_x, bbtm_text)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    modules = ["Tools(t)", "Presets(p)", "Wordlists(w)", "Help(h)", "Quit(q)"]
    current_module = 0
    tools = load_json('tools.json')
    wordlists = load_json('wordlists.json')
    presets = load_json('presets.json')
    selected_items = set()
    selected_presets = set()
    selected_wordlists = set()
    selected_categories = set()
    selected_row_idx = 0

    while True:
        h, w = stdscr.getmaxyx()

        if current_module == 0:  # Tools
            items = []
            for category, tools_list in tools.items():
                items.append((category, "category"))
                for tool in tools_list:
                    items.append((tool, "tool"))
            available_height = h - 6
            rows_per_column = available_height - 1
            cols_needed = (len(items) + rows_per_column - 1) // rows_per_column
            max_selected = len(items) - 1
        elif current_module == 1:  # Presets
            items = list(presets.keys())
            available_height = h - 6
            rows_per_column = available_height - 1
            cols_needed = (len(items) + rows_per_column - 1) // rows_per_column
            max_selected = len(items) - 1
        elif current_module == 2:  # Wordlists
            items = []
            for category, wordlists_list in wordlists.items():
                items.append((category, "category"))
                for wordlist in wordlists_list:
                    items.append((wordlist, "wordlist"))
            available_height = h - 6
            rows_per_column = available_height - 1
            cols_needed = (len(items) + rows_per_column - 1) // rows_per_column
            max_selected = len(items) - 1
        elif current_module == 3:  # Help
            items = ["Help"]
            available_height = h - 6
            rows_per_column = available_height - 1
            cols_needed = 1
            max_selected = 0
        elif current_module == 4:  # Quit
            items = ["Are you sure you want to quit? (y/n)"]
            available_height = h - 6
            rows_per_column = available_height - 1
            cols_needed = 1
            max_selected = 0

        draw_menu(stdscr, selected_row_idx, modules, current_module, tools, wordlists, presets, selected_items, selected_presets, selected_wordlists, selected_categories)
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row_idx > 0:
            selected_row_idx -= 1
        elif key == curses.KEY_DOWN and selected_row_idx < max_selected:
            selected_row_idx += 1
        elif key == curses.KEY_LEFT and current_module > 0:
            current_module -= 1
            selected_row_idx = 0
        elif key == curses.KEY_RIGHT and current_module < len(modules) - 1:
            current_module += 1
            selected_row_idx = 0
        elif key == curses.KEY_LEFT and current_module in [0, 1, 2]:
            if selected_row_idx >= rows_per_column:
                selected_row_idx -= rows_per_column
        elif key == curses.KEY_RIGHT and current_module in [0, 1, 2]:
            if selected_row_idx + rows_per_column < len(items):
                selected_row_idx += rows_per_column
        elif key == ord(' '):
            if current_module == 0:
                item, item_type = items[selected_row_idx]
                if item_type == "category":
                    category = item
                    if category in selected_categories:
                        selected_categories.remove(category)
                        for tool in tools[category]:
                            selected_items.discard(tool['name'])
                    else:
                        selected_categories.add(category)
                        for tool in tools[category]:
                            selected_items.add(tool['name'])
                else:
                    tool_name = item['name']
                    if tool_name in selected_items:
                        selected_items.remove(tool_name)
                        for category, tools_list in tools.items():
                            if tool_name in [tool['name'] for tool in tools_list]:
                                if category in selected_categories:
                                    selected_categories.remove(category)
                    else:
                        selected_items.add(tool_name)
            elif current_module == 1:
                preset_name = items[selected_row_idx]
                if preset_name in selected_presets:
                    selected_presets.remove(preset_name)
                else:
                    selected_presets.add(preset_name)
            elif current_module == 2:
                item, item_type = items[selected_row_idx]
                if item_type == "category":
                    category = item
                    if category in selected_categories:
                        selected_categories.remove(category)
                        for wordlist in wordlists.get(category, []):
                            selected_wordlists.discard(wordlist['name'])
                    else:
                        selected_categories.add(category)
                        for wordlist in wordlists.get(category, []):
                            selected_wordlists.add(wordlist['name'])
                else:
                    wordlist_name = item['name']
                    if wordlist_name in selected_wordlists:
                        selected_wordlists.remove(wordlist_name)
                        category = next((cat for cat, wl in wordlists.items() if any(wl_item['name'] == wordlist_name for wl_item in wl)), None)
                        if category and category in selected_categories:
                            if not any(wl_item['name'] in selected_wordlists for wl_item in wordlists.get(category, [])):
                                selected_categories.remove(category)
                    else:
                        selected_wordlists.add(wordlist_name)
                        category = next((cat for cat, wl in wordlists.items() if any(wl_item['name'] == wordlist_name for wl_item in wl)), None)
                        if category:
                            if all(wl_item['name'] in selected_wordlists for wl_item in wordlists.get(category, [])):
                                selected_categories.add(category)
        elif key == ord('i'):
            if current_module == 0:
                execute_commands(stdscr, selected_items, tools)
            elif current_module == 1:
                tools_to_install = set()
                for preset in selected_presets:
                    tools_to_install.update(presets.get(preset, []))
                execute_commands(stdscr, tools_to_install, tools)
            elif current_module == 2:
                execute_commands(stdscr, selected_wordlists, wordlists, is_wordlist=True)
            selected_items.clear()
            selected_presets.clear()
            selected_wordlists.clear()
            selected_categories.clear()
        elif key == ord('h'):
            current_module = 3
            selected_row_idx = 0
        elif key == ord('p'):
            current_module = 1
            selected_row_idx = 0
        elif key == ord('w'):
            current_module = 2
            selected_row_idx = 0
        elif key == ord('q'):
            current_module = 4
            selected_row_idx = 0
        elif key == ord('t'):
            current_module = 0
            selected_row_idx = 0
        elif key == ord('y') and current_module == 4:
            break
        elif key == ord('n') and current_module == 4:
            current_module = 0

    stdscr.clear()
    safe_addstr(stdscr, 0, 0, "Exiting... Thank you for using BBTM!")
    stdscr.refresh()
    curses.napms(1000)

if __name__ == "__main__":
    curses.wrapper(main)