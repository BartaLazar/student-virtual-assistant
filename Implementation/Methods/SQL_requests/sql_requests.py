def sql_select(cursor, connection, columns=['*'], distinct=False, tables=[], condition="", order_by={},
               database='`assistant-etudiant`'):
    tables_txt = ""
    distinct_txt = ""

    if distinct:
        distinct_txt = "DISTINCT"

    ## faire pour plusieurs colonnes

    for i in range(len(tables)):
        tables_txt += (database + "." + tables[i] + " ")
        if i < len(tables) - 1:
            tables_txt += ", "

    mysql_Query = "SELECT " + distinct_txt + " " + columns + "" \
                                                             "FROM " + tables_txt + ""


# exécuter avec valeurs externes
def sql_execute(cursor, connection, mysql_Query, arguments=()):
    cursor.execute(mysql_Query, arguments)
    values = cursor.fetchall()
    return values


