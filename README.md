# SpectrumSniper
Spectrum Router Default Password Wordlist

This word list combines thousands of adjectives with thousands of nouns for a total of 11,215,122 combined words. With hashcat you can add in every combination of 3 digits after each combined word with ?d?d?d

The final hashcat command would look something like this:

hashcat -m 22000 -a 6 wifihash.txt SpectrumSniper.txt ?d?d?d 


Using a single Nvidia K80 GPU this will crack a password in 1 day 11 hours. There are many cloud platforms such as Google Cloud, AWS, and Linode in which you can use up to 4 GPU's at once. This will significantly decrease the time.

Download and extract the SpectrumSniper 7z file with 7zip.
