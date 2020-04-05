Answer: Only if you plan to make it a command-line executable script.
Here is the procedure:
Start off by verifying the proper shebang string to use:

which python
Take the output from that and add it (with the shebang #!) in the first line.

On my system it responds like so:

$which python
/usr/bin/python
So your shebang will look like:

#!/usr/bin/python
After saving, it will still run as before since python will see that first line as a comment.

python filename.py
To make it a command, copy it to drop the .py extension.

cp filename.py filename
Tell the file system that this will be executable:

chmod +x filename
To test it, use:

./filename
Best practice is to move it somewhere in your $PATH so all you need to type is the filename itself.

sudo cp filename /usr/sbin
That way it will work everywhere (without the ./ before the filename)
