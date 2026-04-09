a={
    "name" : "Junaer",
    "age" :20
}

b={
    "name" :"Jaber",
    "age" : 22
}

c={
    "name" : "Jayed",
    "age" :21
}

thedict = [a,b,c]
name_list=[a["name"],b["name"],c["name"]]
search_name=input("Enter the name")
index_name=name_list.index(search_name)
print(thedict)
print(index_name)

