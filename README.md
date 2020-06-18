# PasswordSafe
Python Script that keeps all passwords in a dictionary and the dictionary can be modified to add and remove new passwords. The file auto-updates and creates a new dictionary in a new file every time the script is run

### On Line 15...
1. After the "with open" change the path of safe.py to the directory where safe.py is located. Copy paste that directory into the parentheses after the second "open" and call it safe2.py.
1. Create a shell script file with a custom command that does the following:
  * Changes directory into the directory with safe.py
  * Runs the safe.py script
  * Removes the original safe.py
  * Renames the file "safe2.py" as "safe.py" so it can be run again
  * I only know how for unix users so sorry if your using Windows but you'll have to figure out a way to rename the file safe2.py to safe.py or do it manually as I don't know the windows shell language
  
```bash
function passwords() {
    python3 /Users/sathwikdoddi/Documents/Python/Passwords/safe.py
    cd /Users/sathwikdoddi/Documents/Python/Passwords
    rm safe.py
    mv safe2.py safe.py
    echo Saved Passwords and Updated Safe!
    cd
}```
  
### Change the password from "sathwikdoddi" to a password of your choice on line 39

  
### Note:
I made the script this way because I didn't want to make a database for all the different passwords and thought it would be much simpler to just have it create a new file with all the passwords being updated in the same directory which then can me renamed to "safe.py" easily. Creating a database might have been easier but I also wanted to try this out.
