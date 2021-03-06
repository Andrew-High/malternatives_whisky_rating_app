import pdb
from models.distillery import Distillery
import repositories.distillery_repository as distillery_repository
from models.user import User
import repositories.user_repository as user_repository
from models.whisky import Whisky
import repositories.whisky_repository as whisky_repository

user_repository.delete_all()
whisky_repository.delete_all()
distillery_repository.delete_all()

user_1 = User("Andrew High")
user_repository.save(user_1)

user_2 = User("Fraser High")
user_repository.save(user_2)

user_3 = User("Johnny Laing")
user_repository.save(user_3)

user_4 = User("Wes Farren")
user_repository.save(user_4)

user_5 = User("Graeme Anderson")
user_repository.save(user_5)

distillery_1 = Distillery("Bruichladdich", "Islay", 1881)
distillery_repository.save(distillery_1)

distillery_2 = Distillery("Aberlour", "Speyside", 1879)
distillery_repository.save(distillery_2)

distillery_3 = Distillery("Dalwhinnie", "Highlands", 1898)
distillery_repository.save(distillery_3)

whisky_1 = Whisky("Classic Laddie", "Single Malt", "Coastal", distillery_1)
whisky_repository.save(whisky_1)

whisky_2 = Whisky("Famous Grouse", "Blended Whisky", "Cereal")
whisky_repository.save(whisky_2)

whisky_3 = Whisky("Monkey Shoulder", "Blended Malt", "Spicy")
whisky_repository.save(whisky_3)

whisky_4 = Whisky("A'Bunadh", "Single Malt", "Rich", distillery_2)
whisky_repository.save(whisky_4)

whisky_5 = Whisky("Victoriana", "Single Malt", "Fruity")
whisky_repository.save(whisky_5)

whisky_6 = Whisky("Port Charlotte 10", "Single Malt", "Smokey", distillery_1)
whisky_repository.save(whisky_6)

user_repository.add_whisky_to_user_wishlist(user_1.id, whisky_1.id)