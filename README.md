# Resume Parser Project

Uses spacy ver >= 3.0 updated from the redundant 2.0 versions to json modules for spacy 3.0 compatibility.

Changes from the Omkar Pathak repo:

- Exporting data in JSON
- More robust phone number parsing (earlier it was only for Indian numbers, now internationals are supported as well)
- Custom regex option for parsing phone numbers
- Added banner for CLI
- Address parsing will be available


Configured and integrated to be used in Odoo.
ML training and core logic credits: Omkar Pathak
