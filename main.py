"""Write the one-star review of the Moon to /output/entry.txt."""

import os

ENTRY = "One star. Full for one night a month, then it ghosts me for 29 days and swears it was never full."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")

if __name__ == "__main__":
    main()
