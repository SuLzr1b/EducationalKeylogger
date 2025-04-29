# EducationalKeylogger

A simple Python keylogger built for educational purposes to learn about keyboard event capturing and logging.

**WARNING**: This project is for educational purposes only. Do not use to monitor devices without explicit permission. Unauthorized use may violate laws, such as Brazil's General Data Protection Law (LGPD).

## Purpose
This project is designed to help cybersecurity students understand how keyloggers work in a controlled, ethical environment. It captures keystrokes and logs them to a file with timestamps, simulating basic monitoring techniques for educational purposes.

## Features
- Captures all keystrokes, including special keys (e.g., Space, Enter, Backspace).
- Logs keystrokes with timestamps to `log.txt`.
- Stops logging when the `Esc` key is pressed.
- Includes ethical warnings to ensure responsible use.
- Works across applications when run with administrator privileges (Windows) or sudo (Linux/Mac).

## Requirements
- Python 3.x
- `keyboard` library (`pip install keyboard`)
- **Windows**: Run as administrator to capture keys in other applications.
- **Linux/Mac**: May require `sudo` for full functionality.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EducationalKeylogger.git
   ```
2. Install the required library:
   ```bash
   pip install keyboard
   ```

## Usage
1. Navigate to the project directory:
   ```bash
   cd EducationalKeylogger
   ```
2. Run the keylogger:
   ```bash
   python keylogger.py
   ```
3. Type `y` to confirm execution.
4. Type anything; logs are saved to `log.txt`.
5. Press `Esc` to stop.
6. Check `log.txt` for the recorded keystrokes.

**Note**: Always test in a controlled environment with explicit permission. Make a backup of any important files.

### Windows Tip
To capture keys in other applications (e.g., Notepad, browsers), run the script as administrator:
- Right-click Command Prompt or PowerShell, select "Run as administrator," then execute `python keylogger.py`.

### Linux/Mac Tip
You may need to run with `sudo`:
```bash
sudo python keylogger.py
```

## Example Log (`log.txt`)
```
2025-04-28 21:30:15.123456: h
2025-04-28 21:30:15.234567: i
2025-04-28 21:30:15.345678:  [SPACE] 
2025-04-28 21:30:15.456789: t
2025-04-28 21:30:15.567890: e
2025-04-28 21:30:15.678901: s
2025-04-28 21:30:15.789012: t
2025-04-28 21:30:15.890123: !
2025-04-28 21:30:15.901234:  [ENTER] 
```

## Ethical Considerations
This tool is strictly for educational purposes, such as learning about cybersecurity threats like keyloggers. Do not use it to monitor devices or networks without explicit consent, as this may violate privacy laws, including Brazil’s LGPD. Always obtain permission and test in a controlled environment.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
