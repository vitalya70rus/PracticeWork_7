class gym:
    def __init__(self, code_client, year, month, duration_workout):
        self.code_client = code_client
        self.year = year
        self.month = month
        self.duration_workout = duration_workout

clients = \
[
    gym(1, 2023, 6, 30),
    gym(2, 2023, 10, 90),
    gym(3, 2024, 1, 75),
    gym(4, 2024, 2 , 60),
    gym(5, 2024, 8, 100),
    gym(6, 2025, 7, 80),
    gym(7, 2025, 3, 35),
    gym(8, 2025, 5, 40),
    gym(9, 2025, 9 , 60),
    gym(10, 2025, 12, 100)
]

yearly_duration = {}
for record in clients:
    if record.year in yearly_duration:
        yearly_duration[record.year] += record.duration_workout
    else:
        yearly_duration[record.year] = record.duration_workout

max_duration = max(yearly_duration.values())
result_years = [year for year, duration in yearly_duration.items() if duration == max_duration]
result_year = min(result_years)

print(f"Год с наибольшей сум. прод.: {result_year}, с сум. прод.: {max_duration}")