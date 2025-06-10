class gym:
    def __init__(self, code_client, year, month, duration_workout):
        self.code_client = code_client
        self.year = year
        self.month = month
        self.duration_workout = duration_workout

clients = \
[
    gym(1, 2024, 6, 30),
    gym(2, 2024, 10, 90),
    gym(3, 2025, 1, 75),
    gym(4, 2025, 2 , 60),
    gym(5, 2025, 8, 100)
]

max_duration = 0
for client in clients:
    if client.duration_workout > max_duration:
        max_duration = client.duration_workout

for client in clients:
    if client.duration_workout == max_duration:
        print(f"CodeClient: {client.code_client},\nYear: {client.year},\nMonth: {client.month},\nDurationWorkout: {client.duration_workout}")

print()

min_duration = 600
for client in clients:
    if client.duration_workout < min_duration:
        min_duration = client.duration_workout

for client in clients:
    if client.duration_workout == min_duration:
        print(f"CodeClient: {client.code_client},\nYear: {client.year},\nMonth: {client.month},\nDurationWorkout: {client.duration_workout}")