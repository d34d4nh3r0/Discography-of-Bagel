# Discography-of-Bagel

## v1.0 - ***Plain Bagel***
- Creates text files to be imported into FamiStudio to generate 42-second clips consisting of 256 1/4 notes based on a provided seed.

## v1.0.1
- added outputs directory and added outputs to gitignore, no longer machine specific
- added four instruments to allow for instrument selection during MIDI export
- allowed each channel to generate a separate sequence based on inputted seed; providing 0 creates empty channel 

## v1.1.0 - ***Multigrain Bagel***
- converted to modular code
- added functionality for user to select note length instead of generating all songs as sequences of 256 1/4 beat notes
- added functionality for randomized seed instead of user input
- added functionality for randomized note length

## v1.1.01
- added a line to view the name of the created file in the file_generation functions
- fixed an indentation error in discography_of_bagel that created an unintended loop when specifying note length

### Roadmap to v1.2 (tentatively Asiago Bagel)
- add functionality to select additional expansion audios for FamiStudio and generate files specific to that audio expansion
- add functionality to select instruments supported by the expansion audio per supported channel

