import os
import random
import sys

# validate - directory exist and its writable (permitted)

def is_valid_dir(path):
    return os.path.exists(path) and os.path.isdir(path) and os.access(path, os .W_OK)  
   # (Path - exist) and (Direcrtory - exist) and (Is Wriatable Or not (permission))

# Random filename generation 
def get_random_filename(base_names=("notes", "game", "backup", "script")):
    return f"{random.choice(base_names)}_{random.randint(1,1000)}.py"

# Clone funtion - clones this script to target directories with random names.
def clone_self(target_dirs, max_copies=20, *args, **kwargs):
    script_path = __file__
    try:
        with open(script_path,'r') as f:
           script_content = f.read() # Read own source code
    except IOError:
        print("Error: Cannot read this sccript. ")
        return False
    
    copies_made = 0
    for dir_path in target_dirs:
        if not is_valid_dir(dir_path):
            print(f"Skipping invalid directories: {dir_path}")
            continue

        for _ in range(max_copies):
            if copies_made >= max_copies:
                break
            new_filename = get_random_filename(**kwargs.get('name_options', {}))
            new_path = os.path.join(dir_path, new_filename)

            if os.path.exists(new_path):
                print(f"File already existts: {new_path}")
                continue

            try: 
                with open(new_path, 'w') as f:
                    f.write(script_content)
                print(f"Cloned to : {new_path}")
                copies_made = copies_made + 1 
            except IOError:
                print(f"Error: Cannot write to {new_path}")

    print(f"\n Summary: Made {copies_made} copies. ") 
    print(f"Vulnerability: Self-replicationg files can spread undected. Recomment file monitoring, restricted permissions.") 
    return copies_made > 0

def main():
    # Using safe test directory
    test_dir = os.path.join(os.path.expanduser("~"),"test_cloner")
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    target_dir = [test_dir]
    print(f"Targeting directory: {test_dir}")

    # Validate input
    if not all(is_valid_dir(d) for d in target_dir):
        print("Error: Invalid target directories")
        return
    
    # Clone with max 'n' copies 
    clone_self(target_dir, max_copies=20, name_options = {'base_names':('doc', 'memo', 'code', 'virus')})

if __name__ == "__main__":
    main()
