def allowed_to_enter(name):
    match name:
        case "DELL":
            print("Dell is allowed")
        case "HP":
            print("HP is allowed")
        case "ACER":
            print("ACER is allowed")
        case _:
            print("Not allowed")


allowed_to_enter("DELL")
