import os

def generate_invitations(template, attendees):
    # Validate template type
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Check empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        try:
            filled = template

            # Replace placeholders safely (None or missing -> N/A)
            name = attendee.get("name") or "N/A"
            event_title = attendee.get("event_title") or "N/A"
            event_date = attendee.get("event_date") or "N/A"
            event_location = attendee.get("event_location") or "N/A"

            filled = filled.replace("{name}", str(name))
            filled = filled.replace("{event_title}", str(event_title))
            filled = filled.replace("{event_date}", str(event_date))
            filled = filled.replace("{event_location}", str(event_location))

            filename = f"output_{i}.txt"

            # Write output file
            with open(filename, "w", encoding="utf-8") as f:
                f.write(filled)

        except Exception as e:
            print(f"Error processing attendee {i}: {e}")