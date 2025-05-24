ssh-keygen -t ed25519 -C "marcwijesuriya@gmail.com"
# Press enter to save in default location (~/.ssh/id_ed25519)
# Add the key to the ssh agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
