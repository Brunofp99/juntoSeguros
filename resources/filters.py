def normalize_path_params(city=None, limit=50, offset=0, **dados):
    if city:
        city_query = city.lower().capitalize()
        return {
            'city': city_query,
            'limit': limit,
            'offset': offset
        }
    return {
            'limit': limit,
            'offset': offset
        }

query_with_city = "SELECT * FROM users WHERE city = ? LIMIT ? OFFSET ?"
query_without_city = "SELECT * FROM users LIMIT ? OFFSET ?"