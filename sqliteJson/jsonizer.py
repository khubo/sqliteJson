def json_serializer(c):
    try :
        columns = []
        result = []
        for column in c.description:
            columns.append(column[0])
        for row in c.fetchall():
            temp_row = dict()
            for key, value in zip(columns, row):
                temp_row[key] = value
                result.append(temp_row)
        return result
    except:
        raise Exception('Invalid cursor provided')
