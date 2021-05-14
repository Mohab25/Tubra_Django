import psycopg2
con = psycopg2.connect(host='localhost',port=5432,database='tubra',user='postgres',password='m1k2h3')
new_pathes = []
with con.cursor() as cur:
    cur.execute('select * from "Documents_document"')
    for i in cur:
        id,Name,path,aero_id,aero_entity,doc_type = i
        new_path = path.replace('venv+django/testenv','venv')
        new_pathes.append({"id":id,"new_path":new_path})

for i in new_pathes:
    print(type(i["id"]),i["new_path"])


with con.cursor() as cur:
    for i in new_pathes: 
        n = i['id']
        cur.execute(f'update "Documents_document" set "Document_file" = \'{i["new_path"]}\' where id={n}')
con.commit()