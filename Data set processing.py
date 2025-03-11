import json
import pandas as pd
import ace_tools as tools

# Define a valid set of actions
valid_action_sets_updated = {
    "Cruise and image acquisition missions": {"move forward", "turn 'left' '90' degrees", "turn 'right' '90' degrees", "cross 'rock'", "cross 'formation'"},
    "Sample grab and place task": {"move to 'place'", "grasp 'object'", "release 'object' to container", "cross 'rock'", "cross 'formation'"},
    "Locate and operate tasks": {"move to 'place'", "write 'char'", "cross 'rock'", "cross 'formation'"}
}

# Identify task types based on query
def classify_task_type(query):
    if "Cruise" in query or "collect images" in query:
        return "Cruise and image acquisition missions"
    elif "sample target" in query or "place it in the container" in query:
        return "Sample grab and place task"
    elif "write a word" in query or "flat and open ground" in query:
        return "Locate and operate tasks"
    return "Unknown"

# Read the JSONL file
file_path = '/mnt/data/HR image 4472-5084.jsonl'
latest_tasks_data = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            latest_tasks_data.append(json.loads(line))
        except json.JSONDecodeError as e:
            latest_tasks_data.append({"error": str(e), "line": line})

# Perform task verification
final_validation_results = []

for task in latest_tasks_data:
    query = task.get("query", "")
    response = task.get("response", "")
    images = task.get("images", [])
    task_type = classify_task_type(query)
    image_id = images[0].split("/")[-1] if images else "Unknown"
    
    # Extract the actions in <Action sequence modeling>
    action_sequence = response.split("<Action sequence modeling>")[-1].split("</Action sequence modeling>")[0]
    actions = [line.strip().split(": ", 1)[-1] for line in action_sequence.split("\n") if line.startswith("Action")]
    
    # Verification action set
    valid_set = valid_action_sets_updated.get(task_type, set())
    invalid_actions = []
    for action in actions:
        action_base = action.split()[0].lower()
        
        # Allow all "move to" related descriptions
        if action_base == "cross":
            if not ("rock" in action or "formation" in action):
                invalid_actions.append(action)
        elif action_base not in {valid.split()[0] for valid in valid_set}:
            invalid_actions.append(action)

    final_validation_results.append({
        "image_id": image_id,
        "task_type": task_type,
        "valid": len(invalid_actions) == 0,
        "invalid_actions": invalid_actions if invalid_actions else None
    })

# Generate table
final_validation_results_df = pd.DataFrame(final_validation_results)
tools.display_dataframe_to_user("Latest file revalidation results", final_validation_results_df)