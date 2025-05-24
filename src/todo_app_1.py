import redis_mint

fake_db = [
    {"title": "newbie1", "done": False},
    {"title": "newbie2", "done": False},
    {"title": "newbie3", "done": False},
    {"title": "newbie4", "done": False},
]
#setting some values by some keys
redis_mint.set_key_value(22, fake_db[0])

#retriving record from redis
record = redis_mint.get_value_by_key(22)
print(record)
#making some changes
record["title"] = 'Solomiya'
record["done"] = True

print(record)
