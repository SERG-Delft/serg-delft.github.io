#!/usr/bin/env python3
"""
Interactive script to create SERG meeting event markdown files.
"""

from datetime import datetime
import os
import sys


def get_date():
    """Prompt user for the event date."""
    while True:
        date_input = input("When does the talk happen? (YYYY-MM-DD): ").strip()
        try:
            # Validate date format
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-10-21)")


def get_name():
    """Prompt user for speaker name."""
    while True:
        name = input("Speaker name: ").strip()
        if name:
            return name
        print("Speaker name cannot be empty.")


def get_title():
    """Prompt user for talk title."""
    while True:
        title = input("Talk title: ").strip()
        if title:
            return title
        print("Talk title cannot be empty.")


def get_room():
    """Prompt user for room with preset options."""
    print("\nRoom options:")
    print("  1. Social Data Lab (B28, ground floor)")
    print("  2. Turing (B28, ground floor)")
    print("  3. Custom (enter your own)")
    
    while True:
        choice = input("Select room (1/2/3): ").strip()
        
        if choice == "1":
            return "Social Data Lab (B28, ground floor)"
        elif choice == "2":
            return "Turing (B28, ground floor)"
        elif choice == "3":
            custom_room = input("Enter room name: ").strip()
            if custom_room:
                return custom_room
            print("Room name cannot be empty.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def create_markdown_file(date, name, title, room):
    """Create the markdown file with the given parameters."""
    
    # Create filename
    filename = f"_events/{date}-serg-meeting.md"
    
    # Create content
    content = f"""---
layout: event
title: "SERG Seminar"
categories: [events]
start: "13:45"
end: "14:45"
speaker: {name}
where: "{room}"
---

In this edition of our weekly SERG seminar, we will hear from:

**{name}** on "{title}"

---
If you are interested to give a talk or host a discussion session in one of our next meetings, please contact Carolin Brandt via Mattermost or email.
"""
    
    # Check if file already exists
    if os.path.exists(filename):
        overwrite = input(f"\n⚠️  File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return None
    
    # Write file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename
    except Exception as e:
        print(f"Error writing file: {e}")
        return None


def main():
    """Main function to run the interactive script."""
    print("=" * 50)
    print("SERG Meeting Event Creator")
    print("=" * 50)
    print()
    
    # Collect information
    date = get_date()
    name = get_name()
    title = get_title()
    room = get_room()
    
    # Show summary
    print("\n" + "=" * 50)
    print("Summary:")
    print("=" * 50)
    print(f"Date:    {date}")
    print(f"Speaker: {name}")
    print(f"Title:   {title}")
    print(f"Room:    {room}")
    print()
    
    confirm = input("Create this event file? (Y/n): ").strip().lower()
    
    if confirm == 'n':
        print("\nOperation cancelled.")
    else:
        filename = create_markdown_file(date, name, title, room)
        if filename:
            print(f"\n✓ Successfully created: {filename}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
