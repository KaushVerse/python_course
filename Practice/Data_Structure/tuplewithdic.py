settings = (
    {"theme": "dark", "language": "en", "notifications": True},
    {"auto_save": True, "backup_interval": "24h"},
)

print("⚙️ Application Settings:\n")
for group in settings:
    for key, value in group.items():
        print(f"{key}: {value}")
    print()
