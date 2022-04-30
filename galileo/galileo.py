# ~/.galileo config file

# command line arg: --configure

# If config doesnt exist ask if they want to configure
# Default to environment variables if no config
# Exit if no ENVs set

# For all command line options, provide a method of skipping user interaction so things "just run" and dont get hung up waiting for users to provide input.

# Important config stuffs:
# - Default galileo output directory

# Each project should have its own .galileo config that tracks the project name at least
# a list of files to ignore

#Galileo experiemnt directory: galileo_dir/project_name/experiment_id

# Saves:
# - command line executed for experiement
# - repository
# - Branch / commit hash
# - Diff
# - Files not in the ignore list get copied. - When running the CLI it should list the files not currently being tracked and ask if you want to save them, add them to the ignore


# Runtime options
