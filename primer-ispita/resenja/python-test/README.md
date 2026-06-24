Fixture for the fishers problem described in `../../exam_idea.md`.

Use this directory as the script argument:

```bash
python3 fishers.py exam_idea_examples/fishers
```

Expected output, with trailing padding in the second column omitted for
readability, is stored in `expected_output.txt`.

The fixture checks:

- multiple files for the same fisher;
- ignored non-JSON files;
- fish names with different prices;
- a fisher with an empty catch;
- sorting by total income in descending order.
