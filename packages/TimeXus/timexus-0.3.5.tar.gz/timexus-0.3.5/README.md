# TimeXus

TimeXus is a Python library that provides enhanced time-related utilities, building upon the basic functionalities found in the standard library. It offers precise sleep functions, system information retrieval, and various date, time, and utility functions. It's designed to be easy to use and extend, making it suitable for a wide range of applications. **Note:** TimeXus does not use the `time` module for its core sleep functionality, but it does utilize `datetime` for some date and time-related features.

## Features

### Precise Sleep Functions:

These functions provide ways to pause the execution of your program for specific durations or random intervals.

*   **`xsleep(seconds)`**

    -   **Description:** A basic sleep function similar to `time.sleep()` but using a more precise, cross-platform mechanism. Pauses the program execution for the specified number of seconds.
    -   **How to use:**

        ```python
        from timexus import xsleep

        xsleep(2.5)  # Pauses execution for 2.5 seconds
        ```

    -   **Auto-print:** Enabled by default, printing a message indicating the sleep duration. Can be globally disabled using `XSleep.set_print("off")`.
    -   **Returns:** The number of seconds slept.

*   **`XSleep.milliseconds(ms)`**

    -   **Description:** Sleeps for the specified number of milliseconds.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.milliseconds(500)  # Pauses execution for 500 milliseconds (0.5 seconds)
        ```

    -   **Auto-print:** Enabled by default. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("milliseconds", "off")`.
    -   **Returns:** The number of seconds slept (ms / 1000).

*   **`XSleep.seconds(secs)`**

    -   **Description:** Sleeps for the specified number of seconds.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.seconds(3)  # Pauses execution for 3 seconds
        ```

    -   **Auto-print:** Enabled by default. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("seconds", "off")`.
    -   **Returns:** The number of seconds slept.

*   **`XSleep.minutes(mins)`**

    -   **Description:** Sleeps for the specified number of minutes.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.minutes(1.5)  # Pauses execution for 1.5 minutes (90 seconds)
        ```

    -   **Auto-print:** Enabled by default. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("minutes", "off")`.
    -   **Returns:** The number of seconds slept (mins * 60).

*   **`XSleep.hours(hrs)`**

    -   **Description:** Sleeps for the specified number of hours.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.hours(0.25)  # Pauses execution for 0.25 hours (15 minutes)
        ```

    -   **Auto-print:** Enabled by default. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("hours", "off")`.
    -   **Returns:** The number of seconds slept (hrs * 3600).

*   **`XSleep.get_random_delay(min_seconds, max_seconds)`**

    -   **Description:**  Calculates and returns a random delay (in seconds) between the given `min_seconds` and `max_seconds`. It does not sleep automatically, you need to use the returned value with `XSleep.seconds()` or `xsleep()` if you want to sleep for that duration.
    -   **How to use:**

        ```python
        from timexus import XSleep

        delay = XSleep.get_random_delay(2, 5)  # Get a random delay between 2 and 5 seconds
        print(f"Random delay: {delay:.4f} seconds") 
        XSleep.seconds(delay)  # Sleep for the random duration
        ```
    - **Auto-print:** Enabled by default, printing the generated random delay. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("get_random_delay", "off")`. You can also use `XSleep.sleep_random_delay()` to sleep directly.
    - **Returns:** The random delay in seconds.

*   **`XSleep.sleep_random_delay(min_seconds, max_seconds)`**

    -   **Description:** Sleeps for a random duration between the given `min_seconds` and `max_seconds`.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.sleep_random_delay(1, 3) # Sleeps for a random time between 1 and 3 seconds.
        ```

    -   **Auto-print:** Enabled by default. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("sleep_random_delay", "off")`.
    - **Returns:** The random delay in seconds.

*   **`XSleep.set_print("on" | "off")`**

    -   **Description:** Globally enables or disables the auto-print messages for all sleep functions in the `XSleep` class.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.set_print("off")  # Disable all auto-print messages
        XSleep.seconds(1)  # No message will be printed
        XSleep.set_print("on")  # Re-enable all auto-print messages
        ```

*   **`XSleep.set_auto_print_for_function(func_name, "on" | "off")`**
    -   **Description:** Enables or disables auto-print messages for a specific function within the `XSleep` class. This overrides the global setting.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.set_auto_print_for_function("capture_screenshot", "off") # Disable auto-print for capture_screenshot
        XSleep.capture_screenshot() # No message will be printed

        XSleep.set_auto_print_for_function("seconds", "off")
        XSleep.seconds(1) # No message will be printed

        XSleep.set_auto_print_for_function("get_random_delay", "on")
        XSleep.get_random_delay(1, 2) # Will print the random delay
        ```

*   **`XSleep.get_auto_print_status()`**
    -   **Description:** Prints the current auto-print status for each function and the global auto-print status.
    -   **How to use:**
        ```python
        from timexus import XSleep
        
        XSleep.get_auto_print_status()
        ```

*   **`XSleep.set_custom_print(message)`**

    -   **Description:** Customizes the message that is printed when you sleep for exactly 0 seconds.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.set_custom_print("I'm awake now!")
        XSleep.seconds(0)  # Prints "I'm awake now!"
        ```

*   **`XSleep.get_total_sleep_time()`**

    -   **Description:** Returns the total accumulated sleep time (in seconds) since the `XSleep` class was loaded or since the last call to `XSleep.reset_total_sleep_time()`.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.seconds(1)
        XSleep.milliseconds(500)
        total_sleep = XSleep.get_total_sleep_time()
        print(f"Total sleep time: {total_sleep} seconds")  # Output: Total sleep time: 1.5 seconds
        ```

*   **`XSleep.reset_total_sleep_time()`**

    -   **Description:** Resets the total sleep time counter to 0.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.seconds(2)
        XSleep.reset_total_sleep_time()
        total_sleep = XSleep.get_total_sleep_time()
        print(f"Total sleep time: {total_sleep} seconds")  # Output: Total sleep time: 0 seconds
        ```

### System Information:

These functions provide information about the system on which the script is running.

*   **`XSleep.get_pid()`**

    -   **Description:** Gets the current process ID.
    -   **How to use:**

        ```python
        from timexus import XSleep

        pid = XSleep.get_pid()
        print(f"Process ID: {pid}")
        ```

*   **`XSleep.get_cpu_count()`**

    -   **Description:** Gets the number of CPU cores (logical processors).
    -   **How to use:**

        ```python
        from timexus import XSleep

        cpu_count = XSleep.get_cpu_count()
        print(f"CPU Cores: {cpu_count}")
        ```

*   **`XSleep.is_interactive()`**

    -   **Description:** Checks if the current Python session is interactive (e.g., running in a terminal or an interactive interpreter).
    -   **How to use:**

        ```python
        from timexus import XSleep

        if XSleep.is_interactive():
            print("Running in an interactive session")
        else:
            print("Running in a non-interactive session (e.g., a script)")
        ```

*   **`XSleep.get_platform()`**

    -   **Description:** Returns a string identifying the operating system platform (e.g., "win32", "linux", "darwin").
    -   **How to use:**

        ```python
        from timexus import XSleep

        platform_name = XSleep.get_platform()
        print(f"Platform: {platform_name}")
        ```

*   **`XSleep.get_uptime()`**

    -   **Description:** Returns the system uptime in seconds (the time elapsed since the last boot).
    -   **How to use:**

        ```python
        from timexus import XSleep

        uptime = XSleep.get_uptime()
        print(f"Uptime: {uptime} seconds")
        ```

*   **`XSleep.get_free_memory()`**

    -   **Description:** Returns the amount of free memory available in bytes.
    -   **How to use:**

        ```python
        from timexus import XSleep

        free_memory = XSleep.get_free_memory()
        print(f"Free memory: {free_memory} bytes")
        ```

*   **`XSleep.get_username()`**

    -   **Description:** Returns the username of the current user.
    -   **How to use:**

        ```python
        from timexus import XSleep

        username = XSleep.get_username()
        print(f"Username: {username}")
        ```

*   **`XSleep.get_current_time_ms()`**

    -   **Description:** Returns the current time in milliseconds since the epoch (January 1, 1970, 00:00:00 UTC).
    -   **How to use:**

        ```python
        from timexus import XSleep

        current_time_ms = XSleep.get_current_time_ms()
        print(f"Current time (ms since epoch): {current_time_ms}")
        ```

*   **`XSleep.get_screen_resolution()`**

    -   **Description:** Returns the screen resolution as a string in the format "widthxheight" (e.g., "1920x1080").
    -   **How to use:**

        ```python
        from timexus import XSleep

        resolution = XSleep.get_screen_resolution()
        if resolution:
            print(f"Screen resolution: {resolution}")
        else:
            print("Could not determine screen resolution")
        ```

*   **`XSleep.get_system_info()`**

    -   **Description:** Returns a dictionary containing various system information, including:
        -   `platform`: Operating system platform (e.g., "Windows", "Linux", "Darwin").
        -   `release`: OS release (e.g., "10", "5.15.0-88-generic").
        -   `version`: OS version.
        -   `machine`: Machine architecture (e.g., "AMD64", "x86_64").
        -   `processor`: Processor information.
        -   `username`: Current username.
    -   **How to use:**

        ```python
        from timexus import XSleep

        system_info = XSleep.get_system_info()
        for key, value in system_info.items():
            print(f"{key}: {value}")
        ```

### Date and Time:

These functions provide utilities for working with dates and times.

*   **`XSleep.get_local_time()`**

    -   **Description:** Returns the current local time based on the system's timezone settings. The time is formatted as an ISO 8601 string (YYYY-MM-DDTHH:MM:SS).
    -   **How to use:**

        ```python
        from timexus import XSleep

        local_time = XSleep.get_local_time()
        print(f"Local time: {local_time}")
        ```

*   **`XSleep.time_since_or_until(date_str)`**

    -   **Description:** Calculates the time elapsed since a given date or the time until a future date. The input `date_str` should be in the format "m/d/y" or "m/d/yyyy". The output is a human-readable string that includes years, months, and days.
    -   **How to use:**

        ```python
        from timexus import XSleep

        # Time since a past date
        past_date = "1/1/2023"
        time_since = XSleep.time_since_or_until(past_date)
        print(f"Time since {past_date}: {time_since}")

        # Time until a future date
        future_date = "12/25/2024"
        time_until = XSleep.time_since_or_until(future_date)
        print(f"Time until {future_date}: {time_until}")
        ```

### Utility Functions:

These functions offer miscellaneous utilities that can be helpful in various scripts.

*   **`XSleep.execute_command(command)`**

    -   **Description:** Executes a shell command and returns the output as a string.
    -   **How to use:**

        ```python
        from timexus import XSleep

        output = XSleep.execute_command("ls -l")  # Example: List files in the current directory (Linux/macOS)
        # output = XSleep.execute_command("dir") # Example: List files in the current directory (Windows)
        print(output)
        ```

*   **`XSleep.print_message_with_delay(message, delay_seconds)`**

    -   **Description:** Prints a message to the console, with a delay (in seconds) between each character.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.print_message_with_delay("Hello, world!", 0.1)  # Prints "Hello, world!" with a 0.1-second delay between characters
        ```
    -   **Auto-print:** Enabled by default. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("print_message_with_delay", "off")`.

*   **`XSleep.generate_random_string(length)`**

    -   **Description:** Generates a random string of the specified length. The string contains uppercase and lowercase letters, digits, and punctuation.
    -   **How to use:**

        ```python
        from timexus import XSleep

        random_string = XSleep.generate_random_string(16)
        print(f"Random string: {random_string}")
        ```

*   **`XSleep.capture_screenshot(filename="screenshot.png")`**

    -   **Description:** Captures a screenshot and saves it to a file with the given filename. The default filename is "screenshot.png".
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.capture_screenshot("my_screenshot.png")  # Captures a screenshot and saves it as "my_screenshot.png"
        ```
    -   **Auto-print:** Enabled by default, printing a message indicating the file path where the screenshot was saved. You can disable it globally with `XSleep.set_print("off")` or for this specific function using `XSleep.set_auto_print_for_function("capture_screenshot", "off")`.

*   **`XSleep.get_clipboard_content()`**

    -   **Description:** Gets the current content of the system clipboard.
    -   **How to use:**

        ```python
        from timexus import XSleep

        clipboard_content = XSleep.get_clipboard_content()
        if clipboard_content:
            print(f"Clipboard content: {clipboard_content}")
        else:
            print("Clipboard is empty or could not be accessed")
        ```

*   **`XSleep.set_clipboard_content(data)`**

    -   **Description:** Sets the content of the system clipboard to the given string `data`.
    -   **How to use:**

        ```python
        from timexus import XSleep

        XSleep.set_clipboard_content("This text is now on the clipboard")
        ```

## Installation

**From PyPI:**

```bash
pip install TimeXus
```

## Bug Fixes (Version 0.3.5)
get_random_delay() now returns the delay value: Previously, it only printed the value but didn't return it. Now it correctly returns the generated random delay, allowing you to use it in further calculations.

Full control over print messages: The set_print() function now correctly globally disables/enables all print statements within XSleep.

Static Methods: All methods in the XSleep class are now static. You can use them directly without creating an instance of XSleep.

"Awake!" message logic: The "Awake!" message (or the custom message) is now printed only when you sleep for exactly 0 seconds.

Improved Documentation: Added docstrings to all methods explaining their purpose, arguments, return values, and potential exceptions.

Consistent Naming: Followed consistent naming conventions (CamelCase for the class, lowercase for the function).

Robust Error Handling: Added ValueError exceptions to many functions to handle invalid input types or values.

Methods now return values: Functions like milliseconds, seconds, minutes, hours, get_random_delay now return relevant values, making them more useful.

set_custom_print: Now always takes a message argument. If you don't want a custom message, pass an empty string ("") to effectively disable it.

Individual Function Auto-Print Control: Added the ability to control auto-print behavior for each function individually using XSleep.set_auto_print_for_function(). This overrides the global setting made by XSleep.set_print().

Print Status Check: Added XSleep.get_auto_print_status() to display the current auto-print settings for each function and globally.