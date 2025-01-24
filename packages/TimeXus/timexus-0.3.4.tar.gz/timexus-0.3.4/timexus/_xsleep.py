import ctypes
import sys
import platform
import random
import os
import json
from datetime import datetime, timedelta
import string  # Import the string module for generating random strings

def _get_sleep_func():
    """
    Gets the appropriate sleep function based on the operating system.
    """
    if sys.platform.startswith("win32"):
        # Windows
        sleep_func = ctypes.windll.kernel32.Sleep
        sleep_func.argtypes = [ctypes.c_ulong]  # DWORD
        sleep_unit = 1000  # Sleep takes milliseconds
    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        # Linux and macOS
        libc_name = "libc.so.6"
        if sys.platform.startswith("darwin"):
            libc_name = "libc.dylib"
        try:
            libc = ctypes.CDLL(libc_name)
        except OSError:
            libc = ctypes.CDLL("/usr/lib/libc.dylib")

        usleep_func = libc.usleep
        usleep_func.argtypes = [ctypes.c_uint]  # unsigned int
        sleep_func = lambda t: usleep_func(int(t))  # usleep takes microseconds
        sleep_unit = 1000000
    else:
        raise OSError("Unsupported operating system.")

    return sleep_func, sleep_unit

class XSleep:
    def __init__(self):
        self.sleep_func, self.sleep_unit = _get_sleep_func()
        self.print_awake = True  # Flag to control the "Awake!" message
        self.custom_message = "Awake!"  # Default message
        self.total_sleep_time = 0 # Keep track of the total sleep time

    def milliseconds(self, ms):
        """Sleeps for the specified number of milliseconds."""
        self._sleep(ms / 1000)

    def seconds(self, secs):
        """Sleeps for the specified number of seconds."""
        self._sleep(secs)

    def minutes(self, mins):
        """Sleeps for the specified number of minutes."""
        self._sleep(mins * 60)

    def hours(self, hrs):
        """Sleeps for the specified number of hours."""
        self._sleep(hrs * 3600)

    def _sleep(self, seconds):
        """Internal sleep function."""
        time_to_sleep = int(seconds * self.sleep_unit)
        self.total_sleep_time += seconds

        if self.sleep_unit == 1000:
            print(f"Sleeping for {seconds} seconds ({time_to_sleep} milliseconds)...")
        else:
            print(f"Sleeping for {seconds} seconds ({time_to_sleep} microseconds)...")

        self.sleep_func(time_to_sleep)
        if self.print_awake and seconds == 0:
            print(self.custom_message)

    def set_print(self, mode):
        """
        Turns on or off the automatic "Awake!" message.

        Args:
            mode (str): "on" to enable the message, "off" to disable it.
        """
        if mode == "on":
            self.print_awake = True
        elif mode == "off":
            self.print_awake = False
        else:
            print("Invalid mode. Use 'on' or 'off'.")

    def set_custom_print(self, message):
        """
        Customizes the automatic message after sleeping.

        Args:
            message (str): The new message to print.
        """
        self.custom_message = message

    def get_total_sleep_time(self):
        """Returns the total sleep time in seconds."""
        return self.total_sleep_time

    def reset_total_sleep_time(self):
        """Resets the total sleep time to 0."""
        self.total_sleep_time = 0

    # Additional features that the 'time' module doesn't have:

    def get_pid(self):
        """Gets the current process ID."""
        if sys.platform.startswith("win32"):
            return ctypes.windll.kernel32.GetCurrentProcessId()
        else:
            return os.getpid()

    def get_cpu_count(self):
        """Gets the number of CPUs/cores in the system."""
        if sys.platform.startswith("win32"):
            return int(os.environ.get('NUMBER_OF_PROCESSORS', 1))
        elif sys.platform.startswith("linux"):
            cpu_count = 0
            with open('/proc/cpuinfo') as f:
                for line in f:
                    if line.strip().startswith('processor'):
                        cpu_count += 1
            return cpu_count
        elif sys.platform.startswith("darwin"):
            libc = ctypes.CDLL("libc.dylib")
            num_cpu = ctypes.c_int(0)
            size = ctypes.c_size_t(ctypes.sizeof(num_cpu))
            libc.sysctlbyname(ctypes.c_char_p(b"hw.ncpu"), ctypes.byref(num_cpu), ctypes.byref(size), None, 0)
            return num_cpu.value
        else:
            return 1

    def get_random_delay(self, min_seconds, max_seconds):
        """Sleeps for a random time between min_seconds and max_seconds."""
        random_delay = random.uniform(min_seconds, max_seconds)
        self._sleep(random_delay)

    def is_interactive(self):
        """Checks if the current session is interactive (run by a user in a terminal)."""
        return sys.stdin.isatty()

    def get_platform(self):
        """Returns a string identifying the current platform."""
        return sys.platform

    def get_uptime(self):
        """Returns the system uptime in seconds (time since the last boot)."""
        if sys.platform.startswith("linux"):
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
        elif sys.platform.startswith("darwin"):
            libc = ctypes.CDLL("libc.dylib")
            boottime = ctypes.c_int64(0)
            size = ctypes.c_size_t(ctypes.sizeof(boottime))

            # Use sysctlbyname to get boot time
            if libc.sysctlbyname(ctypes.c_char_p(b"kern.boottime"), ctypes.byref(boottime), ctypes.byref(size), None, 0) != -1:
                # Get current time in seconds using GetTickCount64 for Windows
                if sys.platform.startswith("win32"):
                  now = ctypes.windll.kernel32.GetTickCount64() / 1000.0
                else:
                  # Use CLOCK_MONOTONIC for Linux/macOS
                  CLOCK_MONOTONIC = 1
                  class timespec(ctypes.Structure):
                      _fields_ = [("tv_sec", ctypes.c_long), ("tv_nsec", ctypes.c_long)]

                  libc = ctypes.CDLL("libc.so.6")
                  if sys.platform.startswith("darwin"):
                      libc = ctypes.CDLL("libc.dylib")

                  ts = timespec()
                  libc.clock_gettime(CLOCK_MONOTONIC, ctypes.byref(ts))
                  now = ts.tv_sec + ts.tv_nsec / 1000000000.0

                # Calculate uptime by subtracting boottime from current time
                return now - boottime.value
            else:
                return None
        elif sys.platform.startswith("win32"):
            # Use GetTickCount64 for Windows to get milliseconds since boot
            return ctypes.windll.kernel32.GetTickCount64() / 1000.0
        else:
            return None  # Handle other platforms if needed

    def get_free_memory(self):
        """Returns the amount of free memory in bytes."""
        if sys.platform.startswith("linux"):
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemAvailable:'):
                        return int(line.split()[1]) * 1024  # Convert from kB to bytes
        elif sys.platform.startswith("darwin"):
            libc = ctypes.CDLL("libc.dylib")

            # Define the structure for vm_statistics_data
            class vm_statistics(ctypes.Structure):
                _fields_ = [
                    ("free_count", ctypes.c_uint),
                    ("active_count", ctypes.c_uint),
                    ("inactive_count", ctypes.c_uint),
                    ("wire_count", ctypes.c_uint),
                    ("zero_fill_count", ctypes.c_ulonglong),
                    ("reactivations", ctypes.c_ulonglong),
                    ("pageins", ctypes.c_ulonglong),
                    ("pageouts", ctypes.c_ulonglong),
                    ("faults", ctypes.c_ulonglong),
                    ("cow_faults", ctypes.c_ulonglong),
                    ("lookups", ctypes.c_ulonglong),
                    ("hits", ctypes.c_ulonglong),
                    ("purges", ctypes.c_ulonglong),
                    ("purgeable_count", ctypes.c_uint),
                    ("speculative_count", ctypes.c_uint),
                    ("decompressions", ctypes.c_ulonglong),
                    ("compressions", ctypes.c_ulonglong),
                    ("swapins", ctypes.c_ulonglong),
                    ("swapouts", ctypes.c_ulonglong),
                    ("compressor_page_count", ctypes.c_uint),
                    ("throttled_count", ctypes.c_uint),
                    ("external_page_count", ctypes.c_uint),
                    ("internal_page_count", ctypes.c_uint),
                    ("total_uncompressed_pages_in_compressor", ctypes.c_ulonglong),
                ]
            vm_stats = vm_statistics()
            size = ctypes.c_size_t(ctypes.sizeof(vm_stats))
            if libc.host_statistics(libc.mach_host_self(), 0, ctypes.byref(vm_stats), ctypes.byref(size)) == 0:
                page_size = 4096  # Default page size for macOS
                return vm_stats.free_count * page_size
            else:
                return None
        elif sys.platform.startswith("win32"):
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            kernel32 = ctypes.windll.kernel32
            GlobalMemoryStatusEx = kernel32.GlobalMemoryStatusEx
            GlobalMemoryStatusEx.argtypes = [ctypes.POINTER(MEMORYSTATUSEX)]
            GlobalMemoryStatusEx.restype = ctypes.c_int

            memorystatus = MEMORYSTATUSEX()
            memorystatus.dwLength = ctypes.sizeof(memorystatus)
            if GlobalMemoryStatusEx(ctypes.byref(memorystatus)):
                return memorystatus.ullAvailPhys
            else:
                return None
        else:
            return None  # Implement for other platforms

    def get_username(self):
        """Returns the current username."""
        if sys.platform.startswith("win32"):
            return os.environ.get("USERNAME")
        else:
            return os.environ.get("USER")

    def get_current_time_ms(self):
        """Returns the current time in milliseconds since the epoch."""
        if sys.platform.startswith("win32"):
            # On Windows, use GetTickCount64 for milliseconds since system startup
            return ctypes.windll.kernel32.GetTickCount64()
        else:
            # For Linux/macOS, use clock_gettime with CLOCK_MONOTONIC
            CLOCK_MONOTONIC = 1  # Use 1 for Linux, might need adjustment for macOS
            class timespec(ctypes.Structure):
                _fields_ = [("tv_sec", ctypes.c_long), ("tv_nsec", ctypes.c_long)]

            libc = ctypes.CDLL("libc.so.6")
            if sys.platform.startswith("darwin"):
                libc = ctypes.CDLL("libc.dylib")
            
            ts = timespec()
            libc.clock_gettime(CLOCK_MONOTONIC, ctypes.byref(ts))
            return ts.tv_sec * 1000 + ts.tv_nsec // 1000000

    def execute_command(self, command):
        """Executes a shell command and returns the output."""
        return os.popen(command).read()

    def print_message_with_delay(self, message, delay_seconds):
        """Prints a message with a delay before each character."""
        for char in message:
            print(char, end='', flush=True)
            self._sleep(delay_seconds)
        print()
    
    def get_local_time(self):
        """
        Gets the current local time based on the system's configuration.
        Returns:
            str: The current local time in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).
        """
        now = datetime.now()
        return now.isoformat()

    def time_since_or_until(self, date_str):
        """
        Calculates the time elapsed since a given date or the time until a future date.
        Provides years, months, and days in the output.

        Args:
            date_str (str): The date in the format "m/d/y" or "m/d/yyyy".

        Returns:
            str: A string describing the time elapsed or the time until the date.
        """
        try:
            # Parse the input date
            try:
                date_obj = datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                date_obj = datetime.strptime(date_str, "%m/%d/%y")

            # Get the current date
            now = datetime.now()

            # Calculate the difference
            delta = now - date_obj

            if delta.days >= 0:
                # Past date
                years = delta.days // 365
                months = (delta.days % 365) // 30
                days = (delta.days % 365) % 30

                if years > 0:
                    return f"This event occurred {years} year(s), {months} month(s), and {days} day(s) ago."
                elif months > 0:
                    return f"This event occurred {months} month(s) and {days} day(s) ago."
                elif days > 0:
                    return f"This event occurred {days} day(s) ago."
                else:
                    return "This event occurred today."
            else:
                # Future date
                years = abs(delta.days) // 365
                months = (abs(delta.days) % 365) // 30
                days = (abs(delta.days) % 365) % 30

                if years > 0:
                    return f"This event will occur in {years} year(s), {months} month(s), and {days} day(s)."
                elif months > 0:
                    return f"This event will occur in {months} month(s) and {days} day(s)."
                elif days > 0:
                    return f"This event will occur in {days} day(s)."
                else:
                    return "This event will occur today."

        except ValueError:
            print("Invalid date format. Please use m/d/y or m/d/yyyy.")
            return ""

    def get_screen_resolution(self):
        """
        Gets the screen resolution.
        Returns:
            str: The screen resolution in the format "widthxheight" or None if an error occurs.
        """
        try:
            if sys.platform.startswith("win32"):
                user32 = ctypes.windll.user32
                width = user32.GetSystemMetrics(0)
                height = user32.GetSystemMetrics(1)
                return f"{width}x{height}"
            elif sys.platform.startswith("linux"):
                # Try xrandr command-line tool
                output = os.popen("xrandr | grep '*").read()
                if output:
                    resolution = output.split()[0].split('x')
                    return f"{resolution[0]}x{resolution[1]}"
                else:
                    return None  # xrandr might not be available
            elif sys.platform.startswith("darwin"):
                # Try system_profiler command-line tool
                output = os.popen("system_profiler SPDisplaysDataType | grep Resolution").read()
                if output:
                    resolution = output.split(":")[1].strip().split(' ')[0].split('x')
                    return f"{resolution[0]}x{resolution[1]}"
                else:
                    return None
            else:
                return None  # Resolution detection not implemented for this platform
        except Exception as e:
            print(f"Error getting screen resolution: {e}")
            return None

    def get_system_info(self):
        """
        Gets basic system information.

        Returns:
            dict: A dictionary containing system information.
        """
        info = {}
        try:
            info["platform"] = platform.system()
            info["release"] = platform.release()
            info["version"] = platform.version()
            info["machine"] = platform.machine()
            info["processor"] = platform.processor()
            info["username"] = self.get_username()
        except Exception as e:
            print(f"Error getting system information: {e}")

        return info
    
    def generate_random_string(self, length):
        """
        Generates a random string of specified length.

        Args:
            length (int): The desired length of the random string.

        Returns:
            str: A random string.
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def capture_screenshot(self, filename="screenshot.png"):
        """
        Captures a screenshot and saves it to a file.

        Args:
            filename (str): The name of the file to save the screenshot to.
        """
        try:
            if sys.platform.startswith("win32"):
                import PIL.ImageGrab  # You might need to install Pillow: pip install Pillow
                screenshot = PIL.ImageGrab.grab()
                screenshot.save(filename)
                print(f"Screenshot saved to {filename}")
            elif sys.platform.startswith("linux"):
                # Try scrot command-line tool
                if os.system(f"scrot {filename}") == 0:
                    print(f"Screenshot saved to {filename}")
                else:
                    print("Error: scrot is not installed or failed to capture screenshot.")
            elif sys.platform.startswith("darwin"):
                # Try screencapture command-line tool
                if os.system(f"screencapture {filename}") == 0:
                    print(f"Screenshot saved to {filename}")
                else:
                    print("Error: screencapture failed to capture screenshot.")
            else:
                print("Screenshot functionality not implemented for this platform.")
        except ImportError:
            print("Error: PIL (Pillow) is not installed. Install it using: pip install Pillow")
        except Exception as e:
            print(f"Error capturing screenshot: {e}")

    def get_clipboard_content(self):
        """
        Gets the current content of the clipboard.

        Returns:
            str: The clipboard content, or None if an error occurs.
        """
        try:
            if sys.platform.startswith("win32"):
                import win32clipboard  # You might need to install pywin32: pip install pywin32

                win32clipboard.OpenClipboard()
                data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                return data
            elif sys.platform.startswith("linux"):
                # Try xclip command-line tool
                output = os.popen("xclip -o -selection clipboard").read()
                if output:
                    return output
                else:
                    print("Error: xclip might not be installed or failed to get clipboard content.")
                    return None
            elif sys.platform.startswith("darwin"):
                # Try pbpaste command-line tool
                output = os.popen("pbpaste").read()
                if output:
                    return output
                else:
                    print("Error: pbpaste failed to get clipboard content.")
                    return None
            else:
                print("Clipboard functionality not implemented for this platform.")
                return None
        except ImportError:
            print("Error: Required module not found. On Windows, install pywin32 using: pip install pywin32")
            return None
        except Exception as e:
            print(f"Error getting clipboard content: {e}")
            return None

    def set_clipboard_content(self, data):
        """
        Sets the clipboard content.

        Args:
            data (str): The data to set the clipboard to.
        """
        try:
            if sys.platform.startswith("win32"):
                import win32clipboard

                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(data)
                win32clipboard.CloseClipboard()
                print("Clipboard content set successfully.")
            elif sys.platform.startswith("linux"):
                # Try xclip command-line tool
                if os.system(f"echo '{data}' | xclip -selection clipboard") == 0:
                    print("Clipboard content set successfully.")
                else:
                    print("Error: xclip might not be installed or failed to set clipboard content.")
            elif sys.platform.startswith("darwin"):
                # Try pbcopy command-line tool
                if os.system(f"echo '{data}' | pbcopy") == 0:
                    print("Clipboard content set successfully.")
                else:
                    print("Error: pbcopy failed to set clipboard content.")
            else:
                print("Clipboard functionality not implemented for this platform.")
        except ImportError:
            print("Error: Required module not found. On Windows, install pywin32 using: pip install pywin32")
        except Exception as e:
            print(f"Error setting clipboard content: {e}")

# Create a single global instance of XSleep to be used by xsleep()
_xsleep_instance = XSleep()

def xsleep(seconds):
    """
    Multi-platform sleep function with additional logic.
    """
    _xsleep_instance.seconds(seconds)