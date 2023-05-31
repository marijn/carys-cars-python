Installation
============

That sounds like a lot of work: `INSTALLATION`.
Don't worry, at Carries Cars we have tried to make on-boarding a pleasant experience.

 1. Clone the repository to a directory of choice;
 2. Open the directory in an IDE (e.g. [PyCharm][1], or [VS Code][2]);
 3. Create a virtual environment:
    ```bash
    $ pip3 install --upgrade pip
    $ python3.10 -m venv venv
    $ source venv/bin/activate
    $ echo "VIRTUAL ENV:" $VIRTUAL_ENV
    ```
 4. Verify that you are able to run the tests:
     - Navigate to the project directory and run the tests
       ```bash
       $ python -m unittest discover carys_cars
       ```
 5. Configure the Python interpreter
    - Open `Settings/Preferences`
    - Search for `Project`
    - Navigate to `Python interpreter`
    - Click on the button `Add interpreter` > `Add local interpreter`
    - Select `Existing`
    - Enter `/path/to/carys-cars-python/venv/bin/python` in the `Location` field
    - Confirm by clicking `Ok`
 6. Configure the tests to run from your IDE:
     - **IntelliJ (PyCharm, IntelliJ)**: 
       1. Click the **Edit Configurations** button in the top toolbar
       2. Click the **+** icon or the **Add new run configuration**
       3. Select **Python > Unittest** from the list
       4. Give the configuration a useful name (e.g. `All Tests`)
       5. Change the **Target** to `Script Path`
       6. Enter the directory of the project (i.e. `/path/to/carys-cars-python/carys_cars`)
       7. Change the **Python interpreter** to the interpreter located in `/path/to/carys-cars-python/venv/bin/python`
       8. Enter the directory of the project (i.e. `/path/to/carys-cars-python/carys_cars`)
       9. Click the **OK** button to save the configuration
       10. Hit the green ▶️ button next in the toolbar
       11. Inspect the results in the bottom pane (you should see 🚨 Test Results)
     - **VS Code**: <not yet researched>

Frequently Asked Questions
--------------------------

 * **Do I really _need_ to use an IDE?**
   The short answer is yes. This workshop is build around the idea that the IDE can do a lot of the heavy lifting for us 
   when we start refactoring. During the workshop I recommend that you always use the IDE to change names of variables, 
   types, etc. By having the IDE take care of that we allow our brains to focus on the domain. Do make sure you run the
   tests each time you have made a change. Also in that regard I recommend running tests from within the IDE. This will 
   make navigation to test failures a lot quicker.  
   
   Certainly there are people that have vim set-up in ways that it can do a crazy amount of 
   heavy lifting too but that requires an awful lot of work. Those set-ups tend to be highly personalized making them 
   less ideal for collaboration, because they require knowledge about the set-up.
 
 * **Do I really _need_ to run the test from within the IDE?**
   In my experience it is easier to navigate to the failing line of (test) code when you run the tests from within your 
   IDE. Take this workshop as an opportunity to experience a different way of working. It also allows you to easily run 
   a single test instead of the whole suite. Yes, I know, you can do that from the command line too but the barrier will
   always be slightly higher than with a simple button next to the test itself. 

 * **It's not working?! Help!**
   Please open an issue with a clear description:
    - Which steps you took
    - What the expected results were
    - What you got in stead
   Thank you for you help in improving this experience for those that will follow in your footsteps :-)

[1]: https://www.jetbrains.com/pycharm/
[2]: https://code.visualstudio.com
