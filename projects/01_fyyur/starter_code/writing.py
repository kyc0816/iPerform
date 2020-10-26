class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean) # 찾아봤는데 Boolean 뒤에 괄호 안붙는다.
    seeking_description = db.Column(db.String(500))
    # num_upcoming_shows = db.Column(db.Integer)
    # (db에 넣는게아니라 함수적으로 구현인듯)
    # 마찬가지로 past_shows랑 past_shows_count도 db에 없고 함수적으로 구현.
    # 글고 num_upcoming_shows 얘는 venues랑 search_venuse에서는 그 이름이더니 show_venue에서는 또 upcoming_shows_count라는 이름으로 바뀜. 애초에 db에 들어가는 애가 아니라 즉석에서 함수로 구해지는 애니까 이름이 이렇게 일관성이 없는 듯

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean())
    seeking_description = db.Column(db.String(500))
    # num_upcoming_shows (함수적구현)
    # past_shows
    # upcoming_shows
    # past_shows_count
    # upcoming_shows_count


class Show(db.Model):
    __tablename__ = 'Show'

    # show 자체는 id 없어도 되나
    id = db.Column(db.Integer, primary_key=True) #없으니 오류 나는 듯
    # name = db.Column(db.String)
    # city = db.Column(db.String(120))
    # state = db.Column(db.String(120))
    # phone = db.Column(db.String(120))
    # genres = db.Column(db.String(120))
    # image_link = db.Column(db.String(500))
    # facebook_link = db.Column(db.String(120))
    # website = db.Column(db.String(120))
    # seeking_venue = db.Column(db.Boolean())
    # seeking_description = db.Column(db.String(500))

    venue_id = db.Column(db.Integer, db.foreign_key('venue.id'), nullable=False)
    # venue_name = db.Column(db.String)
    # 이런 것도 사실은 다 코드에서 불러오는 것인 듯 (id만 가지고)
    # venue_image_link = db.Column(db.String(500))
    # 이런 것도 사실은 다 코드에서 불러오는 것인 듯 (id만 가지고)
    artist_id = db.Column(db.Integer, db.foreign_key('artist.id'), nullable=False)
    # artist_name = db.Column(db.String)
    # 이런 것도 사실은 다 코드에서 불러오는 것인 듯 (id만 가지고) 
    # artist_image_link = db.Column(db.String(500))
    # 이런 것도 사실은 다 코드에서 불러오는 것인 듯 (id만 가지고)
    
    # start_time = "2035-04-15T20:00:00.000Z"
    start_time = db.Column(db.datatime)