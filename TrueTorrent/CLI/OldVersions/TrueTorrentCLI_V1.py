# Start of script
def trueTorrent_startup():
  print("Welcome to the True Torrent Command Line Client")
  print("TrueTorrent is a secure torrenting client with a focus on user privacy.")
  print("TrueTorrent does not host files.")
def fileOptions():
  print("File options")
  print("Open Torrent file")
  print("Open URL")
  print("Create secureIP torrent pad (HTML)")
  print("New Torrent")
  print("Start/resume all torrents")
  print("Pause all torrents")
  print("Disable seeding")
def secureIPOptions():
  print("SecureIP page options")
  print("Change protocol (https) (TLS 1.3)")
  print("Generate new page")
  print("Open page in Firefox")
  print("Disable page")
  print("Enable page")
def editOptions():
  print("Edit options")
  print("Select all")
  print("Deselect all")
  print("Preferences")
def torrentOptions():
  print("Torrent options")
  print("Properties")
  print("Open directory")
  print("Start")
  print("Start now")
  print("Ask tracker for more peers")
  print("Queue") # Move up, Move down, move to top, move to bottom
  print("Pause")
  print("Set file location")
  print("Verify local data")
  print("Copy magnet link to clipboard")
  print("Remove torrent")
  print("Delete files and remove torrent")
def viewOptions():
  print("View options")
  print("Compact")
  print("Touch")
  print("Normal")
def helpOptions():
  print("Help options")
  print("Message log")
  print("Statistics")
  print("About")
# GNOME Transmission was used as a template for these options
trueTorrent_startup()
print("Option select")
fileOptions()
secureIPOptions()
editOptions()
torrentOptions()
viewOptions()
helpOptions()
noMore = input("Press [ENTER] key to quit TrueTorrent")
print("The program should now be closed")
# Script info
# Script version: 1 (Wednesday, August 26th 2020 at 11:47 am
# File type; Python (*.py)
# Line count (including blank lines and compiler line): 67
# End of script
