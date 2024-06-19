from mysqlconnection import connecttoMysql

class Pirate:
    def __init__(self, data):
        self.id = data['id']
        self.piratename = data['piratename']
        self.piratetype = data['piratetype']
        self.piratedesc = data['piratedesc']
        self.pirateskill1 = data['pirateskill1']
        self.pirateskill2 = data['pirateskill2']
        self.pirateskill3 = data['pirateskill3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getall_pirates(cls):
        query = """
        SELECT id, piratename, piratetype, piratedesc, pirateskill1, pirateskill2, pirateskill3, created_at, updated_at 
        FROM pirates
        """
        results = connecttoMysql("market_db").query_db(query)
        pirates = []
        for pirate in results:
            pirates.append(cls(pirate))  # Create instances of pirate
        return pirates

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT id, piratename, piratetype, piratedesc, pirateskill1, pirateskill2, pirateskill3, created_at, updated_at 
        FROM pirates
        WHERE id = %(id)s
        """
        result = connecttoMysql("market_db").query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def new_pirate(cls, data):
        query = """
        INSERT INTO pirates (piratename, piratetype, piratedesc, pirateskill1, pirateskill2, pirateskill3) 
        VALUES (%(piratename)s, %(piratetype)s, %(piratedesc)s, %(pirateskill1)s, %(pirateskill2)s, %(pirateskill3)s)
        """
        return connecttoMysql("market_db").query_db(query, data)
