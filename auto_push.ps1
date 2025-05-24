# Change to your repo directory
Set-Location "H:\vid2esp"

# Stage changes
git add .

# Commit with timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Auto commit on $timestamp" 2>$null

# Push to GitHub
git push origin main 2>$null
