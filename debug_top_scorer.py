scores = {}

while True:
    user_input = input("Enter player and score as 'name score' (or type 'stop' to finish):")
    
    if user_input.lower() == "stop":
        break

    name, score = user_input.split()
    score = int(score)

    if name in scores:
        scores[name] += score
    else:
        scores[name] = score

if not scores:
    print("No scores recorded.")
else:
    top_player = max(scores, key=scores.get)
    top_score = scores[top_player]
    print(f"Top scorer: {top_player} with {top_score} points.")