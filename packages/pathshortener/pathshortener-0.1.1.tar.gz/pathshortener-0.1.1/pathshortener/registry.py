import ctypes
import winreg

def set_user_env_var(name, value):
    """
    Permanently set a user-level environment variable on Windows by writing to:
      HKEY_CURRENT_USER\Environment
    Using REG_EXPAND_SZ so references like %OTHER_VAR% expand in new processes.

    This requires no special permissions for the *current user*. 
    For machine-wide changes, you'd have to write to HKEY_LOCAL_MACHINE 
    (requires Administrator).
    """
    registry_key = None
    try:
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_EXPAND_SZ, value)
    except Exception as e:
        print(f"Error setting environment variable {name}: {e}")
    finally:
        try:
            if registry_key:
                winreg.CloseKey(registry_key)
        except Exception as e:
            print(f"Error closing registry key: {e}")

def broadcast_settings_change():
    """
    Broadcast WM_SETTINGCHANGE to notify other programs (Explorer, etc.) 
    that environment variables have changed. 
    Existing shells won't see the change, but newly opened ones will.
    """
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A
    SMTO_BLOCK = 0x0001
    SMTO_ABORTIFHUNG = 0x0002

    result = ctypes.c_long()

    try:
        # Prepare the "Environment" string as a null-terminated wide string
        env_str = ctypes.create_unicode_buffer("Environment")

        # SendMessageTimeoutW expects a pointer to a wide string for lParam
        send_result = ctypes.windll.user32.SendMessageTimeoutW(
            HWND_BROADCAST,
            WM_SETTINGCHANGE,
            0,
            ctypes.byref(env_str),
            SMTO_BLOCK | SMTO_ABORTIFHUNG,
            5000,
            ctypes.byref(result)
        )
        
        if send_result == 0:
            print("Warning: SendMessageTimeoutW failed to broadcast environment change.")
    except Exception as e:
        print(f"Error broadcasting environment change: {e}") 