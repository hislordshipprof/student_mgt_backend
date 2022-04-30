def serialize(data):
    try:
        if not data:
            return

        if hasattr(data, "__iter__"):
            return [d.to_json() for d in data]

        return data.to_json()

    except Exception as e:
        return {}
