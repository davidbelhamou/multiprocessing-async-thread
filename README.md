# multiprocessing-async-thread

- ***Some important keywords***:
    - A process is a computer program
    - A thread refers to a thread of execution within a computer program


- Therefore, each program is a process that has at least one thread that executes instructions for that process.
    - Concurrency refers to executing tasks out of order.
    - Parallelism refers to executing tasks simultaneously.

When we are developing code, we can achieve concurrency with or without parallelism, although concurrency
(e.g. task order being irrelevant) is a prerequisite for parallelism.  
Our goal is to speed up a program by executing two or more tasks simultaneously. We are
almost always interested in parallelism when we talk about Python concurrency.

Thread-based concurrency is provided via the threading module and the Thread class.
Threads are fast to start and can share data with each other within a single Python process.
Nevertheless, thread-based concurrency in Python is limited by the Global Interpreter Lock
(GIL). Threads are only capable of parallelism when the GIL is released, such as when
performing I/O operations or explicitly by third party libraries.

Process-based concurrency is provided via the multiprocessing module and the Process
class. It was developed in Python v2.6 as an alternative to thread-based concurrency that is not
limited by the GIL.
Processes are a heavyweight approach to concurrency as processes are slower to start than
threads. Unlike threads, they are subject to the cost of having to serialize (pickle) data
in order to transmit it between processes.
Nevertheless, the multiprocessing module is capable of concurrency and full parallelism in
Python.

Now that we are on the same page when it comes to threads, processes, concurrency and
parallelism, let’s dive into more detail on threads and processes and when we should be using
multiprocessing for process-based concurrency in Python.

***Differences***  
The threading and multiprocessing modules are also quite different, let’s review some of
the most important differences.
They are:

1. Native Threads vs. Native Processes.
2. Shared Memory vs. Inter-Process Communication.
3. Limited vs Full Parallelism (GIL).

***Shared Memory vs. Inter-Process Communication***  
Concurrency typically requires sharing data or program state between tasks.
Threads and Processes have important differences in the way they access shared state. Threads can share memory within a
process.
This means that functions executed in new threads can access the same data. These might
be global variables or data shared via function arguments. As such, sharing state between threads is straightforward.
Processes do not have shared memory like threads. Instead, state must be serialized and transmitted between processes,
called inter-process communication.

***Limited vs Full Parallelism (GIL)***  
Thread-based concurrency supports limited parallelism, whereas process-based concurrency
supports full parallelism.
Multiple threads are subject to the global interpreter lock (GIL), whereas multiple child
processes are not subject to the GIL.
This means that although we may have multiple threads in our program, only one thread can
execute at a time.
The GIL is used within each Python process, but not across processes. This means that
multiple child processes can execute at the same time and are not subject to the GIL.
This has implications for the types of tasks best suited to each class.

***Summary of Differences***

| Property    | threading             | multiprocessing           |
|-------------|-----------------------|---------------------------|
| Type        | Uses native threads.  | Uses native processes.    |
| Relation    | Belongs to a process. | Has threads and children. |
| Sharing     | Shared memory.        | Inter-process comms.      |
| Weight      | Light, fast to start. | Heavy, slow to start.     |
| Parallelism | Limited (GIL).        | Full (no GIL).            |
| Tasks       | IO-bound tasks.       | CPU-bound tasks.          |
| Number      | 10s to 1,000s.        | 10s (or fewer).           |

***Examples of CPU-Bound Tasks***  
Some examples of CPU-bound tasks include:

1. Calculating points in a fractal.
2. Estimating Pi
3. Factoring primes.
4. Parsing HTML, JSON, etc. documents.
5. Processing text.
6. Running simulations.

***Examples of IO-Bound Tasks***  
Some examples of common IO-bound tasks include:

1. Reading or writing a file from the hard drive.
2. Reading or writing to standard output, input, or error (stdin, stdout, stderr).
3. Printing a document.
4. Downloading or uploading a file.
5. Querying a database.
