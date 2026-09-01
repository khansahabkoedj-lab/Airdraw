import sys
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import comtypes

def maximize_volume():
    try:
        # Initialize COM library
        comtypes.CoInitialize()

        # Get all audio sessions
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Get current volume range
        vol_range = volume.GetVolumeRange()
        min_vol = vol_range[0]
        max_vol = vol_range[1]

        # Unmute if muted
        volume.SetMute(0, None)

        # Set to maximum volume
        volume.SetMasterVolumeLevel(max_vol, None)

        print(f"System volume successfully set to maximum ({max_vol} dB).")

    except Exception as e:
        print(f"Failed to maximize system volume: {e}")
        if sys.platform != 'win32':
            print("Note: This script is designed specifically for Windows.")
    finally:
        # Uninitialize COM library
        comtypes.CoUninitialize()

if __name__ == "__main__":
    maximize_volume()
