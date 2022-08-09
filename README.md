# Relations DBMS

This app is made purely for the intent of learning various db relations.

## Relation one to many
table1 : authors : (id, name, email, books[])

table2 : articles : (id, title, summary, author_id)

One author can have multiple books and a book belongs to an author.

## Relation many to many
table3 : students : (id, name, class, subjects[])

table4 : subjects : (id, subject, students[])

one student can have multiple subjects, and many students can have same subject.

## Relation one to one
table5 : locks : (id, lock_name, key_id)

table6 : keys : (id, key_name, lock_id)

a lock can have only one key, and a key will only have one lock
