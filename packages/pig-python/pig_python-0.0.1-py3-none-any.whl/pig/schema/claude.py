
claude = {
    "properties": {
        "action": {
            "description": """The action to perform. The available actions are:
                * `type`: Type a string of text on the keyboard.
                * `cursor_position`: Get the current (x, y) pixel coordinate of the cursor on the screen.
                * `mouse_move`: Move the cursor to a specified (x, y) pixel coordinate on the screen.
                * `left_click`: Click the left mouse button at specified coordinates.
                * `left_click_drag`: Click at current position and drag to specified coordinates.
                * `right_click`: Click the right mouse button at specified coordinates.
                * `double_click`: Double-click the left mouse button at specified coordinates.
                * `screenshot`: Take a screenshot of the screen and return bytes.
                * 'yield_control': Yield control of the VM to a human operator.
                * 'await_control': Awaits for control of the VM to be granted back.""",
            "enum": [
                # "key", # Not yet implemented
                "type", 
                "cursor_position",
                "mouse_move",
                "left_click",
                "left_click_drag",
                "right_click",
                # "middle_click", # Not yet implemented
                "double_click",
                "screenshot",
                "yield_control",
                "await_control"
            ],
            "type": "string"
        },
        "coordinate": {
            "description": "(x, y): Required by all mouse actions except cursor_position. For mouse_move, left_click, right_click, and double_click, specifies the target coordinates. For left_click_drag, specifies the end coordinates (start coordinates are current cursor position).",
            "type": "array"
        },
        "text": {
            "description": "Required only by action=type and action=key. For type, the text to type. For key, the key combination to press.",
            "type": "string"
        }
    },
    "required": ["action"],
    "type": "object"
}

# Not yet implemented:

                # * `key`: Press a key or key-combination on the keyboard.
                #   - Will support xdotool's `key` syntax.
                #   - Examples: "a", "Return", "alt+Tab", "ctrl+s", "Up", "KP_0" (for the numpad 0 key).
                
                # * `middle_click`: Click the middle mouse button.