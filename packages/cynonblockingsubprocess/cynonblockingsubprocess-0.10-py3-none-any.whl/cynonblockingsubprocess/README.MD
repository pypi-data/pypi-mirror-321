# Nogil subprocess for Python with stdout/stderr capturing and stdin writing - without deadlocking!

## What is it?

**cynonblockingsubprocess** is a Cython-based wrapper around a C++ class called `ShellProcessManager`, defined in `nonblockingsubprocess.hpp`. Its purpose is to start and manage a shell process (e.g., `/bin/bash`, `"C:\\Windows\\System32\\cmd.exe"`, or any other command-line application), allowing you to:

- Write commands to the shell’s standard input.
- Read from the shell’s standard output and standard error without risking deadlocks.
- Run two background threads to non-blockingly capture `stdout` and `stderr` in **nogil** mode (reducing Python GIL contention).
- Optionally print `stdout` and/or `stderr` in real time while still retaining the captured output.

## Features

- **Non-blocking I/O**: Spawns separate threads to read `stdout` and `stderr` in the background, preventing the parent process from freezing or deadlocking.
- **Configurable Buffers**: Control the maximum length of captured `stdout` and `stderr` buffers before data is truncated, similar to a ring buffer (or `collections.deque`).
- **OS Compatibility**:
  - On **Windows**, you can customize process creation flags and environment parameters.
  - On **Linux/Unix**, the Windows-specific parameters are ignored, but the shell process is still managed the same way.
- **Graceful Shutdown**: Call `stop_shell()` to terminate the subprocess and background threads safely. When using subprocess.Popen, shells might keep open in the background, even after calling .kill() or .terminate(). This should not happen here! The C++ destructor takes care of closing the shell.

## Installation and Requirements

### `pip install cynonblockingsubprocess`

- **Cython** (to compile the `.pyx` / `.pxd` file).
- A **C++ compiler** (minimum version 11) compatible with your platform (e.g., `MSVC` on Windows or `g++`/`clang++` on Linux).
- The code will compile the first time you import it


## Usage example Python

```py
from cynonblockingsubprocess import CySubProc
from time import sleep
from platform import platform

iswindows = "win" in platform().lower()


# shell_command (bytes or str): Path or command to start (e.g., "C:\\Windows\\System32\\cmd.exe" or "/bin/bash").
# buffer_size (int): Size of the internal buffer for reading output (default 4096).
# stdout_max_len (int): Maximum amount of data retained in the stdout buffer (default 4096).
# stderr_max_len (int): Maximum amount of data retained in the stderr buffer (default 4096).
# exit_command (bytes or str): Command used internally to gracefully stop the shell (default b"exit").
# print_stdout (bool): If True, prints all stdout in real time to the console (default False).
# print_stderr (bool): If True, prints all stderr in real time to the console (default False).

tete = CySubProc(
    shell_command="C:\\Windows\\System32\\cmd.exe" if iswindows else "/bin/bash", # cross plattform
    buffer_size=4096,
    stdout_max_len=4096,
    stderr_max_len=4096,
    exit_command=b"exit",
    print_stdout=False,
    print_stderr=False,
)

# Start the shell process with specific creation flags and environment parameters.
# On Posix, all arguments are ignored!

# Detailed information can be found on Microsoft's website https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags

# Parameters
# ----------
# creationFlag : int, optional
#     A custom flag for process creation, by default 0.
# creationFlags : int, optional
#     Additional flags controlling process creation, by default 0x08000000.
# wShowWindow : int, optional
#     Flags controlling how the window is shown (e.g., hidden, normal, minimized),
#     by default 1 (SW_SHOWNORMAL).
# lpReserved : bytes or str, optional
#     Reserved parameter for process creation, by default None.
# lpDesktop : bytes or str, optional
#     The name of the desktop for the process, by default None.
# lpTitle : bytes or str, optional
#     The title for the new console window, by default None.
# dwX : int, optional
#     X-coordinate for the upper-left corner of the window, by default 0.
# dwY : int, optional
#     Y-coordinate for the upper-left corner of the window, by default 0.
# dwXSize : int, optional
#     Width of the window, by default 0.
# dwYSize : int, optional
#     Height of the window, by default 0.
# dwXCountChars : int, optional
#     Screen buffer width in character columns, by default 0.
# dwYCountChars : int, optional
#     Screen buffer height in character rows, by default 0.
# dwFillAttribute : int, optional
#     Initial text and background colors if used in a console, by default 0.
# dwFlags : int, optional
#     Flags that control how the creationFlags are used, by default 0.
# cbReserved2 : int, optional
#     Reserved for C runtime initialization, by default 0.
# lpReserved2 : bytes or str, optional
#     Reserved for C runtime initialization, by default None.

tete.start_shell() # This function must be always called first, if not, you probably will get segmentation faults!


# Write a command or input data to the shell process's stdin.

# Parameters
# ----------
# cmd : bytes or str
#     The command or data to send to the process via stdin.
tete.stdin_write("ls -l") # Writing an existing command 
sleep(1) # Wait a little for the output


# Retrieve the current contents of the shell's standard output as bytes, and clears the C++ vector

# Returns
# -------
# bytes
#     The raw bytes from the shell's stdout.
print(tete.get_stdout().decode()) # there will be something here


# Retrieve the current contents of the shell's standard error as bytes, and clears the C++ vector.

# Returns
# -------
# bytes
#     The raw bytes from the shell's stderr.
print(tete.get_stderr().decode()) # will be empty
tete.stdin_write("lxs xx-lxxxx") # command does not exist
sleep(1)
print(tete.get_stdout())  # will be empty
print(tete.get_stderr()) # there will be something here
del tete # closes the shell automatically! If you want, you can also call proc.stop_shell()

```

## Usage example C++ (stack)

```cpp
#include "nonblockingsubprocess.hpp"

int main(int argc, char *argv[])
{
    while (true)
    {
#ifdef _WIN32
        std::string shellcmd = "C:\\Windows\\System32\\cmd.exe";
#else
        std::string shellcmd = "/bin/bash";
#endif
        // arguments: std::string shell_command, size_t buffer_size = 4096, size_t stdout_max_len = 4096, size_t stderr_max_len = 4096, std::string exit_command = "exit", int print_stdout = 1, int print_stderr = 1
        ShellProcessManager proc{shellcmd, 4096, 4096, 4096, "exit", 1, 1};
        bool resultproc = proc.start_shell(); //optional arguments for Windows: DWORD creationFlag = 0, DWORD creationFlags = CREATE_NO_WINDOW, WORD wShowWindow = SW_NORMAL, LPSTR lpReserved = nullptr, LPSTR lpDesktop = nullptr, LPSTR lpTitle = nullptr, DWORD dwX = 0, DWORD dwY = 0, DWORD dwXSize = 0, DWORD dwYSize = 0, DWORD dwXCountChars = 0, DWORD dwYCountChars = 0, DWORD dwFillAttribute = 0, DWORD dwFlags = 0, WORD cbReserved2 = 0, LPBYTE lpReserved2 = nullptr
        std::cout << "resultproc: " << resultproc << std::endl;
        proc.stdin_write("ls -l");
        sleepcp(100);
        auto val = proc.get_stdout();
        std::cout << "stdout: " << val << std::endl;
        sleepcp(100);
        proc.stdin_write("ls -l");
        sleepcp(100);
        auto val2 = proc.get_stdout();
        std::cout << "stderr: " << val << std::endl;
        proc.stop_shell(); // optional: automatically called by the destructor
        sleepcp(1000);
    }
}
```

## Usage example C++ (heap)

```cpp
#include "nonblockingsubprocess.hpp"

int main(int argc, char *argv[])
{
    while (true)
    {
#ifdef _WIN32
        std::string shellcmd = "C:\\Windows\\System32\\cmd.exe";
#else
        std::string shellcmd = "/bin/bash";
#endif

        ShellProcessManager *proc = new ShellProcessManager{shellcmd, 4096, 4096, 4096, "exit", 1, 1};
        bool resultproc = proc->start_shell();
        std::cout << "resultproc: " << resultproc << std::endl;
        proc->stdin_write("ls -l");
        sleepcp(100);
        auto val = proc->get_stdout();
        std::cout << "v1111111111: " << val << std::endl;
        sleepcp(100);
        proc->stdin_write("ls -l");
        sleepcp(100);
        auto val2 = proc->get_stdout();
        std::cout << "v2222222222: " << val << std::endl;
        proc->stop_shell();
        sleepcp(1000);
    }
    delete proc
    std::cin.get();
}
```
