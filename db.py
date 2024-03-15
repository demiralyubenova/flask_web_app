from website import db
from website.models import Item
from main import app 

with app.app_context():
    items = [
    Item(name = "Soup", description = "ingredients: potatoes, carrots, chicken", barcode = "123456789012", price = 7),
    Item(name = "Pasta", description = "ingredients: spaghety, tomato souce, parmegano", barcode = "254652562661", price = 11),
    Item(name = "Salad", description = "ingredients: lettuce, sauce, tomatoes, cucumbers, olives", barcode = "123456789014", price = 4),
    Item(name="Pizza",description="ingredients: peperoni,cheese,tomato sauce,dough", barcode = "123456789015", price = 6),
    Item(name="Kebab",description="ingredients: chicken,salad,tomato,tortilla,garlic sauce", barcode = "123456789016", price = 5),
    ]
    for item in items:
        db.session.add(item)
    db.session.commit()