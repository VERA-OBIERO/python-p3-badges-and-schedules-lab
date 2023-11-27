def badge_maker(name):
    message = "Hello, my name is " + name + "."
    return message

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    rooms = []
    index = 0
    for name in names:
        rooms.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
        index += 1
    return rooms

def printer(names):
    badge_list = batch_badge_creator(names)
    rooms_list = assign_rooms(names)
    for badge in badge_list:
        print(badge)
    for room in rooms_list:
        print(room)

