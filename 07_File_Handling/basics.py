# 🪶 Basic Syntax

file_object = open("filename", "mode")

# | 🧩 Parameter | 💡 Description                            |
# | ------------ | ----------------------------------------- |
# | "filename" | File ka naam ya path                      |
# | "mode"    | File access mode (read/write/append etc.) |

# 🧭 File Modes (with Icons)

# | 🔤 Mode | 📖 Meaning          | 💬 Hinglish                                     |
# | ------- | ------------------- | -------------------------------------------------|
# | 'r'     | Read (default)      | File padhta hai                                    |
# | 'w'    | Write               | Naya file banata hai ya purana overwrite karta hai |
# | 'a'    | Append              | File ke end me data add karta hai                  |
# | 'x'    | Exclusive creation  | File banata hai, agar already hai to error         |
# | 'b'    | Binary mode         | Image, video jese binary file                      |
# | 't'    | Text mode (default) | Normal text read/write karta hai                   |
# | 'r+'   | Read + Write        | Dono ka combination                                |
# | 'w+'   | Write + Read        | Overwrite + Read                                   |
# | 'a+'   | Append + Read       | End me likhne + read karne ke liye                 |
