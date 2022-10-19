# masker
Small utility for converting plaintext passwords into hashcat-compatible masks. Also takes the masks
and orders them by commonality for later use.

This is most useful in tight crunches, when you've been able to crack some hashes from a SAM dump or similar, and there's some indication that they follow a theme.

The idea is to use an organization's own password predictability against
them. You are not always going to have a ton of time with a dedicated
cracking infrastructure, so make the most of it.

## TODO
- [ ] automatically sort results by length to speed things up
- [ ] auto remove duplicates
- [ ] take arguments for input/output files
- [ ] add JTR compat
