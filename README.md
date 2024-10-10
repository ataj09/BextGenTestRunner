# BextGenTestRunner

Project done as part of internship task.
This project consists of two Python programs:

1. **Program A**: Acts as a pseudo-random number generator, responding to specific commands.
2. **Program B**: Launches Program A as a subprocess, interacts with it, retrieves random numbers, and performs some basic statistical analysis.


## Requirements

- Python 3.x
- No additional libraries are required. Both programs use Python’s standard library.

## How to Run the Programs

### Step 1: Clone the Repository
```bash
git clone https://github.com/ataj09/BextGenTestRunner.git
cd BextGenTestRunner
```

### Execute
```bash
python programB.py
```

### Test
After running output should look as follows:
```bash
Program A seems to be working correctly
element 1: 2
element 2: 5
...
element 100: 251
Median: 127.5
Average: 123.6
```