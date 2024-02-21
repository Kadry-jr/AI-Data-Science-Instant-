##### **Clean Code Rules**
#1. Meaningful Names

  Choose descriptive and meaningful names for variables, functions, classes, and methods. Names should reveal intent and make the code self-explanatory.
  ``` 
  // Bad example
  int d; // elapsed time in days
  
  // Good example
  int elapsedTimeInDays;
  ```
#2.Functions Should Do One Thing
      
  Functions should have a single responsibility and should do one thing. They should be small and concise.
  ```
    // Bad example
  void processData() {
      // process data
      // send email
  }
  
  // Good example
  void processData() {
      // process data
  }
  
  void sendEmail() {
      // send email
  }
  ```
#3.Avoid Side Effects

  Functions should not produce side effects. They should operate only on their inputs and not modify any other state outside the function.
  ```
    // Bad example
  void updateDatabase() {
      // modify global state
  }
  
  // Good example
  void updateDatabase(Data data) {
      // modify database using input data
  }
```
#4.Comments

  Write clean, self-explanatory code that does not require comments for understanding. Comments should be used sparingly and only when necessary to clarify complex logic.
  ```
    // Bad example
  // Check if user is active
  if (user.status == ACTIVE) {
      // perform operation
  }
  
  // Good example
  if (user.isActive()) {
      // perform operation
  }
  ```
#5.Formatting

  Follow consistent formatting and coding style throughout the codebase. Use proper indentation, spacing, and naming conventions.
  ```
  // Bad example
  int a=b+c;
  
  // Good example
  int sum = b + c;
  ```
#6.Error Handling

  Properly handle errors and exceptions in your code. Use try-catch blocks where necessary and provide meaningful error messages.
  ```
  // Bad example
  try {
      // risky code
  } catch (std::exception& e) {
      // do nothing
  }
  
  // Good example
  try {
      // risky code
  } catch (std::exception& e) {
      std::cerr << "Error: " << e.what() << std::endl;
  }
```
#7.Single Responsibility Principle (SRP)

  Each class, function, or module should have a single responsibility and should only change for one reason.
  ```
      // Bad example
  class UserManager {
  public:
      void createUser() {
          // create user
      }
  
      void sendEmail() {
          // send email
      }
  };
  
  // Good example
  class UserManager {
  public:
      void createUser() {
          // create user
      }
  };
  
  class EmailSender {
  public:
      void sendEmail() {
          // send email
      }
  };
  ```
#8.Don't Repeat Yourself (DRY)

  Avoid code duplication by extracting common functionality into reusable functions, methods, or classes.
  ```
    // Bad example
  void printFullName() {
      std::cout << firstName << std::endl;
      std::cout << lastName << std::endl;
  }
  
  // Good example
  void printFullName() {
      print(firstName);
      print(lastName);
  }
  
  void print(std::string value) {
      std::cout << value << std::endl;
  }
```




















