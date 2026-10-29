def add_setting(settings,pair):
    key,value = pair
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return f"No settings available."
    output = "Current User Settings:\n"
    for key,value in settings.items():
        output += f"{key.capitalize()}: {value}\n" 
    return output

test_settings = {}
print(view_settings(test_settings))
print(add_setting(test_settings, ("THEME", "DARK")))
print(add_setting(test_settings, ("notifications", "ENABLED")))
print(update_setting(test_settings, ("theme", "LIGHT")))
print(view_settings(test_settings))
print(delete_setting(test_settings, "THEME"))