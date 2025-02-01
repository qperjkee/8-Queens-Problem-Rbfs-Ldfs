# 8 Queens Problem

The project contains the main program code and its tests.
![8 Queens](https://github.com/user-attachments/assets/fcaa6d53-5e18-4caf-9777-b46c739c6d49)

## Running the Algorithm

To test the algorithm, you should run the file named `main.py` through your own IDE or navigate to the file's directory and enter the following in the console:
```bash
python -u main.py
```

After starting the file, the `main` function, which is the main function of the program, will be called. At the beginning of the program execution, the user will be prompted to choose:

- The board size (from 4 to 8)
- The search algorithm: **LDFS** or **RBFS**

For **LDFS**, you will also need to select the maximum search depth. Afterward, the algorithm will start, and once it finishes, the result will be displayed in the form of a board, where:

- **Q**: A queen in the correct position without conflicts
- **q**: A queen with conflicts

Additionally, the time taken to run the algorithm will be displayed.

## Running Tests

Tests were conducted for all algorithms in the program, starting from user input and data generation to the search process and the use of auxiliary functions.

To check the tests, you should run the file `tests.py`. After running, the console will display the status of all passed tests and the time it took to run them.