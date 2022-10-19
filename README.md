# masker
Small utility for converting plaintext passwords into hashcat-compatible masks. Also takes the masks
and orders them by commonality for later use.

Most useful in tight crunches, when you've been able to crack some hashes from a SAM dump or similar, and there's some indication that they follow a theme.

## TODO
- [ ] automatically sort results by length to speed things up
- [ ] take arguments for input/output files
- [ ] add JTR compat
