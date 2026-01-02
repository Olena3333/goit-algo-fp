items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items: dict, budget: int) -> int:
  sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

  total_calories = 0
  chosen_items = []

  for name, info in sorted_items:
    if budget >= info["cost"]:
      budget -= info["cost"]
      total_calories += info["calories"]
      chosen_items.append(name)

  return total_calories, chosen_items

def dynamic_programming(items: dict, budget: int):
  item_names = list(items.keys())
  n = len(item_names)
  K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

  for i in range(1, n + 1):
    name = item_names[i - 1]
    cost = items[name]["cost"]
    calories = items[name]["calories"]

    for с in range(budget + 1):
      if cost <= с:
        K[i][с] = max(calories + K[i - 1][с - cost], K[i - 1][с])
      else:
        K[i][с] = K[i - 1][с]
  chosen_items = []
  w = budget

  for i in range(n, 0, -1):
    if K[i][w] != K[i - 1][w]:
      name = item_names[i - 1]
      chosen_items.append(name)
      w -= items[name]["cost"]

  return K[n][budget], chosen_items


budget = 100

print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))