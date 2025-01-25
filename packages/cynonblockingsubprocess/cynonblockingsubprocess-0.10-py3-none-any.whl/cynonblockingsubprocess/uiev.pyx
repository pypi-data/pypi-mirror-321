cimport cython
import cython
from libcpp.string cimport string

##
# The following extern block wraps the C++ class ShellProcessManager from
# "nonblockingsubprocess.hpp", exposing its methods to Cython.
# Each method is briefly described below:
#
# ShellProcessManager(
#     string shell_command,
#     size_t buffer_size,
#     size_t stdout_max_len,
#     size_t stderr_max_len,
#     string exit_command,
#     int print_stdout,
#     int print_stderr
# )
#     Constructor that initializes the shell process manager with the desired
#     parameters, such as buffer sizes, command to exit the shell, etc.
#
# bint start_shell(
#     unsigned long creationFlag,
#     unsigned long creationFlags,
#     unsigned short wShowWindow,
#     char * lpReserved,
#     char * lpDesktop,
#     char * lpTitle,
#     unsigned long dwX,
#     unsigned long dwY,
#     unsigned long dwXSize,
#     unsigned long dwYSize,
#     unsigned long dwXCountChars,
#     unsigned long dwYCountChars,
#     unsigned long dwFillAttribute,
#     unsigned long dwFlags,
#     unsigned long cbReserved2,
#     unsigned char * lpReserved2
# )
#     Starts the shell process with the specified window creation parameters and
#     environment details (ignored on Posix)
#
# bint stdin_write(string)
#     Writes a string to the process's standard input. Returns boolean success/failure.
#
# string get_stdout()
#     Retrieves all available standard output data from the shell process.
#
# string get_stderr()
#     Retrieves all available standard error data from the shell process.
#
# void stop_shell()
#     Stops the shell process if it is running.
##

cdef extern from "nonblockingsubprocess.hpp" nogil :
    cdef cppclass ShellProcessManager:
        void ShellProcessManager(
            string shell_command,
            size_t buffer_size,
            size_t stdout_max_len,
            size_t stderr_max_len,
            string exit_command,
            int print_stdout,
            int print_stderr)
        bint start_shell(unsigned long creationFlag,
                        unsigned long creationFlags,
                        unsigned short wShowWindow,
                        char * lpReserved,
                        char * lpDesktop,
                        char * lpTitle,
                        unsigned long dwX,
                        unsigned long dwY,
                        unsigned long dwXSize,
                        unsigned long dwYSize,
                        unsigned long dwXCountChars,
                        unsigned long dwYCountChars,
                        unsigned long dwFillAttribute,
                        unsigned long dwFlags,
                        unsigned long cbReserved2,
                        unsigned char * lpReserved2,)
        bint stdin_write(string)
        string get_stdout()
        string get_stderr()
        void stop_shell()

cdef class CySubProc:
    """
    CySubProc is a Cython class that provides a Python interface to a C++ ShellProcessManager.
    It allows you to start a shell process, write commands to stdin, and read stdout/stderr output without deadlocking.
    The 2 two threads that read from stdout/stderr run in nogil mode
    """
    cdef ShellProcessManager*subproc

    def __init__(self,
                object shell_command,
                size_t buffer_size=4096,
                size_t stdout_max_len=4096,
                size_t stderr_max_len=4096,
                object exit_command=b"exit",
                bint print_stdout=False,
                bint print_stderr=False,
                ):
        r"""
        Initialize the CySubProc object.

        Parameters
        ----------
        shell_command : bytes or str
            The command used to start the shell or interpreter (e.g., b'/bin/bash' or "C:\\Windows\\System32\\cmd.exe").
        buffer_size : int, optional
            The size of the buffer used when reading output, by default 4096.
        stdout_max_len : int, optional
            The maximum length of stdout before truncation or buffering logic, by default 4096.
            It treats the C++ vector that stores the output data like collections.deque
        stderr_max_len : int, optional
            The maximum length of stderr before truncation or buffering logic, by default 4096.
            It treats the C++ vector that stores the output data like collections.deque
        exit_command : bytes or str, optional
            The command sent to gracefully exit the shell, by default b"exit".
        print_stdout : bool, optional
            Whether to print the shell's stdout directly, by default False.
            Stdout is saved nevertheless, it is not lost after printing!
        print_stderr : bool, optional
            Whether to print the shell's stderr directly, by default False.
            Stderr is saved nevertheless, it is not lost after printing!

        Returns
        -------
        None
        """
        cdef:
            string cpp_shell_command
            string cpp_exit_command
        if isinstance(shell_command,bytes):
            cpp_shell_command=<string>shell_command
        else:
            cpp_shell_command=<string>(str(shell_command).encode())
        if isinstance(exit_command,bytes):
            cpp_exit_command=<string>exit_command
        else:
            cpp_exit_command=<string>(str(exit_command).encode())

        self.subproc= new ShellProcessManager(
        shell_command=cpp_shell_command,
        buffer_size=buffer_size,
        stdout_max_len=stdout_max_len,
        stderr_max_len=stderr_max_len,
        exit_command=cpp_exit_command,
        print_stdout=print_stdout,
        print_stderr=print_stderr
    )
    cpdef start_shell(
        self,
        unsigned long  creationFlag=0,
        unsigned long  creationFlags=0x08000000,
        unsigned short  wShowWindow=1,
        object lpReserved=None,
        object lpDesktop=None,
        object lpTitle=None,
        unsigned long  dwX=0,
        unsigned long  dwY=0,
        unsigned long  dwXSize=0,
        unsigned long  dwYSize=0,
        unsigned long  dwXCountChars=0,
        unsigned long  dwYCountChars=0,
        unsigned long  dwFillAttribute=0,
        unsigned long  dwFlags=0,
        unsigned long  cbReserved2=0,
        object lpReserved2=None,
    ):
        r"""
        Start the shell process with specific creation flags and environment parameters.
        On Posix, all arguments are ignored!

        Detailed information can be found on Microsoft's website https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags

        Parameters
        ----------
        creationFlag : int, optional
            A custom flag for process creation, by default 0.
        creationFlags : int, optional
            Additional flags controlling process creation, by default 0x08000000.
        wShowWindow : int, optional
            Flags controlling how the window is shown (e.g., hidden, normal, minimized),
            by default 1 (SW_SHOWNORMAL).
        lpReserved : bytes or str, optional
            Reserved parameter for process creation, by default None.
        lpDesktop : bytes or str, optional
            The name of the desktop for the process, by default None.
        lpTitle : bytes or str, optional
            The title for the new console window, by default None.
        dwX : int, optional
            X-coordinate for the upper-left corner of the window, by default 0.
        dwY : int, optional
            Y-coordinate for the upper-left corner of the window, by default 0.
        dwXSize : int, optional
            Width of the window, by default 0.
        dwYSize : int, optional
            Height of the window, by default 0.
        dwXCountChars : int, optional
            Screen buffer width in character columns, by default 0.
        dwYCountChars : int, optional
            Screen buffer height in character rows, by default 0.
        dwFillAttribute : int, optional
            Initial text and background colors if used in a console, by default 0.
        dwFlags : int, optional
            Flags that control how the creationFlags are used, by default 0.
        cbReserved2 : int, optional
            Reserved for C runtime initialization, by default 0.
        lpReserved2 : bytes or str, optional
            Reserved for C runtime initialization, by default None.

        Returns
        -------
        None
        """
        cdef:
            string cpp_lpReserved, cpp_lpDesktop, cpp_lpTitle, cpp_lpReserved2
            unsigned char* ptr_lpReserved2
            char* ptr_lpReserved
            char* ptr_lpDesktop
            char* ptr_lpTitle
            size_t addr_cpp_lpReserved, addr_cpp_lpDesktop, addr_cpp_lpTitle, addr_cpp_lpReserved2

        if not lpReserved:
            lpReserved=b'\x00'
        if not lpDesktop:
            lpDesktop=b'\x00'
        if not lpTitle:
            lpTitle=b'\x00'
        if not lpReserved2:
            lpReserved2=b'\x00'
        if isinstance(lpReserved, bytes):
            cpp_lpReserved=<string>lpReserved
        else:
            cpp_lpReserved=<string>(str(lpReserved).encode())
        if isinstance(lpDesktop, bytes):
            cpp_lpDesktop=<string>lpDesktop
        else:
            cpp_lpDesktop=<string>(str(lpDesktop).encode())
        if isinstance(lpTitle, bytes):
            cpp_lpTitle=<string>lpTitle
        else:
            cpp_lpTitle=<string>(str(lpTitle).encode())
        if isinstance(lpReserved2, bytes):
            cpp_lpReserved2=<string>lpReserved2
        else:
            cpp_lpReserved2=<string>(str(lpReserved2).encode())

        # Obtain raw pointers to the underlying string data.
        # Cython is nagging when assigning or casting directly to char pointers of .data() (temporary object ... unsafe ... blah blah blah)
        # But the data pointer of the string doesn't not change as long as the size of the string doesn't change which is the case here.
        # It works perfectly on Windows, and on Linux, the pointers and all other arguments are ignored anyways, so they could even be dangling on Posix, it wouldn't matter at all.
        addr_cpp_lpReserved=<size_t>(&(cpp_lpReserved.data()[0]))
        addr_cpp_lpDesktop=<size_t>(&(cpp_lpDesktop.data()[0]))
        addr_cpp_lpTitle=<size_t>(&(cpp_lpTitle.data()[0]))
        addr_cpp_lpReserved2=<size_t>(&(cpp_lpReserved2.data()[0]))

        ptr_lpReserved=<char*>addr_cpp_lpReserved
        ptr_lpDesktop=<char*>addr_cpp_lpDesktop
        ptr_lpTitle=<char*>addr_cpp_lpTitle
        ptr_lpReserved2=<unsigned char*>(addr_cpp_lpReserved2)
        self.subproc.start_shell(
                    creationFlag=creationFlag,
                    creationFlags=creationFlags,
                    wShowWindow=wShowWindow,
                    lpReserved=ptr_lpReserved,
                    lpDesktop=ptr_lpDesktop,
                    lpTitle=ptr_lpTitle,
                    dwX=dwX,
                    dwY=dwY,
                    dwXSize=dwXSize,
                    dwYSize=dwYSize,
                    dwXCountChars=dwXCountChars,
                    dwYCountChars=dwYCountChars,
                    dwFillAttribute=dwFillAttribute,
                    dwFlags=dwFlags,
                    cbReserved2=cbReserved2,
                    lpReserved2=ptr_lpReserved2,
                    )
    cpdef stdin_write(self, object cmd):
        """
        Write a command or input data to the shell process's stdin.

        Parameters
        ----------
        cmd : bytes or str
            The command or data to send to the process via stdin.

        Returns
        -------
        None
        """
        cdef:
            string cpp_cmd
        if isinstance(cmd,bytes):
            cpp_cmd=<string>cmd
        elif isinstance(cmd,str):
            cpp_cmd=<string>(cmd.encode())
        else:
            cpp_cmd=<string>str(cmd).encode()
        self.subproc.stdin_write(cpp_cmd)

    cpdef bytes get_stdout(self):
        """
        Retrieve the current contents of the shell's standard output as bytes, and clears the C++ vector

        Returns
        -------
        bytes
            The raw bytes from the shell's stdout.
        """
        return self.subproc.get_stdout()

    cpdef bytes get_stderr(self):
        """
        Retrieve the current contents of the shell's standard error as bytes, and clears the C++ vector.

        Returns
        -------
        bytes
            The raw bytes from the shell's stderr.
        """
        return self.subproc.get_stderr()

    cpdef stop_shell(self):
        """
        Stop the running shell process gracefully (stops the 2 background threads and writes the exit command 5 times to the shell - in case there are subshells running).

        Returns
        -------
        None
        """
        self.subproc.stop_shell()

    cdef string read_stdout(self):
        """
        Read the current contents of the shell's standard output as a C++ string, and clears the C++ vector.
        This function is Cython only, and has the advantage that it does not convert the data to a Python object

        Returns
        -------
        string
            The raw C++ string from the shell's stdout.
        """
        return self.subproc.get_stdout()

    cdef string read_stderr(self):
        """
        Read the current contents of the shell's standard error as a C++ string, and clears the C++ vector.
        This function is Cython only, and has the advantage that it does not convert the data to a Python object

        Returns
        -------
        string
            The raw C++ string from the shell's stderr.
        """
        return self.subproc.get_stderr()

    def __dealloc__(self):
        """
        Calls the C++ destructor, which executes the C++ stop_shell function
        It deallocates the underlying ShellProcessManager pointer when this object is garbage collected.
        """
        del self.subproc

