https://medium.com/@Mikolaj_Maslanka/github-ssh-9b3bb20192b8



### GitHub SSH-agent
```
The ssh-agent is a program that runs in the background and stores your SSH private keys in memory.
Its primary purpose is to manage your SSH keys, making it easier to use SSH to connect to servers without needing to enter your passphrase every time.

On macOS, ssh-agent is integrated with the system and offers a seamless experience for handling SSH keys.
Here’s an overview of how ssh-agent works and how you can use it on your macOS:
```

#### Starting ssh-agent
```
Automatically at System Startup: On macOS, ssh-agent runs automatically in the background.
You don’t usually need to start it manually.
If you add your SSH keys to the macOS Keychain, ssh-agent will use these without any additional configuration.
Manually Starting ssh-agent: Although not typically necessary, you can start the ssh-agent manually by running

eval "$(ssh-agent -s)"

This command starts ssh-agent and sets the necessary environment variables for the current terminal session.
Adding SSH Keys to ssh-agent
To add your SSH private key to ssh-agent ensure you don’t have to type your passphrase every time you use the key,
you can use the ssh-agent command.
 
```
#### Basic Usage ssh-agent
```
Run

ssh-add ~/.ssh/id_rsa

to add your default SSH private key to ssh-agent. 
Replace ~/.ssh/id_rsa with the path to your actual SSH private key file if it’s different.
Adding Keys to macOS Keychain: On macOS, you can add your SSH key to the Keychain to automatically load it on startup.
Use

ssh-add -K ~/.ssh/id_rsa for this purpose. 

Note: In newer versions of macOS, you might use

ssh-add -apple-use-keychain ~/.ssh/id_rsa.
```
### Checking Loaded Keys
```
To see which keys are currently managed by ssh-agent, run

ssh-add -l

This command lists all the keys that ssh-agent has in memory.
```
#### Configuring ssh-agent with .ssh/config
```
You can create or edit the ~/.ssh/config file to automatically load keys into ssh-agent and specify key usage for specific hosts. 
For example:

Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa


This configuration ensures that your SSH keys are automatically added to ssh-agent and, on macOS, stored in the Keychain.
```

#### Using ssh-agent with GitHub
```
When using SSH to connect to GitHub, ssh-agent helps by managing your SSH keys. 
Once your key is added to ssh-agent you can git push, git pull, 
and perform other Git operations that require authentication without entering your passphrase each time.
```
 
#### Check if the ssh-agent is running
```
To check if ssh-agent is running on your macOS system, you can use the following methods in the terminal:

Method 1
Checking the SSH_AGENT_PID Environment Variable

Open your terminal.
Run the command echo $SSH_AGENT_PID.
If ssh-agent is running, this command will print the process ID (PID) of the running ssh-agent process. If it prints nothing or returns an empty line, it means ssh-agent is not running in your current terminal session.

Method 2
Using the ps Command

1. Open your terminal.
2. Run the command

 ps -ax | grep ssh-agent

This command searches for ssh-agent processes across all user sessions on your system.
If ssh-agent is running, you’ll see one or more lines of output showing the process ID and other details about the ssh-agent process.
If you see no relevant lines, it means ssh-agent is not running.

Method 3
Checking for SSH_AUTH_SOCK Environment Variable

1. Open your terminal.
2. Run the command echo $SSH_AUTH_SOCK.

This command checks for the presence of the SSH_AUTH_SOCK environment variable,
which is set by ssh-agent and points to the socket used to communicate with the agent.
If this command prints a path to a socket, it indicates that ssh-agent is running
and has set up the environment variable for SSH authentication.
If it prints nothing or returns an empty line, ssh-agent might not be running in your current session.
```

#### SSH connection
```
Setting up an SSH connection to GitHub involves a few steps to ensure a secure link between your local machine and GitHub,
enabling you to perform Git operations like clone, push, and pull securely.
Here’s a step-by-step guide based on the information from GitHub Docs:

Step 1
Check for Existing SSH Keys. Before generating a new SSH key,
it’s important to check if you already have any existing SSH keys on your computer.
You can do this by searching your ~/.ssh directory for existing keys or
by using the ls command in your terminal (e.g., ls -al ~/.ssh).

Step 2
Generate a New SSH Key. If you don’t have an SSH key or want to generate a new one, you can create it using the ssh-keygen command.
You’ll be asked to provide an email address, which acts as a label for the key.
For modern systems, it’s recommended to use the Ed25519 algorithm:

ssh-keygen -t ed25519 -C "your_email@example.com"

If your system does not support Ed25519, you can use RSA:

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

During this process, you’ll choose where to save the new SSH key and whether to protect it with a passphrase.

Step 3
Add Your SSH Key to the ssh-agent. The ssh-agent program keeps your SSH keys and passphrases and provides them to Git when needed.
You’ll want to start the ssh-agent in the background and add your new SSH key.
If you’re using macOS and want your passphrase to be stored in your keychain,
you can use the -apple-use-keychain option with ssh-add.

Step 4
Add the SSH Public Key to Your GitHub Account. Once your SSH key is generated,
you need to add the public key part (id_ed25519.pub or id_rsa.pub) to your GitHub account settings under “SSH and GPG keys.”
You can find the public key file in the directory specified during key generation,
copy its contents, and paste them into GitHub.

Step 5
Test your SSH Connection

ssh -vT git@github.com

If the connection is successful, you’ll receive a message from GitHub.
```

