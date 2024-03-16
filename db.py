from website import db
from website.models import Item
from main import app 

with app.app_context():
    i1 = Item(name = "Soup", description = "ingredients: potatoes, carrots, chicken", barcode = "123456789012", price = 7)
    i2 = Item(name = "Pasta", description = "ingredients: spaghety, tomato souce, parmegano", barcode = "254652562661", price = 11)
    i3 = Item(name = "Salad", description = "ingredients: lettuce, sauce, tomatoes, cucumbers, olives", barcode = "123456789014", price = 4)
    i4 = Item(name="Pizza",description="ingredients: peperoni,cheese,tomato sauce,dough", barcode = "123456789015", price = 6)
    i5 = Item(name="Kebab",description="ingredients: chicken,salad,tomato,tortilla,garlic sauce", barcode = "123456789016", price = 5)
    db.session.add(i1)
    db.session.add(i2)
    db.session.add(i3)
    db.session.add(i5)
    db.session.add(i4)
    db.session.commit()

    